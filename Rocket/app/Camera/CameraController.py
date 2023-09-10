import asyncio
import time
import logging
import threading

from Enums.TimelineEnum import TimelineEnum
from DataStorage import DataStorage
from Camera.camera_driver import start_recording

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


async def run_camera_cycle(starting_time: float):
    """Runs the camera cycle according to the timeline.

    Args:
        starting_time (float): The time at which the program started.
    """
    logging.info("Starting camera cycle")

    while (time.perf_counter() - starting_time < TimelineEnum.SODS_ON.get_adapted_value):
        await DataStorage().save_camera_status(0)
        logging.debug("Camera is OFF")
        await asyncio.sleep(0.3)

    record_for = TimelineEnum.SODS_OFF.value - TimelineEnum.SODS_ON.value

    try:
        # TODO: Uncomment the following line when the camera_driver#start_recording function is implemented.
        # threading.Thread(
        #     target=start_recording,
        #     args=(record_for,)
        # ).start()
        pass
    except Exception:
        logging.error("An Error has occured in the Camera Driver")
        await DataStorage().save_camera_status(3)
        return

    await DataStorage().save_camera_status(2)
    logging.info("Camera is RECORDING")

    while (time.perf_counter() - starting_time < TimelineEnum.SODS_OFF.get_adapted_value):
        await DataStorage().save_camera_status(2)
        logging.debug("Camera is RECORDING")
        await asyncio.sleep(0.3)

    logging.info("Camera has STOPPED RECORDING")
    logging.info("Finished camera cycle")
