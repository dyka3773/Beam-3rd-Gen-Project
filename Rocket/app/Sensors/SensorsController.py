import asyncio
import time
import logging

from Enums.TimelineEnum import TimelineEnum
from DataStorage import DataStorage
from Sensors import temp_press_sensor_driver

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


async def run_sensors_cycle(starting_time: float):
    """Runs the sensors cycle according to the timeline.

    Args:
        starting_time (float): The time at which the program started.
    """
    logging.info('Starting the sensors cycle.')
    while (time.perf_counter() - starting_time < TimelineEnum.SODS_OFF.get_adapted_value):
        temp_1 = temp_press_sensor_driver.read_temp(1)
        temp_2 = temp_press_sensor_driver.read_temp(2)

        press_1 = temp_press_sensor_driver.read_pressure(1)
        press_2 = temp_press_sensor_driver.read_pressure(2)

        await DataStorage().save_sensor_data(temp_1, temp_2, press_1, press_2)
        logging.debug(
            f'Temperature 1: {temp_1} - Temperature 2: {temp_2} - Pressure 1: {press_1} - Pressure 2: {press_2}')

        await asyncio.sleep(0.3)

    logging.info('Finished the sensors cycle.')
