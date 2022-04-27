import cv2
import os
import bezier
from sklearn.ensemble import RandomForestRegressor

from tqdm import tqdm

from random import seed
from random import randrange
import numpy as np

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import splines

import math

DATASET_PATH_LIST = ["../dataset/train/", "../dataset/valid/", "../dataset/test/"]


CURVE_RANGE_MIN_X = 20
CURVE_RANGE_MAX_X = 230

CURVE_RANGE_MIN_Y = 40
CURVE_RANGE_MAX_Y = 220

DISTANCE_ABOVE_Y = 110
DISTANCE_BELOW_Y = 50


'''
def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
'''

def createLUT(x, y):
    xNodes = np.array([0, x, 255])
    yNodes = np.array([0, y, 255])

    spline = interp1d(xNodes, yNodes, kind='quadratic', fill_value='extrapolate')
    xRange = range(0, 256, 1)

    lut = spline(xRange)

    lut = [max(min(l, 255), 0) for l in lut]

    lut = np.array(np.uint8(lut))

    return lut

seed(1)

for path in DATASET_PATH_LIST:
    fullPath = os.path.join(path, "images/")
    print(f"Luminating {path}")
    for file in tqdm(os.listdir(fullPath)):
        filePath = os.path.join(fullPath, file)
        image = cv2.imread(filePath)

        randLumValueX = np.uint8(randrange(CURVE_RANGE_MIN_X, CURVE_RANGE_MAX_X))
        randLumValueY = np.uint8(randrange(max(CURVE_RANGE_MIN_Y, randLumValueX - DISTANCE_BELOW_Y), min(CURVE_RANGE_MAX_Y, randLumValueX + DISTANCE_ABOVE_Y)))

        lut = createLUT(randLumValueX, randLumValueY)

        #print(lut)

        image = cv2.LUT(image, lut)

        cv2.imwrite(filePath, image)