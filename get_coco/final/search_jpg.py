import os
import shutil
dataDir = '/home/hoon/YOLO_PARSING/'

txt_files = [f for f in os.listdir(dataDir + 'annotations') if f.endswith('.txt')]

for txt_file in txt_files:
    img_file = os.path.splitext(txt_file)[0] + '.jpg'
    img_path = os.path.join(dataDir + 'images', img_file)
    new_folder_path = os.path.join(dataDir + 'mm')
    if os.path.exists(img_path):
        shutil.move(img_path, new_folder_path)
        print(f"Found matching image: {img_file}")
    else:
        print(f"Image not found for: {txt_file}")

