import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# The above code is a hack used to import modules from the parent directory. 
# NOTE: I DO NOT recommend using this in production code.

import logging

from DataStorage import DataStorage
from ErrorHandling.CustomException import CustomException
from ErrorHandling.ErrorCode import ErrorCode
import Motor.motor_driver as motor

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s', 
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

async def run_motor(speed : int) -> None | CustomException:
    """Runs the motor at the specified speed after making sure that everything is working as expected.
    
    Args:
        speed (int): The speed at which the motor should run.
        
    Raises:
        CustomException: If the temperature or pressure is too high or too low.
    """
    if speed == 0: # I'm making the assumption that if we need to stop the motor, we do not need to check the other components.
        # TODO: Uncomment the following line when this function is implemented
        # stop_motor_at_the_edge_of_the_cell()
        logging.debug('The motor has been stopped at the edge of the cell')
        return
    
    logging.debug('Checking if the other components are working as expected')
    avg_temp = await get_avg_temp() # FIXME: These are just placeholders. IDK if we actually need to get the average temperature and pressure.
    if avg_temp is None or avg_temp > 50 or avg_temp < 0: # TODO: Change the values to the correct ones
        raise CustomException(
            f'The temperature is too high or too low or null. The average temperature is {avg_temp=}.',
            ErrorCode.OVERHEAT_ERROR
        )
    
    avg_pressure = await get_avg_pressure() # FIXME: These are just placeholders. IDK if we actually need to get the average temperature and pressure.
    if avg_pressure is None or avg_pressure > 100 or avg_pressure < 0: # TODO: Change the values to the correct ones
        raise CustomException(
            f'The pressure is too high or too low or null. The average pressure is {avg_pressure=}', 
            ErrorCode.OVERPRESSURE_ERROR
        )
    
    logging.debug('The other components are working as expected')
    
    # TODO: Uncomment the following line when the motor driver is implemented
    # motor.run(speed)
    
    logging.debug(f'Running the motor at speed {speed}')
    
    
def stop_motor_at_the_edge_of_the_cell():
    """Stops the motor at the edge of the cell."""
    raise NotImplementedError('This function is not implemented yet.')
    
async def get_avg_temp() -> float | None:
    """Returns the average temperature of the two temperature sensors.
    
    Returns:
        float: The average temperature of the two temperature sensors.
    """
    
    # FIXME: This can be sooo optimized.
    
    temp_list = [DataStorage().get_temperature_of_sensor(i) for i in range(1, 3)]
    
    if None in temp_list:
        return None
    
    return sum(temp_list) / len(temp_list)

async def get_avg_pressure() -> float | None:
    """Returns the average pressure of the two pressure sensors.
    
    Returns:
        float: The average pressure of the two pressure sensors.
    """
    
    # FIXME: This can be sooo optimized.
    
    pressure_list = [DataStorage().get_pressure_of_sensor(i) for i in range(1, 3)]
    
    if None in pressure_list:
        return None
    
    return sum(pressure_list) / len(pressure_list)