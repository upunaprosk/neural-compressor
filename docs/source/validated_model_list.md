
Validated Models
======
Intel® Neural Compressor validated examples with multiple compression techniques. The typical examples link can be found in [example tables](https://github.com/intel/neural-compressor/blob/master/examples/README.md), and the performance/accuracy results is available here.

1. [Validated Quantization Examples](#Validated-Quantization-Examples)

    1.1. [TensorFlow Models with Intel TensorFlow 2.12.0](#tensorflow-models-with-Intel-tensorflow-2120)

    1.2. [TensorFlow Models with Intel® Extension for TensorFlow* 1.2.0](#tensorflow-models-with-intel-extension-for-tensorflow-120)

    1.3. [PyTorch Models with Torch 2.0.1+cpu in PTQ Mode](#pytorch-models-with-torch-201cpu-in-ptq-mode)

    1.4. [PyTorch Models with Torch 2.0.1+cpu in QAT Mode](#pytorch-models-with-torch-201cpu-in-qat-mode)

    1.5. [PyTorch Models with Intel® Extension for PyTorch* 2.0.1+cpu](#pytorch-models-with-intel-extension-for-pytorch-201cpu)

    1.6. [PyTorch Models with Torch 2.0.1+cpu in WOQ Mode](#pytorch-models-with-torch-201cpu-in-woq-mode)

    1.7. [ONNX Models with ONNX Runtime 1.15.0](#onnx-models-with-onnx-runtime-1150)

    1.8. [ONNX Models with ONNX Runtime 1.15.0 in WOQ Mode](#onnx-models-with-onnx-runtime-1150-in-woq-mode)

3. [Validated Pruning Examples](#Validated-Pruning-Examples)

4. [Validated Knowledge Distillation Examples](#Validated-Knowledge-Distillation-Examples)

5. [Validated ONNX QDQ INT8 Models on Multiple Hardware through ONNX Runtime](#validated-onnx-qdq-int8-models-on-multiple-hardware-through-onnx-runtime)

## Validated Quantization Examples

System summary: Test by Intel on 06/19/2023. 1-node, 1x Intel(R) Xeon(R) Platinum 8480+ @3.8GHz, 56 cores/socket, HT On, Turbo On, Total Memory 256GB (16x16GB DDR5 4800 MT/s [4800 MT/s]), BIOS 3A14.TEL2P1, microcode 0x2b0001b0,   
CentOS Stream 8, gcc (GCC) 8.5.0 20210514 (Red Hat 8.5.0-10), DL Models, Frameworks: TensorFlow/ONNXRT/PyTorch, Datatype: FP32/INT8/BF16.  
Using 1 socket, 4 cores/instance, 14 instances and batch size 1 to benchmark most of the model.  
Using 1 socket, 56 cores/instance, 1 instance and batch size 1 for some large models performance measurement.   

Performance varies by use, configuration and other factors.  
For more complete information about performance and benchmark results, visit www.intel.com/benchmarks

### TensorFlow Models with Intel TensorFlow 2.12.0

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s4c14ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>ResNet50 v1.0</td>
    <td>pb</td>
    <td>74.12%</td>
    <td>74.27%</td>
    <td>-0.21%</td>
    <td>2721.21</td>
    <td>638.25</td>
    <td>4.26x</td>
  </tr>
  <tr>
    <td>ResNet50 v1.5</td>
    <td>pb</td>
    <td>76.23%</td>
    <td>76.46%</td>
    <td>-0.31%</td>
    <td>2123.70</td>
    <td>552.94</td>
    <td>3.84x</td>
  </tr>
  <tr>
    <td>ResNet101</td>
    <td>pb</td>
    <td>77.50%</td>
    <td>76.45%</td>
    <td>1.37%</td>
    <td>1477.29</td>
    <td>432.29</td>
    <td>3.42x</td>
  </tr>
  <tr>
    <td>Inception V1</td>
    <td>pb</td>
    <td>70.44%</td>
    <td>69.74%</td>
    <td>1.01%</td>
    <td>3267.92</td>
    <td>1266.03</td>
    <td>2.58x</td>
  </tr>
  <tr>
    <td>Inception V2</td>
    <td>pb</td>
    <td>74.38%</td>
    <td>73.97%</td>
    <td>0.57%</td>
    <td>2399.76</td>
    <td>1098.67</td>
    <td>2.18x</td>
  </tr>
  <tr>
    <td>Inception V3</td>
    <td>pb</td>
    <td>76.71%</td>
    <td>76.75%</td>
    <td>-0.05%</td>
    <td>1593.59</td>
    <td>508.58</td>
    <td>3.13x</td>
  </tr>
  <tr>
    <td>Inception V4</td>
    <td>pb</td>
    <td>80.18%</td>
    <td>80.27%</td>
    <td>-0.11%</td>
    <td>1032.10</td>
    <td>249.39</td>
    <td>4.14x</td>
  </tr>
  <tr>
    <td>Inception ResNet V2</td>
    <td>pb</td>
    <td>80.34%</td>
    <td>80.40%</td>
    <td>-0.07%</td>
    <td>427.28</td>
    <td>185.60</td>
    <td>2.30x</td>
  </tr>
  <tr>
    <td>MobileNet V1</td>
    <td>pb</td>
    <td>71.78%</td>
    <td>70.96%</td>
    <td>1.16%</td>
    <td>5503.87</td>
    <td>1791.62</td>
    <td>3.07x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>pb</td>
    <td>72.52%</td>
    <td>71.76%</td>
    <td>1.07%</td>
    <td>3639.83</td>
    <td>1864.72</td>
    <td>1.95x</td>
  </tr>
  <tr>
    <td>VGG16</td>
    <td>pb</td>
    <td>72.64%</td>
    <td>70.89%</td>
    <td>2.47%</td>
    <td>1538.21</td>
    <td>236.22</td>
    <td>6.51x</td>
  </tr>
  <tr>
    <td>VGG19</td>
    <td>pb</td>
    <td>72.69%</td>
    <td>71.01%</td>
    <td>2.37%</td>
    <td>1368.21</td>
    <td>196.94</td>
    <td>6.95x</td>
  </tr>
  <tr>
    <td>ResNetV2 50</td>
    <td>pb</td>
    <td>70.44%</td>
    <td>69.64%</td>
    <td>1.15%</td>
    <td>1105.19</td>
    <td>657.45</td>
    <td>1.68x</td>
  </tr>
  <tr>
    <td>ResNetV2 101</td>
    <td>pb</td>
    <td>72.65%</td>
    <td>71.87%</td>
    <td>1.08%</td>
    <td>716.49</td>
    <td>369.95</td>
    <td>1.94x</td>
  </tr>
  <tr>
    <td>ResNetV2 152</td>
    <td>pb</td>
    <td>73.07%</td>
    <td>72.37%</td>
    <td>0.97%</td>
    <td>508.60</td>
    <td>269.31</td>
    <td>1.89x</td>
  </tr>
  <tr>
    <td>Densenet 121</td>
    <td>pb</td>
    <td>73.59%</td>
    <td>72.89%</td>
    <td>0.97%</td>
    <td>617.94</td>
    <td>498.43</td>
    <td>1.24x</td>
  </tr>
  <tr>
    <td>Densenet 161</td>
    <td>pb</td>
    <td>76.35%</td>
    <td>76.29%</td>
    <td>0.08%</td>
    <td>372.04</td>
    <td>242.05</td>
    <td>1.54x</td>
  </tr>
  <tr>
    <td>Densenet 169</td>
    <td>pb</td>
    <td>74.34%</td>
    <td>74.65%</td>
    <td>-0.41%</td>
    <td>496.41</td>
    <td>411.94</td>
    <td>1.21x</td>
  </tr>
  <tr>
    <td>EfficientNet B0</td>
    <td>ckpt</td>
    <td>76.14%</td>
    <td>76.76%</td>
    <td>-0.81%</td>
    <td>748.42</td>
    <td>709.43</td>
    <td>1.05x</td>
  </tr>
  <tr>
    <td>SSD ResNet50 V1</td>
    <td>pb</td>
    <td>37.88%</td>
    <td>38.00%</td>
    <td>-0.31%</td>
    <td>134.81</td>
    <td>31.06</td>
    <td>4.34x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1</td>
    <td>pb</td>
    <td>22.98%</td>
    <td>23.13%</td>
    <td>-0.64%</td>
    <td>1273.79</td>
    <td>671.84</td>
    <td>1.90x</td>
  </tr>
  <tr>
    <td>SSD ResNet50 v1</td>
    <td>ckpt</td>
    <td>37.89%</td>
    <td>38.00%</td>
    <td>-0.30%</td>
    <td>136.53</td>
    <td>27.88</td>
    <td>4.90x</td>
  </tr>
  <tr>
    <td>SSD MobileNet v1</td>
    <td>ckpt</td>
    <td>22.96%</td>
    <td>23.13%</td>
    <td>-0.72%</td>
    <td>1235.03</td>
    <td>477.83</td>
    <td>2.58x</td>
  </tr>
  <tr>
    <td>SSD ResNet34</td>
    <td>pb</td>
    <td>21.70%</td>
    <td>22.09%</td>
    <td>-1.76%</td>
    <td>179.37</td>
    <td>13.96</td>
    <td>12.85x</td>
  </tr>
  <tr>
    <td>Faster R-CNN Inception ResNet V2</td>
    <td>pb</td>
    <td>37.47%</td>
    <td>38.31%</td>
    <td>-2.18%</td>
    <td>5.39</td>
    <td>3.01</td>
    <td>1.79x</td>
  </tr>
  <tr>
    <td>Faster R-CNN Inception ResNet V2</td>
    <td>SavedModel</td>
    <td>37.79%</td>
    <td>38.31%</td>
    <td>-1.34%</td>
    <td>5.35</td>
    <td>1.89</td>
    <td>2.83x</td>
  </tr>
  <tr>
    <td>Faster R-CNN ResNet101</td>
    <td>pb</td>
    <td>30.32%</td>
    <td>30.39%</td>
    <td>-0.23%</td>
    <td>156.71</td>
    <td>23.50</td>
    <td>6.67x</td>
  </tr>
  <tr>
    <td>Faster R-CNN ResNet101</td>
    <td>SavedModel</td>
    <td>30.33%</td>
    <td>30.39%</td>
    <td>-0.20%</td>
    <td>152.21</td>
    <td>18.50</td>
    <td>8.23x</td>
  </tr>
  <tr>
    <td>Faster R-CNN ResNet50</td>
    <td>pb</td>
    <td>26.64%</td>
    <td>26.59%</td>
    <td>0.21%</td>
    <td>173.07</td>
    <td>28.83</td>
    <td>6.00x</td>
  </tr>
  <tr>
    <td>YOLOv3</td>
    <td>pb</td>
    <td>82.13%</td>
    <td>82.35%</td>
    <td>-0.28%</td>
    <td>211.67</td>
    <td>87.89</td>
    <td>2.41x</td>
  </tr>
  <tr>
    <td>BERT large SQuAD</td>
    <td>pb</td>
    <td>92.47</td>
    <td>92.99</td>
    <td>-0.56%</td>
    <td>46.87</td>
    <td>16.65</td>
    <td>2.82x</td>
  </tr>
  <tr>
    <td>BERT large SQuAD (ONNX Model Zoo)</td>
    <td>pb</td>
    <td>92.42</td>
    <td>92.98</td>
    <td>-0.61%</td>
    <td>42.35</td>
    <td>17.03</td>
    <td>2.49x</td>
  </tr>
  <tr>
    <td>BERT base MRPC</td>
    <td>ckpt</td>
    <td>86.03%</td>
    <td>86.52%</td>
    <td>-0.57%</td>
    <td>424.94</td>
    <td>174.10</td>
    <td>2.44x</td>
  </tr>
  <tr>
    <td>Transformer LT</td>
    <td>pb</td>
    <td>25.77</td>
    <td>25.86</td>
    <td>-0.34%</td>
    <td>42.11</td>
    <td>22.11</td>
    <td>1.90x</td>
  </tr>
  <tr>
    <td>Transformer lt MLPerf</td>
    <td>pb</td>
    <td>27.10</td>
    <td>27.17</td>
    <td>-0.25%</td>
    <td>9.82</td>
    <td>4.29</td>
    <td>2.29x</td>
  </tr>
  <tr>
    <td>Wide Deep large DS</td>
    <td>pb</td>
    <td>77.75%</td>
    <td>77.67%</td>
    <td>0.10%</td>
    <td>55612.97</td>
    <td>43479.53</td>
    <td>1.28x</td>
  </tr>
</tbody>
</table>

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s56c1ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>Mask R-CNN Inception V2</td>
    <td>pb</td>
    <td>28.60%</td>
    <td>28.73%</td>
    <td>-0.44%</td>
    <td>39.35</td>
    <td>23.84</td>
    <td>1.65x</td>
  </tr>
  <tr>
    <td>Mask R-CNN Inception V2</td>
    <td>ckpt</td>
    <td>28.60%</td>
    <td>28.73%</td>
    <td>-0.44%</td>
    <td>40.21</td>
    <td>23.90</td>
    <td>1.68x</td>
  </tr>
  <tr>
    <td>GPT2</td>
    <td>pb</td>
    <td>66.89%</td>
    <td>67.57%</td>
    <td>-1.00%</td>
    <td>9.67</td>
    <td>7.22</td>
    <td>1.34x</td>
  </tr>
</tbody>
</table>

### TensorFlow Models with Intel® Extension for TensorFlow* 1.2.0

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s4c14ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>ResNet50 v1.0</td>
    <td>pb</td>
    <td>74.16%</td>
    <td>74.27%</td>
    <td>-0.15%</td>
    <td>2716.04</td>
    <td>569.18</td>
    <td>4.77x</td>
  </tr>
  <tr>
    <td>ResNet50 v1.5</td>
    <td>pb</td>
    <td>76.27%</td>
    <td>76.46%</td>
    <td>-0.26%</td>
    <td>2683.90</td>
    <td>476.14</td>
    <td>5.64x</td>
  </tr>
  <tr>
    <td>Inception V1</td>
    <td>pb</td>
    <td>69.59%</td>
    <td>69.74%</td>
    <td>-0.22%</td>
    <td>2349.32</td>
    <td>1035.63</td>
    <td>2.27x</td>
  </tr>
  <tr>
    <td>Inception V2</td>
    <td>pb</td>
    <td>73.75%</td>
    <td>73.97%</td>
    <td>-0.30%</td>
    <td>2399.93</td>
    <td>930.62</td>
    <td>2.58x</td>
  </tr>
  <tr>
    <td>Inception V4</td>
    <td>pb</td>
    <td>80.03%</td>
    <td>80.27%</td>
    <td>-0.31%</td>
    <td>763.85</td>
    <td>262.22</td>
    <td>2.91x</td>
  </tr>
  <tr>
    <td>MobileNet V1</td>
    <td>pb</td>
    <td>70.61%</td>
    <td>70.96%</td>
    <td>-0.48%</td>
    <td>4003.12</td>
    <td>1677.22</td>
    <td>2.39x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>pb</td>
    <td>71.15%</td>
    <td>71.76%</td>
    <td>-0.85%</td>
    <td>2766.36</td>
    <td>2643.21</td>
    <td>1.05x</td>
  </tr>
  <tr>
    <td>VGG16</td>
    <td>pb</td>
    <td>70.84%</td>
    <td>70.89%</td>
    <td>-0.07%</td>
    <td>1495.88</td>
    <td>238.52</td>
    <td>6.27x</td>
  </tr>
  <tr>
    <td>VGG19</td>
    <td>pb</td>
    <td>71.03%</td>
    <td>71.01%</td>
    <td>0.03%</td>
    <td>1372.91</td>
    <td>199.52</td>
    <td>6.88x</td>
  </tr>
  <tr>
    <td>ResNetV2 50</td>
    <td>pb</td>
    <td>69.43%</td>
    <td>69.64%</td>
    <td>-0.30%</td>
    <td>1457.53</td>
    <td>630.41</td>
    <td>2.31x</td>
  </tr>
  <tr>
    <td>ResNetV2 101</td>
    <td>pb</td>
    <td>71.84%</td>
    <td>71.87%</td>
    <td>-0.05%</td>
    <td>842.53</td>
    <td>338.44</td>
    <td>2.49x</td>
  </tr>
  <tr>
    <td>ResNetV2 152</td>
    <td>pb</td>
    <td>72.26%</td>
    <td>72.37%</td>
    <td>-0.15%</td>
    <td>645.86</td>
    <td>231.63</td>
    <td>2.79x</td>
  </tr>
  <tr>
    <td>EfficientNet B0</td>
    <td>ckpt</td>
    <td>76.76%</td>
    <td>76.76%</td>
    <td>0.00%</td>
    <td>938.82</td>
    <td>707.22</td>
    <td>1.33x</td>
  </tr>
  <tr>
    <td>EfficientNet V2 B0</td>
    <td>SavedModel</td>
    <td>78.63%</td>
    <td>78.62%</td>
    <td>0.01%</td>
    <td>1533.95</td>
    <td>1258.45</td>
    <td>1.22x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1</td>
    <td>pb</td>
    <td>22.90%</td>
    <td>23.13%</td>
    <td>-0.99%</td>
    <td>981.29</td>
    <td>647.07</td>
    <td>1.52x</td>
  </tr>
  <tr>
    <td>SSD MobileNet v1</td>
    <td>ckpt</td>
    <td>22.92%</td>
    <td>23.13%</td>
    <td>-0.89%</td>
    <td>850.31</td>
    <td>444.12</td>
    <td>1.91x</td>
  </tr>
  <tr>
    <td>Faster R-CNN Inception ResNet V2</td>
    <td>pb</td>
    <td>38.02%</td>
    <td>38.31%</td>
    <td>-0.74%</td>
    <td>7.08</td>
    <td>2.93</td>
    <td>2.42x</td>
  </tr>
  <tr>
    <td>Faster R-CNN Inception ResNet V2</td>
    <td>SavedModel</td>
    <td>38.18%</td>
    <td>38.31%</td>
    <td>-0.32%</td>
    <td>6.61</td>
    <td>2.79</td>
    <td>2.37x</td>
  </tr>
  <tr>
    <td>YOLOv3</td>
    <td>pb</td>
    <td>80.27%</td>
    <td>82.35%</td>
    <td>-2.53%</td>
    <td>543.50</td>
    <td>80.59</td>
    <td>6.74x</td>
  </tr>
  <tr>
    <td>BERT large SQuAD</td>
    <td>pb</td>
    <td>92.67</td>
    <td>92.97</td>
    <td>-0.33%</td>
    <td>72.27</td>
    <td>18.39</td>
    <td>3.93x</td>
  </tr>
  <tr>
    <td>BERT base MRPC</td>
    <td>ckpt</td>
    <td>86.28%</td>
    <td>86.28%</td>
    <td>0.00%</td>
    <td>947.96</td>
    <td>233.07</td>
    <td>4.07x</td>
  </tr>
  <tr>
    <td>DistilBERT base</td>
    <td>pb</td>
    <td>90.48%</td>
    <td>91.06%</td>
    <td>-0.64%</td>
    <td>788.64</td>
    <td>462.35</td>
    <td>1.71x</td>
  </tr>
  <tr>
    <td>Transformer LT</td>
    <td>pb</td>
    <td>25.73</td>
    <td>25.86</td>
    <td>-0.47%</td>
    <td>42.07</td>
    <td>29.21</td>
    <td>1.44x</td>
  </tr>
  <tr>
    <td>Transformer lt MLPerf</td>
    <td>pb</td>
    <td>27.13</td>
    <td>27.17</td>
    <td>-0.14%</td>
    <td>10.43</td>
    <td>4.84</td>
    <td>2.15x</td>
  </tr>
  <tr>
    <td>Wide Deep large DS</td>
    <td>pb</td>
    <td>77.66%</td>
    <td>77.67%</td>
    <td>-0.02%</td>
    <td>51958.00</td>
    <td>39974.56</td>
    <td>1.30x</td>
  </tr>
</tbody>
</table>

### PyTorch Models with Torch 2.0.1+cpu in PTQ Mode

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s4c14ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>ResNet18</td>
    <td>static</td>
    <td>69.61%</td>
    <td>69.76%</td>
    <td>-0.22%</td>
    <td>1631.83</td>
    <td>662.13</td>
    <td>2.46x</td>
  </tr>
  <tr>
    <td>ResNet50</td>
    <td>static</td>
    <td>75.92%</td>
    <td>76.15%</td>
    <td>-0.30%</td>
    <td>1162.83</td>
    <td>330.92</td>
    <td>3.51x</td>
  </tr>
  <tr>
    <td>Inception V3</td>
    <td>static</td>
    <td>69.47%</td>
    <td>69.52%</td>
    <td>-0.07%</td>
    <td>968.67</td>
    <td>334.53</td>
    <td>2.90x</td>
  </tr>
  <tr>
    <td>ResNeSt50</td>
    <td>static</td>
    <td>80.80%</td>
    <td>81.04%</td>
    <td>-0.30%</td>
    <td>394.38</td>
    <td>40.76</td>
    <td>9.67x</td>
  </tr>
  <tr>
    <td>ResNeXt101_32x8d</td>
    <td>static</td>
    <td>78.94%</td>
    <td>79.31%</td>
    <td>-0.46%</td>
    <td>558.59</td>
    <td>108.42</td>
    <td>5.15x</td>
  </tr>
  <tr>
    <td>Efficientnet_b0</td>
    <td>static</td>
    <td>76.89%</td>
    <td>77.67%</td>
    <td>-1.01%</td>
    <td>703.73</td>
    <td>656.12</td>
    <td>1.07x</td>
  </tr>
  <tr>
    <td>Efficientnet_b3</td>
    <td>static</td>
    <td>77.82%</td>
    <td>78.54%</td>
    <td>-0.93%</td>
    <td>510.58</td>
    <td>391.05</td>
    <td>1.31x</td>
  </tr>
  <tr>
    <td>Efficientnet_b7</td>
    <td>static</td>
    <td>73.55%</td>
    <td>73.92%</td>
    <td>-0.50%</td>
    <td>233.29</td>
    <td>150.09</td>
    <td>1.55x</td>
  </tr>
  <tr>
    <td>Peleenet</td>
    <td>static</td>
    <td>71.85%</td>
    <td>72.10%</td>
    <td>-0.35%</td>
    <td>857.72</td>
    <td>585.60</td>
    <td>1.46x</td>
  </tr>
  <tr>
    <td>YOLO V3</td>
    <td>static</td>
    <td>55.09%</td>
    <td>54.93%</td>
    <td>0.31%</td>
    <td>160.97</td>
    <td>60.60</td>
    <td>2.66x</td>
  </tr>
  <tr>
    <td>SSD ResNet34</td>
    <td>static</td>
    <td>19.52</td>
    <td>19.63</td>
    <td>-0.58%</td>
    <td>141.67</td>
    <td>11.75</td>
    <td>12.05x</td>
  </tr>
  <tr>
    <td>Roberta base MRPC</td>
    <td>static</td>
    <td>92.69%</td>
    <td>93.59%</td>
    <td>-0.96%</td>
    <td>407.78</td>
    <td>174.53</td>
    <td>2.34x</td>
  </tr>
  <tr>
    <td>CamemBERT base MRPC</td>
    <td>static</td>
    <td>88.93%</td>
    <td>89.28%</td>
    <td>-0.39%</td>
    <td>402.78</td>
    <td>173.56</td>
    <td>2.32x</td>
  </tr>
  <tr>
    <td>DistilBERT base MRPC</td>
    <td>dynamic</td>
    <td>90.20%</td>
    <td>90.27%</td>
    <td>-0.07%</td>
    <td>748.28</td>
    <td>343.54</td>
    <td>2.18x</td>
  </tr>
  <tr>
    <td>DistilBERT base MRPC</td>
    <td>static</td>
    <td>89.53%</td>
    <td>90.27%</td>
    <td>-0.82%</td>
    <td>804.57</td>
    <td>343.24</td>
    <td>2.34x</td>
  </tr>
  <tr>
    <td>ALBERT base MRPC</td>
    <td>static</td>
    <td>92.63%</td>
    <td>92.63%</td>
    <td>0.00%</td>
    <td>352.44</td>
    <td>162.26</td>
    <td>2.17x</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>91.60%</td>
    <td>92.25%</td>
    <td>-0.71%</td>
    <td>302.57</td>
    <td>183.57</td>
    <td>1.65x</td>
  </tr>
  <tr>
    <td>Xlm Roberta MRPC</td>
    <td>static</td>
    <td>88.36%</td>
    <td>88.62%</td>
    <td>-0.29%</td>
    <td>404.61</td>
    <td>173.71</td>
    <td>2.33x</td>
  </tr>
  <tr>
    <td>Xlm Roberta MRPC</td>
    <td>dynamic</td>
    <td>88.24%</td>
    <td>88.24%</td>
    <td>0.00%</td>
    <td>382.72</td>
    <td>174.63</td>
    <td>2.19x</td>
  </tr>
  <tr>
    <td>BERT base MRPC</td>
    <td>static</td>
    <td>89.63%</td>
    <td>90.42%</td>
    <td>-0.87%</td>
    <td>407.58</td>
    <td>173.66</td>
    <td>2.35x</td>
  </tr>
  <tr>
    <td>BERT base COLA</td>
    <td>static</td>
    <td>54.51%</td>
    <td>53.39%</td>
    <td>2.10%</td>
    <td>414.72</td>
    <td>173.86</td>
    <td>2.39x</td>
  </tr>
  <tr>
    <td>BERT base STSB</td>
    <td>static</td>
    <td>87.55%</td>
    <td>88.05%</td>
    <td>-0.57%</td>
    <td>413.76</td>
    <td>173.34</td>
    <td>2.39x</td>
  </tr>
  <tr>
    <td>BERT base SST-2</td>
    <td>static</td>
    <td>91.51%</td>
    <td>92.32%</td>
    <td>-0.87%</td>
    <td>410.87</td>
    <td>173.63</td>
    <td>2.37x</td>
  </tr>
  <tr>
    <td>BERT large COLA</td>
    <td>static</td>
    <td>62.84%</td>
    <td>63.35%</td>
    <td>-0.80%</td>
    <td>138.89</td>
    <td>51.65</td>
    <td>2.69x</td>
  </tr>
  <tr>
    <td>BERT base RTE</td>
    <td>static</td>
    <td>72.56%</td>
    <td>72.56%</td>
    <td>0.00%</td>
    <td>385.23</td>
    <td>173.32</td>
    <td>2.22x</td>
  </tr>
  <tr>
    <td>BERT large MRPC</td>
    <td>static</td>
    <td>90.22%</td>
    <td>90.38%</td>
    <td>-0.17%</td>
    <td>141.61</td>
    <td>51.67</td>
    <td>2.74x</td>
  </tr>
  <tr>
    <td>BERT large QNLI</td>
    <td>static</td>
    <td>90.87%</td>
    <td>91.54%</td>
    <td>-0.74%</td>
    <td>407.84</td>
    <td>173.52</td>
    <td>2.35x</td>
  </tr>
  <tr>
    <td>BERT large RTE</td>
    <td>static</td>
    <td>73.29%</td>
    <td>74.01%</td>
    <td>-0.98%</td>
    <td>141.64</td>
    <td>51.33</td>
    <td>2.76x</td>
  </tr>
  <tr>
    <td>BERT large RTE</td>
    <td>dynamic</td>
    <td>71.48%</td>
    <td>74.01%</td>
    <td>-3.41%</td>
    <td>126.49</td>
    <td>51.34</td>
    <td>2.46x</td>
  </tr>
  <tr>
    <td>BERT large SQuAD</td>
    <td>static</td>
    <td>92.27</td>
    <td>93.16</td>
    <td>-0.95%</td>
    <td>37.61</td>
    <td>16.57</td>
    <td>2.27x</td>
  </tr>
  <tr>
    <td>GPT J WikiText</td>
    <td>static</td>
    <td>3.36</td>
    <td>2.34</td>
    <td>NA</td>
    <td>0.87</td>
    <td>0.28</td>
    <td>3.15x</td>
  </tr>
  <tr>
    <td>Reformer Crime and Punishment</td>
    <td>static</td>
    <td>1.88</td>
    <td>1.87</td>
    <td>0.23%</td>
    <td>449.73</td>
    <td>364.78</td>
    <td>1.23x</td>
  </tr>
  <tr>
    <td>lvwerra/pegasus-samsum</td>
    <td>static</td>
    <td>42.50</td>
    <td>42.67</td>
    <td>-0.39%</td>
    <td>101.32</td>
    <td>37.80</td>
    <td>2.68x</td>
  </tr>
</tbody>
</table>

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s56c1ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>openai/whisper-large</td>
    <td>dynamic</td>
    <td>97.07%</td>
    <td>96.96%</td>
    <td>0.12%</td>
    <td>0.60</td>
    <td>0.47</td>
    <td>1.28x</td>
  </tr>
  <tr>
    <td>abeja/gpt-neox-japanese-2.7b</td>
    <td>static</td>
    <td>4.30</td>
    <td>3.52</td>
    <td>22.06%</td>
    <td>1.03</td>
    <td>0.56</td>
    <td>1.84x</td>
  </tr>
</tbody>
</table>

### PyTorch Models with Torch 2.0.1+cpu in QAT Mode

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s4c14ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>ResNet18</td>
    <td>static</td>
    <td>69.74%</td>
    <td>69.76%</td>
    <td>-0.03%</td>
    <td>1723.70</td>
    <td>654.17</td>
    <td>2.63x</td>
  </tr>
  <tr>
    <td>ResNet50</td>
    <td>static</td>
    <td>76.05%</td>
    <td>76.15%</td>
    <td>-0.12%</td>
    <td>1141.22</td>
    <td>306.04</td>
    <td>3.73x</td>
  </tr>
  <tr>
    <td>ResNeXt101_32x8d</td>
    <td>static</td>
    <td>79.28%</td>
    <td>79.31%</td>
    <td>-0.04%</td>
    <td>558.92</td>
    <td>106.82</td>
    <td>5.23x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>static</td>
    <td>69.73%</td>
    <td>71.84%</td>
    <td>-2.93%</td>
    <td>1379.34</td>
    <td>729.22</td>
    <td>1.89x</td>
  </tr>
  <tr>
    <td>BERT base MRPC</td>
    <td>static</td>
    <td>89.70%</td>
    <td>90.40%</td>
    <td>-0.77%</td>
    <td>389.77</td>
    <td>173.54</td>
    <td>2.25x</td>
  </tr>
</tbody>
</table>

### PyTorch Models with Intel® Extension for PyTorch* 2.0.1+cpu

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s4c14ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>ResNet18</td>
    <td>static</td>
    <td>75.98%</td>
    <td>76.15%</td>
    <td>-0.22%</td>
    <td>1980.94</td>
    <td>672.93</td>
    <td>2.94x</td>
  </tr>
  <tr>
    <td>ResNet50</td>
    <td>static</td>
    <td>69.56%</td>
    <td>69.76%</td>
    <td>-0.29%</td>
    <td>5032.32</td>
    <td>1500.16</td>
    <td>3.35x</td>
  </tr>
  <tr>
    <td>ResNeXt101_32x16d_wsl</td>
    <td>static</td>
    <td>84.04%</td>
    <td>84.17%</td>
    <td>-0.15%</td>
    <td>533.60</td>
    <td>78.84</td>
    <td>6.77x</td>
  </tr>
  <tr>
    <td>SSD ResNet34</td>
    <td>static</td>
    <td>19.93%</td>
    <td>20.00%</td>
    <td>-0.38%</td>
    <td>84.02</td>
    <td>15.68</td>
    <td>5.36x</td>
  </tr>
  <tr>
    <td>bert-large-uncased-whole-word-masking-finetuned-squad</td>
    <td>static</td>
    <td>92.93</td>
    <td>93.16</td>
    <td>-0.25%</td>
    <td>161.44</td>
    <td>22.19</td>
    <td>7.27x</td>
  </tr>
  <tr>
    <td>distilbert-base-uncased-distilled-squad</td>
    <td>static</td>
    <td>86.09</td>
    <td>86.84</td>
    <td>-0.86%</td>
    <td>556.19</td>
    <td>149.79</td>
    <td>3.71x</td>
  </tr>
</tbody>
</table>

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s56c1ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>EleutherAI/gpt-j-6B</td>
    <td>static</td>
    <td>78.60%</td>
    <td>79.20%</td>
    <td>-0.76%</td>
    <td>4.87</td>
    <td>1.55</td>
    <td>3.14x</td>
  </tr>
</tbody>
</table>


### PyTorch Models with Torch 2.0.1+cpu in WOQ Mode

<table class="tg">
<thead>
  <tr>
    <th class="tg-rq3n" rowspan="2">Model name</th>
    <th class="tg-rq3n" rowspan="2">Configuration</th>
    <th class="tg-rq5v">Lambada_openai</th>
    <th class="tg-oo9c">Hellaswag</th>
    <th class="tg-oo9c">Winogrande</th>
    <th class="tg-oo9c">Piqa</th>
    <th class="tg-oo9c" colspan="2">Average<br>[Mean accuracy of previous four tasks]</th>
    <th class="tg-oo9c">Wikitext</th>
  </tr>
  <tr>
    <th class="tg-71nf">Accuracy</th>
    <th class="tg-im72">Accuracy</th>
    <th class="tg-im72">Accuracy</th>
    <th class="tg-im72">Accuracy</th>
    <th class="tg-im72">Accuracy</th>
    <th class="tg-iire">Accuracy Ratio<br>[INT4/FP32]</th>
    <th class="tg-haiz">Word_perplexity</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-rq3n" rowspan="5">EleutherAI/gpt-j-6b</td>
    <td class="tg-rq3n">FP32</td>
    <td class="tg-rq3n">0.6831</td>
    <td class="tg-vxga">0.4954</td>
    <td class="tg-vxga">0.6409</td>
    <td class="tg-vxga">0.7541</td>
    <td class="tg-vxga">0.6434</td>
    <td class="tg-iire">/</td>
    <td class="tg-vxga">10.8816</td>
  </tr>
  <tr>
    <td class="tg-rq3n">GPTQ<br>W4G128Asym</td>
    <td class="tg-rq3n">0.679</td>
    <td class="tg-vxga">0.4895</td>
    <td class="tg-vxga">0.6433</td>
    <td class="tg-vxga">0.7476</td>
    <td class="tg-vxga">0.6399</td>
    <td class="tg-p7cy">0.9945</td>
    <td class="tg-vxga">11.0999</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-vxga">0.6829</td>
    <td class="tg-vxga">0.4923</td>
    <td class="tg-vxga">0.6401</td>
    <td class="tg-vxga">0.7486</td>
    <td class="tg-vxga">0.6410</td>
    <td class="tg-p7cy">0.9963</td>
    <td class="tg-vxga">11.0141</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Sym</td>
    <td class="tg-vxga">0.685</td>
    <td class="tg-vxga">0.4907</td>
    <td class="tg-vxga">0.6361</td>
    <td class="tg-vxga">0.7443</td>
    <td class="tg-vxga">0.6390</td>
    <td class="tg-p7cy">0.9932</td>
    <td class="tg-vxga">11.1498</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Sym</td>
    <td class="tg-vxga">0.6911</td>
    <td class="tg-vxga">0.4899</td>
    <td class="tg-vxga">0.6448</td>
    <td class="tg-vxga">0.7497</td>
    <td class="tg-vxga">0.6439</td>
    <td class="tg-p7cy">1.0008</td>
    <td class="tg-vxga">11.0927</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="3">facebook/opt-6.7b</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.6769</td>
    <td class="tg-vxga">0.5049</td>
    <td class="tg-im72">0.6543</td>
    <td class="tg-im72">0.7628</td>
    <td class="tg-vxga">0.6497</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">12.2862</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.6804</td>
    <td class="tg-folj">0.4984</td>
    <td class="tg-im72">0.6535</td>
    <td class="tg-im72">0.7568</td>
    <td class="tg-vxga">0.6473</td>
    <td class="tg-p7cy">0.9962</td>
    <td class="tg-im72">12.4193</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Sym</td>
    <td class="tg-im72">0.6885</td>
    <td class="tg-vxga">0.4973</td>
    <td class="tg-im72">0.6433</td>
    <td class="tg-im72">0.753</td>
    <td class="tg-vxga">0.6455</td>
    <td class="tg-p7cy">0.9935</td>
    <td class="tg-im72">12.4607</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="2">decapoda-research/llama-7b-hf</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.7361</td>
    <td class="tg-vxga">0.5642</td>
    <td class="tg-im72">0.6709</td>
    <td class="tg-im72">0.7835</td>
    <td class="tg-vxga">0.6887</td>
    <td class="tg-p7cy">/</td>
    <td class="tg-im72">9.4202</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.7244</td>
    <td class="tg-folj">0.5603</td>
    <td class="tg-im72">0.6614</td>
    <td class="tg-im72">0.7835</td>
    <td class="tg-vxga">0.6824</td>
    <td class="tg-p7cy">0.9909</td>
    <td class="tg-im72">9.5881</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="4">decapoda-research/llama-13b-hf</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.7627</td>
    <td class="tg-vxga">0.5911</td>
    <td class="tg-im72">0.7009</td>
    <td class="tg-im72">0.7878</td>
    <td class="tg-vxga">0.7106</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">8.212</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.7518</td>
    <td class="tg-vxga">0.5843</td>
    <td class="tg-im72">0.6961</td>
    <td class="tg-im72">0.7911</td>
    <td class="tg-vxga">0.7058</td>
    <td class="tg-p7cy">0.9932</td>
    <td class="tg-im72">8.4319</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.7572</td>
    <td class="tg-im72">0.5898</td>
    <td class="tg-im72">0.7056</td>
    <td class="tg-im72">0.7894</td>
    <td class="tg-vxga">0.7105</td>
    <td class="tg-p7cy">0.9998</td>
    <td class="tg-im72">8.3429</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Sym</td>
    <td class="tg-im72">0.7596</td>
    <td class="tg-im72">0.5841</td>
    <td class="tg-im72">0.6977</td>
    <td class="tg-im72">0.7905</td>
    <td class="tg-vxga">0.7080</td>
    <td class="tg-p7cy">0.9963</td>
    <td class="tg-im72">8.4916</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="4">decapoda-research/llama-30b-hf</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.7759</td>
    <td class="tg-im72">0.6266</td>
    <td class="tg-im72">0.7277</td>
    <td class="tg-im72">0.8096</td>
    <td class="tg-vxga">0.7350</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">6.2384</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.778</td>
    <td class="tg-im72">0.624</td>
    <td class="tg-im72">0.7269</td>
    <td class="tg-im72">0.8047</td>
    <td class="tg-vxga">0.7334</td>
    <td class="tg-p7cy">0.9979</td>
    <td class="tg-im72">6.4237</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.7706</td>
    <td class="tg-im72">0.6239</td>
    <td class="tg-im72">0.7285</td>
    <td class="tg-im72">0.8058</td>
    <td class="tg-vxga">0.7322</td>
    <td class="tg-p7cy">0.9963</td>
    <td class="tg-im72">6.4697</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Sym</td>
    <td class="tg-im72">0.7836</td>
    <td class="tg-im72">0.6195</td>
    <td class="tg-im72">0.7269</td>
    <td class="tg-im72">0.8047</td>
    <td class="tg-vxga">0.7337</td>
    <td class="tg-p7cy">0.9983</td>
    <td class="tg-im72">6.5604</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="3">meta-llama/Llama-2-7b-chat-hf</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.7058</td>
    <td class="tg-im72">0.5732</td>
    <td class="tg-im72">0.648</td>
    <td class="tg-im72">0.7715</td>
    <td class="tg-vxga">0.6746</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">11.7107</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.6982</td>
    <td class="tg-im72">0.5637</td>
    <td class="tg-im72">0.6527</td>
    <td class="tg-im72">0.7704</td>
    <td class="tg-vxga">0.6713</td>
    <td class="tg-p7cy">0.9950</td>
    <td class="tg-im72">11.9702</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.6953</td>
    <td class="tg-im72">0.5682</td>
    <td class="tg-im72">0.6575</td>
    <td class="tg-im72">0.7758</td>
    <td class="tg-vxga">0.6742</td>
    <td class="tg-p7cy">0.9994</td>
    <td class="tg-im72">11.9317</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="3">meta-llama/Llama-2-7b-hf</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.7392</td>
    <td class="tg-im72">0.567</td>
    <td class="tg-im72">0.6709</td>
    <td class="tg-im72">0.7835</td>
    <td class="tg-vxga">0.6902</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">8.7911</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.7353</td>
    <td class="tg-im72">0.5642</td>
    <td class="tg-im72">0.6622</td>
    <td class="tg-im72">0.7829</td>
    <td class="tg-vxga">0.6862</td>
    <td class="tg-p7cy">0.9942</td>
    <td class="tg-im72">8.9635</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Sym</td>
    <td class="tg-im72">0.7246</td>
    <td class="tg-im72">0.5617</td>
    <td class="tg-im72">0.6756</td>
    <td class="tg-im72">0.7797</td>
    <td class="tg-vxga">0.6854</td>
    <td class="tg-p7cy">0.9931</td>
    <td class="tg-im72">9.2799</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="4">meta-llama/Llama-2-13b-chat-hf</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.7312</td>
    <td class="tg-im72">0.6059</td>
    <td class="tg-im72">0.7103</td>
    <td class="tg-im72">0.7835</td>
    <td class="tg-vxga">0.7077</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">10.2213</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.7273</td>
    <td class="tg-im72">0.6018</td>
    <td class="tg-im72">0.7088</td>
    <td class="tg-im72">0.7742</td>
    <td class="tg-vxga">0.7030</td>
    <td class="tg-p7cy">0.9934</td>
    <td class="tg-im72">2538.083</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.7283</td>
    <td class="tg-im72">0.6053</td>
    <td class="tg-im72">0.7024</td>
    <td class="tg-im72">0.7764</td>
    <td class="tg-vxga">0.7031</td>
    <td class="tg-p7cy">0.9935</td>
    <td class="tg-im72">1889.374</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Sym</td>
    <td class="tg-im72">0.727</td>
    <td class="tg-im72">0.5997</td>
    <td class="tg-im72">0.7024</td>
    <td class="tg-im72">0.778</td>
    <td class="tg-vxga">0.7018</td>
    <td class="tg-p7cy">0.9916</td>
    <td class="tg-im72">2504.497</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="4">meta-llama/Llama-2-13b-hf</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.7677</td>
    <td class="tg-im72">0.5972</td>
    <td class="tg-im72">0.6961</td>
    <td class="tg-im72">0.7878</td>
    <td class="tg-vxga">0.7122</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">7.8984</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.7627</td>
    <td class="tg-im72">0.5933</td>
    <td class="tg-im72">0.689</td>
    <td class="tg-im72">0.7851</td>
    <td class="tg-vxga">0.7075</td>
    <td class="tg-p7cy">0.9934</td>
    <td class="tg-im72">1556.448</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.7675</td>
    <td class="tg-im72">0.5934</td>
    <td class="tg-im72">0.6977</td>
    <td class="tg-im72">0.7856</td>
    <td class="tg-vxga">0.7111</td>
    <td class="tg-p7cy">0.9984</td>
    <td class="tg-im72">1514.927</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Sym</td>
    <td class="tg-im72">0.7566</td>
    <td class="tg-im72">0.5899</td>
    <td class="tg-im72">0.7032</td>
    <td class="tg-im72">0.7856</td>
    <td class="tg-vxga">0.7088</td>
    <td class="tg-p7cy">0.9953</td>
    <td class="tg-im72">1374.728</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="2">bigscience/bloom-7b1</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.5764</td>
    <td class="tg-im72">0.4628</td>
    <td class="tg-im72">0.6456</td>
    <td class="tg-im72">0.7269</td>
    <td class="tg-vxga">0.6029</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">30.6438</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Sym</td>
    <td class="tg-im72">0.5799</td>
    <td class="tg-im72">0.4542</td>
    <td class="tg-im72">0.6361</td>
    <td class="tg-im72">0.7312</td>
    <td class="tg-vxga">0.6004</td>
    <td class="tg-p7cy">0.9957</td>
    <td class="tg-im72">32.0626</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="2">bigscience/bloomz-7b1</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.5593</td>
    <td class="tg-im72">0.4789</td>
    <td class="tg-im72">0.6527</td>
    <td class="tg-im72">0.7628</td>
    <td class="tg-vxga">0.6134</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">51.7432</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.5525</td>
    <td class="tg-im72">0.4731</td>
    <td class="tg-im72">0.6504</td>
    <td class="tg-im72">0.7617</td>
    <td class="tg-vxga">0.6094</td>
    <td class="tg-p7cy">0.9935</td>
    <td class="tg-im72">52.7828</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="4">databricks/dolly-v1-6b</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.6866</td>
    <td class="tg-im72">0.5098</td>
    <td class="tg-im72">0.6433</td>
    <td class="tg-im72">0.7622</td>
    <td class="tg-im72">0.6505</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">11.3242</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.6878</td>
    <td class="tg-im72">0.5058</td>
    <td class="tg-im72">0.6393</td>
    <td class="tg-im72">0.7633</td>
    <td class="tg-im72">0.6491</td>
    <td class="tg-iire">0.9978</td>
    <td class="tg-im72">11.5514</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.6864</td>
    <td class="tg-im72">0.5084</td>
    <td class="tg-im72">0.6519</td>
    <td class="tg-im72">0.7568</td>
    <td class="tg-im72">0.6509</td>
    <td class="tg-iire">1.0006</td>
    <td class="tg-im72">11.4728</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Sym</td>
    <td class="tg-im72">0.6876</td>
    <td class="tg-im72">0.5045</td>
    <td class="tg-im72">0.6433</td>
    <td class="tg-im72">0.7541</td>
    <td class="tg-im72">0.6474</td>
    <td class="tg-iire">0.9952</td>
    <td class="tg-im72">11.6474</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="2">databricks/dolly-v2-7b</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.6379</td>
    <td class="tg-im72">0.5282</td>
    <td class="tg-im72">0.614</td>
    <td class="tg-im72">0.7448</td>
    <td class="tg-im72">0.6312</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">16.161</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.6377</td>
    <td class="tg-im72">0.5228</td>
    <td class="tg-im72">0.5991</td>
    <td class="tg-im72">0.7448</td>
    <td class="tg-im72">0.6261</td>
    <td class="tg-iire">0.9919</td>
    <td class="tg-im72">16.4096</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="4">EleutherAI/gpt-neo-2.7b</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.6224</td>
    <td class="tg-im72">0.4271</td>
    <td class="tg-im72">0.577</td>
    <td class="tg-im72">0.722</td>
    <td class="tg-im72">0.5871</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">13.9359</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.6123</td>
    <td class="tg-im72">0.4227</td>
    <td class="tg-im72">0.5738</td>
    <td class="tg-im72">0.7203</td>
    <td class="tg-im72">0.5823</td>
    <td class="tg-iire">0.9917</td>
    <td class="tg-im72">14.3377</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.615</td>
    <td class="tg-im72">0.4259</td>
    <td class="tg-im72">0.5714</td>
    <td class="tg-im72">0.7247</td>
    <td class="tg-im72">0.5843</td>
    <td class="tg-iire">0.9951</td>
    <td class="tg-im72">14.2083</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Sym</td>
    <td class="tg-im72">0.6154</td>
    <td class="tg-im72">0.4208</td>
    <td class="tg-im72">0.5777</td>
    <td class="tg-im72">0.7198</td>
    <td class="tg-im72">0.5834</td>
    <td class="tg-iire">0.9937</td>
    <td class="tg-im72">14.3121</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="3">EleutherAI/gpt-neox-20b</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.7233</td>
    <td class="tg-im72">0.5359</td>
    <td class="tg-im72">0.6614</td>
    <td class="tg-im72">0.7753</td>
    <td class="tg-im72">0.6740</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">9.195</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.7186</td>
    <td class="tg-im72">0.5328</td>
    <td class="tg-im72">0.6535</td>
    <td class="tg-im72">0.7699</td>
    <td class="tg-im72">0.6687</td>
    <td class="tg-iire">0.9922</td>
    <td class="tg-im72">9.3463</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.7268</td>
    <td class="tg-im72">0.533</td>
    <td class="tg-im72">0.659</td>
    <td class="tg-im72">0.7715</td>
    <td class="tg-im72">0.6726</td>
    <td class="tg-iire">0.9979</td>
    <td class="tg-im72">9.2897</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="2">mosaicml/mpt-7b</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.7056</td>
    <td class="tg-im72">0.5718</td>
    <td class="tg-im72">0.6859</td>
    <td class="tg-im72">0.7927</td>
    <td class="tg-im72">0.6890</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">9.9324</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.7006</td>
    <td class="tg-im72">0.5655</td>
    <td class="tg-im72">0.6803</td>
    <td class="tg-im72">0.7965</td>
    <td class="tg-im72">0.6857</td>
    <td class="tg-iire">0.9952</td>
    <td class="tg-im72">10.1515</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="2">mosaicml/mpt-7b-chat</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.655</td>
    <td class="tg-im72">0.5752</td>
    <td class="tg-im72">0.6748</td>
    <td class="tg-im72">0.7845</td>
    <td class="tg-im72">0.6724</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">13.5951</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.6472</td>
    <td class="tg-im72">0.5716</td>
    <td class="tg-im72">0.6685</td>
    <td class="tg-im72">0.784</td>
    <td class="tg-im72">0.6678</td>
    <td class="tg-iire">0.9932</td>
    <td class="tg-im72">13.8539</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="2">mosaicml/mpt-7b-instruct</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.6918</td>
    <td class="tg-im72">0.5819</td>
    <td class="tg-im72">0.678</td>
    <td class="tg-im72">0.7927</td>
    <td class="tg-im72">0.6861</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">10.8863</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.6864</td>
    <td class="tg-im72">0.5765</td>
    <td class="tg-im72">0.6827</td>
    <td class="tg-im72">0.7873</td>
    <td class="tg-im72">0.6832</td>
    <td class="tg-iire">0.9958</td>
    <td class="tg-im72">11.1451</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="2">mosaicml/mpt-7b-storywriter</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.693</td>
    <td class="tg-im72">0.5477</td>
    <td class="tg-im72">0.663</td>
    <td class="tg-im72">0.784</td>
    <td class="tg-im72">0.6719</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">9.9125</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.6854</td>
    <td class="tg-im72">0.5443</td>
    <td class="tg-im72">0.6661</td>
    <td class="tg-im72">0.7813</td>
    <td class="tg-im72">0.6693</td>
    <td class="tg-iire">0.9961</td>
    <td class="tg-im72">10.1137</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="4">tiiuae/falcon-rw-7b</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.6604</td>
    <td class="tg-im72">0.5419</td>
    <td class="tg-im72">0.6598</td>
    <td class="tg-im72">0.7753</td>
    <td class="tg-im72">0.6594</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">11.7616</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.6484</td>
    <td class="tg-im72">0.5369</td>
    <td class="tg-im72">0.6575</td>
    <td class="tg-im72">0.7807</td>
    <td class="tg-im72">0.6559</td>
    <td class="tg-iire">0.9947</td>
    <td class="tg-im72">11.9411</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.6571</td>
    <td class="tg-im72">0.5398</td>
    <td class="tg-im72">0.6582</td>
    <td class="tg-im72">0.7764</td>
    <td class="tg-im72">0.6579</td>
    <td class="tg-iire">0.9978</td>
    <td class="tg-im72">11.8809</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Sym</td>
    <td class="tg-im72">0.652</td>
    <td class="tg-im72">0.535</td>
    <td class="tg-im72">0.6575</td>
    <td class="tg-im72">0.7682</td>
    <td class="tg-im72">0.6532</td>
    <td class="tg-iire">0.9906</td>
    <td class="tg-im72">12.0048</td>
  </tr>
  <tr>
    <td class="tg-vxga" rowspan="3">tiiuae/falcon-7b-instruct</td>
    <td class="tg-vxga">FP32</td>
    <td class="tg-im72">0.6437</td>
    <td class="tg-im72">0.5177</td>
    <td class="tg-im72">0.6669</td>
    <td class="tg-im72">0.7824</td>
    <td class="tg-im72">0.6527</td>
    <td class="tg-iire">/</td>
    <td class="tg-im72">14.5053</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G128Asym</td>
    <td class="tg-im72">0.6301</td>
    <td class="tg-im72">0.5142</td>
    <td class="tg-im72">0.6654</td>
    <td class="tg-im72">0.7835</td>
    <td class="tg-im72">0.6483</td>
    <td class="tg-iire">0.9933</td>
    <td class="tg-im72">14.8146</td>
  </tr>
  <tr>
    <td class="tg-vxga">GPTQ<br>W4G32Asym</td>
    <td class="tg-im72">0.6377</td>
    <td class="tg-im72">0.517</td>
    <td class="tg-im72">0.6598</td>
    <td class="tg-im72">0.7807</td>
    <td class="tg-im72">0.6488</td>
    <td class="tg-iire">0.9941</td>
    <td class="tg-im72">14.6953</td>
  </tr>
</tbody>
</table>


### ONNX Models with ONNX Runtime 1.15.0

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s4c14ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>ResNet50 V1.5</td>
    <td>qlinearops</td>
    <td>72.16%</td>
    <td>72.29%</td>
    <td>-0.19%</td>
    <td>1412.05</td>
    <td>710.02</td>
    <td>1.99x</td>
  </tr>
  <tr>
    <td>ResNet50 V1.5</td>
    <td>qdq</td>
    <td>72.14%</td>
    <td>72.29%</td>
    <td>-0.22%</td>
    <td>1564.39</td>
    <td>712.38</td>
    <td>2.20x</td>
  </tr>
  <tr>
    <td>ResNet50 V1.5 MLPerf</td>
    <td>qlinearops</td>
    <td>76.11%</td>
    <td>76.46%</td>
    <td>-0.46%</td>
    <td>1377.47</td>
    <td>719.66</td>
    <td>1.91x</td>
  </tr>
  <tr>
    <td>ResNet50 V1.5 MLPerf</td>
    <td>qdq</td>
    <td>76.13%</td>
    <td>76.46%</td>
    <td>-0.44%</td>
    <td>1446.69</td>
    <td>703.40</td>
    <td>2.06x</td>
  </tr>
  <tr>
    <td>ResNet50 V1.5 (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>74.82%</td>
    <td>74.99%</td>
    <td>-0.22%</td>
    <td>1579.31</td>
    <td>747.73</td>
    <td>2.11x</td>
  </tr>
  <tr>
    <td>ResNet50 V1.5 (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>74.82%</td>
    <td>74.99%</td>
    <td>-0.23%</td>
    <td>1508.21</td>
    <td>749.43</td>
    <td>2.01x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>qlinearops</td>
    <td>65.49%</td>
    <td>66.89%</td>
    <td>-2.09%</td>
    <td>6950.77</td>
    <td>4214.56</td>
    <td>1.65x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>qdq</td>
    <td>65.49%</td>
    <td>66.89%</td>
    <td>-2.10%</td>
    <td>6881.60</td>
    <td>4192.78</td>
    <td>1.64x</td>
  </tr>
  <tr>
    <td>MobileNet V2 (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>68.38%</td>
    <td>69.48%</td>
    <td>-1.59%</td>
    <td>6563.24</td>
    <td>3804.18</td>
    <td>1.73x</td>
  </tr>
  <tr>
    <td>MobileNet V2 (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>68.38%</td>
    <td>69.48%</td>
    <td>-1.59%</td>
    <td>6631.12</td>
    <td>3922.70</td>
    <td>1.69x</td>
  </tr>
  <tr>
    <td>VGG16</td>
    <td>qlinearops</td>
    <td>66.56%</td>
    <td>66.69%</td>
    <td>-0.19%</td>
    <td>423.44</td>
    <td>158.01</td>
    <td>2.68x</td>
  </tr>
  <tr>
    <td>VGG16</td>
    <td>qdq</td>
    <td>66.59%</td>
    <td>66.69%</td>
    <td>-0.15%</td>
    <td>571.02</td>
    <td>161.69</td>
    <td>3.53x</td>
  </tr>
  <tr>
    <td>VGG16 (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>72.33%</td>
    <td>72.40%</td>
    <td>-0.09%</td>
    <td>598.92</td>
    <td>163.53</td>
    <td>3.66x</td>
  </tr>
  <tr>
    <td>VGG16 (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>72.33%</td>
    <td>72.40%</td>
    <td>-0.09%</td>
    <td>594.66</td>
    <td>164.39</td>
    <td>3.62x</td>
  </tr>
  <tr>
    <td>MobileNet V3 MLPerf</td>
    <td>qlinearops</td>
    <td>75.56%</td>
    <td>75.74%</td>
    <td>-0.24%</td>
    <td>5473.90</td>
    <td>2567.96</td>
    <td>2.13x</td>
  </tr>
  <tr>
    <td>MobileNet V3 MLPerf</td>
    <td>qdq</td>
    <td>75.56%</td>
    <td>75.74%</td>
    <td>-0.24%</td>
    <td>5455.36</td>
    <td>2563.80</td>
    <td>2.13x</td>
  </tr>
  <tr>
    <td>ShuffleNet V2 (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>66.09%</td>
    <td>66.36%</td>
    <td>-0.41%</td>
    <td>6818.46</td>
    <td>3839.67</td>
    <td>1.78x</td>
  </tr>
  <tr>
    <td>ShuffleNet V2 (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>66.09%</td>
    <td>66.36%</td>
    <td>-0.41%</td>
    <td>5750.72</td>
    <td>3861.83</td>
    <td>1.49x</td>
  </tr>
  <tr>
    <td>GoogleNet (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>67.71%</td>
    <td>67.79%</td>
    <td>-0.12%</td>
    <td>1783.63</td>
    <td>1095.06</td>
    <td>1.63x</td>
  </tr>
  <tr>
    <td>GoogleNet (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>67.73%</td>
    <td>67.79%</td>
    <td>-0.09%</td>
    <td>1755.03</td>
    <td>1071.04</td>
    <td>1.64x</td>
  </tr>
  <tr>
    <td>SqueezeNet (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>56.54%</td>
    <td>56.87%</td>
    <td>-0.57%</td>
    <td>9918.09</td>
    <td>5639.89</td>
    <td>1.76x</td>
  </tr>
  <tr>
    <td>SqueezeNet (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>56.54%</td>
    <td>56.87%</td>
    <td>-0.57%</td>
    <td>9423.22</td>
    <td>5501.30</td>
    <td>1.71x</td>
  </tr>
  <tr>
    <td>CaffeNet (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>56.21%</td>
    <td>56.30%</td>
    <td>-0.16%</td>
    <td>3363.62</td>
    <td>1015.06</td>
    <td>3.31x</td>
  </tr>
  <tr>
    <td>CaffeNet (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>56.25%</td>
    <td>56.30%</td>
    <td>-0.09%</td>
    <td>3276.82</td>
    <td>798.28</td>
    <td>4.10x</td>
  </tr>
  <tr>
    <td>AlexNet (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>54.73%</td>
    <td>54.79%</td>
    <td>-0.10%</td>
    <td>2104.66</td>
    <td>985.33</td>
    <td>2.14x</td>
  </tr>
  <tr>
    <td>AlexNet (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>54.71%</td>
    <td>54.79%</td>
    <td>-0.14%</td>
    <td>2054.60</td>
    <td>745.36</td>
    <td>2.76x</td>
  </tr>
  <tr>
    <td>ZFNet (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>55.84%</td>
    <td>55.96%</td>
    <td>-0.21%</td>
    <td>864.73</td>
    <td>456.41</td>
    <td>1.89x</td>
  </tr>
  <tr>
    <td>ZFNet (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>55.86%</td>
    <td>55.96%</td>
    <td>-0.18%</td>
    <td>866.80</td>
    <td>455.75</td>
    <td>1.90x</td>
  </tr>
  <tr>
    <td>Inception V1 (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>67.21%</td>
    <td>67.24%</td>
    <td>-0.05%</td>
    <td>1802.03</td>
    <td>1170.74</td>
    <td>1.54x</td>
  </tr>
  <tr>
    <td>Inception V1 (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>67.21%</td>
    <td>67.24%</td>
    <td>-0.05%</td>
    <td>1813.29</td>
    <td>1164.87</td>
    <td>1.56x</td>
  </tr>
  <tr>
    <td>EfficientNet (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>76.98%</td>
    <td>77.11%</td>
    <td>-0.17%</td>
    <td>2615.12</td>
    <td>1349.97</td>
    <td>1.94x</td>
  </tr>
  <tr>
    <td>EfficientNet (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>76.99%</td>
    <td>77.11%</td>
    <td>-0.16%</td>
    <td>2343.94</td>
    <td>1322.86</td>
    <td>1.77x</td>
  </tr>
  <tr>
    <td>DenseNet (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>60.53%</td>
    <td>60.96%</td>
    <td>-0.70%</td>
    <td>630.80</td>
    <td>499.98</td>
    <td>1.26x</td>
  </tr>
  <tr>
    <td>SSD (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>18.83%</td>
    <td>18.98%</td>
    <td>-0.77%</td>
    <td>56.69</td>
    <td>14.56</td>
    <td>3.89x</td>
  </tr>
  <tr>
    <td>SSD (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>18.62%</td>
    <td>18.98%</td>
    <td>-1.89%</td>
    <td>57.54</td>
    <td>14.55</td>
    <td>3.95x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1</td>
    <td>qlinearops</td>
    <td>22.44%</td>
    <td>23.10%</td>
    <td>-2.86%</td>
    <td>1288.14</td>
    <td>878.69</td>
    <td>1.47x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1</td>
    <td>qdq</td>
    <td>22.44%</td>
    <td>23.10%</td>
    <td>-2.86%</td>
    <td>1173.88</td>
    <td>851.00</td>
    <td>1.38x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1 (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>22.96%</td>
    <td>23.02%</td>
    <td>-0.27%</td>
    <td>1114.65</td>
    <td>825.47</td>
    <td>1.35x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1 (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>22.96%</td>
    <td>23.02%</td>
    <td>-0.27%</td>
    <td>1056.30</td>
    <td>792.66</td>
    <td>1.33x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V2</td>
    <td>qlinearops</td>
    <td>23.87%</td>
    <td>24.67%</td>
    <td>-3.25%</td>
    <td>788.51</td>
    <td>669.72</td>
    <td>1.18x</td>
  </tr>
  <tr>
    <td>YOLOv3 (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>27.01%</td>
    <td>28.73%</td>
    <td>-5.99%</td>
    <td>140.21</td>
    <td>110.43</td>
    <td>1.27x</td>
  </tr>
  <tr>
    <td>YOLOv4 (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>32.30%</td>
    <td>33.71%</td>
    <td>-4.19%</td>
    <td>72.95</td>
    <td>64.95</td>
    <td>1.12x</td>
  </tr>
  <tr>
    <td>DUC (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>81.63%</td>
    <td>81.92%</td>
    <td>-0.36%</td>
    <td>9.12</td>
    <td>4.96</td>
    <td>1.84x</td>
  </tr>
  <tr>
    <td>Tiny YOLOv3 (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>11.83%</td>
    <td>12.42%</td>
    <td>-4.73%</td>
    <td>1163.39</td>
    <td>993.96</td>
    <td>1.17x</td>
  </tr>
  <tr>
    <td>Ultra Face (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>83.23%</td>
    <td>83.65%</td>
    <td>-0.49%</td>
    <td>8501.08</td>
    <td>1922.19</td>
    <td>4.42x</td>
  </tr>
  <tr>
    <td>Emotion FERPlus (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>7.97%</td>
    <td>8.00%</td>
    <td>-0.35%</td>
    <td>3552.60</td>
    <td>3114.19</td>
    <td>1.14x</td>
  </tr>
  <tr>
    <td>ArcFace (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>99.80%</td>
    <td>99.80%</td>
    <td>0.00%</td>
    <td>558.78</td>
    <td>246.87</td>
    <td>2.26x</td>
  </tr>
  <tr>
    <td>BERT base MRPC</td>
    <td>qlinearops</td>
    <td>85.54%</td>
    <td>86.03%</td>
    <td>-0.57%</td>
    <td>399.04</td>
    <td>226.03</td>
    <td>1.77x</td>
  </tr>
  <tr>
    <td>BERT base MRPC</td>
    <td>qdq</td>
    <td>85.54%</td>
    <td>86.03%</td>
    <td>-0.57%</td>
    <td>392.26</td>
    <td>223.21</td>
    <td>1.76x</td>
  </tr>
  <tr>
    <td>BERT base MRPC</td>
    <td>integerops</td>
    <td>85.29%</td>
    <td>86.03%</td>
    <td>-0.85%</td>
    <td>474.99</td>
    <td>222.71</td>
    <td>2.13x</td>
  </tr>
  <tr>
    <td>DistilBERT base MRPC</td>
    <td>qdq</td>
    <td>84.56%</td>
    <td>84.56%</td>
    <td>0.00%</td>
    <td>557.05</td>
    <td>399.46</td>
    <td>1.39x</td>
  </tr>
  <tr>
    <td>DistilBERT base MRPC</td>
    <td>integerops</td>
    <td>85.54%</td>
    <td>84.56%</td>
    <td>1.16%</td>
    <td>963.92</td>
    <td>399.36</td>
    <td>2.41x</td>
  </tr>
  <tr>
    <td>Mobile bert MRPC</td>
    <td>qdq</td>
    <td>85.54%</td>
    <td>86.28%</td>
    <td>-0.85%</td>
    <td>529.98</td>
    <td>394.46</td>
    <td>1.34x</td>
  </tr>
  <tr>
    <td>Mobile bert MRPC</td>
    <td>integerops</td>
    <td>85.54%</td>
    <td>86.28%</td>
    <td>-0.85%</td>
    <td>603.66</td>
    <td>398.15</td>
    <td>1.52x</td>
  </tr>
  <tr>
    <td>Roberta base MRPC</td>
    <td>integerops</td>
    <td>90.93%</td>
    <td>89.95%</td>
    <td>1.09%</td>
    <td>485.74</td>
    <td>223.54</td>
    <td>2.17x</td>
  </tr>
  <tr>
    <td>BERT SQuAD (ONNX Model Zoo)</td>
    <td>integerops</td>
    <td>80.29</td>
    <td>80.67</td>
    <td>-0.47%</td>
    <td>187.63</td>
    <td>95.88</td>
    <td>1.96x</td>
  </tr>
  <tr>
    <td>MobileBERT SQuAD MLPerf (ONNX Model Zoo)</td>
    <td>integerops</td>
    <td>89.87</td>
    <td>90.03</td>
    <td>-0.17%</td>
    <td>144.88</td>
    <td>124.08</td>
    <td>1.17x</td>
  </tr>
  <tr>
    <td>BiDAF (ONNX Model Zoo)</td>
    <td>integerops</td>
    <td>65.93%</td>
    <td>66.08%</td>
    <td>-0.23%</td>
    <td>2757.83</td>
    <td>2279.38</td>
    <td>1.21x</td>
  </tr>
  <tr>
    <td>GPT2 lm head WikiText (ONNX Model Zoo)</td>
    <td>integerops</td>
    <td>31.98</td>
    <td>29.00</td>
    <td>10.31%</td>
    <td>15.35</td>
    <td>9.73</td>
    <td>1.58x</td>
  </tr>
  <tr>
    <td>BERT base cased MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>90.21%</td>
    <td>90.42%</td>
    <td>-0.23%</td>
    <td>357.89</td>
    <td>211.81</td>
    <td>1.69x</td>
  </tr>
  <tr>
    <td>BERT base uncased MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>89.58%</td>
    <td>90.42%</td>
    <td>-0.93%</td>
    <td>472.44</td>
    <td>211.65</td>
    <td>2.23x</td>
  </tr>
  <tr>
    <td>Roberta base MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>91.00%</td>
    <td>91.38%</td>
    <td>-0.41%</td>
    <td>365.03</td>
    <td>214.66</td>
    <td>1.70x</td>
  </tr>
  <tr>
    <td>Roberta base MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>90.85%</td>
    <td>91.38%</td>
    <td>-0.58%</td>
    <td>489.85</td>
    <td>212.20</td>
    <td>2.31x</td>
  </tr>
  <tr>
    <td>XLM Roberta base MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>89.37%</td>
    <td>90.10%</td>
    <td>-0.81%</td>
    <td>302.49</td>
    <td>212.76</td>
    <td>1.42x</td>
  </tr>
  <tr>
    <td>XLM Roberta base MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>89.66%</td>
    <td>90.10%</td>
    <td>-0.50%</td>
    <td>343.75</td>
    <td>213.09</td>
    <td>1.61x</td>
  </tr>
  <tr>
    <td>Camembert base MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>89.28%</td>
    <td>89.28%</td>
    <td>0.00%</td>
    <td>270.01</td>
    <td>215.48</td>
    <td>1.25x</td>
  </tr>
  <tr>
    <td>Camembert base MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>89.19%</td>
    <td>89.28%</td>
    <td>-0.10%</td>
    <td>491.01</td>
    <td>212.92</td>
    <td>2.31x</td>
  </tr>
  <tr>
    <td>MiniLM L12 H384 uncased MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>90.13%</td>
    <td>90.97%</td>
    <td>-0.93%</td>
    <td>1051.67</td>
    <td>583.85</td>
    <td>1.80x</td>
  </tr>
  <tr>
    <td>MiniLM L12 H384 uncased MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>91.07%</td>
    <td>90.97%</td>
    <td>0.10%</td>
    <td>1076.27</td>
    <td>589.80</td>
    <td>1.82x</td>
  </tr>
  <tr>
    <td>DistilBERT base uncased SST-2 (HuggingFace)</td>
    <td>qlinearops</td>
    <td>90.71%</td>
    <td>91.06%</td>
    <td>-0.38%</td>
    <td>896.69</td>
    <td>396.85</td>
    <td>2.26x</td>
  </tr>
  <tr>
    <td>DistilBERT base uncased SST-2 (HuggingFace)</td>
    <td>integerops</td>
    <td>90.25%</td>
    <td>91.06%</td>
    <td>-0.88%</td>
    <td>753.88</td>
    <td>396.59</td>
    <td>1.90x</td>
  </tr>
  <tr>
    <td>Albert base v2 SST-2 (HuggingFace)</td>
    <td>qlinearops</td>
    <td>91.40%</td>
    <td>92.32%</td>
    <td>-0.99%</td>
    <td>274.17</td>
    <td>210.87</td>
    <td>1.30x</td>
  </tr>
  <tr>
    <td>Albert base v2 SST-2 (HuggingFace)</td>
    <td>integerops</td>
    <td>91.86%</td>
    <td>92.32%</td>
    <td>-0.50%</td>
    <td>271.85</td>
    <td>211.18</td>
    <td>1.29x</td>
  </tr>
  <tr>
    <td>MiniLM L6 H384 uncased SST-2 (HuggingFace)</td>
    <td>qlinearops</td>
    <td>89.45%</td>
    <td>90.14%</td>
    <td>-0.76%</td>
    <td>2022.40</td>
    <td>1124.12</td>
    <td>1.80x</td>
  </tr>
  <tr>
    <td>MiniLM L6 H384 uncased SST-2 (HuggingFace)</td>
    <td>integerops</td>
    <td>89.91%</td>
    <td>90.14%</td>
    <td>-0.26%</td>
    <td>2010.50</td>
    <td>1127.41</td>
    <td>1.78x</td>
  </tr>
  <tr>
    <td>MiniLM L6 H384 uncased SST-2 (HuggingFace)</td>
    <td>qlinearops</td>
    <td>87.70%</td>
    <td>88.29%</td>
    <td>-0.67%</td>
    <td>401.24</td>
    <td>211.92</td>
    <td>1.89x</td>
  </tr>
  <tr>
    <td>MiniLM L6 H384 uncased SST-2 (HuggingFace)</td>
    <td>integerops</td>
    <td>88.19%</td>
    <td>88.29%</td>
    <td>-0.12%</td>
    <td>494.84</td>
    <td>212.01</td>
    <td>2.33x</td>
  </tr>
  <tr>
    <td>Electra small discriminator MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>89.57%</td>
    <td>89.83%</td>
    <td>-0.29%</td>
    <td>1804.17</td>
    <td>1154.99</td>
    <td>1.56x</td>
  </tr>
  <tr>
    <td>Electra small discriminator MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>89.27%</td>
    <td>89.83%</td>
    <td>-0.63%</td>
    <td>1961.57</td>
    <td>1158.86</td>
    <td>1.69x</td>
  </tr>
  <tr>
    <td>BERT mini MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>86.70%</td>
    <td>86.52%</td>
    <td>0.21%</td>
    <td>4986.29</td>
    <td>3444.92</td>
    <td>1.45x</td>
  </tr>
  <tr>
    <td>BERT mini MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>86.16%</td>
    <td>86.52%</td>
    <td>-0.41%</td>
    <td>5603.86</td>
    <td>3320.38</td>
    <td>1.69x</td>
  </tr>
  <tr>
    <td>Xlnet base cased MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>89.74%</td>
    <td>89.86%</td>
    <td>-0.13%</td>
    <td>108.36</td>
    <td>91.63</td>
    <td>1.18x</td>
  </tr>
  <tr>
    <td>Xlnet base cased MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>89.58%</td>
    <td>89.86%</td>
    <td>-0.31%</td>
    <td>108.27</td>
    <td>92.24</td>
    <td>1.17x</td>
  </tr>
  <tr>
    <td>BART large MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>91.77%</td>
    <td>91.20%</td>
    <td>0.63%</td>
    <td>58.98</td>
    <td>51.23</td>
    <td>1.15x</td>
  </tr>
  <tr>
    <td>BART large MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>92.36%</td>
    <td>91.20%</td>
    <td>1.28%</td>
    <td>96.02</td>
    <td>51.12</td>
    <td>1.88x</td>
  </tr>
  <tr>
    <td>DeBERTa v3 base MRPC (HuggingFace)</td>
    <td>qlinearops</td>
    <td>91.85%</td>
    <td>92.23%</td>
    <td>-0.40%</td>
    <td>161.42</td>
    <td>147.11</td>
    <td>1.10x</td>
  </tr>
  <tr>
    <td>DeBERTa v3 base MRPC (HuggingFace)</td>
    <td>integerops</td>
    <td>92.39%</td>
    <td>92.23%</td>
    <td>0.17%</td>
    <td>170.50</td>
    <td>147.28</td>
    <td>1.16x</td>
  </tr>
  <tr>
    <td>Spanbert SQuAD (HuggingFace)</td>
    <td>qlinearops</td>
    <td>91.14</td>
    <td>91.98</td>
    <td>-0.91%</td>
    <td>69.94</td>
    <td>42.36</td>
    <td>1.65x</td>
  </tr>
  <tr>
    <td>Spanbert SQuAD (HuggingFace)</td>
    <td>integerops</td>
    <td>91.40</td>
    <td>91.98</td>
    <td>-0.63%</td>
    <td>80.06</td>
    <td>42.62</td>
    <td>1.88x</td>
  </tr>
  <tr>
    <td>Bert base multilingual cased SQuAD (HuggingFace)</td>
    <td>qlinearops</td>
    <td>88.42</td>
    <td>89.13</td>
    <td>-0.79%</td>
    <td>71.67</td>
    <td>42.36</td>
    <td>1.69x</td>
  </tr>
  <tr>
    <td>Bert base multilingual cased SQuAD (HuggingFace)</td>
    <td>integerops</td>
    <td>88.70</td>
    <td>89.13</td>
    <td>-0.48%</td>
    <td>79.42</td>
    <td>42.32</td>
    <td>1.88x</td>
  </tr>
  <tr>
    <td>DistilBert base uncased SQuAD (HuggingFace)</td>
    <td>qlinearops</td>
    <td>86.33</td>
    <td>86.86</td>
    <td>-0.62%</td>
    <td>112.14</td>
    <td>67.59</td>
    <td>1.66x</td>
  </tr>
  <tr>
    <td>DistilBert base uncased SQuAD (HuggingFace)</td>
    <td>integerops</td>
    <td>86.05</td>
    <td>86.86</td>
    <td>-0.94%</td>
    <td>159.29</td>
    <td>67.70</td>
    <td>2.35x</td>
  </tr>
  <tr>
    <td>BERT large uncased whole word masking SQuAD (HuggingFace)</td>
    <td>qlinearops</td>
    <td>92.34</td>
    <td>93.16</td>
    <td>-0.88%</td>
    <td>24.56</td>
    <td>12.71</td>
    <td>1.93x</td>
  </tr>
  <tr>
    <td>BERT large uncased whole word masking SQuAD (HuggingFace)</td>
    <td>integerops</td>
    <td>92.99</td>
    <td>93.16</td>
    <td>-0.18%</td>
    <td>26.76</td>
    <td>12.72</td>
    <td>2.10x</td>
  </tr>
  <tr>
    <td>Roberta large SQuAD v2 (HuggingFace)</td>
    <td>qlinearops</td>
    <td>89.03</td>
    <td>89.02</td>
    <td>0.02%</td>
    <td>16.85</td>
    <td>12.95</td>
    <td>1.30x</td>
  </tr>
  <tr>
    <td>Roberta large SQuAD v2 (HuggingFace)</td>
    <td>integerops</td>
    <td>89.04</td>
    <td>89.02</td>
    <td>0.02%</td>
    <td>26.85</td>
    <td>12.95</td>
    <td>2.07x</td>
  </tr>
  <tr>
    <td>GPT2 WikiText (HuggingFace)</td>
    <td>qlinearops</td>
    <td>30.25</td>
    <td>29.00</td>
    <td>4.33%</td>
    <td>12.63</td>
    <td>9.76</td>
    <td>1.29x</td>
  </tr>
  <tr>
    <td>GPT2 WikiText (HuggingFace)</td>
    <td>integerops</td>
    <td>29.68</td>
    <td>29.00</td>
    <td>2.36%</td>
    <td>13.54</td>
    <td>9.72</td>
    <td>1.39x</td>
  </tr>
  <tr>
    <td>DistilGPT2 WikiText (HuggingFace)</td>
    <td>qlinearops</td>
    <td>44.93</td>
    <td>43.43</td>
    <td>3.46%</td>
    <td>20.45</td>
    <td>16.72</td>
    <td>1.22x</td>
  </tr>
  <tr>
    <td>DistilGPT2 WikiText (HuggingFace)</td>
    <td>integerops</td>
    <td>44.62</td>
    <td>43.43</td>
    <td>2.74%</td>
    <td>21.91</td>
    <td>16.73</td>
    <td>1.31x</td>
  </tr>
  <tr>
    <td>LayoutLM FUNSD (HuggingFace)</td>
    <td>qlinearops</td>
    <td>78.15%</td>
    <td>78.35%</td>
    <td>-0.25%</td>
    <td>60.41</td>
    <td>43.95</td>
    <td>1.37x</td>
  </tr>
  <tr>
    <td>LayoutLM FUNSD (HuggingFace)</td>
    <td>integerops</td>
    <td>77.58%</td>
    <td>78.35%</td>
    <td>-0.98%</td>
    <td>65.82</td>
    <td>43.83</td>
    <td>1.50x</td>
  </tr>
  <tr>
    <td>LayoutLMv3 FUNSD (HuggingFace)</td>
    <td>qlinearops</td>
    <td>89.85%</td>
    <td>90.49%</td>
    <td>-0.71%</td>
    <td>31.12</td>
    <td>29.13</td>
    <td>1.07x</td>
  </tr>
  <tr>
    <td>LayoutLMv3 FUNSD (HuggingFace)</td>
    <td>integerops</td>
    <td>90.07%</td>
    <td>90.49%</td>
    <td>-0.46%</td>
    <td>35.01</td>
    <td>27.92</td>
    <td>1.25x</td>
  </tr>
</tbody>
</table>

<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance 1s56c1ins1bs<br>Throughput(samples/sec)</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>Faster R-CNN (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>34.06%</td>
    <td>34.37%</td>
    <td>-0.88%</td>
    <td>3.99</td>
    <td>3.28</td>
    <td>1.21x</td>
  </tr>
  <tr>
    <td>Faster R-CNN (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>33.98%</td>
    <td>34.37%</td>
    <td>-1.12%</td>
    <td>4.00</td>
    <td>3.37</td>
    <td>1.19x</td>
  </tr>
  <tr>
    <td>Mask R-CNN (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>33.13%</td>
    <td>33.72%</td>
    <td>-1.74%</td>
    <td>3.36</td>
    <td>2.95</td>
    <td>1.14x</td>
  </tr>
  <tr>
    <td>Mask R-CNN (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>33.29%</td>
    <td>33.72%</td>
    <td>-1.28%</td>
    <td>3.38</td>
    <td>2.98</td>
    <td>1.14x</td>
  </tr>
  <tr>
    <td>FCN (ONNX Model Zoo)</td>
    <td>qlinearops</td>
    <td>64.54%</td>
    <td>64.98%</td>
    <td>-0.67%</td>
    <td>28.19</td>
    <td>12.60</td>
    <td>2.24x</td>
  </tr>
  <tr>
    <td>FCN (ONNX Model Zoo)</td>
    <td>qdq</td>
    <td>64.54%</td>
    <td>64.98%</td>
    <td>-0.67%</td>
    <td>28.22</td>
    <td>12.56</td>
    <td>2.25x</td>
  </tr>
</tbody>
</table>

### ONNX Models with ONNX Runtime 1.15.0 in WOQ Mode

<table class="tg">
<thead>
  <tr>
    <th rowspan="2">Model name</th>
    <th rowspan="2">Configuration</th>
    <th colspan="2">Lambada_openai</th>
    <th rowspan="2">Accuracy Ratio<br>[INT4/FP32]</th>
  </tr>
  <tr>
    <th>Accuracy</th>
    <th>Perplexity</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">meta-llama/Llama-2-7b-chat-hf</td>
    <td>FP32</td>
    <td>0.7058</td>
    <td>3.2788</td>
    <td>/</td>
  </tr>
  <tr>
    <td>GPTQ<br>W4G32Asym</td>
    <td>0.7002</td>
    <td>3.4124</td>
    <td>0.9921</td>
  </tr>
  <tr>
    <td rowspan="2">meta-llama/Llama-2-7b-hf</td>
    <td>FP32</td>
    <td>0.7392</td>
    <td>3.3950</td>
    <td>/</td>
  </tr>
  <tr>
    <td>GPTQ<br>W4G32Asym</td>
    <td>0.7312</td>
    <td>3.5711</td>
    <td>0.9892</td>
  </tr>
  <tr>
    <td rowspan="2">meta-llama/Llama-2-13b-chat-hf</td>
    <td>FP32</td>
    <td>0.7312</td>
    <td>2.9163</td>
    <td>/</td>
  </tr>
  <tr>
    <td>GPTQ<br>W4G128Asym</td>
    <td>0.7240</td>
    <td>2.9945</td>
    <td>0.9902</td>
  <tr>
    <td rowspan="3">meta-llama/Llama-2-13b-hf</td>
    <td>FP32</td>
    <td>0.7677</td>
    <td>3.0438</td>
    <td>/</td>
  </tr>
  <tr>
    <td>GPTQ<br>W4G128Asym</td>
    <td>0.7634</td>
    <td>3.1186</td>
    <td>0.9944</td>
  <tr>
    <td>GPTQ<br>W4G32Asym</td>
    <td>0.7615</td>
    <td>3.1276</td>
    <td>0.9919</td>
  </tr>
  <tr>
    <td rowspan="2">meta-llama/Llama-2-70b-chat-hf</td>
    <td>FP32</td>
    <td>0.7543</td>
    <td>2.6181</td>
    <td>/</td>
  </tr>
  <tr>
    <td>RTN<br>W4G32Asym</td>
    <td>0.7518</td>
    <td>2.6496</td>
    <td>0.9967</td>
  </tr>
  <tr>
    <td rowspan="2">meta-llama/Llama-2-70b-hf</td>
    <td>FP32</td>
    <td>0.7964</td>
    <td>2.6612</td>
    <td>/</td>
  </tr>
  <tr>
    <td>RTN<br>W4G32Sym</td>
    <td>0.7941</td>
    <td>2.7243</td>
    <td>0.9971</td>
  </tr>
</tbody>
</table>


## Validated Pruning Examples

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Task</br>Dataset</th>
    <th rowspan="2">Dense Accuracy<br>Sparse Accuracy</th>
    <th rowspan="2">Relative Drop</th>
    <th rowspan="2">Sparsity ratio<br>Sparsity Pattern</th>
    <th rowspan="2">Comments<br>Balanced<br>or unbalanced ratio</th>
  </tr>
  <tr>
  </tr>
</thead>
<tbody>  
  <tr>
    <td>Bert-Mini</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=76.87</br>f1=76.2</td>
    <td>-0.80%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Bert-Mini</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=76.87</br>f1=76.2</td>
    <td>-0.80%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=76.87</br>f1=77.62</td>
    <td>+0.98%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Distilbert-base-uncased</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=86.90</br>f1=86.15</td>
    <td>-0.86%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Distilbert-base-uncased</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=86.90</br>f1=87.50</td>
    <td>+0.69%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-base-uncased</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=88.59</br>f1=87.78</td>
    <td>-0.92%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-base-uncased</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=88.59</br>f1=89.40</td>
    <td>+0.91%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-large</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=91.23</br>f1=90.91</td>
    <td>-0.35%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-large</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=91.23</br>f1=91.67</td>
    <td>+0.48%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>MRPC</td>
    <td>f1=87.52</br>f1=87.22</td>
    <td>-0.34%</td>
    <td>90%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>MRPC</td>
    <td>f1=87.52</br>f1=87.33</td>
    <td>-0.22%</td>
    <td>90%</br>structured 4x1</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>MRPC</td>
    <td>f1=87.52</br>f1=86.89</td>
    <td>-0.72%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>MRPC</td>
    <td>f1=87.52</br>f1=86.8</td>
    <td>-0.83%</td>
    <td>60%</br>structured per channel</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Distilbert-base-uncased</td>
    <td>text classification</br>MRPC</td>
    <td>f1=90.26</br>f1=89.85</td>
    <td>-0.46%</td>
    <td>90%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>  
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Distilbert-base-uncased</td>
    <td>text classification</br>MRPC</td>
    <td>f1=90.26</br>f1=90.88</td>
    <td>+0.69%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy=87.61</br>accuracy=86.92</td>
    <td>-0.79%</td>
    <td>90%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy=87.61</br>accuracy=87.73</td>
    <td>+0.14%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy=87.61</br>accuracy=86.92</td>
    <td>-0.79%</td>
    <td>50%</br>structured per channel</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>ResNet50</td>
    <td>image recognition</br>ImageNet</td>
    <td>top1 acc = 78.95</br>top1 acc = 80.10</td>
    <td>-1.43%</td>
    <td>75%</br>structured 2x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  <tr>
    <td>YOLO-v5s6</td>
    <td>object detection</br>COCO</td>
    <td>AP0.50:0.95/AP0.50=0.404/0.6</br>AP0.50:0.95/AP0.50=0.393/0.584</td>
    <td>-2.72%</td>
    <td>80%</br>unstructured</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Large</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=91.34</br>f1=90.7</td>
    <td>-0.07%</td>
    <td>80%</br>structured 2x1</td>
    <td>group lasso</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>MNLI</td>
    <td>[m, mm] = [84.57, 84.79]</br>[m, mm] = [82.45, 83.27]</td>
    <td>[-2.51%, -1.80%]</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>    
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>MNLI</td>
    <td>[m, mm] = [84.57, 84.79]</br>[m, mm] = [83.20, 84.11]</td>
    <td>[-1.62%, -0.80%]</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>    
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy = 92.32</br>accuracy = 91.51</td>
    <td>-0.88%</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>    
  </tr>
  <tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy = 92.32</br>accuracy = 92.20</td>
    <td>-0.13%</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>       
  </tr>
  <tr>  
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy = 92.32</br>accuracy = 91.97</td>
    <td>-0.38%</td>
    <td>20%</br>unstructured</td>
    <td>gradient sensitivity</br>balanced</td>       
  </tr>
  <tr>  
  </tr>  
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>QQP</td>
    <td>[accuracy, f1] = [91.10, 88.05]</br>[accuracy, f1] = [90.48, 87.06]</td>
    <td>[-0.68%, -1.12%]</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>        
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>QQP</td>
    <td>[accuracy, f1] = [91.10, 88.05]</br>[accuracy, f1] = [90.92, 87.78]</td>
    <td>[-0.20%, -0.31%]</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>        
  </tr>
  <tr>
  </tr>   
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>QNLI</td>
    <td>accuracy = 91.54</br>accuracy = 90.39</td>
    <td>-1.26%</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>        
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>QNLI</td>
    <td>accuracy = 91.54</br>accuracy = 90.87</td>
    <td>-0.73%</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>      
  </tr>
  <tr>
  </tr>   
  <tr>
    <td>Bert-Base</td>
    <td>question answering</td>
    <td>[em, f1] = [79.34, 87.10]</br>[em, f1] = [77.27, 85.75]</td>
    <td>[-2.61%, -1.54%]</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>   
  </tr>  
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>question answering</td>
    <td>[em, f1] = [79.34, 87.10]</br>[em, f1] = [78.03, 86.50]</td>
    <td>[-1.65%, -0.69%]</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>       
  </tr>  
  <tr>
  </tr>  
</tbody>
</table>

## Validated Knowledge Distillation Examples

|  Example Name       | Dataset   | Student<br>(Metrics)                 | Teacher<br>(Metrics)               | Student With Distillation<br>(Metrics Improvement)  | Student With <br>Distributed Distillation<br>(Metrics Improvement)  |
|---------------------|-----------|--------------------------------------|------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| MobileNet example   | CIFAR-10  | MobileNetV2-0.35<br>(0.7965 ACC)     | WideResNet40-2<br>(0.9522 ACC)     |   0.8178 ACC<br>(0.0213 ACC)                        |   0.8235 ACC<br>(0.027 ACC)                        |
| CNN example         | CIFAR-100 | CNN-2<br>(0.5494 ACC)                | CNN-10<br>(0.7153 ACC)             |   0.5540 ACC<br>(0.0046 ACC)                        |   0.5523 ACC<br>(0.0029 ACC)                        |
| VGG example         | CIFAR-100 | VGG-8-BN<br>(0.7022 ACC)             | VGG-13-BN<br>(0.7415 ACC)          |   0.7025 ACC<br>(0.0003 ACC)                        |   NA                        |
| ResNet example      | ImageNet  | ResNet18<br>(0.6739 ACC)             | ResNet50<br>(0.7399 ACC)           |   0.6845 ACC<br>(0.0106 ACC)                        |   NA                        |
| BlendCnn example    |   MRPC    | BlendCnn<br>(0.7034 ACC)             | BERT-Base<br>(0.8382 ACC)          |   0.7034 ACC<br>(0 ACC)                             |   NA                        |
| BiLSTM example      |  SST-2    | BiLSTM<br>(0.8314 ACC)               | RoBERTa-Base<br>(0.9403 ACC)       |   0.9048 ACC<br>(0.0734 ACC)                        |   NA                        |
|DistilBERT example   |  SQuAD    | DistilBERT<br>(0.7323/0.8256 EM/F1)  | BERT-Base<br>(0.8084/0.8814 EM/F1) |   0.7442/0.8371 EM/F1<br>(0.0119/0.0115 EM/F1)      |   NA                        |
|TinyBERT example     |  MNLI     | TinyBERT<br>(0.8018/0.8044 m/mm)     | BERT-Base<br>(0.8363/0.8411 m/mm)  |   0.8025/0.8074 m/mm<br>(0.0007/0.0030 m/mm)        |   NA                        |
|BERT-3 example       |  QQP      | BERT-3<br>(0.8626/0.8213 EM/F1)      | BERT-Base<br>(0.9091/0.8782 EM/F1) |   0.8684/0.8259 EM/F1<br>(0.0058/0.0046 EM/F1)      |   NA                        |
|DistilRoBERTa example|  COLA     | DistilRoBERTa<br>(0.6057 ACC)        | RoBERTa-Large<br>(0.6455 ACC)      |   0.6187 ACC<br>(0.0130 ACC)                        |   NA                        |

## Validated ONNX QDQ INT8 Models on Multiple Hardware through ONNX Runtime

<table class="docutils">
<thead>
  <tr>
    <th class="tg-y3we">Model (ONNX QDQ)</th>
    <th class="tg-pm1l">AWS c6i.2xlarge (Intel)<br>CPU Execution Provider</th>
    <th class="tg-pm1l">AWS c6a.2xlarge (AMD)<br>CPU Execution Provider</th>
    <th class="tg-pm1l">AWS c6g.2xlarge (ARM)<br>CPU Execution Provider</th>
    <th class="tg-8d8j">NVidia A100<br>CUDA Execution<br>Provider</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-cwad">ResNet50</td>
    <td class="tg-pm1l">74.76%</td>
    <td class="tg-pm1l">68.95%</td>
    <td class="tg-pm1l">74.76%</td>
    <td class="tg-6q5x">74.75%</td>
  </tr>
  <tr>
    <td class="tg-cwad">BERT-base</td>
    <td class="tg-pm1l">85.54%</td>
    <td class="tg-pm1l">84.56%</td>
    <td class="tg-pm1l">85.54%</td>
    <td class="tg-6q5x">84.31%</td>
  </tr>
  <tr>
    <td class="tg-cwad">ResNet50 V1.5</td>
    <td class="tg-pm1l">72.20%</td>
    <td class="tg-pm1l">67.70%</td>
    <td class="tg-pm1l">72.20%</td>
    <td class="tg-6q5x">72.29%</td>
  </tr>
  <tr>
    <td class="tg-cwad">MobileNet V2</td>
    <td class="tg-pm1l">65.82%</td>
    <td class="tg-pm1l">58.56%</td>
    <td class="tg-pm1l">65.83%</td>
    <td class="tg-pm1l">65.63%</td>
  </tr>
  <tr>
    <td class="tg-cwad">SSD MobileNet V1</td>
    <td class="tg-pm1l">22.45%</td>
    <td class="tg-pm1l">16.53%</td>
    <td class="tg-pm1l">22.45%</td>
    <td class="tg-pm1l">22.35%</td>
  </tr>
  <tr>
    <td class="tg-cwad">DistilBERT base MRPC</td>
    <td class="tg-pm1l">84.56%</td>
    <td class="tg-pm1l">83.82%</td>
    <td class="tg-pm1l">84.56%</td>
    <td class="tg-6q5x">84.56%</td>
  </tr>
  <tr>
    <td class="tg-cwad">SqueezeNet</td>
    <td class="tg-pm1l">56.54%</td>
    <td class="tg-pm1l">53.52%</td>
    <td class="tg-pm1l">56.54%</td>
    <td class="tg-6q5x">56.55%</td>
  </tr>
  <tr>
    <td class="tg-cwad">SSD</td>
    <td class="tg-pm1l">18.63%</td>
    <td class="tg-pm1l">18.54%</td>
    <td class="tg-pm1l">18.63%</td>
    <td class="tg-6q5x">18.61%</td>
  </tr>
  <tr>
    <td class="tg-cwad">AlexNet</td>
    <td class="tg-pm1l">54.71%</td>
    <td class="tg-pm1l">47.06%</td>
    <td class="tg-pm1l">54.71%</td>
    <td class="tg-pm1l">54.79%</td>
  </tr>
  <tr>
    <td class="tg-cwad">CaffeNet</td>
    <td class="tg-pm1l">56.25%</td>
    <td class="tg-pm1l">52.35%</td>
    <td class="tg-pm1l">56.27%</td>
    <td class="tg-pm1l">56.24%</td>
  </tr>
  <tr>
    <td class="tg-cwad">GoogleNet</td>
    <td class="tg-pm1l">67.73%</td>
    <td class="tg-pm1l">63.56%</td>
    <td class="tg-pm1l">67.72%</td>
    <td class="tg-6q5x">67.76%</td>
  </tr>
  <tr>
    <td class="tg-cwad">ZFNet</td>
    <td class="tg-pm1l">55.86%</td>
    <td class="tg-pm1l">45.09%</td>
    <td class="tg-pm1l">55.86%</td>
    <td class="tg-pm1l">55.89%</td>
  </tr>
  <tr>
    <td class="tg-cwad">Inception V1</td>
    <td class="tg-pm1l">67.21%</td>
    <td class="tg-pm1l">63.03%</td>
    <td class="tg-pm1l">67.20%</td>
    <td class="tg-6q5x">67.21%</td>
  </tr>
  <tr>
    <td class="tg-cwad">SSD MobileNet V1 (ONNX Model Zoo)</td>
    <td class="tg-pm1l">22.86%</td>
    <td class="tg-pm1l">16.94%</td>
    <td class="tg-pm1l">22.80%</td>
    <td class="tg-pm1l">22.87%</td>
  </tr>
  <tr>
    <td class="tg-cwad">Mobile bert MRPC</td>
    <td class="tg-pm1l">85.54%</td>
    <td class="tg-pm1l">84.56%</td>
    <td class="tg-pm1l">85.54%</td>
    <td class="tg-pm1l">85.54%</td>
  </tr>
  <tr>
    <td class="tg-cwad">Roberta base MRPC</td>
    <td class="tg-pm1l">89.46%</td>
    <td class="tg-pm1l">90.44%</td>
    <td class="tg-pm1l">89.71%</td>
    <td class="tg-pm1l">89.71%</td>
  </tr>
  <tr>
    <td class="tg-cwad">ResNet50 V1.5 MLPerf</td>
    <td class="tg-pm1l">76.14%</td>
    <td class="tg-pm1l">72.80%</td>
    <td class="tg-pm1l">76.14%</td>
    <td class="tg-6q5x">76.17%</td>
  </tr>
  <tr>
    <td class="tg-cwad">VGG16</td>
    <td class="tg-pm1l">66.69%</td>
    <td class="tg-pm1l">64.25%</td>
    <td class="tg-pm1l">66.69%</td>
    <td class="tg-pm1l">66.64%</td>
  </tr>
  <tr>
    <td class="tg-cwad">VGG16 (ONNX Model Zoo)</td>
    <td class="tg-pm1l">72.31%</td>
    <td class="tg-pm1l">69.35%</td>
    <td class="tg-pm1l">72.32%</td>
    <td class="tg-pm1l">72.34%</td>
  </tr>
  <tr>
    <td class="tg-cwad">MobileNet V3 MLPerf</td>
    <td class="tg-pm1l">75.57%</td>
    <td class="tg-pm1l">70.78%</td>
    <td class="tg-pm1l">75.56%</td>
    <td class="tg-6q5x">75.52%</td>
  </tr>
  <tr>
    <td class="tg-cwad">EfficientNet</td>
    <td class="tg-pm1l">77.61%</td>
    <td class="tg-pm1l">76.52%</td>
    <td class="tg-pm1l">77.56%</td>
    <td class="tg-pm1l">77.60%</td>
  </tr>
  <tr>
    <td class="tg-cwad">MobileNet V2 (ONNX Model Zoo)</td>
    <td class="tg-pm1l">68.51%</td>
    <td class="tg-pm1l">62.48%</td>
    <td class="tg-pm1l">68.58%</td>
    <td class="tg-pm1l">68.48%</td>
  </tr>
  <tr>
    <td class="tg-413a">ShuffleNet V2</td>
    <td class="tg-pm1l">66.12%</td>
    <td class="tg-pm1l">58.41%</td>
    <td class="tg-pm1l">66.11%</td>
    <td class="tg-pm1l">66.11%</td>
  </tr>
</tbody>
</table>
