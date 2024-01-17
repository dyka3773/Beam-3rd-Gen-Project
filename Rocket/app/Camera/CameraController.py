import asyncio
import time
import logging
import threading

from Enums.TimelineEnum import TimelineEnum
from DataStorage import DataStorage
from Camera.camera_driver import start_recording
import Camera.led_driver as led_driver

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
)


async def run_camera_cycle(starting_time: float):
    """Runs the camera cycle according to the timeline.

    Args:
        starting_time (float): The time at which the program started.
    """
    logging.info("Starting camera cycle")

    while (time.perf_counter() - starting_time < TimelineEnum.SODS_ON.adapted_value):
        await DataStorage().save_camera_status(0)
        logging.debug("Camera is OFF")
        await asyncio.sleep(0.3)

    led_driver.turn_on_led()
    logging.info("LEDS are ON")
    # await DataStorage().save_led_status(1) # TODO: Implement this functionality

    # NOTE: With the current fps reach this will use about 1.1GB of storage # IDK what timeline this followed
    #       This means that we can perform the full experiment cycle about 80 times before running out of storage
    record_for = TimelineEnum.SODS_OFF.value - TimelineEnum.SODS_ON.value

    try:
        threading.Thread(
            target=start_recording,
            args=(record_for,),
            daemon=True
        ).start()
    except Exception:
        logging.error("An Error has occured in the Camera Driver")
        await DataStorage().save_camera_status(3)
        return

    while (time.perf_counter() - starting_time < TimelineEnum.SODS_OFF.adapted_value):
        await DataStorage().save_camera_status(2)
        logging.debug("Camera is RECORDING")
        await asyncio.sleep(0.3)

    logging.info("Camera has STOPPED RECORDING")
    logging.info("Finished camera cycle")
