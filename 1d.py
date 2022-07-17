import cv2
import numpy as np

path = r'C:\Users\DELL\Desktop\MCA\2nd SEM\Image Processing\lab assignmnt\madara.jpg'
img = cv2.imread(path,cv2.IMREAD_COLOR) 
height, width = img.shape[:2]
quarter_height, quarter_width = height / 4, width / 4
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]]) 
img_translation = cv2.warpAffine(img, T, (width, height)) 
cv2.imshow("Originalimage", img) 
cv2.imshow('Translation', img_translation)
cv2.waitKey() 
cv2.destroyAllWindows()
