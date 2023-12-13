import logging
import time

import u3


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

SCAN_FREQUENCY = 48000  # Hz


def start_recording(card: u3.U3, record_for: float = 650):
    """Starts recording with the sound card.

    Args:
        record_for (int, optional): The number of seconds to record for. Defaults to 650.
    """
    start = time.perf_counter()

    try:
        with open("AIO0-1.txt", "w+") as file:

            file.write("AIN0, AIN1\n")

            while True:

                # The stream will stop only if we have surpassed the record_for time
                if time.perf_counter() - start > record_for:
                    break

                file.write(f"{card.getAIN(0)}, {card.getAIN(1)}\n")

    except Exception as e:
        logging.error("Error while recording from sound card")
        logging.error(e)
