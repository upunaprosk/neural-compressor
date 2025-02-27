# Installation

1. [Linux Installation](#linux-installation)

    1.1. [Prerequisites](#prerequisites)

    1.2. [Install from Binary](#install-from-binary)

    1.3. [Install from Source](#install-from-source)

    1.4. [Install from AI Kit](#install-from-ai-kit)

2. [Windows Installation](#windows-installation)

    2.1. [Prerequisites](#prerequisites-1)

    2.2. [Install from Binary](#install-from-binary-1)

    2.3. [Install from Source](#install-from-source-1)

3. [System Requirements](#system-requirements)

   3.1. [Validated Hardware Environment](#validated-hardware-environment)

   3.2. [Validated Software Environment](#validated-software-environment)

## Linux Installation
### Prerequisites
You can install Neural Compressor using one of three options: Install single component from binary or source, or get the Intel-optimized framework together with the library by installing the [Intel® oneAPI AI Analytics Toolkit](https://software.intel.com/content/www/us/en/develop/tools/oneapi/ai-analytics-toolkit.html).

The following prerequisites and requirements must be satisfied for a successful installation:

- Python version: 3.7 or 3.8 or 3.9 or 3.10 or 3.11

> Notes:
> - If you get some build issues, please check [frequently asked questions](faq.md) at first.

### Install from Binary

  ```Shell
  # install stable basic version from pypi
  pip install neural-compressor
  ```

  ```Shell
  # install nightly version
  git clone https://github.com/intel/neural-compressor.git
  cd neural-compressor
  pip install -r requirements.txt
  # install nightly basic version from pypi
  pip install -i https://test.pypi.org/simple/ neural-compressor
  ```

  ```Shell
  # install stable basic version from from conda
  conda install neural-compressor -c conda-forge -c intel
  ```

### Install from Source

  ```Shell
  git clone https://github.com/intel/neural-compressor.git
  cd neural-compressor
  pip install -r requirements.txt
  # build with basic functionality
  python setup.py install
  ```

### Install from AI Kit

The Intel® Neural Compressor library is released as part of the [Intel® oneAPI AI Analytics Toolkit](https://software.intel.com/content/www/us/en/develop/tools/oneapi/ai-analytics-toolkit.html) (AI Kit). The AI Kit provides a consolidated package of Intel's latest deep learning and machine optimizations all in one place for ease of development. Along with Neural Compressor, the AI Kit includes Intel-optimized versions of deep learning frameworks (such as TensorFlow and PyTorch) and high-performing Python libraries to streamline end-to-end data science and AI workflows on Intel architectures.

The AI Kit is distributed through many common channels, including from Intel's website, YUM, APT, Anaconda, and more. Select and [download](https://software.intel.com/content/www/us/en/develop/tools/oneapi/ai-analytics-toolkit/download.html) the AI Kit distribution package that's best suited for you and follow the [Get Started Guide](https://software.intel.com/content/www/us/en/develop/documentation/get-started-with-ai-linux/top.html) for post-installation instructions.

|Download|Guide|
|-|-|
|[Download AI Kit](https://software.intel.com/content/www/us/en/develop/tools/oneapi/ai-analytics-toolkit/) |[AI Kit Get Started Guide](https://software.intel.com/content/www/us/en/develop/documentation/get-started-with-ai-linux/top.html) |

## Windows Installation

### Prerequisites

The following prerequisites and requirements must be satisfied for a successful installation:

- Python version: 3.7 or 3.8 or 3.9 or 3.10 or 3.11

### Install from Binary

  ```Shell
  # install stable basic version from pypi
  pip install neural-compressor
  ```

  ```Shell
  # install stable basic version from from conda
  conda install pycocotools -c esri
  conda install neural-compressor -c conda-forge -c intel
  ```

### Install from Source

```Shell
  git clone https://github.com/intel/neural-compressor.git
  cd neural-compressor
  pip install -r requirements.txt
  # build with basic functionality
  python setup.py install
  ```

## System Requirements

### Validated Hardware Environment
#### Intel® Neural Compressor supports CPUs based on [Intel 64 architecture or compatible processors](https://en.wikipedia.org/wiki/X86-64):

* Intel Xeon Scalable processor (formerly Skylake, Cascade Lake, Cooper Lake, Ice Lake, and Sapphire Rapids)
* Intel Xeon CPU Max Series (formerly Sapphire Rapids HBM)

#### Intel® Neural Compressor supports GPUs built on Intel's Xe architecture:

* Intel Data Center GPU Flex Series (formerly Arctic Sound-M)
* Intel Data Center GPU Max Series (formerly Ponte Vecchio)

#### Intel® Neural Compressor quantized ONNX models support multiple hardware vendors through ONNX Runtime:

* Intel CPU, AMD/ARM CPU, and NVidia GPU. Please refer to the validated model [list](./validated_model_list.md#validated-onnx-qdq-int8-models-on-multiple-hardware-through-onnx-runtime).

### Validated Software Environment

* OS version: CentOS 8.4, Ubuntu 22.04
* Python version: 3.7, 3.8, 3.9, 3.10, 3.11

<table class="docutils">
<thead>
  <tr style="vertical-align: middle; text-align: center;">
    <th>Framework</th>
    <th>TensorFlow</th>
    <th>Intel<br>TensorFlow</th>
    <th>Intel®<br>Extension for<br>TensorFlow*</th>
    <th>PyTorch</th>
    <th>Intel®<br>Extension for<br>PyTorch*</th>
    <th>ONNX<br>Runtime</th>
    <th>MXNet</th>
  </tr>
</thead>
<tbody>
  <tr align="center">
    <th>Version</th>
    <td class="tg-7zrl"> <a href=https://github.com/tensorflow/tensorflow/tree/v2.13.0>2.13.0</a><br>
    <a href=https://github.com/tensorflow/tensorflow/tree/v2.12.1>2.12.1</a><br>
    <a href=https://github.com/tensorflow/tensorflow/tree/v2.11.1>2.11.1</a><br></td>
    <td class="tg-7zrl"> <a href=https://github.com/Intel-tensorflow/tensorflow/tree/v2.13.0>2.13.0</a><br>
    <a href=https://github.com/Intel-tensorflow/tensorflow/tree/v2.12.0>2.12.0</a><br>
    <a href=https://github.com/Intel-tensorflow/tensorflow/tree/v2.11.0>2.11.0</a><br></td>
    <td class="tg-7zrl"> <a href=https://github.com/intel/intel-extension-for-tensorflow/tree/v2.13.0.0>v2.13.0.0</a><br>
    <a href=https://github.com/intel/intel-extension-for-tensorflow/tree/v1.2.0>1.2.0</a><br>
    <a href=https://github.com/intel/intel-extension-for-tensorflow/tree/v1.1.0>1.1.0</a></td>
    <td class="tg-7zrl"><a href=https://github.com/pytorch/pytorch/tree/v2.0.1>2.0.1+cpu</a><br>
    <a href=https://github.com/pytorch/pytorch/tree/v1.13.1>1.13.1+cpu</a><br>
    <a href=https://github.com/pytorch/pytorch/tree/v1.12.1>1.12.1+cpu</a><br></td>
    <td class="tg-7zrl"><a href=https://github.com/intel/intel-extension-for-pytorch/tree/v2.0.100+cpu>2.0.1+cpu</a><br>
    <a href=https://github.com/intel/intel-extension-for-pytorch/tree/v1.13.100+cpu>1.13.1+cpu</a><br>
    <a href=https://github.com/intel/intel-extension-for-pytorch/tree/v1.12.100>1.12.1+cpu</a><br></td>
    <td class="tg-7zrl"><a href=https://github.com/microsoft/onnxruntime/tree/v1.15.1>1.15.1</a><br>
    <a href=https://github.com/microsoft/onnxruntime/tree/v1.14.1>1.14.1</a><br>
    <a href=https://github.com/microsoft/onnxruntime/tree/v1.13.1>1.13.1</a><br></td>
    <td class="tg-7zrl"><a href=https://github.com/apache/incubator-mxnet/tree/1.9.1>1.9.1</a><br></td>
  </tr>
</tbody>
</table>

> **Note:**
> Set the environment variable ``TF_ENABLE_ONEDNN_OPTS=1`` to enable oneDNN optimizations if you are using TensorFlow before v2.9. oneDNN is the default for TensorFlow since [v2.9](https://github.com/tensorflow/tensorflow/releases/tag/v2.9.0) ([Intel Cascade Lake](https://www.intel.com/content/www/us/en/products/platforms/details/cascade-lake.html) and newer CPUs).
