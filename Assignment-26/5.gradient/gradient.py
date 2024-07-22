import cv2
import numpy as np

img = np.zeros((255,400), dtype=np.uint8)


for i in range (0,255):
    
        img[254-i,0:400]=i


cv2.imshow("",img)
cv2.waitKey()