#5. Drawing on Images OpenCV allows d
# 
# rawing shapes on images. 
# #1 Draw a line, rectangle, and circle. 
# #2 Add text 'Computer Vision'. 
import cv2

img = cv2.imread("image.jpg")


cv2.line(img, (50, 50), (300, 50), (255, 0, 0), 2)

cv2.rectangle(img, (50, 100), (300, 200), (0, 255, 0), 2)

cv2.circle(img, (200, 300), 50, (0, 0, 255), 2)

cv2.putText(img, "Computer Vision", (50, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 255, 255), 2)

cv2.imshow("Drawing", img)
cv2.waitKey(0)

# #3 Explain parameters for drawing functions. 
#cv2.line(image, start_point, end_point, color, thickness)start_point → (x1, y1)
#end_point → (x2, y2)
#color → (B, G, R)
#thickness → line width 
# #cv2.rectangle(image, top_left, bottom_right, color, thickness)
#top_left → starting corner
#bottom_right → ending corner
#🔹 Circle
#cv2.circle(image, center, radius, color, thickness)
#center → (x, y)
#radius → size of circle
#4 How is color represented in OpenCV?
#(B, G, R)
#Examples:
#(255, 0, 0) → Blue
#(0, 0, 255) → Red
#(255, 255, 255) → White
#(0, 0, 0) → Black