import cv2

img=cv2.imread("Assignment-27/1.batman-logo/image_1.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,img=cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
cv2.namedWindow("batman", cv2.WINDOW_NORMAL)
cv2.resizeWindow("batman", 920, 634) 
cv2.putText(img,"BATMAN",(150,400),cv2.FONT_HERSHEY_SIMPLEX,2,255,5)
cv2.imshow("batman",img)

cv2.waitKey()