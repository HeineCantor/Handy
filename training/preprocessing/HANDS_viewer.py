import cv2
import os

SUBJECT_DIRS = "/home/heinecantor/Scaricati/Subjects"
IMG_SIZE = (960, 540)

for subjectDir in os.listdir(SUBJECT_DIRS):
    subjectDirPath = os.path.join(SUBJECT_DIRS, subjectDir)
    imagesPath = os.path.join(SUBJECT_DIRS, subjectDir + "/" + subjectDir)
    for imageName in os.listdir(imagesPath):
        imagePath = os.path.join(imagesPath, imageName)
        image = cv2.imread(imagePath)
        labelName = imageName.removesuffix(".png") + ".txt"
        labelPath = os.path.join(subjectDirPath, "labels/" + labelName)
        labelFile = open(labelPath, 'r')
        for line in labelFile:
            lineSplit = line.split(' ')
            xSquare = (float(lineSplit[1]) - float(lineSplit[3]) / 2)*IMG_SIZE[0]
            ySquare = (float(lineSplit[2]) - float(lineSplit[4]) / 2)*IMG_SIZE[1]
            widthSquare = float(lineSplit[3]) * IMG_SIZE[0]
            heightSquare = float(lineSplit[4]) * IMG_SIZE[1]
            cv2.rectangle(image, (int(xSquare), int(ySquare)), (int(xSquare + widthSquare), int(ySquare + heightSquare)), color=(255,0,0), thickness=2)
        cv2.imshow("Immagine", image)
        cv2.waitKey(0)
        break