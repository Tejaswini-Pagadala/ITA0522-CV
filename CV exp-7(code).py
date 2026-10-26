import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image
img = cv2.imread(r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png")

if img is None:
    print("Image not found!")
else:
    # Step 2: Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 3: Create a kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Step 4: Apply erosion
    eroded_img = cv2.erode(gray_img, kernel, iterations=1)

    # Step 5: Display original and eroded images
    plt.subplot(1, 2, 1)
    plt.imshow(gray_img, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(eroded_img, cmap="gray")
    plt.title("Eroded Image")
    plt.axis("off")

    plt.show()
