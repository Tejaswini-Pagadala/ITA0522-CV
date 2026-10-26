
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images (1).jpg", 0)
equalized = cv2.equalizeHist(img)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(equalized, cmap="gray")
plt.title("Equalized Image")
plt.axis("off")

plt.show()
