import os
import csv
import ast
from tqdm import tqdm

SUBJECT_DIRS = "/home/heinecantor/Scaricati/Subjects"
IMG_SIZE = (960, 540)

for subjectDir in os.listdir(SUBJECT_DIRS):
    dirPath = os.path.join(SUBJECT_DIRS, subjectDir)
    os.makedirs(dirPath + "/labels", exist_ok=True)
    file = open(os.path.join(dirPath, subjectDir + ".txt"))
    csvReader = csv.reader(file)
    for idx, row in tqdm(enumerate(csvReader)):
        if idx == 0:
            continue
        newFile = []
        fileName = row[0].split('\\')[-1]
        for idx, item in enumerate(row[2:]):
            item = item.replace(" ", ",")
            itemList = ast.literal_eval(item)
            if(any(itemList)):
                rowList = []
                rowList.append(str(idx))
                yoloX = itemList[0] + (itemList[2] / 2)
                yoloY = itemList[1] + (itemList[3] / 2)
                yoloX = yoloX / IMG_SIZE[0]
                yoloY = yoloY / IMG_SIZE[1]
                yoloWidth = itemList[2] / IMG_SIZE[0]
                yoloHeight = itemList[3] / IMG_SIZE[1]
                rowList.append(str(yoloX))
                rowList.append(str(yoloY))
                rowList.append(str(yoloWidth))
                rowList.append(str(yoloHeight))
                line = " ".join(rowList)
                newFile.append(line)

        filePath = os.path.join(dirPath, "labels/" + fileName.removesuffix(".png") + ".txt")
        fileSaver = open(filePath, 'w')
        fileSaver.writelines('\n'.join(newFile))
        fileSaver.close()      
    
