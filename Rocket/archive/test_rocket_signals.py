import Jetson.GPIO as GPIO
import time

LO_pin = 11
SOE_pin = 13
SODS_pin = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LO_pin, GPIO.IN)
GPIO.setup(SOE_pin, GPIO.IN)
GPIO.setup(SODS_pin, GPIO.IN)


def get_status_of_signal(signal):
    """Gets the status of the given signal.

    Args:
        signal (PinsEnum): The signal to get the status of.

    Returns:
        bool: The status of the given signal.
    """
    return GPIO.input(signal) == GPIO.HIGH


while True:
    print(get_status_of_signal(11))
    print(get_status_of_signal(13))
    print(get_status_of_signal(15))
    print()
    time.sleep(1)
