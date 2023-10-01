import asyncio
import logging
import time

from Motor.MotorController import run_motor_cycle
from Heaters.HeatersController import run_heaters_cycle
from Sensors.SensorsController import run_sensors_cycle
from Camera.CameraController import run_camera_cycle
from SoundCard.SoundCardController import run_sound_card_cycle

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

# TODO: Install dependencies on Jetson Nano


async def main():

    # TODO: Implement a way to know if the application is running in test mode or flight mode
    test_mode = False

    # NOTE: This should be the same as POWER_ON during flight_mode
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
            run_sensors_cycle(time_at_start_of_program),
            run_sound_card_cycle(time_at_start_of_program),
            run_camera_cycle(time_at_start_of_program),
            run_heaters_cycle(time_at_start_of_program),
            run_motor_cycle(time_at_start_of_program),
        )


if __name__ == '__main__':
    asyncio.run(main())
