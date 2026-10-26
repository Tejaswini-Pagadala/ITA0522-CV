
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png")

if img is None:
    print("Image not found!")
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilated_img = cv2.dilate(gray_img, kernel, iterations=1)

    plt.subplot(1, 2, 1)
    plt.imshow(gray_img, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(dilated_img, cmap="gray")
    plt.title("Dilated Image")
    plt.axis("off")

    plt.show()
