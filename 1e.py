import cv2

path = r'C:\Users\DELL\Desktop\MCA\2nd SEM\Image Processing\lab assignmnt\madara.jpg'
img = cv2.imread(path,cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
cv2.imshow('Canny Edge Detection', edges) 
cv2.waitKey(0)
cv2.destroyAllWindows()
