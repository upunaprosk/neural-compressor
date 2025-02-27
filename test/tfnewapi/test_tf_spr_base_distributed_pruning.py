"""Tests for the TensorFlow pruning with distributed training and inference."""
import hashlib
import os
import re
import shutil
import signal
import subprocess
import sys
import time
import unittest
from platform import platform, system

import cpuinfo
import tensorflow as tf

from neural_compressor.adaptor.tf_utils.util import version1_lt_version2
from neural_compressor.utils import logger


def build_fake_ut():
    fake_ut = '''
from __future__ import print_function
import tensorflow
from tensorflow.keras.layers import Dense, Conv2D, BatchNormalization, Activation
from  tensorflow.keras.layers import AveragePooling2D, Input, Flatten
from  tensorflow.keras.callbacks import LearningRateScheduler
from  tensorflow.keras.callbacks import ReduceLROnPlateau
from  tensorflow.keras.regularizers import l2
from  tensorflow.keras.models import Model
from  tensorflow.keras.datasets import cifar10
import numpy as np
import os
import sys
import cpuinfo
import shutil
import unittest
from neural_compressor.adaptor.tf_utils.util import version1_lt_version2
from neural_compressor.utils import logger
from neural_compressor.utils.utility import CpuInfo

def lr_schedule(epoch):
    """Learning Rate Schedule
    Learning rate is scheduled to be reduced after 80, 120, 160, 180 epochs.
    Called automatically every epoch as part of callbacks during training.
    # Arguments
        epoch (int): The number of epochs
    # Returns
        lr (float32): learning rate
    """
    lr = 1e-3
    if epoch > 180:
        lr *= 0.5e-3
    elif epoch > 160:
        lr *= 1e-3
    elif epoch > 120:
        lr *= 1e-2
    elif epoch > 80:
        lr *= 1e-1
    print('Learning rate: ', lr)
    return lr

def resnet_layer(inputs,
                 num_filters=8,
                 kernel_size=3,
                 strides=1,
                 activation='relu',
                 batch_normalization=True,
                 conv_first=True):
    """2D Convolution-Batch Normalization-Activation stack builder
    # Arguments
        inputs (tensor): input tensor from input image or previous layer
        num_filters (int): Conv2D number of filters
        kernel_size (int): Conv2D square kernel dimensions
        strides (int): Conv2D square stride dimensions
        activation (string): activation name
        batch_normalization (bool): whether to include batch normalization
        conv_first (bool): conv-bn-activation (True) or
            bn-activation-conv (False)
    # Returns
        x (tensor): tensor as input to the next layer
    """
    conv = Conv2D(num_filters,
                  kernel_size=kernel_size,
                  strides=strides,
                  padding='same',
                  use_bias=True,
                  kernel_initializer='he_normal',
                  kernel_regularizer=l2(1e-4))

    x = inputs
    if conv_first:
        x = conv(x)
        # if batch_normalization:
        #     x = BatchNormalization()(x)
        if activation is not None:
            x = Activation(activation)(x)
    else:
        # if batch_normalization:
        #     x = BatchNormalization()(x)
        if activation is not None:
            x = Activation(activation)(x)
        x = conv(x)
    return x

def resnet_v2(input_shape, depth, num_classes=10):
    """ResNet Version 2 Model builder [b]
    Stacks of (1 x 1)-(3 x 3)-(1 x 1) BN-ReLU-Conv2D or also known as
    bottleneck layer
    First shortcut connection per layer is 1 x 1 Conv2D.
    Second and onwards shortcut connection is identity.
    At the beginning of each stage, the feature map size is halved (downsampled)
    by a convolutional layer with strides=2, while the number of filter maps is
    doubled. Within each stage, the layers have the same number filters and the
    same filter map sizes.
    Features maps sizes:
    conv1  : 32x32,  16
    stage 0: 32x32,  64
    stage 1: 16x16, 128
    stage 2:  8x8,  256
    # Arguments
        input_shape (tensor): shape of input image tensor
        depth (int): number of core convolutional layers
        num_classes (int): number of classes (CIFAR10 has 10)
    # Returns
        model (Model): Keras model instance
    """
    if (depth - 2) % 9 != 0:
        raise ValueError('depth should be 9n+2 (eg 56 or 110 in [b])')
    # Start model definition.
    num_filters_in = 4
    num_res_blocks = int((depth - 2) / 9)

    inputs = Input(shape=input_shape)
    # v2 performs Conv2D with BN-ReLU on input before splitting into 2 paths
    x = resnet_layer(inputs=inputs,
                     num_filters=num_filters_in,
                     conv_first=True)

    # Instantiate the stack of residual units
    for stage in range(1):
        for res_block in range(num_res_blocks):
            activation = 'relu'
            batch_normalization = True
            strides = 1
            if stage == 0:
                num_filters_out = num_filters_in * 4
                if res_block == 0:  # first layer and first stage
                    activation = None
                    batch_normalization = False
            else:
                num_filters_out = num_filters_in * 2
                if res_block == 0:  # first layer but not first stage
                    strides = 2    # downsample

            # bottleneck residual unit
            y = resnet_layer(inputs=x,
                             num_filters=num_filters_in,
                             kernel_size=1,
                             strides=strides,
                             activation=activation,
                             batch_normalization=batch_normalization,
                             conv_first=False)
            y = resnet_layer(inputs=y,
                             num_filters=num_filters_in,
                             conv_first=False)

            y = resnet_layer(inputs=y,
                             num_filters=num_filters_out,
                             kernel_size=1,
                             conv_first=False)
            if res_block == 0:
                # linear projection residual shortcut connection to match
                # changed dims
                x = resnet_layer(inputs=x,
                                 num_filters=num_filters_out,
                                 kernel_size=1,
                                 strides=strides,
                                 activation=None,
                                 batch_normalization=False)
            x = tensorflow.keras.layers.add([x, y])

        num_filters_in = num_filters_out

    # Add classifier on top.
    # v2 has BN-ReLU before Pooling
    # x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = AveragePooling2D(pool_size=8)(x)
    y = Flatten()(x)
    outputs = Dense(num_classes,
                    activation='softmax',
                    kernel_initializer='he_normal')(y)

    # Instantiate model.
    model = Model(inputs=inputs, outputs=outputs)
    return model

# Training parameters
batch_size = 128  # orig paper trained all networks with batch_size=128
epochs = 1
num_classes = 10

# Subtracting pixel mean improves accuracy
subtract_pixel_mean = True

n = 1
depth = n * 9 + 2

def train():
    # Load the CIFAR10 data.
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()

    # Input image dimensions.
    input_shape = x_train.shape[1:]
    # Normalize data.
    x_train = x_train.astype('float32') / 255
    x_test = x_test.astype('float32') / 255

    x_train_mean = np.mean(x_train, axis=0)
    x_train -= x_train_mean
    x_test -= x_train_mean

    # Convert class vectors to binary class matrices.
    y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes)
    y_test = tensorflow.keras.utils.to_categorical(y_test, num_classes)

    model = resnet_v2(input_shape=input_shape, depth=depth)

    model.compile(loss='categorical_crossentropy',
                optimizer=tensorflow.keras.optimizers.Adam(learning_rate=0.01),
                metrics=['accuracy'])
    model.summary()

    lr_scheduler = LearningRateScheduler(lr_schedule)

    lr_reducer = ReduceLROnPlateau(factor=np.sqrt(0.1),
                                cooldown=0,
                                patience=5,
                                min_lr=0.5e-6)

    callbacks = [lr_reducer, lr_scheduler]

    # Run training, with or without data augmentation.
    model.fit(x_train, y_train,
                batch_size=batch_size,
                epochs=epochs,
                validation_data=(x_test, y_test),
                shuffle=True,
                callbacks=callbacks)

    # Score trained model.
    scores = model.evaluate(x_test, y_test, verbose=1)
    print('Test loss:', scores[0])
    print('Test accuracy:', scores[1])
    model.save("baseline_model")

class TrainDataset(object):
    def __init__(self):
        (x_train, y_train), (x_test, y_test) = cifar10.load_data()
        x_train, y_train = x_train[:100], y_train[:100]
        x_train = x_train.astype('float32') / 255
        x_test = x_test.astype('float32') / 255

        # If subtract pixel mean is enabled
        x_train_mean = np.mean(x_train, axis=0)
        x_train -= x_train_mean
        x_test -= x_train_mean

        # Convert class vectors to binary class matrices.
        y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes)
        y_test = tensorflow.keras.utils.to_categorical(y_test, num_classes)
        self.test_images = x_test
        self.test_labels = y_test
        self.train_images = x_train
        self.train_labels = y_train

    def __len__(self):
        return len(self.train_images)

    def __getitem__(self, idx):
        return self.train_images[idx], self.train_labels[idx]

class EvalDataset(object):
    def __init__(self):
        (x_train, y_train), (x_test, y_test) = cifar10.load_data()

        x_train = x_train.astype('float32') / 255
        x_test = x_test.astype('float32') / 255

        # If subtract pixel mean is enabled
        x_train_mean = np.mean(x_train, axis=0)
        x_train -= x_train_mean
        x_test -= x_train_mean

        # Convert class vectors to binary class matrices.
        y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes)
        y_test = tensorflow.keras.utils.to_categorical(y_test, num_classes)
        self.test_images = x_test
        self.test_labels = y_test

    def __len__(self):
        return len(self.test_images)

    def __getitem__(self, idx):
        return self.test_images[idx], self.test_labels[idx]

class TestTensorflowPruning(unittest.TestCase):
    def setUp(self):
        logger.info(f"CPU: {cpuinfo.get_cpu_info()['brand_raw']}")
        logger.info(f"Test: {sys.modules[__name__].__file__}-{self.__class__.__name__}-{self._testMethodName}")

    def tearDown(self):
        logger.info(f"{self._testMethodName} done.\\n")

    def test_tensorflow_pruning(self):
        from neural_compressor.experimental import Pruning, common
        from neural_compressor.utils import logger
        prune = Pruning("./fake_yaml.yaml")
        prune.train_distributed = True
        prune.evaluation_distributed = True
        prune.train_dataloader = common.DataLoader(TrainDataset(), batch_size=16)
        prune.eval_dataloader = common.DataLoader(EvalDataset(), batch_size=32)
        prune.model = './baseline_model'
        pruned_model = prune()
        stats, sparsity = pruned_model.report_sparsity()
        logger.info(stats)
        logger.info(sparsity)
        self.assertGreater(sparsity, 20)
        self.assertGreater(prune.baseline_score, 0.729)
        if bool(CpuInfo().bf16):
            self.assertGreater(prune.last_score, 0.742)
        else:
            self.assertGreater(prune.last_score, 0.743)


if __name__ == '__main__':
    unittest.main()
    '''
    with open("fake_ut.py", "w", encoding="utf-8") as f:
        f.write(fake_ut)
        build_fake_yaml()


