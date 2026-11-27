import cv2

img = cv2.imread(
    r"C:\Users\Hello\OneDrive\Gambar\Screenshots\images (1).png"
)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if img is None:
    print("Image not found!")
elif face_cascade.empty():
    print("Face detector not loaded!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    print("Total number of faces:", len(faces))

    cv2.imshow("Face Counting", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
