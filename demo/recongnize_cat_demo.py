import cv2
import time
import RPi.GPIO as GPIO

# OpenCV
cap = cv2.VideoCapture(0)
cat_cascade = cv2.CascadeClassifier('../cat_cascade.xml')

while True:
    # グレースケール
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # cascade
    objects = cat_cascade.detectMultiScale(gray, 1.3, 3)

    # draw
    for (x, y, w, h) in objects:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # show
    cv2.imshow('frame', gray)

    # q key end
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
