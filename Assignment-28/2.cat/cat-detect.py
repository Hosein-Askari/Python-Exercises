import cv2 


catface_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalcatface.xml') 



img = cv2.imread("Assignment-28/2.cat/image.jpg")


 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

 
faces = catface_cascade.detectMultiScale(gray,1.1,1) 

for (x,y,w,h) in faces: 

    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
    

cv2.imshow('img',img) 

cv2.waitKey()

