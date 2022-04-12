import os

DATASET_PATH_LIST = ["../dataset/train/", "../dataset/valid/", "../dataset/test/"]

for path in DATASET_PATH_LIST:
    fullPath = os.path.join(path, "labels/")
    for file in os.listdir(fullPath):
        filePath = os.path.join(fullPath, file)

        fileStream = open(filePath, 'r')
        newFile = []
        for line in fileStream:
            lineArray = line.split(' ')
            lineArray[0] = '0'
            newLine = " ".join(lineArray)
            newFile.append(newLine)

        fileStream.close()

        fileStream = open(filePath, 'w')
        fileStream.writelines(newFile)
        fileStream.close()
            