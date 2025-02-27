# -*- coding: utf-8 -*-
# Copyright (c) 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Profiling class factory."""

from typing import Optional

from neural_compressor.experimental.data.dataloaders.onnxrt_dataloader import ONNXRTDataLoader
from neural_compressor.model.onnx_model import ONNXModel
from neural_compressor.profiling.profiler.onnxrt_profiler.profiler import Profiler


class ProfilerFactory:
    """Profiler factory."""

    @staticmethod
    def get_profiler(
        model: ONNXModel,
        dataloader: ONNXRTDataLoader,
        log_file: Optional[str] = None,
        *args,
        **kwargs,
    ) -> Profiler:
        """Get profiling for specified framework.

        Args:
            model: model to be profiled
            dataloader: DataLoader object
            log_file: optional path to log file

        Returns:
            Profiler instance if model is supported else None
        """
        return Profiler(model, dataloader, log_file)
