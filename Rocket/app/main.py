import asyncio # NOTE: This might change eventually to the threading module
import logging
import time

from MotorController import run_motor_cycle

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s', 
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

async def main():
    
    test_mode = False # TODO: Implement a way to know if the application is running in test mode or flight mode
    
    time_at_start_of_program = time.perf_counter()
    
    if test_mode:
        logging.info('''
        ========================================
        Starting the application in TEST mode.
        ========================================''')
        
        await asyncio.gather(
            # TODO: Add the tasks that should be run in test mode
        )
    else:
        logging.info('''
        ========================================
        Starting the application in FLIGHT mode.
        ========================================''')
        
        await asyncio.gather(
            # TODO: Complete the tasks that should be run in flight mode
            run_motor_cycle(time_at_start_of_program)
        )


if __name__ == '__main__':
    asyncio.run(main())