import RPi.GPIO as GPIO
import time

# Define the GPIO pin number
gpio_pin = 18

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin as an output
GPIO.setup(gpio_pin, GPIO.OUT)

# Define the frequency in Hz (e.g., 1 Hz)
frequency = 1

try:
    while True:
        # Toggle the GPIO pin high (3.3V)
        GPIO.output(gpio_pin, GPIO.HIGH)
        time.sleep(2.5 / frequency)
        print("GPIO.HIGH\n")

        # Toggle the GPIO pin low (0V)
        GPIO.output(gpio_pin, GPIO.LOW)
        time.sleep(2.5 / frequency)
        print("GPIO.LOW\n")

except KeyboardInterrupt:
    pass

# Cleanup and release resources
GPIO.cleanup()
print("cleanup")
