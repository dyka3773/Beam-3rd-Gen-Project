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

            for data_batch in card.streamData():

                # The stream will stop only if we have surpassed the record_for time
                if time.perf_counter() - start > record_for:
                    break

                if data_batch is not None:
                    if data_batch["errors"] != 0:
                        logging.debug(
                            f"Errors counted: {data_batch['errors']} ; {time.perf_counter()}")

                    if data_batch["numPackets"] != card.packetsPerRequest:
                        logging.warn(
                            f"----- UNDERFLOW : {data_batch['numPackets']} ; {time.perf_counter()}")

                    if data_batch["missed"] != 0:
                        logging.warn(f"+++ Missed {data_batch['missed']}")

                    file.write(f"{data_batch['AIN0']}, {data_batch['AIN1']}\n")

                else:
                    # Got no data back from our read.
                    # This only happens if your stream isn't faster than the USB read
                    # timeout, ~1 sec.
                    logging.debug(f"No data ; {time.perf_counter()}")
    except Exception as e:
        logging.error("Error while recording from sound card")
        logging.error(e)
