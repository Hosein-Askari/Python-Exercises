import cv2
import numpy as np


image1=cv2.imread("Assignment-29/image1.PNG")
image2=cv2.imread("Assignment-29/image2.PNG")

image1=cv2.resize(image1,(300,400))
image2=cv2.resize(image2,(300,400))
result_1=image1
result_5=image2
image1=image1.astype(np.float32)
image2=image2.astype(np.float32)
result_2=image1*3/4+image2*1/4
result_3=image1/2+image2/2
result_4=image1*1/4+image2*3/4
result_2=result_2.astype(np.uint8)
result_3=result_3.astype(np.uint8)
result_4=result_4.astype(np.uint8)

# concatenate image Horizontally 
result = np.concatenate((result_1, result_2,result_3,result_4,result_5), axis=1) 
cv2.imshow("",result)
cv2.imwrite("result.jpg",result)
cv2.waitKey()