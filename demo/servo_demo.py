import RPi.GPIO as GPIO
import time

#GPIOのモードをBMC
GPIO.setmode(GPIO.BCM)

#GPIO 17を出力
GPIO.setup(17,GPIO.OUT)

#17番ピンのサーボモータ設定
servo = GPIO.PWM(17, 50)

# 制御開始
# 2.5が0度、12が180度
servo.start(2.5)
time.sleep(0.5)

servo.ChangeDutyCycle(12)
time.sleep(0.5)

servo.ChangeDutyCycle(2.5)
time.sleep(0.5)

# 停止
servo.stop()
GPIO.cleanup()
