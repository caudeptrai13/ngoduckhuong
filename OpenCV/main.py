import cv2
import numpy as np
img = cv2.imread('image.PNG')
img = img.transpose(2,0,1)
blue = img[0]
green = img[1]
red = img[2]
gray = 0.299*red + 0.587*green + 0.114*blue
cv2.imshow("gray",gray/255)
threshold = gray
threshold = np.where(threshold > 110,255, 0)
print(threshold)
cv2.imshow("threshold",threshold/255)
cv2.waitKey(10000)