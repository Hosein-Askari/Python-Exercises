import cv2
import numpy as np

img = np.zeros((400,400,), dtype=np.uint8)
for i in range(0,301,100):
    for j in range (0,351,100):
        img[i:i+50,j:j+50]=255
        img[i+50:i+100,j+50:j+100]=255



cv2.imshow("",img)
cv2.waitKey()