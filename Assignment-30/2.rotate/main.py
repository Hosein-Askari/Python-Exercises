import cv2
import numpy as np
from TFLightFaceDetector import UltraLightFaceDetecion
from TFLightFaceAlignment import CoordinateAlignmentModel



def get_landmarks(frame,face_organ):

    land_mark=[]
    boxes, scores = fd.inference(frame)

    for pred in fa.get_landmarks(frame, boxes):
        if face_organ=="lips":
            for i in [52,55,56,53,59,58,61,68,67,71,63,64]:
                land_mark.append(pred[i])
        elif face_organ=="left_eye":
            for i in [35,41,40,42,39,37,33,36]:
                land_mark.append(pred[i])
        elif face_organ=="right_eye":
            for i in [89,90,87,91,93,96,94,95]:
                land_mark.append(pred[i])

    return land_mark


def make_filter_from_face(land_mark,main_img):


    land_mark=np.array(land_mark,dtype=int)

    x,y,w,h=cv2.boundingRect(land_mark)

    mask=np.ones_like(main_img,np.uint8)*255
    cv2.drawContours(mask,[land_mark],-1,([0,0,0]),-1)
    mask=np.where(mask==([0,0,0]),main_img,mask)

    crop=mask[y:y+h,x:x+w]
    crop=cv2.resize(crop,(0,0),fx=1,fy=1.3)
    crop = cv2.rotate(crop,cv2.ROTATE_180)
    mask[y-h//4:y-h//4+crop.shape[0],x:x+w]=crop
    
  
    return mask


def put_filter_on_face(foreground,background):
    

    foreground_new = np.zeros(background.shape, dtype=np.uint8)

    foreground_new[0:foreground.shape[0], 0:foreground.shape[1]] = foreground

    
    lip_gray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
    _, lip_binary = cv2.threshold(lip_gray,254,255,cv2.THRESH_BINARY)
    lip_binary = 255 - lip_binary

    lip_binary_blur = cv2.GaussianBlur(lip_binary,(21,21),0)
    
    lip_binary_blur = cv2.blur(lip_binary,(21,21))
    
    lip_binary_blur = cv2.multiply(cv2.subtract(lip_binary_blur, 120), 2)
    
    lip_binary_blur = cv2.cvtColor(lip_binary_blur, cv2.COLOR_GRAY2RGB)

    alpha_new = np.zeros(background.shape, dtype=np.uint8)

    alpha_new[0:lip_binary_blur.shape[0], 0:lip_binary_blur.shape[1]] = lip_binary_blur

    
    alpha = alpha_new.astype(float)/255
    alpha = alpha / 255.0

    
    
    foreground = foreground_new.astype(float)
    background = background.astype(float)
    
    alpha = alpha_new.astype(float)/255

    
    foreground = cv2.multiply(alpha, foreground)
    
    background = cv2.multiply(1.0 - alpha, background)
    
    outImage = cv2.add(foreground, background)
    
    return outImage

fd = UltraLightFaceDetecion("Assignment-30/2.rotate/weights/RFB-320.tflite",conf_threshold=0.88)

fa = CoordinateAlignmentModel("Assignment-30/2.rotate/weights/coor_2d106.tflite")

img=cv2.imread("Assignment-30/2.rotate/image.jpg")

mouth_land_mark=get_landmarks(img,"lips")
filter=make_filter_from_face(mouth_land_mark,img)
result=put_filter_on_face(filter,img)

mouth_land_mark=get_landmarks(img,"right_eye")
filter=make_filter_from_face(mouth_land_mark,img)
result=put_filter_on_face(filter,result)

mouth_land_mark=get_landmarks(img,"left_eye")
filter=make_filter_from_face(mouth_land_mark,img)
result=put_filter_on_face(filter,result)

cv2.imshow("result",result/255)
cv2.waitKey(0) 
result=cv2.rotate(result,cv2.ROTATE_180)
cv2.imshow("result",result/255)
cv2.waitKey(0)  