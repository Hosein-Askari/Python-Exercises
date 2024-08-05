import os
import cv2
import numpy as np


    
path = os.listdir(f"Assignment-29/2.Black hole/images/1")

image1=[cv2.imread(f"Assignment-29/2.Black hole/images/1/"+image) for image in path]
image2=[cv2.imread(f"Assignment-29/2.Black hole/images/2/"+image) for image in path]        
image3=[cv2.imread(f"Assignment-29/2.Black hole/images/3/"+image) for image in path]
image4=[cv2.imread(f"Assignment-29/2.Black hole/images/4/"+image) for image in path]

result1 = np.concatenate((image1[0], image2[0]), axis=1) 
result2 = np.concatenate((image3[0], image4[0]), axis=1) 
result=   np.concatenate((result1, result2), axis=0) 
result=cv2.resize(result,(1000,720))
cv2.imshow("",result)
cv2.waitKey()

image1=[image.astype(np.float16) for image in image1]
image2=[image.astype(np.float16) for image in image2]      
image3=[image.astype(np.float16) for image in image3]
image4=[image.astype(np.float16) for image in image4]


image11 = (image1[0]+image1[1]+image1[2]+image1[3]+image1[4])/5
image11=image11.astype(np.uint8)
image22 =( image2[0]+image2[1]+image2[2]+image2[3]+image2[4])/5
image22=image22.astype(np.uint8)
image33 = (image3[0]+image3[1]+image3[2]+image3[3]+image3[4])/5
image33=image33.astype(np.uint8)
image44 = (image4[0]+image4[1]+image4[2]+image4[3]+image4[4])/5
image44=image44.astype(np.uint8)


result1 = np.concatenate((image11, image22), axis=1) 
result2 = np.concatenate((image33, image44), axis=1) 
result=   np.concatenate((result1, result2), axis=0) 
result=cv2.resize(result,(1000,720))
cv2.imshow("",result)
cv2.waitKey()
