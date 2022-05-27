import numpy as np
import cv2
import torch
import pandas as pd

TEXT_FONT = cv2.FONT_HERSHEY_PLAIN
TEXT_SCALE = 1.2
TEXT_THICKNESS = 1
TEXT_COLOR = (0, 255, 0)

DEBUG = True

#inizializzazione video

stream = cv2.VideoCapture('video_name.mp4')

prev_frame_time = 0
new_frame_time = 0

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yoloL30newpre.pt')
model.eval()

# Idea: mandare in input alla rete l'immagine filtrata (passa-basso / passa-banda)

while True:
    (sourceAvailable, frame) = stream.read()

    if not sourceAvailable:
        print("Source video non disponibile.")
        break

    #frame = cv2.flip(frame, 1)

    result = model(frame)
    pandas = result.pandas()

    grabbed = False #non hai afferrato nessun oggetto

    if len(pandas.xyxy) > 0:
        for res in pandas.xyxy: #per ogni bounding box
            for i in range(len(res)):
                pt1 = (int(res["xmin"][i]), int(res["ymin"][i]))
                pt2 = (int(res["xmax"][i]), int(res["ymax"][i]))

                className = res["name"][i]

                coloreBox = (255, 0, 0)
                coloreBaricentro = (0, 0, 255)

                if(className == "Nine_VFR" or className == "Nine_VFL"):
                    coloreBaricentro = (0, 255, 0)
                    coloreBox = (0, 255, 0)
                    grabbed = True
                else:
                    grabbed = False

                baricentroX = (pt2[0] + pt1[0]) // 2
                baricentroY = (pt1[1] + pt2[1]) // 2
                baricentro = (baricentroX, baricentroY)

                cv2.rectangle(frame, pt1, pt2, color=coloreBox, thickness=2)
                cv2.circle(frame, baricentro, 1, color=coloreBaricentro, thickness=4)

                if DEBUG:
                    font_size = cv2.getTextSize(className, TEXT_FONT, TEXT_SCALE, TEXT_THICKNESS)

                    textP1 = pt1[0] + 5
                    textP2 = pt1[1] + font_size[1] - 10

                    cv2.putText(frame, className, (textP1, textP2), TEXT_FONT, TEXT_SCALE, TEXT_COLOR, TEXT_THICKNESS)
    
    cv2.imshow("Frame", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

stream.release()
