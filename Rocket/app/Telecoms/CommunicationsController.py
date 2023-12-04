import platform
import serial
import logging

from DataStorage import DataStorage
from Rocket.app.Enums.ErrorCodesEnum import ErrorCodesEnum

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
else:
    port = "/dev/ttyTHS1"

baud_rate = 9600

# Create a serial connection
# 0.166 seconds is half of 3Hz and we also need to account for the time it takes to read the data
ser = serial.Serial(port, baud_rate, timeout=0.166)


async def run_telecoms_cycle():
    """Send and receive data from the serial port."""
    try:
        while True:
            # Send the last saved data to the serial port
            data_to_send = await DataStorage().get_first_row_of_all_data()
            if data_to_send:
                ser.write(*data_to_send)

            # Read whether the experiment should run on TEST or FLIGHT mode
            # TODO: In case we have more time, we could also receive commands from the serial port
            mode = ser.readline().decode("utf-8").rstrip()
            if mode:
                logging.info(f"Received data: {mode}")
                await DataStorage().save_mode(mode)
    except Exception as e:
        logging.error(f"Error in telecoms cycle: {e}")
        await DataStorage().save_error_code(ErrorCodesEnum.CONNECTION_ERROR.value)
