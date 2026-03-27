#1 Resize the image to 800 × 600.


#import cv2

#img = cv2.imread("image.jpg")

#resized = cv2.resize(img, (800, 600))

#cv2.imshow("Resized", resized)
#cv2.waitKey(0)

#2 Crop the region from coordinates (100, 100) to (400, 400).
 #cropped = img[100:400, 100:400]
#cv2.imshow("Cropped", cropped)
#cv2.waitKey(0)

#3 Write a Python program to perform both resizing and cropping.
import cv2

img = cv2.imread("image.jpg")

resized = cv2.resize(img, (800, 600))

cropped = resized[100:400, 100:400]

cv2.imshow("image", cropped)
cv2.waitKey(0)

#4 Explain how slicing works in cropping.
 #Cutting a small part of the image using row and column positions