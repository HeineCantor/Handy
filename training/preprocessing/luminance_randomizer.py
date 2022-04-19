import cv2
import os

from tqdm import tqdm

from random import seed
from random import randrange

import numpy as np

DATASET_PATH_LIST = ["../dataset/train/", "../dataset/valid/", "../dataset/test/"]
LUMINANCE_RANGE_MIN = -10
LUMINANCE_RANGE_MAX = 180

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

seed(1)

for path in DATASET_PATH_LIST:
    fullPath = os.path.join(path, "images/")
    print(f"Luminating {path}")
    for file in tqdm(os.listdir(fullPath)):
        filePath = os.path.join(fullPath, file)
        image = cv2.imread(filePath)

        randLumValue = np.uint8(randrange(LUMINANCE_RANGE_MIN, LUMINANCE_RANGE_MAX))

        image = increase_brightness(image, randLumValue)

        cv2.imwrite(filePath, image)