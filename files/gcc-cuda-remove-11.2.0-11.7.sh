#!/bin/bash

export PATH=$(echo "$PATH" | sed -e 's/:\/opt\/gcc-11.2.0\/bin//' -e 's/:\/opt\/cuda-11.7.1\/bin//')
export LD_LIBRARY_PATH=$(echo "$LD_LIBRARY_PATH" | sed -e 's/:\/opt\/cuda-11.7.1\/lib64//')
unset CUDA_HOME
unset CUDA_ROOT
unset CUDA_PATH
unset CUDA_INC_PATH
unset CUDA_VISIBLE_DEVICES