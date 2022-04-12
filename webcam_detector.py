from typing import Type
import numpy as np
import cv2
import time
import math
import torch
import pandas as pd
import tqdm

TEXT_FONT = cv2.FONT_HERSHEY_PLAIN
TEXT_SCALE = 0.8
TEXT_THICKNESS = 2
TEXT_COLOR = (0, 255, 0)

#inizializzazione video

stream = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0

#model = torch.hub.load('ultralytics/yolov5', 'yolov5m6', pretrained=True)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
model.eval()

while True:
    (grabbed, frame) = stream.read()

    if not grabbed:
        print("Source video non disponibile.")
        break

    frame = cv2.flip(frame, 1)

    result = model(frame)
    pandas = result.pandas()

    if len(pandas.xyxy) > 0:
        for res in pandas.xyxy: #per ogni bounding box
            for i in range(len(res)):
                pt1 = (int(res["xmin"][i]), int(res["ymin"][i]))
                pt2 = (int(res["xmax"][i]), int(res["ymax"][i]))

                cv2.rectangle(frame, pt1, pt2, color=(255,0,0), thickness=2)

                text = res["name"][i]

                font_size = cv2.getTextSize(text, TEXT_FONT, TEXT_SCALE, TEXT_THICKNESS)

                textP1 = pt1[0] + 5
                textP2 = pt1[1] + font_size[1] + 5

                cv2.putText(frame, text, (textP1, textP2), TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS)
    
    cv2.imshow("Frame", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

    