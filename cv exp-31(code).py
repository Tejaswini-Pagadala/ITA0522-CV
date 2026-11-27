import cv2
import matplotlib.pyplot as plt

img = cv2.imread(
    r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png"
)

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    threshold_value = int(input("Enter threshold value (0-255): "))

    ret, result = cv2.threshold(
        gray, threshold_value, 255, cv2.THRESH_BINARY
    )

    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Image")

    plt.subplot(1, 2, 2)
    plt.imshow(result, cmap="gray")
    plt.title("Segmented Image")

    plt.show()
