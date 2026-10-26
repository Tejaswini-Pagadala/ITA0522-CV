
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png")

if img is None:
    print("Image not found!")
else:
    watermarked = img.copy()

    cv2.putText(watermarked, "WATERMARK",
                (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(watermarked, cv2.COLOR_BGR2RGB))
    plt.title("Watermarked Image")
    plt.axis("off")

    plt.show()
