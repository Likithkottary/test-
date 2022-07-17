import cv2 
import imutils

path = r'C:\Users\DELL\Desktop\MCA\2nd SEM\Image Processing\lab assignmnt\madara.jpg'

image = cv2.imread(path,cv2.IMREAD_COLOR) 
Rotated_img=imutils.rotate(image,angle=60) 
cv2.imshow("Rotated image",Rotated_img) 
cv2.waitKey()
cv2.destroyAllWindows()
