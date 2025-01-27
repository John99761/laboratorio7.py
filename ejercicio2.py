import cv2
import os


cascPath = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(cascPath)

cap = cv2.VideoCapture(0)

while True:
    
    _, img = cap.read()

    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    
    cv2.imshow("img", img)

    # Romper el bucle si se presiona la tecla 'Esc'
    k = cv2.waitKey(30)
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()

