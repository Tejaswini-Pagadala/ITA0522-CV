import cv2
import numpy as np

img = cv2.imread(
    r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png"
)

if img is None:
    print("Image not found!")
else:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 0, 0])
    upper = np.array([180, 255, 100])

    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    cv2.imshow("Original Image", img)
    cv2.imshow("Foreground Subtracted", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
