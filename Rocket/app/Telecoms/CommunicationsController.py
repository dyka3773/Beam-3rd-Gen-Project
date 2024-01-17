import platform
import asyncio
import logging
import time
from serial_asyncio import open_serial_connection
from functools import cache

from DataStorage import DataStorage
from Enums.ErrorCodesEnum import ErrorCodesEnum
from Enums.TimelineEnum import TimelineEnum

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


async def run_telecoms_cycle(starting_time: float):
    """Send and receive data from the serial port.

    Args:
        starting_time(float): The time at the start of the program.
    """
    _, writer = await open_serial_connection(url=port, baudrate=38400)

    try:
        while True:
            # Send the last saved data to the serial port
            data_to_send = await DataStorage().get_last_row_of_all_data()
            if data_to_send:
                logging.info(f"Sending data: {data_to_send}")
                writer.write(format_data_to_send(*data_to_send))

            await writer.drain()

            await asyncio.sleep(0.3)  # 3 times per second

            if time.perf_counter() - starting_time > TimelineEnum.SODS_OFF.adapted_value:
                logging.info("Stopping the telecoms cycle...")
                break

    except Exception as e:
        logging.error(f"Error in telecoms cycle: {e}")
        await DataStorage().save_error_code(ErrorCodesEnum.CONNECTION_ERROR.value)


@cache
def format_data_to_send(*data):
    """Formats the data to send to the serial port into a byte array.

    Args:
        *data: The data to send to the serial port.

    Returns:
        The data to send to the serial port in a byte array format.
    """
    return bytes(f"{','.join(map(str, data))}\n", 'utf-8')
