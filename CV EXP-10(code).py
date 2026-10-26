
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png")

if img is None:
    print("Image not found!")
else:
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
    plt.title("90 Degree Clockwise Rotation")
    plt.axis("off")

    plt.show()
