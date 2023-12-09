import asyncio
import logging
import time

from Motor.MotorController import run_motor_cycle
from Heaters.HeatersController import run_heaters_cycle
from DataStorage import DataStorage
from Camera.CameraController import run_camera_cycle
from SoundCard.SoundCardController import run_sound_card_cycle
from Telecoms.CommunicationsController import run_telecoms_cycle

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


async def main():
    # NOTE: This should be the same as POWER_ON during flight_mode
    time_at_start_of_program = time.perf_counter()

    telecoms_task = asyncio.create_task(run_telecoms_cycle())

    # Make sure the telecoms cycle has started and we have received the mode from the ground station
    await asyncio.sleep(2)
    test_mode = await DataStorage().get_mode() == 'TEST'

    if test_mode:
        logging.info('''
        ========================================
        Starting the application in TEST mode.
        ========================================''')

        await asyncio.gather(
            # run_sensors_cycle(time_at_start_of_program),
            run_sound_card_cycle(time_at_start_of_program),
            run_camera_cycle(time_at_start_of_program),
            run_heaters_cycle(time_at_start_of_program),
            # The only thing that is not run in test mode is the motor
        )
    else:
        logging.info('''
        ========================================
        Starting the application in FLIGHT mode.
        ========================================''')

        await asyncio.gather(
            # run_sensors_cycle(time_at_start_of_program),
            run_sound_card_cycle(time_at_start_of_program),
            run_camera_cycle(time_at_start_of_program),
            run_heaters_cycle(time_at_start_of_program),
            run_motor_cycle(time_at_start_of_program),
        )

    telecoms_task.cancel()


if __name__ == '__main__':
    asyncio.run(main())
