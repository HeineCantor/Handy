import numpy as np
import imutils
import cv2
import time
import math

#inizializzazione video

stream = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0

first_iter = True

backgroundImage = None
backgroundAvailable = False

blur = 21
canny_low = 15
canny_high = 150
min_area = 0.0005
max_area = 0.95
dilate_iter = 10
erode_iter = 10
mask_color = (0.0,0.0,0.0)

while True:
    (grabbed, frame) = stream.read()

    if not grabbed:
        print("Source video non disponibile.")
        break

    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    fps = math.floor(fps)
    prev_frame_time = new_frame_time

    cv2.putText(frame, f"{fps}", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (120, 0, 0), 2)

    cv2.imshow("Frame", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

    