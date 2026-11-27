import cv2

img = cv2.imread(
    r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png"
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    smiles = smile_cascade.detectMultiScale(
        gray, scaleFactor=1.7, minNeighbors=20
    )

    for (x, y, w, h) in smiles:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

    print("Number of smiles detected:", len(smiles))

    cv2.imshow("Smile Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
