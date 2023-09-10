import asyncio
import time
import logging

from DataStorage import DataStorage
from Enums.TimelineEnum import TimelineEnum
from Enums.MotorSpeedsEnum import MotorSpeedsEnum
from Motor import motor_util, motor_driver

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


async def run_motor_cycle(starting_time: float):
    """Runs the motor cycle according to the timeline.

    Args:
        starting_time (float): The time at which the program started.
    """
    logging.info("Starting motor cycle")
    logging.info('Motor speed is set to STOP')

    while (time.perf_counter() - starting_time < TimelineEnum.START_MOTOR.get_adapted_value):
        await DataStorage().save_motor_speed(MotorSpeedsEnum.STOP.value)
        logging.debug('Motor speed is set to STOP')
        await asyncio.sleep(0.3)

    # TODO: Uncomment the following line when the motor_driver#run function is implemented.
    # motor_driver.run(MotorSpeedsEnum.FULL_SPEED.value) # NOTE: This is set here like that assuming the PWM works like the Raspberry Pi PWM. @see the snippet from Rocket\archive\motor_control.py
    await DataStorage().save_motor_speed(MotorSpeedsEnum.FULL_SPEED.value)
    logging.info('Motor speed is set to FULL_SPEED')

    await asyncio.sleep(0.3)

    while (time.perf_counter() - starting_time < TimelineEnum.SOE_ON.get_adapted_value):
        await DataStorage().save_motor_speed(MotorSpeedsEnum.FULL_SPEED.value)
        logging.info('Motor speed is set to FULL_SPEED')
        await asyncio.sleep(0.3)

    # TODO: Uncomment the following line when the motor_util#stop_motor_at_the_edge_of_the_cell function is implemented.
    # motor_util.stop_motor_at_the_edge_of_the_cell()
    await DataStorage().save_motor_speed(MotorSpeedsEnum.STOP.value)
    logging.info('Motor speed is set to STOP')

    await asyncio.sleep(0.3)

    while (time.perf_counter() - starting_time < TimelineEnum.SODS_OFF.get_adapted_value):
        await DataStorage().save_motor_speed(MotorSpeedsEnum.STOP.value)
        logging.debug('Motor speed is set to STOP')
        await asyncio.sleep(0.3)


async def test_run_motor(speed: int = 0):
    """Runs the motor at the specified speed after making sure that everything is working as expected.
    In case no value is given, the motor perform one cycle and stop

    Args:
        speed (int): The speed at which the motor should run. Defaults to 0.
    """
    raise NotImplementedError('This function is not implemented yet.')
