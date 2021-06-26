import cv2
import numpy as np
img = cv2.imread('bienso1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 200, 255)
(_,contours,_) = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
bienso = contours[0]
(x,y,w,h) = cv2.boundingRect(bienso)
max = w * h
for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)
    if (w * h > max):   # Tim contour lon nhat
        max = w * h
        bienso = contour
(x,y,w,h) = cv2.boundingRect(bienso)
img_bienso = img[y:y + h, x:x + w] # Cat bien so
height,width = h,w
img_gray = cv2.cvtColor(img_bienso, cv2.COLOR_BGR2GRAY)
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#canny_cut = cv2.Canny(img_gray,240,255)
_, threshhold_img = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)
(_,contours,_) = cv2.findContours(threshhold_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
number = []
for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)
    if (h >= w and h * 3 >= height and h * 2 <= height):
        number.append(np.copy(img_bienso[y:y + h, x:x + w]))
        cv2.rectangle(img_bienso, (x, y), (x + w, y + h), (0, 255, 0), 2)
#cv2.imshow("imggray",canny_cut)
#cv2.waitKey(300000)
for num in number:
    cv2.imshow("a",num)
    cv2.waitKey(2000)
