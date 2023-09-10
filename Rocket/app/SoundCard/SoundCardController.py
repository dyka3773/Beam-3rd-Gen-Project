import asyncio
import time
import logging
import threading

from Enums.TimelineEnum import TimelineEnum
from DataStorage import DataStorage
from SoundCard.sound_card_driver import start_recording

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


async def run_sound_card_cycle(starting_time: float):
    """Runs the sound card cycle according to the timeline.

    Args:
        starting_time (float): The time at which the program started.
    """
    logging.info("Starting sound card cycle")
    logging.debug("Sound card is OFF")

    while (time.perf_counter() - starting_time < TimelineEnum.SODS_ON.get_adapted_value):
        await DataStorage().save_sound_card_status(0)
        logging.debug("Sound card is OFF")
        await asyncio.sleep(0.3)

    record_for = TimelineEnum.SODS_OFF.value - TimelineEnum.SODS_ON.value

    try:
        start_recording(record_for)
    except Exception:
        logging.error("An Error has occured in the Sound Card Driver")
        await DataStorage().save_sound_card_status(3)
        return

    await DataStorage().save_sound_card_status(2)
    logging.info("Sound card is RECORDING")

    while (time.perf_counter() - starting_time < TimelineEnum.SODS_OFF.get_adapted_value):
        await DataStorage().save_sound_card_status(2)
        logging.debug("Sound card is RECORDING")
        await asyncio.sleep(0.3)

    logging.info("Sound card has STOPPED RECORDING")
    logging.info("Finished sound card cycle")
