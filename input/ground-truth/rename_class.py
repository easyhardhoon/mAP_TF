import os


word_map = {
    "fire_hydrant": "fire_hydrant", 
    "traffic_light": "traffic_light", 
    "stop_sign": "stop_sign", 
    "parking_meter": "parking_meter", 
    "sports_ball": "sports_ball", 
    "baseball_bat": "baseball_bat", 
    "baseball_glove": "baseball_glove",
    "tennis_racket": "tennis_racket",
    "wine_glass": "wine_glass",
    "hot_dog": "hot_dog",
    "potted_plant": "potted_plant",
    "dining_table": "dining_table",
    "cell_phone": "cell_phone",
    "teddy_bear": "teddy_bear",
    "hair_drier": "hair_drier",
    "motorbike": "motorbike", #m o t o r c y c l e
    "person": "person",
    "bicycle": "bicycle",
    "car": "car",
    "aeroplane": "aeroplane", #a i r p l a n e
    "bus": "bus",
    "train": "train",
    "truck": "truck",
    "boat": "boat",
    "bench": "bench",
    "bird": "bird",
    "cat": "cat",
    "dog": "dog",
    "horse": "horse",
    "sheep": "sheep",
    "cow": "cow",
    "elephant": "elephant",
    "bear": "bear",
    "zebra": "zebra",
    "giraffe": "giraffe",
    "backpack": "backpack",
    "umbrella": "umbrella",
    "handbag": "handbag",
    "tie": "tie",
    "suitcase": "suitcase",
    "frisbee": "frisbee",
    "skis": "skis",
    "snowboard": "snowboard",
    "kite": "kite",
    "banana": "banana",
    "apple": "apple",
    "sandwich": "sandwich",
    "orange": "orange",
    "broccoli": "broccoli",
    "carrot": "carrot",
    "pizza": "pizza",
    "donut": "donut",
    "cake": "cake",
    "chair": "chair",
    "sofa": "sofa", #c o u c h
    "bed": "bed",
    "toilet": "toilet",
    "tvmonitormonitor": "tvmonitormonitormonitormonitor",  #t v
    "laptop": "laptop",
    "mouse": "mouse",
    "remote": "remote",
    "keyboard": "keyboard",
    "microwave": "microwave",
    "oven": "oven",
    "toaster": "toaster",
    "sink": "sink",
    "refrigerator": "refrigerator",
    "book": "book",
    "clock": "clock",
    "vase": "vase",
    "scissors": "scissors",
    "toothbrush": "toothbrush"
}


def replace_words_in_file(file_path, word_map):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            for old_word, new_word in word_map.items():
                line = line.replace(old_word, new_word)
            file.write(line)

if __name__ == "__main__":
    directory_path = "/home/nvidia/mAP_TF/input/ground-truth"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            replace_words_in_file(file_path, word_map)
            print(f"Replaced in {filename}: {word_map}")

