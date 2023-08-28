import os


word_map = {
    "tvmonitor": "tvmonitor",  #t v
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

