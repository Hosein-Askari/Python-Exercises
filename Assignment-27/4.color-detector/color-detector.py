
# import the opencv library 
import cv2 
import numpy as np
  
# define a video capture object 
vid = cv2.VideoCapture(0) 

mask=np.zeros((480, 640), dtype=np.uint8)
 

while(True): 
    
   
    ret, frame = vid.read() 
   
    ksize = (35, 35) 
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred_frame= cv2.blur(frame, ksize) 
    mask=cv2.rectangle(mask,(280,190),(380,290),255,-1)
    cv2.rectangle(frame,(280,190),(380,290),0,5) 
    
    result_frame=np.where(mask!=255,blurred_frame,frame)
    
    a=np.sum(result_frame[194:286,284:376])
    a=a.astype(np.int32)
    
    if(a//10000<=90):
        cv2.putText(result_frame,"black",(150,400),cv2.FONT_HERSHEY_SIMPLEX,2,255,5)
    
    elif (90<a//10000<150):
        cv2.putText(result_frame,"gray",(150,400),cv2.FONT_HERSHEY_SIMPLEX,2,255,5)

    else :
        cv2.putText(result_frame,"white",(150,400),cv2.FONT_HERSHEY_SIMPLEX,2,255,5)

    cv2.imshow('frame', result_frame) 

    

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
vid.release() 

cv2.destroyAllWindows() 




 