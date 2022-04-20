import os
from random import randrange
from tqdm import tqdm

PATH = "/home/heinecantor/Scaricati/HANDS_yolo"

os.makedirs(PATH + "/train/images", exist_ok=True)
os.makedirs(PATH + "/train/labels", exist_ok=True)

os.makedirs(PATH + "/valid/images", exist_ok=True)
os.makedirs(PATH + "/valid/labels", exist_ok=True)

os.makedirs(PATH + "/test/images", exist_ok=True)
os.makedirs(PATH + "/test/labels", exist_ok=True)

fileImmagini = os.listdir(PATH + "/images")
countImmaginiGlobale = len(fileImmagini)

for i in tqdm(range(countImmaginiGlobale)):
    fileImmagini = os.listdir(PATH + "/images")
    randomPick = randrange(0, len(fileImmagini))

    randomImageName = fileImmagini[randomPick]
    randomLabelName = randomImageName.removesuffix(".png") + ".txt"

    pathSrcRandomImage = PATH + "/images/" + randomImageName
    pathSrcRandomLabel = PATH + "/labels/" + randomLabelName

    dirDest = ""
    if i < 9600:
        dirDest = "/train/"
    elif i < 10800:
        dirDest = "/valid/"
    else:
        dirDest = "/test/"

    pathDstRandomImage = PATH + dirDest + "images/" + randomImageName
    pathDstRandomLabel = PATH + dirDest + "labels/" + randomLabelName

    os.rename(pathSrcRandomImage, pathDstRandomImage)
    os.rename(pathSrcRandomLabel, pathDstRandomLabel)

