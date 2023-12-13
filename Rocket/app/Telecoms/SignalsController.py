import logging
import time
import asyncio

from Enums.TimelineEnum import TimelineEnum
from DataStorage import DataStorage
import Telecoms.Signals.signal_utils as signal_utils

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


async def run_rocket_signals_cycle(starting_time: float):
    """Runs the rocket signals cycle.

    Args:
        starting_time (float): The time at which the program started.
    """
    logging.info("Starting rocket signals cycle")
    while time.perf_counter() - starting_time < TimelineEnum.SODS_OFF.get_adapted_value:
        LO, SOE, SODS = signal_utils.get_signals()
        await DataStorage().save_signals(LO, SOE, SODS)
        logging.info(f"LO: {LO}, SOE: {SOE}, SODS: {SODS}")

        await asyncio.sleep(0.3)
