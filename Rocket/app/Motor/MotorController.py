import asyncio
import time
import logging

from DataStorage import DataStorage
from Enums.TimelineEnum import TimelineEnum
from Enums.MotorSpeedsEnum import MotorSpeedsEnum
from Motor import motor_util
from ErrorHandling.CustomException import CustomException

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
    data_manager = await DataStorage()
    
    await data_manager.save_motor_speed(MotorSpeedsEnum.STOP.value)
    logging.info('Motor speed set to STOP')
    await asyncio.sleep(TimelineEnum.START_MOTOR.value)
    
    # BUG: The code after the above line is almost fully blocking so asyncio is not really useful here. 
    #      It should be changed to the threading module.
    
    interval_check = time.perf_counter()
    
    while (time.perf_counter() - starting_time < TimelineEnum.SOE_ON.value):
        try:
            await motor_util.run_motor(MotorSpeedsEnum.FULL_SPEED.value)
            # NOTE: The above line may be wrong because if the Jetson PWM works as the Raspberry Pi PWM,
            #       then we don't need to call the function `motor_util.run_motor` in a while loop. At least
            #       not without a sleep in the loop. @see the snippet from Rocket\archive\motor_control.py
            #       !!! BUT, if we decide to use the way described there, we need to make sure there is another
            #       way to stop the motor in case of overheat or other errors.
                
            if (time.perf_counter() - interval_check) > 0.3:
                await data_manager.save_motor_speed(MotorSpeedsEnum.FULL_SPEED.value)
                logging.info('Motor speed is set to FULL_SPEED')
                interval_check = time.perf_counter()
        except CustomException as e: # In case of an error, stop the motor, log the error and return
            logging.error(e)
            await motor_util.run_motor(MotorSpeedsEnum.STOP.value)
            await data_manager.save_motor_speed(MotorSpeedsEnum.STOP.value)
            logging.info('Motor speed set to STOP')
            return
    
    try:
        await motor_util.run_motor(MotorSpeedsEnum.STOP.value)
        await data_manager.save_motor_speed(MotorSpeedsEnum.STOP.value)
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