#ssh -X hoon@39.115.19.134 -p9000
#cd YOLO_PARSING/mm
#rm -r *.jpg
#cd ../annotations
#rm -r *.txt
#cd ../
#python3 get_image_and_annotations_and_resize.py
#python3 search_jpg.py
#cd annotations
#scp -P8001 *.txt nvidia@39.115.19.134:~/mAP_TF/input/detection-results
#cd ../mm
#scp -P8001 *.jpg nvidia@39.115.19.134:~/mAP_TF/input/images-optional


