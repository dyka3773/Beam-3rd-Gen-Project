import asyncio
import time
import logging

from Enums.TimelineEnum import TimelineEnum
from DataStorage import DataStorage
from ErrorHandling.CustomException import CustomException
from Enums.ErrorCodesEnum import ErrorCodesEnum
from Heaters import heater_driver
from utils.data_handling_utils import get_avg_temp_of_sensors

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

CELL_UPPER_TEMPERATURE_THRESHOLD = 18
CELL_LOWER_TEMPERATURE_THRESHOLD = 15
ELECTRONICS_UPPER_TEMPERATURE_THRESHOLD = 10
ELECTRONICS_LOWER_TEMPERATURE_THRESHOLD = 5


async def run_heaters_cycle(starting_time: float):
    """Runs the heaters cycle according to the timeline and the regulations given by the Science Team.

    Args:
        starting_time (float): The time at which the program started.
    """
    logging.info("Starting heaters cycle")

    consecutive_failures = 0

    try:
        while (time.perf_counter() - starting_time < TimelineEnum.SODS_OFF.get_adapted_value):
            current_temperature = await get_avg_temp_of_sensors()
            try:
                if current_temperature is None:
                    raise CustomException(
                        f'Could not get temperature data from the temperature sensor.',
                        ErrorCodesEnum.TEMP_SENSOR_NULL_ERROR,
                        DataStorage()
                    )
            except CustomException as e:
                logging.error(e)

                # In case of 5 consecutive failures to get temperature data, raise the exception higher.
                if consecutive_failures >= 5:
                    raise e

                consecutive_failures += 1
                await asyncio.sleep(0.3)
                continue

            current_cell_temp, current_electronics_temp = current_temperature

            consecutive_failures = 0

            current_cell_heaters_state = await DataStorage().get_cell_heater_status()
            current_electronics_heaters_state = await DataStorage().get_electronics_heater_status()

            # The logic for the cell heaters is as follows:
            # If the temperature is above the upper threshold and the heaters are on, turn them off.
            # If the temperature is below the lower threshold and the heaters are off, turn them on.
            # If the temperature is between the thresholds, keep the heaters in their current state.
            if current_cell_temp > CELL_UPPER_TEMPERATURE_THRESHOLD and current_cell_heaters_state:
                # TODO: Uncomment the following line when the heater drivers are implemented.
                # heater_driver.deactivate_cell_heaters()
                await DataStorage().add_cell_heater_status(False)
                logging.info(
                    f'Cell Heaters are purposely DEACTIVATED. Current temperature: {current_cell_temp} C.')
            elif current_cell_temp < CELL_LOWER_TEMPERATURE_THRESHOLD and not current_cell_heaters_state:
                # TODO: Uncomment the following line when the heater drivers are implemented.
                # heater_driver.activate_cell_heaters()
                await DataStorage().add_cell_heater_status(True)
                logging.info(
                    f'Cell Heaters are purposely ACTIVATED. Current temperature: {current_cell_temp} C.')
            else:
                logging.debug(
                    f"Cell Heaters' status is unchanged. Current temperature: {current_cell_temp} C.")

            # The logic for the electronics heaters is the same as the one for the cell heaters.
            if current_electronics_temp > ELECTRONICS_UPPER_TEMPERATURE_THRESHOLD and current_electronics_heaters_state:
                # TODO: Uncomment the following line when the heater drivers are implemented.
                # heater_driver.deactivate_electronics_heaters()
                await DataStorage().add_electronics_heater_status(False)
                logging.info(
                    f'Electronics Heaters are purposely DEACTIVATED. Current temperature: {current_electronics_temp} C.')
            elif current_electronics_temp < ELECTRONICS_LOWER_TEMPERATURE_THRESHOLD and not current_electronics_heaters_state:
                # TODO: Uncomment the following line when the heater drivers are implemented.
                # heater_driver.activate_electronics_heaters()
                await DataStorage().add_electronics_heater_status(True)
                logging.info(
                    f'Electronics Heaters are purposely ACTIVATED. Current temperature: {current_electronics_temp} C.')
            else:
                logging.debug(
                    f"Electronics Heaters' status is unchanged. Current temperature: {current_electronics_temp} C.")

            # In case the heaters are not initialized, initialize them to False.
            if current_cell_heaters_state is None and current_electronics_heaters_state is None:
                await DataStorage().add_electronics_heater_status(False)
                await DataStorage().add_cell_heater_status(False)

            await asyncio.sleep(0.3)

    except CustomException:
        logging.error(
            'The sensors could not be read for 5 consecutive times (1 second). The program will stop the heaters cycle.')
        # TODO: Uncomment the following line when the heater driver is implemented.
        # heater_driver.deactivate_all_heaters()
        return

    logging.info("Finished heaters cycle")


async def test_activate_heaters(duration: int = 0):
    """Activates heaters for a specified duration of time or indefinitely.

    Args:
        duration (int, optional): Duration of time to activate heaters for. To activate heaters indefinitely, set duration to 0. Defaults to 0.
    """
    raise NotImplementedError('This function has not been implemented yet.')
