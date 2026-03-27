# Edge detection is used to identify object boundaries. 
# #1 Apply Canny Edge Detection. 
import cv2

img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150)

cv2.imshow("Edges", edges)
cv2.waitKey(0)

# #2 Experiment with different threshold values. 
edges1 = cv2.Canny(gray, 30, 100)
edges2 = cv2.Canny(gray, 50, 150)
edges3 = cv2.Canny(gray, 100, 200)
# #3 Explain how threshold values affect edges. 
#Canny uses two thresholds:
#Lower threshold
#Upper threshold
 #Effect:
#Low thresholds (30, 100)
# Detects more edges
# Also detects noise (extra unwanted edges)
#Medium thresholds (50, 150)
# Balanced result
#High thresholds (100, 200)
# Detects only strong edges
# Misses weak edges
# #4 Why is edge detection important?