import cv2

img=cv2.imread("Assignment-29/3.Photo to Sketch/car.jpg",0)

inv_img=255-img
blur=cv2.GaussianBlur(inv_img,(41,41),0)
inv_blur=255-blur

sketch= cv2.divide(img,inv_blur,scale=255.0)


cv2.imshow("",sketch)
cv2.imwrite("Assignment-29/3.Photo to Sketch/sketch.jpg",sketch)
cv2.waitKey()
