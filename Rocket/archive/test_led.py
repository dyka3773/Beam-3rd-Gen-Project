import Jetson.GPIO as GPIO
import time

LED_pin = 31

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED_pin, GPIO.OUT)

try:
    while True:
        print(f"Turning LED on")
        GPIO.output(LED_pin, GPIO.HIGH)
        time.sleep(15)
        print(f"Turning LED off")
        GPIO.output(LED_pin, GPIO.LOW)
        print()
        time.sleep(15)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    GPIO.cleanup()
