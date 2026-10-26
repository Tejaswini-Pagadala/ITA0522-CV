
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png")

if img is None:
    print("Image not found!")
else:
    height, width = img.shape[:2]

    x1, y1 = width // 4, height // 4
    x2, y2 = 3 * width // 4, 3 * height // 4

    roi = img[y1:y2, x1:x2].copy()
    result = img.copy()

    # Paste the copied region at the top-left corner
    h, w = roi.shape[:2]
    result[0:h, 0:w] = roi

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
    plt.title("Cropped ROI")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("ROI Pasted")
    plt.axis("off")

    plt.show()
