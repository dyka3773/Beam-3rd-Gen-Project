import logging
import u3
import time
import Jetson.GPIO as GPIO

from Enums.MotorSpeedsEnum import MotorPWMSpeeds
from Enums.PinsEnum import PinsEnum

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
)


def run_motor_cycle_labjack(run_for: float, device: u3.U3):
    """Runs the motor cycle.

    Args:
        starting_time (float): The time at which the program started.
        device (u3.U3): The device to run the motor cycle on (the sound card).
    """
    logging.info("Starting motor cycle")
    value = MotorPWMSpeeds.HALF_SPEED.value  # 50% duty cycle

    config = u3.Timer1Config  # Timer1Config is a class

    logging.info("Starting PWM at 50% duty cycle")
    device.getFeedback(config(TimerMode=1, Value=value))

    # Ramp up the motor speed slowly starting from 50% duty cycle so that we don't draw too much current
    for _ in range(4):
        time.sleep(0.5)
        value = int(value/4)
        device.getFeedback(config(TimerMode=1, Value=value))
        logging.info(
            f"Speed: {100 - int(value/MotorPWMSpeeds.STOP.value*100)} %")

    logging.info("Starting PWM at 100% duty cycle")
    device.getFeedback(config(TimerMode=1, Value=0))

    # 20 seconds of emulsification + 2 seconds of ramping up
    time.sleep(run_for - 2)

    logging.info("Stopping PWM")
    device.getFeedback(config(TimerMode=1, Value=MotorPWMSpeeds.STOP.value))


def run_motor_cycle(run_for: float):
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
