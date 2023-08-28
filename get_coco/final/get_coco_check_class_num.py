from pycocotools.coco import COCO
import random
import os
import urllib
from tqdm import tqdm
from PIL import Image

dataDir = '/home/hoon/YOLO_PARSING/'
coco = COCO(dataDir + 'annotations/instances_val2017.json')
random.seed(42)

all_catIds = coco.getCatIds()
num_images_per_class = 4
imgIds_sampled = []
class_image_counts = {}  # 클래스 아이디 별 이미지 수를 저장할 딕셔너리

for catId in all_catIds:
    imgIds = coco.getImgIds(catIds=catId)
    class_image_counts[catId] = len(imgIds)  # 각 클래스 아이디 별 이미지 수 저장
    imgIds_sampled += random.sample(imgIds, num_images_per_class)

images = coco.loadImgs(imgIds_sampled)
annotations = coco.loadAnns(coco.getAnnIds(imgIds=imgIds_sampled))
categoryDict = {cat['id']: cat['name'] for cat in coco.dataset['categories']}

for catId, count in class_image_counts.items():
    category_name = categoryDict[catId]
    print(f"Class: {category_name}, Image Count: {count}")


