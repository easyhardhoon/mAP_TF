#!/bin/bash
TflitePath="../FBF-TF/tensorflow/lite/tools/make"
echo "@@@get mAP using TFLite::coco_toolkit@@@"

cd ../FBF-TF 
sudo bazel build -s -c opt --copt="-DMESA_EGL_NO_X11_HEADERS" tensorflow/lite/delegates/gpu:libtensorflowlite_gpu_delegate.so

cd ../mAP_TF
sudo ldconfig

pwd
export DISPLAY=:0

. ${TflitePath}/build_aarch64_lib.sh


make mAP


