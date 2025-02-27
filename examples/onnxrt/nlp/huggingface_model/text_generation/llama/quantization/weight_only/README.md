Step-by-Step
============

This example confirms llama's weight only accuracy on [lambada](https://huggingface.co/datasets/lambada).

# Prerequisite

## 1. Environment
```shell
pip install neural-compressor
pip install -r requirements.txt
```
> Note: Validated ONNX Runtime [Version](/docs/source/installation_guide.md#validated-software-environment).

## 2. Prepare Model

```bash
optimum-cli export onnx --model decapoda-research/llama-7b-hf --task text-generation-with-past ./llama_7b
```

# Run

## 1. Quantization

```bash
bash run_quant.sh --input_model=/path/to/model \ # folder path of onnx model
                  --output_model=/path/to/model_tune \ # folder path to save onnx model
                  --batch_size=batch_size # optional \
                  --dataset=NeelNanda/pile-10k \
                  --tokenizer=decapoda-research/llama-7b-hf \ # model name or folder path containing all relevant files for model's tokenizer
                  --algorithm=RTN # support RTN, AWQ, GPTQ
```

## 2. Benchmark

```bash
bash run_benchmark.sh --input_model=path/to/model \ # folder path of onnx model
                      --batch_size=batch_size \ # optional 
                      --tokenizer=decapoda-research/llama-7b-hf \ # model name or folder path containing all relevant files for model's tokenizer
                      --tasks=lambada_openai
```