def build_fake_yaml():
    fake_yaml = """
    model:
      name: resnet_v2_prune
      framework: tensorflow
    pruning:
      train:
        epoch: 4
        optimizer:
          SGD:
            learning_rate: 0.001
            momentum: 0.1
            nesterov: True
            weight_decay: 0.1
        criterion:
          CrossEntropyLoss:
            reduction: sum
      approach:
        weight_compression:
          initial_sparsity: 0.0
          target_sparsity: 0.2
          start_epoch: 0
          end_epoch: 4
          pruners:
            - !Pruner
                start_epoch: 1
                end_epoch: 3
                prune_type: basic_magnitude
    evaluation:
      accuracy:
        metric:
          topk: 1
    """
    with open("fake_yaml.yaml", "w", encoding="utf-8") as f:
        f.write(fake_yaml)


def dir_md5_check(dir):
    files_list = []
    md5_list = []

    def get_files_list(path, list_name):
        for file in sorted(os.listdir(path)):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                get_files_list(file_path, list_name)
            else:
                list_name.append(file_path)

    get_files_list(dir, files_list)
    for file_path in files_list:
        with open(file_path, "rb") as fp:
            data = fp.read()
        file_md5 = hashlib.md5(data).hexdigest()
        md5_list.append(file_md5)
    return md5_list


