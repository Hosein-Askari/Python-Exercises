import cv2

img1=cv2.imread("Assignment-29/4.Find-secret-text/image_1.png")
img2=cv2.imread("Assignment-29/4.Find-secret-text/image_2.png")

img=img2-img1

cv2.imshow("",img)
cv2.waitKey()