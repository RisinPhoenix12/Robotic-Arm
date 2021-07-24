import cv2

img = cv2.imread('')

#reduce noise
img1 = cv2.GaussianBlur(img,(5,5),0)

