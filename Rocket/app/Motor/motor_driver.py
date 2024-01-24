import logging
import time
import Jetson.GPIO as GPIO

from Enums.PinsEnum import PinsEnum

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


def run_motor(run_for: float):
    """Runs the motor cycle.

    Args:
        run_for (float): The time to run the motor for.
    """
    logging.info("Starting motor cycle")

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(PinsEnum.MOTOR_CONTROL.value, GPIO.OUT)

    time_passed = 0

    while time_passed < run_for:
        turn_on_motor()
        time.sleep(0.5)
        if time_passed + 0.5 > run_for:
            turn_off_motor()
            break
        time_passed += 0.5

    turn_off_motor()


def turn_on_motor() -> None:
    try:
        GPIO.output(PinsEnum.MOTOR_CONTROL.value, GPIO.HIGH)
    except Exception as e:
        logging.error("An Error has occured in the LED Driver")
        logging.error(e)
        raise e


def turn_off_motor() -> None:
    try:
        GPIO.output(PinsEnum.MOTOR_CONTROL.value, GPIO.LOW)
    except Exception as e:
        logging.error("An Error has occured in the LED Driver")
        logging.error(e)
        raise e
