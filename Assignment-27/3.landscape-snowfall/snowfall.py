import cv2
import glob
from PIL import Image



image_folder = "Assignment-27/3.landspace-snowfall/images/"
output_gif_path = "Assignment-27/3.landspace-snowfall/snow-fall.gif"
duration_per_frame = 200  # milliseconds






image_paths = glob.glob(f"{image_folder}*.jpg")

image_paths.sort()  
img=cv2.imread(image_paths[0])


frames=[]
break_flag = False
while(1):
    for image in image_paths:
            img = cv2.imread(image)
            img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
            cv2.imshow("",img)
            # img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            frame=Image.fromarray(img)            
            frames.append(frame)
            if cv2.waitKey(100) & 0xFF ==ord('q'):
                break_flag=True
                break
    if break_flag:
        break



frames[0].save(output_gif_path,
               save_all=True,
               append_images=frames[1:],
               duration=duration_per_frame,
               loop=0,
               optimize=True)