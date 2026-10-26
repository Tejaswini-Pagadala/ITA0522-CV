
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png")

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    abs_x = cv2.convertScaleAbs(sobel_x)
    abs_y = cv2.convertScaleAbs(sobel_y)

    sobel = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

    plt.subplot(1, 3, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Grayscale")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(abs_x, cmap="gray")
    plt.title("Sobel X")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(sobel, cmap="gray")
    plt.title("Sobel Filter")
    plt.axis("off")

    plt.show()
