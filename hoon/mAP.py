import numpy as np
import tensorflow as tf
from tensorflow import keras

def get_cls_index(real_bbox_cls_vector):
    real_bbox_cls_index_vector = []
    for i in real_bbox_cls_vector:
        max_index = np.argmax(i)
        real_bbox_cls_index_vector.append(max_index)
    print("real_bbox_cls_index vector:", real_bbox_cls_index_vector)
    print()
    return real_bbox_cls_index_vector

def readDataFromFile(filename):
    data = []
    with open(filename, 'r') as inFile:
        for line in inFile:
            row = [float(value) for value in line.split()]
            data.append(row)
    return data

def main():
    real_bbox_cls_vector = readDataFromFile("./cls.txt")
    real_bbox_loc_vector = readDataFromFile("./loc.txt")
    real_bbox_cls_index_vector = get_cls_index(real_bbox_cls_vector)
    print("size:", len(real_bbox_cls_vector))
    print("size:", len(real_bbox_loc_vector))
    print("size:", len(real_bbox_cls_index_vector))

if __name__ == '__main__':
    main()

