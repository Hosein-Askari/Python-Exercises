import os
import imageio

file_list = sorted(os.listdir("Assignment-8/1-gif/rain/"))
IMAGES=[]
for file_name in file_list:
    file_path = "Assignment-8/1-gif/rain/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)
imageio.mimsave("Assignment-8/1-gif/output.gif",IMAGES)