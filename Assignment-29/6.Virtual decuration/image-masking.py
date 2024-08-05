import cv2

img1=cv2.imread("Assignment-29/6.Virtual decuration/image1.jpg")
img2=cv2.imread("Assignment-29/6.Virtual decuration/image2.jpg")
img3=cv2.imread("Assignment-29/6.Virtual decuration/image3.jpg")


img1=cv2.resize(img1,(img2.shape[1],img2.shape[0]))

img=img3/255.0*img2

img3 = 255-img3

img += img3/255.0*img1

img=img.astype("uint8")


cv2.imshow("",img)

cv2.waitKey()