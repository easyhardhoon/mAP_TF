from pycocotools.coco import COCO
import random
import os
import urllib
from tqdm import tqdm
from PIL import Image

# 데이터를 다운로드할 경로 지정
dataDir = '/home/hoon/YOLO_PARSING/'

# COCO API로 COCO dataset 로드
coco = COCO(dataDir + 'annotations/instances_val2017.json')
random.seed(42)

# 카테고리 ID를 가져오기
catIds = coco.getCatIds()

# 카테고리 ID 중에서 80개 아이디를 0번 인덱스부터 차례대로 출력
for i, cat_id in enumerate(catIds[:80]):
    cat_info = coco.loadCats(cat_id)[0]
    print(f"{i}: {cat_info['name']}")

