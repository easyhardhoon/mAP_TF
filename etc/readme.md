# YOLO parsing dir.
use docker to avoid corrupting FBF-TF with tensorflow(keras) 
**mAP_TF is related to FBF-TF-hoon(tflite API) & FBF-TF(tflite base code)**


**main flow** 
1. input image 
2. invoke yolov4-tiny.tflite
3. collect loc_vector & cls_vector in tflite::subgraph::tensors
4. save loc_vector & cls_vector and move out of tflite, going to this dir.
5. use docker 
6. run mAP.py using NMS api, mAP api based on tensorflow-keras


