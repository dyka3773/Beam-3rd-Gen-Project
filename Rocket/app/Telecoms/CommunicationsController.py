import platform
import asyncio
import logging
import time
from serial_asyncio import open_serial_connection
from functools import cache

from DataStorage import DataStorage
from Enums.ErrorCodesEnum import ErrorCodesEnum
from Enums.TimelineEnum import TimelineEnum
from Enums.PinsEnum import PinsEnum
import Telecoms.Signals.signal_utils as signal_utils


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
)

# Define the serial port and baud rate
if platform.system() == "Windows":  # If platform is Windows, port is COM5 otherwise /dev/ttyTHS1
    port = "COM5"
    logging.info(f"Running on Windows and using {port}")
else:
    port = "/dev/ttyTHS1"
    logging.info(f"Running on Jetson Nano and using {port}")


async def run_telecoms_cycle():
    """Send and receive data from the serial port.

    Args:
        starting_time(float): The time at the start of the program.
    """
    _, writer = await open_serial_connection(url=port, baudrate=38400)

    try:

        while True:
            if signal_utils.get_status_of_signal(PinsEnum.LO):
                break

            data_to_send = await DataStorage().get_last_row_of_all_data()

            try:
                if data_to_send:
                    logging.info(f"Sending data: {data_to_send}")
                    writer.write(format_data_to_send(*data_to_send))

                await writer.drain()

            except Exception as e:
                logging.error(f"Error in telecoms cycle: {e}")
                await DataStorage().save_error_code(ErrorCodesEnum.CONNECTION_ERROR.value)
                raise e

            await asyncio.sleep(0.3)  # 3 times per second

        logging.info(
            "Received LO signal so now we will continue working for 380 seconds")

        time_when_received_LO = time.perf_counter()

        while (time.perf_counter() - time_when_received_LO < TimelineEnum.SODS_OFF.value):
            data_to_send = await DataStorage().get_last_row_of_all_data()

            try:
                if data_to_send:
                    logging.info(f"Sending data: {data_to_send}")
                    writer.write(format_data_to_send(*data_to_send))

                await writer.drain()

            except Exception as e:
                logging.error(f"Error in telecoms cycle: {e}")
                await DataStorage().save_error_code(ErrorCodesEnum.CONNECTION_ERROR.value)
                raise e

            await asyncio.sleep(0.3)  # 3 times per second

    finally:
        logging.info("Finished telecoms cycle")
        writer.close()
        await writer.wait_closed()


@cache
def format_data_to_send(*data):
    """Formats the data to send to the serial port into a byte array.

    Args:
        *data: The data to send to the serial port.

    Returns:
        The data to send to the serial port in a byte array format.
    """
    return bytes(f"{','.join(map(str, data))}\n", 'utf-8')
