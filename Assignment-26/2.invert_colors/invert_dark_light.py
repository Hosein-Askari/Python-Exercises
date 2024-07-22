import cv2

cnt = 0
def invert_color(img):
    global cnt
    x,y=(img.shape)
    cv2.imshow(f"{cnt}",img)
    cnt += 1
    for i in range(0,x):
        for j in range(0,y):
            if img[i,j]>150:
                img[i,j]= 0
            
            elif img[i,j]<151:
                img[i,j]= 255
    cv2.imshow(f"{cnt}",img)
    cnt += 1

img_1=cv2.imread("Assignment-26/2.invert_colors/1.jpg")
img_2=cv2.imread("Assignment-26/2.invert_colors/2.jpg")
img_1=cv2.cvtColor(img_1,cv2.COLOR_RGB2GRAY)
img_2=cv2.cvtColor(img_2,cv2.COLOR_RGB2GRAY)



invert_color(img_1)
invert_color(img_2)

cv2.waitKey()