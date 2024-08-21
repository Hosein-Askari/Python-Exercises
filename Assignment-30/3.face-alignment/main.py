import cv2
import numpy as np
from PIL import Image
import math
from TFLightFaceDetector import UltraLightFaceDetecion
from TFLightFaceAlignment import CoordinateAlignmentModel


def get_landmarks(img):

    
    boxes, scores = fd.inference(img)

    for pred in fa.get_landmarks(img, boxes):
       
        
        left_eye=pred[88]
        right_eye=pred[38]

    return left_eye,right_eye


def find_rotation_angel(left_eye,right_eye,img,final_angle):
    x=left_eye[0]-right_eye[0]
    y=left_eye[1]-right_eye[1]
    
    angel=(math.degrees(math.atan2(y,x)))
    final_angle += angel
    pil_image = Image.fromarray(img) 
    pil_image=pil_image.rotate(angel,Image.NEAREST,expand=1) 
    image=np.array(pil_image)
    
    if check(image):
        return final_angle
    else:
        left_eye,right_eye=get_landmarks(image)
        return find_rotation_angel(left_eye,right_eye,image,final_angle)


def check(img):

    left_eye,right_eye=get_landmarks(img)
    if -0.1<left_eye[1]-right_eye[1] < 0.1:
        return True
    else:
        return False


def rotate_img(img,angel):
    pil_image = Image.fromarray(img) 
    pil_image=pil_image.rotate(angel,Image.BICUBIC,expand=1) 
    result=np.array(pil_image)

    return result



fd = UltraLightFaceDetecion("Assignment-30/3.face-alignment/weights/RFB-320.tflite",conf_threshold=0.88)

fa = CoordinateAlignmentModel("Assignment-30/3.face-alignment/weights/coor_2d106.tflite")

img=cv2.imread("Assignment-30/3.face-alignment/image.png")

cv2.imshow("",img)
cv2.waitKey(0)

left_eye,right_eye=get_landmarks(img)
angel=find_rotation_angel(left_eye,right_eye,img,0)
result=rotate_img(img,angel)


cv2.imwrite("Assignment-30/3.face-alignment/result.jpg",result)
cv2.imshow("",result)
cv2.waitKey(0)

