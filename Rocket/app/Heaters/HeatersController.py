import asyncio
import time
import logging

from Enums.TimelineEnum import TimelineEnum
from DataStorage import DataStorage
from ErrorHandling.CustomException import CustomException
from Enums.ErrorCodesEnum import ErrorCodesEnum
from Heaters import heater_driver
from utils.data_handling_utils import get_avg_temp

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s', 
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

TEMPERATURE_THRESHOLD = 10 # TODO: Speak with Science Team to determine the threshold for activating heaters.

async def run_heaters_cycle(starting_time: float):
    """Runs the heaters cycle according to the timeline and the regulations given by the Science Team.
    
    Args:
        starting_time (float): The time at which the program started.
    """
    consecutive_failures = 0
    
    try:
        while(time.perf_counter() - starting_time < TimelineEnum.SODS_OFF.value):
            current_temperature = await get_avg_temp()
            try:
                if current_temperature is None:
                    raise CustomException(
                        f'Could not get temperature data from the temperature sensor.', 
                        ErrorCodesEnum.TEMP_SENSOR_NULL_ERROR,
                        DataStorage()
                    )
            except CustomException as e:
                logging.error(e)
                
                if consecutive_failures >= 5: # In case of 5 consecutive failures to get temperature data, raise the exception higher.
                    raise e
                                
                consecutive_failures += 1
                await asyncio.sleep(0.3)
                continue
            
            consecutive_failures = 0
            
            current_heaters_state = await DataStorage().get_heater_status()
                                    
            if (current_temperature < TEMPERATURE_THRESHOLD):
                if not current_heaters_state:
                    # TODO: Uncomment the following line when the heater driver is implemented.
                    # heater_driver.activate_heaters()
                    pass
                
                await DataStorage().save_heater_status(True)
                logging.info(f'Heaters are ACTIVATED. Current temperature: {current_temperature} C.')
            else: # current_temperature >= TEMPERATURE_THRESHOLD
                if current_heaters_state:
                    # TODO: Uncomment the following line when the heater driver is implemented.
                    # heater_driver.deactivate_heaters()
                    pass
                
                await DataStorage().save_heater_status(False)
                logging.info(f'Heaters are DEACTIVATED. Current temperature: {current_temperature} C.')
    
            await asyncio.sleep(0.3)
            
    except CustomException as reraised_exception:
        logging.error('The sensors could not be read for 5 consecutive times (1 second). The program will stop the heaters cycle.')
        # TODO: Uncomment the following line when the heater driver is implemented.
        # heater_driver.deactivate_heaters()
        return
        

async def test_activate_heaters(duration: int = 0):
    """Activates heaters for a specified duration of time or indefinitely.
    
    Args:
        duration (int, optional): Duration of time to activate heaters for. To activate heaters indefinitely, set duration to 0. Defaults to 0.
    """
    raise NotImplementedError('This function has not been implemented yet.')