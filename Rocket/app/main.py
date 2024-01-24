#! /home/dropstar/opt/python-3.10.13/bin/python

import asyncio
import logging

from Camera.CameraController import run_camera_cycle
from Motor.MotorController import run_motor_cycle
from SoundCard.SoundCardController import run_sound_card_cycle
from Telecoms.CommunicationsController import run_telecoms_cycle
from Telecoms.SignalsController import run_rocket_signals_cycle

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
)


async def main():

    logging.info('''
    ========================================
    Starting the application in FLIGHT mode.
    ========================================''')

    await asyncio.gather(
        run_rocket_signals_cycle(),
        run_sound_card_cycle(),
        run_camera_cycle(),
        run_telecoms_cycle(),
        run_motor_cycle()
    )


if __name__ == '__main__':
    asyncio.run(main())
