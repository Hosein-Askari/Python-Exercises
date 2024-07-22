import cv2
import numpy as np

img = np.zeros((400,400,), dtype=np.uint8)

img[150:250,100:120]=255
img[190:210,100:200]=255
img[150:250,200:220]=255


cv2.imshow("",img)
cv2.waitKey()