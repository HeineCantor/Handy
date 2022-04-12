import cv2 
import os

DATASET_PATH_LIST = ["../dataset/train/", "../dataset/valid/", "../dataset/test/"]
newSize = (640, 360)

for path in DATASET_PATH_LIST:
    fullPath = os.path.join(path, "images/")
    for file in os.listdir(fullPath):
        filePath = os.path.join(fullPath, file)
        image = cv2.imread(filePath)
        image = cv2.resize(image, newSize)
        cv2.imwrite(filePath, image)