import cv2
import os

from tqdm import tqdm

from random import gauss, seed
from random import randrange

import numpy as np

DATASET_PATH_LIST = ["../dataset/train/", "../dataset/valid/", "../dataset/test/"]

def gaussianNoise(image, gaussMean = 0, gaussVariance = 1):
    w, h, ch = image.shape

    gauss = np.random.normal(gaussMean, gaussVariance**0.5, image.size)
    gauss = gauss.reshape(w, h, ch).astype('uint8')

    imgGauss = cv2.add(image, gauss)

    return imgGauss

for path in DATASET_PATH_LIST:
    fullPath = os.path.join(path, "images/")
    print(f"Noising {path}")
    for file in tqdm(os.listdir(fullPath)):
        filePath = os.path.join(fullPath, file)
        image = cv2.imread(filePath)

        image = gaussianNoise(image, gaussVariance=0.2)
        cv2.imwrite(filePath, image)