
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png")

if img is None:
    print("Image not found!")
else:
    height, width = img.shape[:2]

    bigger = cv2.resize(img, (width * 2, height * 2))
    smaller = cv2.resize(img, (width // 2, height // 2))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    bigger = cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB)
    smaller = cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(bigger)
    plt.title("Bigger Image (2x)")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(smaller)
    plt.title("Smaller Image (0.5x)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
