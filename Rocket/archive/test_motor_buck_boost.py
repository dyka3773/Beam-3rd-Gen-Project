import Jetson.GPIO as GPIO
import time

motor_pin = 32

GPIO.setmode(GPIO.BOARD)

GPIO.setup(motor_pin, GPIO.OUT)

try:
    while True:
        print(f"Turning Motor on")
        GPIO.output(motor_pin, GPIO.HIGH)
        time.sleep(15)
        print(f"Turning Motor off")
        GPIO.output(motor_pin, GPIO.LOW)
        print()
        time.sleep(15)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    GPIO.cleanup()
