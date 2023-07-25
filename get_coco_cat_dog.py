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

# 'cat'과 'dog' 클래스에 해당하는 카테고리 ID 가져오기
catIds_cat = coco.getCatIds(catNms=['cat'])
catIds_dog = coco.getCatIds(catNms=['dog'])

# 'cat'과 'dog' 클래스에 해당하는 이미지 ID 가져오기
imgIds_cat = coco.getImgIds(catIds=catIds_cat)
imgIds_dog = coco.getImgIds(catIds=catIds_dog)

# 이미지 ID를 랜덤으로 섞어서 40개씩 선택
imgIds_cat_sampled = random.sample(imgIds_cat, 40)
imgIds_dog_sampled = random.sample(imgIds_dog, 40)

# 최종 선택된 이미지 ID 합치기
imgIds_sampled = imgIds_cat_sampled + imgIds_dog_sampled

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
                x_center = round(x + width / 2, 2)
                y_center = round(y + height / 2, 2)
                width = round(width, 2)
                height = round(height, 2)

                # 바운딩 박스 좌표 스케일링
                x_center_scaled = int((x_center / img_pil.width) * target_size[0])
                y_center_scaled = int((y_center / img_pil.height) * target_size[1])
                width_scaled = int((width / img_pil.width) * target_size[0])
                height_scaled = int((height / img_pil.height) * target_size[1])

                f.write(f"{category_name} {x_center_scaled} {y_center_scaled} {width_scaled} {height_scaled}\n")

# 어노테이션 정보 출력 (확인용)
for ann in annotations:
    img_id = ann["image_id"]
    img_info = coco.loadImgs(img_id)[0]
    txt_file = dataDir + 'annotations/' + img_info['file_name'].split('.')[0] + '.txt'

    with open(txt_file, 'r') as f:
        print(f"File: {txt_file}")
        for line in f:
            print(line.strip())

