import cv2

img = cv2.imread(
    r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png"
)

if img is None:
    print("Image not found!")
else:
    text = input("Enter text to display: ")

    cv2.putText(
        img, text, (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 0, 255), 2
    )

    cv2.imshow("Text on Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
