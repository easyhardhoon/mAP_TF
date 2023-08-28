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

# 카테고리 ID를 가져오고, 랜덤으로 섞어서 100개만 선택
catIds = coco.getCatIds()
catIds_sampled = random.sample(catIds, 80)

# 각 카테고리에 속하는 이미지 ID 가져오기
imgIds = []
for catId in catIds_sampled:
    imgIds += coco.getImgIds(catIds=catId)

# 이미지 ID를 랜덤으로 섞어서 100개만 선택
imgIds_sampled = random.sample(imgIds, 80)

# 이미지와 어노테이션 정보 가져오기
images = coco.loadImgs(imgIds_sampled)
annotations = coco.loadAnns(coco.getAnnIds(imgIds=imgIds_sampled))

# 객체 이름과 카테고리 ID를 매핑하는 딕셔너리 생성
categoryDict = {cat['id']: cat['name'] for cat in coco.dataset['categories']}

# 이미지 다운로드 및 어노테이션 정보 저장
target_size = (416, 416)
for img in tqdm(images):
    img_id = img['id']
    img_url = img['coco_url']
    img_file = dataDir + 'images/' + img['file_name']

    # 이미지 다운로드
    if not os.path.exists(img_file):
        urllib.request.urlretrieve(img_url, img_file)

    # 이미지 리사이징
    img_pil = Image.open(img_file)
    img_resized = img_pil.resize(target_size, Image.ANTIALIAS)
    img_resized.save(img_file)

    # 어노테이션 정보 저장
    txt_file = dataDir + 'annotations/' + img['file_name'].split('.')[0] + '.txt'
    with open(txt_file, 'w') as f:
        for ann in annotations:
            if ann["image_id"] == img_id:
                category_id = ann["category_id"]
                category_name = categoryDict[category_id]
                bbox = ann["bbox"]
                x, y, width, height = bbox

                # 바운딩 박스 좌상단 x, y와 우하단 x, y 형식으로 변환
                x_min = x
                y_min = y
                x_max = x + width
                y_max = y + height

                # 바운딩 박스 좌표 스케일링
                x_min_scaled = (x_min / img_pil.width) * target_size[0]
                y_min_scaled = (y_min / img_pil.height) * target_size[1]
                x_max_scaled = (x_max / img_pil.width) * target_size[0]
                y_max_scaled = (y_max / img_pil.height) * target_size[1]

                f.write(f"{category_name} {x_min_scaled} {y_min_scaled} {x_max_scaled} {y_max_scaled}\n")

# 어노테이션 정보 출력 (확인용)
for ann in annotations:
    img_id = ann["image_id"]
    img_info = coco.loadImgs(img_id)[0]
    txt_file = dataDir + 'annotations/' + img_info['file_name'].split('.')[0] + '.txt'

    with open(txt_file, 'r') as f:
        print(f"File: {txt_file}")
        for line in f:
            print(line.strip())

