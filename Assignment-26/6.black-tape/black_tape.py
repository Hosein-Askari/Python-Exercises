import cv2




img=cv2.imread("Assignment-26/6.black-tape/image.jpg")
image = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
for i in range (70,0,-1):
    image[i:i+20,70-i]=0
for i in range (20,0,-1):
    image[0:i,90-i]=0
cv2.imshow("",image)
cv2.waitKey()