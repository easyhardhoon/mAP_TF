echo "## HOON : run docker automatically!!! ##"
echo "==> Run container...."
xhost +local:docker
sudo docker run --rm -it \
	--name mAP_TF_container\
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-v /home/nvidia/mAP_TF:/root/mAP_TF \
	-e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 \
	-p 5000:5000 -p 8888:8888 \
	-u root \
	tf:1.1 \
	/bin/bash
