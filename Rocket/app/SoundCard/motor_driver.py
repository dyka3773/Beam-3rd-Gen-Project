import logging
import u3
import time

from Enums.MotorSpeedsEnum import MotorPWMSpeeds

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


def run_motor_cycle(run_for: float, device: u3.U3):
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


def get_position() -> int:
    """Returns the position of the piston.

    Returns:
        int: The position of the piston in mm.
    """
    raise NotImplementedError('This function is not implemented yet.')


def stop_motor_at_the_edge_of_the_cell():
    """Stops the motor at the edge of the cell."""
    raise NotImplementedError('This function is not implemented yet.')
