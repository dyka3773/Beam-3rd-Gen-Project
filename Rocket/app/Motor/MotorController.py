import asyncio
import time
import logging
import threading

from Enums.TimelineEnum import TimelineEnum
from Enums.PinsEnum import PinsEnum
from DataStorage import DataStorage
from Telecoms.Signals import signal_utils
from Motor.motor_driver import run_motor


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


async def run_motor_cycle():
    """Runs the motor cycle according to the timeline.
    """
    logging.info("Starting motor cycle")

    while True:
        if signal_utils.get_status_of_signal(PinsEnum.LO):
            break

        await DataStorage().save_motor_speed(0)
        logging.debug("Motor is OFF")
        await asyncio.sleep(0.3)

    wait_for = TimelineEnum.START_MOTOR.value - TimelineEnum.LIFT_OFF.value

    time_when_received_LO = time.perf_counter()

    while (time.perf_counter() - time_when_received_LO < wait_for):
        await DataStorage().save_motor_speed(0)
        logging.debug("Motor is OFF")
        await asyncio.sleep(0.3)

    run_motor_for = TimelineEnum.SOE_ON.value - TimelineEnum.START_MOTOR.value
    logging.info(f"Motor will run for {run_motor_for} seconds")
    await DataStorage().save_motor_speed(1)

    threading.Thread(
        target=run_motor,
        args=(run_motor_for,),
        daemon=True
    ).start()

    time_when_motor_started = time.perf_counter()

    while (time.perf_counter() - time_when_motor_started < run_motor_for):
        await DataStorage().save_motor_speed(1)
        logging.debug("Motor is ON")
        await asyncio.sleep(0.3)

    while (time.perf_counter() - time_when_received_LO < TimelineEnum.SODS_OFF.value):
        await DataStorage().save_motor_speed(0)
        logging.debug("Motor is OFF")
        await asyncio.sleep(0.3)
