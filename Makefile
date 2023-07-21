mAP : run_eval.cc
	g++ -o run_eval run_eval.cc -I/usr/include/opencv4\
		-pthread -g -I/home/nvidia/FBF-TF\
		-I/home/nvidia/FBF-TF/tensorflow/lite/tools/make/downloads/flatbuffers/include\
		-L/home/nvidia/FBF-TF/tensorflow/lite/tools/make/gen/linux_aarch64/lib\
		-I/home/nvidia/FBF-TF/tensorflow/lite/tools/make/downloads/absl\
		-L/home/nvidia/FBF-TF/tensorflow/lite/tools/make/downloads/flatbuffers/build\
		-lopencv_gapi\
		-ltensorflow-lite\
		-lflatbuffers /lib/aarch64-linux-gnu/libdl.so.2\
		-I/home/nvidia/FBF-TF/tensorflow/lite/tools/evaluation/proto
		-lopencv_stitching\
		-lopencv_highgui\
		-lopencv_dnn\
		-lopencv_videoio\
		-lopencv_ml -lopencv_video\
		-lopencv_objdetect -lopencv_calib3d -lopencv_imgcodecs -lopencv_features2d -lopencv_flann\
		-lopencv_photo -lopencv_imgproc\
		-lopencv_core\
		/home/nvidia/FBF-TF/bazel-bin/tensorflow/lite/delegates/gpu/libtensorflowlite_gpu_delegate.so\
	 	/usr/lib/aarch64-linux-gnu/libEGL.so\
	        /usr/lib/aarch64-linux-gnu/libGL.so\
		/usr/lib/aarch64-linux-gnu/libGLESv2.so\

