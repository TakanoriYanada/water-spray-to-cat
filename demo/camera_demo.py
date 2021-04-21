import cv2
import numpy as np

def camera():
    cap = cv2.VideoCapture(0)
    isOpened = cap.isOpened()

    if not isOpened:
        return

    while True:
        result, frame = cap.read()
        if not result:
            return

        # 画像表示
        cv2.imshow('camera', frame)

        # キー入力受付
        key = cv2.waitKey(1)

        # Enter / Escで終了
        if (key == 13) or (key == 27):
            break

    cap.release()
    cv2.destroyAllWindows()

camera()
