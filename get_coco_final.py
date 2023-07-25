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
                left, top, width, height = ann["bbox"]

                # 바운딩 박스 좌표 스케일링
                x_c_scaled = (left + width / 2) / img_pil.width * target_size[0]
                y_c_scaled = (top + height / 2) / img_pil.height * target_size[1]
                width_scaled = width / img_pil.width * target_size[0]
                height_scaled = height / img_pil.height * target_size[1]

            ## compute left, top, right, bottom
                left = int(x_c_scaled - width_scaled / 2)
                top = int(y_c_scaled - height_scaled / 2)
                right = int(x_c_scaled + width_scaled / 2)
                bottom = int(y_c_scaled + height_scaled / 2)

            # 좌표 값을 0 미만이 되지 않도록 조정
                left = max(left, 0)
                top = max(top, 0)
                right = min(right, target_size[0])
                bottom = min(bottom, target_size[1])
                f.write(f"{category_name} {left} {top} {right} {bottom}\n")

# 어노테이션 정보 출력 (확인용)
for ann in annotations:
    img_id = ann["image_id"]
    img_info = coco.loadImgs(img_id)[0]
    txt_file = dataDir + 'annotations/' + img_info['file_name'].split('.')[0] + '.txt'

    with open(txt_file, 'r') as f:
        print(f"File: {txt_file}")
        for line in f:
            print(line.strip())

