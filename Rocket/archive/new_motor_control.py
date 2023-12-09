import time
import Jetson.GPIO as GPIO

MOTOR_IN1 = 33
MOTOR_IN2 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_IN1, GPIO.OUT)
GPIO.setup(MOTOR_IN2, GPIO.OUT)

try:
    print("DRV8871 test")

    while True:
        # ramp up forward
        GPIO.output(MOTOR_IN1, GPIO.LOW)
        for i in range(256):
            GPIO.output(MOTOR_IN2, GPIO.HIGH)
            time.sleep(0.01 * i / 255)

        # forward full speed for one second
        time.sleep(1)

        # ramp down forward
        for i in range(255, -1, -1):
            GPIO.output(MOTOR_IN2, GPIO.HIGH)
            time.sleep(0.01 * i / 255)

        # ramp up backward
        GPIO.output(MOTOR_IN2, GPIO.LOW)
        for i in range(256):
            GPIO.output(MOTOR_IN1, GPIO.HIGH)
            time.sleep(0.01 * i / 255)

        # backward full speed for one second
        time.sleep(1)

        # ramp down backward
        for i in range(255, -1, -1):
            GPIO.output(MOTOR_IN1, GPIO.HIGH)
            time.sleep(0.01 * i / 255)

except KeyboardInterrupt:
    GPIO.cleanup()

