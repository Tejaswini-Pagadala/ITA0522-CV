
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png")

if img is None:
    print("Image not found!")
else:
    # Display the input image
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Input Image for Watch Recognition")
    plt.axis("off")
    plt.show()

    print("Image loaded successfully.")
    print("A watch-specific trained model is needed to detect a watch.")
