import platform
import asyncio
import logging
from serial_asyncio import open_serial_connection

from DataStorage import DataStorage
from Enums.ErrorCodesEnum import ErrorCodesEnum

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

# Define the serial port and baud rate
if platform.system() == "Windows":  # If platform is Windows, port is COM5 otherwise /dev/ttyTHS1
    port = "COM5"
    logging.info(f"Running on Windows and using {port}")
else:
    port = "/dev/ttyTHS1"
    logging.info(f"Running on Jetson Nano and using {port}")

baud_rate = 9600


async def run_telecoms_cycle():
    """Send and receive data from the serial port."""
    reader, writer = await open_serial_connection(url=port, baudrate=baud_rate)

    try:
        while True:
            # Send the last saved data to the serial port
            data_to_send = await DataStorage().get_last_row_of_all_data()
            if data_to_send:
                logging.info(f"Sending data: {data_to_send}")
                writer.write(format_data_to_send(*data_to_send))

            await writer.drain()

            await asyncio.sleep(0.166)

            # Read whether the experiment should run on TEST or FLIGHT mode
            # TODO: In case we have more time, we could also receive commands from the serial port
            mode = await reader.readline()  # This is blocking in case there is no data to read
            mode = str(mode, 'utf-8').rstrip()

            if mode:
                logging.info(f"Received data: {mode}")
                await DataStorage().save_mode(mode)

    except Exception as e:
        logging.error(f"Error in telecoms cycle: {e}")
        await DataStorage().save_error_code(ErrorCodesEnum.CONNECTION_ERROR.value)


def format_data_to_send(*data):
    """Formats the data to send to the serial port into a byte array.

    Args:
        *data: The data to send to the serial port.

    Returns:
        The data to send to the serial port in a byte array format.
    """
    return bytes(f"{','.join(map(str, data))}\n", 'utf-8')