class TestDistributed(unittest.TestCase):
    dst_path = "./baseline_model"

    @classmethod
    def setUpClass(cls):
        build_fake_ut()
        build_fake_yaml()
        if system().lower() == "windows":
            shutil.copytree("C:\\tmp\\.neural_compressor\\inc_ut\\resnet_v2\\", os.getcwd(), dirs_exist_ok=True)
        elif system().lower() == "linux":
            shutil.copytree("/tmp/.neural_compressor/inc_ut/resnet_v2/", os.getcwd(), dirs_exist_ok=True)
        if not os.path.exists(cls.dst_path):
            raise FileNotFoundError(f"'{cls.dst_path}' doesn't exist.")
        elif dir_md5_check(cls.dst_path) != [
            "65625fef42f44e6853d4d6d5e4188a49",
            "a783396652bf62db3db4c9f647953175",
            "c7259753419d9fc053df5b2059aef8c0",
            "77f2a1045cffee9f6a43f2594a5627ba",
        ]:
            logger.warning("resnet_v2 baseline_model md5 verification failed.")
            raise ValueError(f"'{cls.dst_path}' md5 verification failed.")
        else:
            logger.info("resnet_v2 baseline_model for TF-spr-base distributed pruning md5 verification succeeded.")

    @classmethod
    def tearDownClass(cls):
        os.remove("fake_ut.py")
        os.remove("fake_yaml.yaml")
        shutil.rmtree("nc_workspace", ignore_errors=True)
        shutil.rmtree("baseline_model", ignore_errors=True)

    def setUp(self):
        logger.info(f"CPU: {cpuinfo.get_cpu_info()['brand_raw']}")
        logger.info(f"Test: {sys.modules[__name__].__file__}-{self.__class__.__name__}-{self._testMethodName}")

    def tearDown(self):
        logger.info(f"{self._testMethodName} done.\n")

    @unittest.skipIf(version1_lt_version2(tf.version.VERSION, "2.10.0"), "Only test TF 2.10.0 or above")
    def test_tf_distributed_pruning(self):
        distributed_cmd = "horovodrun -np 2 python fake_ut.py"
        p = subprocess.Popen(
            distributed_cmd, preexec_fn=os.setsid, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True
        )
        try:
            out, _ = p.communicate()
            for line in out.splitlines():
                print(line.decode().strip())
            matches = re.findall(r"FAILED", out.decode("utf-8"))
            self.assertEqual(matches, [])

            matches = re.findall(r"OK", out.decode("utf-8"))
            self.assertTrue(len(matches) > 0)
        except KeyboardInterrupt:
            os.killpg(os.getpgid(p.pid), signal.SIGKILL)
            assert 0


if __name__ == "__main__":
    unittest.main()
