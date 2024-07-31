
import cv2 
import numpy as np

def face(image):
		
		faces = face_cascade.detectMultiScale(image, 1.3, 4) 
		for (x,y,w,h) in faces: 
		
			crop_face=img[y-120:y+h+50,x-60:x+w+60]
			emoji=face_emoji
			emoji=cv2.resize(emoji,(w+120,h+170),interpolation=1)
			crop_face = np.where(emoji!=(225,101,179),emoji,crop_face)
			img[y-120:y+h+50,x-60:x+w+60]=crop_face
		
		return img

def eyes_lips(image):
		
		lips = lips_cascade.detectMultiScale(image, 1.01,190,minSize=[30,30],maxSize=[80,80]) 
		for (x,y,w,h) in lips: 
			crop_face=img[y-h:y+h+h,x-30:x+100]
			emoji=lips_emoji
			emoji=cv2.resize(emoji,(130,h*3),interpolation=1)
			crop_face = np.where(emoji!=(0,0,0),emoji,crop_face)
			img[y-h:y+h+h,x-30:x+100]=crop_face
			 


		eyes = righteye_cascade.detectMultiScale(image, 1.3,15,minSize=[30,30],maxSize=[80,80]) 
		for x,y,w,h in eyes: 
			crop_face=img[y-h:y+(2*h)+30,x-w+20:x+w+w+w]
			emoji=eyes_emoji
			emoji=cv2.resize(emoji,(w*4-20,3*h+30),interpolation=1)
			crop_face = np.where(emoji!=(0,0,0),emoji,crop_face)
			img[y-h:y+(2*h)+30,x-w+20:x+w+w+w]=crop_face
			
		return img

def blur_face(image):
		
		faces = face_cascade.detectMultiScale(image, 1.2, 4) 
		for (x,y,w,h) in faces: 
			crop_face=img[y:y+h,x:x+w]
			
			resize_face=cv2.resize(crop_face,(10,10))
			crop_face = cv2.resize(resize_face,(w,h),interpolation=cv2.INTER_NEAREST)
			img[y:y+h,x:x+w]=crop_face
		
		return img

def mirror_image(image):
		
		w=image.shape[1]//2
		flip_img = cv2.flip(image,1)
		flip_img = cv2.resize(flip_img,(image.shape[1]//2,image.shape[0]))
		image=cv2.resize(image,(image.shape[1]//2,image.shape[0]))
		img[:,:w] = image
		img[:,w:]=flip_img
		return img



face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt2.xml') 
righteye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_righteye_2splits.xml')
lefteye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_lefteye_2splits.xml')
lips_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')

cap = cv2.VideoCapture(1) 
face_emoji=cv2.imread("Assignment-28/3.face-detect/images/joker.png")
lips_emoji = cv2.imread("Assignment-28/3.face-detect/images/lips.png")
eyes_emoji=cv2.imread("Assignment-28/3.face-detect/images/eyes.png")
# mask= np.zeros_like(emoji)

# result = emoji*(mask//255)

flag=0
faces=[]
while 1: 


	ret, img = cap.read() 

 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
		
	k = cv2.waitKey(30) & 0xff
	if k == ord('1'): 

		flag=1

	elif k == ord('2'): 
		
		flag=2

	elif k == ord('3'): 
		
		flag=3

	elif k == ord('4'): 
		
		flag=4



	
	if flag==1:
		img=face(gray)

	if flag == 2:
		img=eyes_lips(gray)
	if flag == 3:
		img=blur_face(gray)
	if flag == 4:
		img=mirror_image(img)
	cv2.imshow("",img)
	if k==27:
		break
# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
