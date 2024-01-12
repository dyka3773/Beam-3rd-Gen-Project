import Jetson.GPIO as GPIO
import time

jetson_p_pin = (22, 24)
motor_health_pin = (38, 40)
led_health_pin = (16, 18)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(jetson_p_pin, GPIO.IN)
GPIO.setup(motor_health_pin, GPIO.IN)
GPIO.setup(led_health_pin, GPIO.IN)


def get_status_of_signal(signal):
    """Gets the status of the given signal.

    Args:
        signal (PinsEnum): The signal to get the status of.

    Returns:
        bool: The status of the given signal.
    """
    return GPIO.input(signal) == GPIO.HIGH


while True:
    print(f"Jetson: {[get_status_of_signal(pin) for pin in jetson_p_pin]}")
    print(f"Motor: {[get_status_of_signal(pin) for pin in motor_health_pin]}")
    print(f"LED: {[get_status_of_signal(pin) for pin in led_health_pin]}")
    print()
    time.sleep(1)
