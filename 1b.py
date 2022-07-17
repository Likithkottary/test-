import cv2
import numpy as np
import matplotlib.pyplot as plt
path = r'C:\Users\DELL\Desktop\MCA\2nd SEM\Image Processing\lab assignmnt\madara.jpg'
img= cv2.imread(path,cv2.IMREAD_COLOR)
half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(img, (2000, 1610))
stretch_near = cv2.resize(img, (980, 1080),interpolation = cv2.INTER_NEAREST)
Titles =["Original ", "Half ", "Bigger ", "Interpolation Nearest "]
images =[img, half, bigger, stretch_near]
count = 4
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9, top=0.9, wspace=0.4, hspace=0.4)
for i in range(count):
 plt.subplot(2, 2, i + 1)
 plt.title(Titles[i])
 plt.imshow(images[i])
 plt.show()
