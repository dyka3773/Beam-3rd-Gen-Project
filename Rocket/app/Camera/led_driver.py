import Jetson.GPIO as GPIO
import logging

from Enums.PinsEnum import PinsEnum

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


def turn_on_led() -> None:
    try:
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(PinsEnum.LED_CONTROL.value, GPIO.OUT)

        GPIO.output(PinsEnum.LED_CONTROL.value, GPIO.HIGH)
    except Exception as e:
        logging.error("An Error has occured in the LED Driver")
        logging.error(e)
