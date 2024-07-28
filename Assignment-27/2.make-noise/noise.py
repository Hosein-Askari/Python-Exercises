import cv2
import numpy as np
from PIL import Image


frames=[]

while (1):
    img=cv2.imread("Assignment-27/2.make-noise/tv.png")
    img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # img=cv2.rectangle(img,(40,40),(70,70),100,-1)
    img1=np.random.random((186,220))*255
    img1=np.array(img1,np.uint8)
    img[154:340,105:325]=img1
    frame=Image.fromarray(img)
    frames.append(frame)
    cv2.imshow("noise", img)
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break


frames[0].save("Assignment-27/2.make-noise/noise.gif",
               save_all=True,
               append_images=frames[1:],
               duration=100,
               loop=0,
               optimize=True)