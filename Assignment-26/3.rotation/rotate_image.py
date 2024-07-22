import cv2




img=cv2.imread("Assignment-26/3.rotation/3.jpg")
image = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("",image)
cv2.waitKey()