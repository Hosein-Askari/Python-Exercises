import numpy as np
import cv2

 

cap = cv2.VideoCapture('Assignment-29/5.Background estimation/cars.mp4')
 

frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)
 

frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)
 

medianFrame = np.average(frames,axis=0).astype(dtype=np.uint8)    


cv2.imshow('frame', medianFrame)
cv2.waitKey(0)


