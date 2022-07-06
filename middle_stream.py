import os
import glob
import time

path = os.getcwd()
videos = glob.glob(os.getcwd()+"/*.avi")
for item in videos:
    import numpy as np
    import cv2

    # Open the video
    cap = cv2.VideoCapture(item)
    curr = str(time.time()).replace(".","_")
    # Initialize frame counter
    cnt = 0

    # Some characteristics from the original video
    w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

    # Here you can define your croping values
    x,y,h,w = 101,h_frame//4,3*h_frame//4,3*w_frame//4

    # output
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(f'filename_{curr}.avi', fourcc, fps, (w, h))


    # Now we start
    while(cap.isOpened()):
        ret, frame = cap.read()

        cnt += 1 # Counting frames

        # Avoid problems when video finish
        if ret==True:
            # Croping the frame
            crop_frame = frame[y:y+h, x:x+w]


            out.write(crop_frame)

            # cv2.imshow('frame',frame)
            # cv2.imshow('croped',crop_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break


    cap.release()
    out.release()
    cv2.destroyAllWindows()