import logging
import time
import threading

import u3

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

SCAN_FREQUENCY = 48000  # Hz


def start_recording(record_for: float = 650):
    """Starts recording with the sound card.

    Args:
        record_for (int, optional): The number of seconds to record for. Defaults to 650.
    """
    try:
        card = u3.U3()
        card.configU3()
        card.getCalibrationData()
        card.configIO(FIOAnalog=3)  # NOTE: What does this do?

        logging.debug("Configuring sound card")
        card.streamConfig(  # TODO: Look up what each of these parameters do
            NumChannels=2,
            PChannels=[0, 1, 2],
            NChannels=[31, 31],
            Resolution=3,
            ScanFrequency=SCAN_FREQUENCY
        )

        threading.Thread(target=record, args=(card, record_for)).start()
    except Exception as e:
        logging.error("Error in sound card driver")
        logging.error(e)
        raise e


def record(card: u3.U3, record_for: int = 650):
    """Records from the sound card for the specified amount of time.

    Args:
        card (u3.U3): The sound card to record from.
        record_for (int, optional):  The number of seconds to record for. Defaults to 650.

    Raises:
        e: Any exception that occurs while recording.
    """
    try:
        logging.debug("Start stream")
        card.streamStart()
        start = time.perf_counter()
        logging.debug(f"Start time is {start}")

        with open("AIO0.txt", 'w+') as input0, open("AIO1.txt", 'w+') as input1:
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

                    # Writing the input to two separate files
                    input0.write(f"{data_batch['AIN0']}")
                    input1.write(f"{data_batch['AIN1']}")

                    results = card.processStreamData(data_batch['results'])

                    r_aio2 = results['AIN2']

                    print(f"AIN2: {r_aio2}")

                else:
                    # Got no data back from our read.
                    # This only happens if your stream isn't faster than the USB read
                    # timeout, ~1 sec.
                    logging.debug(f"No data ; {time.perf_counter()}")
    except Exception as e:
        logging.error("Error while recording from sound card")
        logging.error(e)
    finally:
        card.streamStop()
        logging.debug("Stream stopped.")
        card.close()
