import numpy as np
import imutils
import cv2
import time
import math

#inizializzazione video

stream = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0

grabbed = False

backSub = cv2.createBackgroundSubtractorMOG2()

while not grabbed:
    input("Premi per prendere una foto del background")
    (grabbed, backgroundFrame) = stream.read()

cv2.imshow("Background frame", backgroundFrame)

while True:
    (grabbed, frame) = stream.read()

    if not grabbed:
        print("Source video non disponibile.")
        break

    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    fps = math.floor(fps)
    prev_frame_time = new_frame_time

    #frame = imutils.resize(frame, width=400)
    fgMask = cv2.subtract(frame, backgroundFrame)

    cv2.putText(frame, f"{fps}", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (120, 0, 0), 2)

    cv2.imshow("Frame", fgMask)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

    