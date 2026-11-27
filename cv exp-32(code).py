import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

img = np.ones((height, width, 3), dtype=np.uint8) * 255

box_w = width // 10
box_h = height // 10

# Black box - Top left
img[0:box_h, 0:box_w] = (0, 0, 0)

# Blue box - Top right
img[0:box_h, width-box_w:width] = (255, 0, 0)

# Green box - Bottom left
img[height-box_h:height, 0:box_w] = (0, 255, 0)

# Red box - Bottom right
img[height-box_h:height, width-box_w:width] = (0, 0, 255)

cv2.imshow("Four Colored Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
