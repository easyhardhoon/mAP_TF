from pycocotools.coco import COCO
import os
import urllib
from tqdm import tqdm
from PIL import Image

dataDir = '/home/hoon/YOLO_PARSING/'
coco = COCO(dataDir + 'annotations/instances_val2017.json')

# get image 2000
imgIds = coco.getImgIds()[:2000]
images = coco.loadImgs(imgIds)

categoryDict = {cat['id']: cat['name'] for cat in coco.dataset['categories']}

target_size = (416, 416)
for img in tqdm(images):
    img_id = img['id']
    img_url = img['coco_url']
    img_file = dataDir + 'images/' + img['file_name']
    if not os.path.exists(img_file):
        urllib.request.urlretrieve(img_url, img_file)
    img_pil = Image.open(img_file)
    img_resized = img_pil.resize(target_size, Image.ANTIALIAS)
    img_resized.save(img_file)
    txt_file = dataDir + 'annotations/' + img['file_name'].split('.')[0] + '.txt'
    with open(txt_file, 'w') as f:
        annIds = coco.getAnnIds(imgIds=img_id)
        annotations = coco.loadAnns(annIds)
        for ann in annotations:
            category_id = ann["category_id"]
            category_name = categoryDict[category_id]
            left, top, width, height = ann["bbox"]
            x_c_scaled = (left + width / 2) / img_pil.width * target_size[0]
            y_c_scaled = (top + height / 2) / img_pil.height * target_size[1]
            width_scaled = width / img_pil.width * target_size[0]
            height_scaled = height / img_pil.height * target_size[1]
            left = int(x_c_scaled - width_scaled / 2)
            top = int(y_c_scaled - height_scaled / 2)
            right = int(x_c_scaled + width_scaled / 2)
            bottom = int(y_c_scaled + height_scaled / 2)
            left = max(left, 0)
            top = max(top, 0)
            right = min(right, target_size[0])
            bottom = min(bottom, target_size[1])
            f.write(f"{category_name} {left} {top} {right} {bottom}\n")

for ann in annotations:
    img_id = ann["image_id"]
    img_info = coco.loadImgs(img_id)[0]
    txt_file = dataDir + 'annotations/' + img_info['file_name'].split('.')[0] + '.txt'

    with open(txt_file, 'r') as f:
        print(f"File: {txt_file}")
        for line in f:
            print(line.strip())

