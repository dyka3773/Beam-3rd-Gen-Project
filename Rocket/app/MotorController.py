import asyncio
import time
import logging
from enum import Enum

from DataStorage import DataStorage
from Timeline import Timeline
from Motor import motor_util
from ErrorHandling.CustomException import CustomException

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s', 
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

class MotorSpeeds(Enum):
    """An enum to store the motor_util speeds."""
    
    STOP = 0
    FULL_SPEED = 255

async def run_motor_cycle(starting_time: float):
    """Runs the motor cycle according to the timeline.

    Args:
        starting_time (float): The time at which the program started.
    """
    DataStorage().save_motor_speed(MotorSpeeds.STOP.value)
    logging.info('Motor speed set to STOP')
    await asyncio.sleep(Timeline.START_MOTOR.value)
    
    # BUG: The code after the above line is almost fully blocking so asyncio is not really useful here. 
    #      It should be changed to the threading module.
    
    interval_check = time.perf_counter()
    
    while (time.perf_counter() - starting_time < Timeline.SOE_ON.value):
        try:
            await motor_util.run_motor(MotorSpeeds.FULL_SPEED.value)
                
            if (time.perf_counter() - interval_check) > 0.3:
                DataStorage().save_motor_speed(MotorSpeeds.FULL_SPEED.value)
                logging.info('Motor speed is set to FULL_SPEED')
                interval_check = time.perf_counter()
        except CustomException as e: # In case of an error, stop the motor, log the error and return
            logging.error(e)
            await motor_util.run_motor(MotorSpeeds.STOP.value)
            DataStorage().save_motor_speed(MotorSpeeds.STOP.value)
            logging.info('Motor speed set to STOP')
            return
    
    try:
        await motor_util.run_motor(MotorSpeeds.STOP.value)
        DataStorage().save_motor_speed(MotorSpeeds.STOP.value)
        logging.info('Motor speed set to STOP')
    except CustomException as e: # In case of an error, log the error and return
        logging.error(e)
        return


async def test_run_motor(speed : int = 0):
    """Runs the motor at the specified speed after making sure that everything is working as expected.
    In case no value is given, the motor perform one cycle and stop
    
    Args:
        speed (int): The speed at which the motor should run. Defaults to 0.
    """
    # NOTE: There is a function in `motor_util.stop_motor_at_the_edge_of_the_cell` which might be useful here.
    raise NotImplementedError('This function is not implemented yet.')