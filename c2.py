#1 Apply Average Blur, Gaussian Blur, and Median Blur.
import cv2

img = cv2.imread("image.jpg")

avg = cv2.blur(img, (5,5))
gaussian = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)

cv2.imshow("Average", avg)
cv2.imshow("Gaussian", gaussian)
cv2.imshow("Median", median)

cv2.waitKey(0)
#2 Compare their outputs.
#average and quassian blue have small blur.median blur have more changes than that.

#3 Which blur is best for salt-and-pepper noise?
#median
#4 What is the role of kernel size?
#Role of Kernel Size
#Kernel = filter size (e.g., 3×3, 5×5)
#Larger kernel → more blur
#Smaller kernel → less blur