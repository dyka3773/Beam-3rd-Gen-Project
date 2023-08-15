import logging

from ErrorHandling.CustomException import CustomException
from Enums.ErrorCodesEnum import ErrorCodesEnum
import Motor.motor_driver as motor
from utils.data_handling_utils import get_avg_temp, get_avg_pressure

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
    if avg_temp is None or avg_temp > 50 or avg_temp < 0: # TODO: Change the values to the correct ones by consulting the Mechanical and the Science teams
        raise CustomException(
            f'The temperature is too high or too low or null. The average temperature is {avg_temp=}.',
            ErrorCodesEnum.OVERHEAT_ERROR
        )
    
    avg_pressure = await get_avg_pressure() # FIXME: These are just placeholders. IDK if we actually need to get the average temperature and pressure.
    if avg_pressure is None or avg_pressure > 100 or avg_pressure < 0: # TODO: Change the values to the correct ones by consulting the Mechanical and the Science teams
        raise CustomException(
            f'The pressure is too high or too low or null. The average pressure is {avg_pressure=}', 
            ErrorCodesEnum.OVERPRESSURE_ERROR
        )
    
    logging.debug('The other components are working as expected')
    
    # TODO: Uncomment the following line when the motor driver is implemented
    # motor.run(speed)
    
    logging.debug(f'Running the motor at speed {speed}')
    
    
def stop_motor_at_the_edge_of_the_cell():
    """Stops the motor at the edge of the cell."""
    raise NotImplementedError('This function is not implemented yet.')