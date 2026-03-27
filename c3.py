#1 Convert a colored image to grayscale.
#import cv2

#img = cv2.imread("image.jpg")

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow("gray", gray)

#cv2.waitKey(0)
#2 Apply Binary Threshold and Adaptive Threshold.
import cv2

img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

adaptive = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11, 2)

cv2.imshow("gray", gray)
cv2.imshow("Binary Threshold", binary)
cv2.imshow("Adaptive Threshold", adaptive)

cv2.waitKey(0)
#3 Explain the difference between global and adaptive thresholding.
#Global Threshold
#Uses one fixed value (like 127)
#Applies the same threshold to entire image
#Simple and fast
#Works well when lighting is uniform
#🔹 Adaptive Threshold
#Uses different values for different regions
#Calculates threshold from neighbour pixels
#Slightly slower
#Works well when lighting is uneven / shadows present

#4 When should each be used?
#Use Global Threshold when:
#Image has uniform lighting
#Background is clear
#Example: simple scanned document
#🔹 Use Adaptive Threshold when:
#Image has shadows / uneven light
#Complex background
#Example: handwritten notes, outdoor images
