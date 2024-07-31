import cv2
import numpy as np

match=np.zeros((440,680,3),np.uint8)
match=np.array(match)

cv2.rectangle(match,(0,0),(680,440),(0,255,0),-1)
cv2.rectangle(match,(20,20),(660,420),(255,255,255),3)
cv2.rectangle(match,(20,130),(60,310),(255,255,255),3)
cv2.rectangle(match,(20,80),(140,360),(255,255,255),3)
cv2.rectangle(match,(620,130),(660,310),(255,255,255),3)
cv2.rectangle(match,(540,80),(660,360),(255,255,255),3)

cv2.circle(match,(340,220),85,(255,255,255),3)

cv2.circle(match,(340,220),4,(255,255,255),4)
cv2.circle(match,(100,220),3,(255,255,255),3)
cv2.circle(match,(580,220),3,(255,255,255),3)

cv2.line(match,(340,20),(340,420),(255,255,255),3)

cv2.imshow("",match)

cv2.waitKey()