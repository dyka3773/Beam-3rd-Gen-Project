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


async def run_rocket_signals_cycle():
    """Runs the rocket signals cycle.
    """
    logging.info("Starting rocket signals cycle")

    while True:
        LO, SOE, SODS = signal_utils.get_signals()
        await DataStorage().save_signals(LO, SOE, SODS)
        logging.info(f"LO: {LO}, SOE: {SOE}, SODS: {SODS}")

        await asyncio.sleep(0.3)

        if LO == 1:
            break

    logging.info(
        "Received LO signal so now we will continue working for 380 seconds")

    time_when_received_LO = time.perf_counter()

    while (time.perf_counter() - time_when_received_LO < TimelineEnum.SODS_OFF.value):
        LO, SOE, SODS = signal_utils.get_signals()
        await DataStorage().save_signals(LO, SOE, SODS)
        logging.info(f"LO: {LO}, SOE: {SOE}, SODS: {SODS}")

        await asyncio.sleep(0.3)

    logging.info("Finished rocket signals cycle")
