import asyncio
import logging
import time

from Camera.CameraController import run_camera_cycle
from SoundCard.SoundCardController import run_sound_card_cycle
from Telecoms.CommunicationsController import run_telecoms_cycle
from Telecoms.SignalsController import run_rocket_signals_cycle

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


async def main():
    # NOTE: This should be the same as POWER_ON during flight_mode or we should sync them up somehow
    time_at_start_of_program = time.perf_counter()

    logging.info('''
    ========================================
    Starting the application in FLIGHT mode.
    ========================================''')

    await asyncio.gather(
        run_rocket_signals_cycle(time_at_start_of_program),
        run_sound_card_cycle(time_at_start_of_program),
        run_camera_cycle(time_at_start_of_program),
        run_telecoms_cycle(time_at_start_of_program),
    )


if __name__ == '__main__':
    asyncio.run(main())
