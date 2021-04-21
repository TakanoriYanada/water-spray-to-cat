import cv2
import time
import RPi.GPIO as GPIO

# OpenCV
cap = cv2.VideoCapture(0)
cat_cascade = cv2.CascadeClassifier('cat_cascade.xml')

# 水スプレー噴射 関数
def spray_water():
    # 関数内でsetupからcleanupまで対応している （stopやsleepで待機している際に、サーボモータが不安定に動くため）
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
    servo = GPIO.PWM(17, 50)
    servo.start(11)
    time.sleep(0.5)

    servo.ChangeDutyCycle(5)
    time.sleep(0.5)

    servo.ChangeDutyCycle(11)
    time.sleep(0.5)

    servo.stop()
    GPIO.cleanup()

cnt = 0
spray_trigger = 0
while True:
    # グレースケール
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 画像を回転（カメラの角度に合わせる）
    image = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)

    # 猫の認識
    objects = cat_cascade.detectMultiScale(image, 1.3, 3)

    # 猫を認識した場合
    if len(objects) > 0:
        # 猫に枠をつける
        for (x, y, w, h) in objects:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 猫の位置情報
        (x, y, w, h) = objects[0]

        # 画像サイズが大きい場合（カメラに近づいたということ）
        if w > 60 and h > 60:
            # 前回か噴射から10カウント以上経過している場合（連続噴射の制御）
            if cnt > spray_trigger + 10:
                # 水スプレー噴射
                spray_water()
                spray_trigger = cnt

    # 画像表示
    cv2.imshow('frame', image)

    # qキーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cnt += 1

cap.release()
cv2.destroyAllWindows()
