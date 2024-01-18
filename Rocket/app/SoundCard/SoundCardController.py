import asyncio
import time
import logging
import threading
from u3 import U3

from Enums.TimelineEnum import TimelineEnum
from DataStorage import DataStorage
from SoundCard.sound_card_driver import start_recording
from Enums.PinsEnum import PinsEnum
from Telecoms.Signals import signal_utils

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

SCAN_FREQUENCY = 48000  # Hz


async def run_sound_card_cycle():
    """Runs the sound card cycle according to the timeline.
    This function is responsible for the control of the sound card which in turn controls:
    - The thermistors
    - The I-VED technique
    """
    logging.info("Starting sound card cycle")

    try:

        card = U3()
        card.configU3()
        card.getCalibrationData()
        card.configIO(  # TODO: Look up what each of these parameters do
            FIOAnalog=3,
            NumberOfTimersEnabled=2
        )
        logging.debug("Configuring Sound Card")

        card.configTimerClock(
            TimerClockBase=3,
            TimerClockDivisor=1
        )

        card.streamConfig(  # TODO: Look up what each of these parameters do
            NumChannels=4,
            PChannels=[0, 1, 2, 3],
            NChannels=[31, 31, 31, 31],
            Resolution=3,
            ScanFrequency=SCAN_FREQUENCY
        )

    except Exception as e:
        logging.error("An Error has occured in the Sound Card Driver")
        logging.error(e)
        await DataStorage().save_sound_card_status(3)
        return

    while True:
        temperature_of_card = card.getTemperature() - 273.15  # Convert to Celsius

        # FIXME: This is voltage and it needs to be converted to temperature by using the utils.thermistor_util
        temperature_of_thermistor1 = card.getAIN(2)
        temperature_of_thermistor2 = card.getAIN(3)

        await DataStorage().save_temperature_of_sensor(temperature_of_card, 3)
        await DataStorage().save_temperature_of_sensor(temperature_of_thermistor1, 1)
        await DataStorage().save_temperature_of_sensor(temperature_of_thermistor2, 2)

        await DataStorage().save_sound_card_status(1)
        logging.info("I-VED is OFF")

        await asyncio.sleep(0.3)

        if signal_utils.get_status_of_signal(PinsEnum.SODS):
            break

    logging.info(
        "Received SODS signal so now we will continue working for 380 seconds")

    time_when_started_recording = time.perf_counter()

    await DataStorage().save_sound_card_status(2)

    record_for = TimelineEnum.SODS_OFF.adapted_value - \
        TimelineEnum.SODS_ON.adapted_value

    threading.Thread(
        target=start_recording,
        args=(card, record_for),
        daemon=True
    ).start()

    logging.info("I-VED is ON and the sound card is RECORDING")

    while (time.perf_counter() - time_when_started_recording < record_for):

        temperature_of_card = card.getTemperature() - 273.15  # Convert to Celsius

        # FIXME: This is voltage and it needs to be converted to temperature by using the utils.thermistor_util
        temperature_of_thermistor1 = card.getAIN(2)
        temperature_of_thermistor2 = card.getAIN(3)

        await DataStorage().save_temperature_of_sensor(temperature_of_card, 3)
        await DataStorage().save_temperature_of_sensor(temperature_of_thermistor1, 1)
        await DataStorage().save_temperature_of_sensor(temperature_of_thermistor2, 2)

        await DataStorage().save_sound_card_status(2)

        await asyncio.sleep(0.3)

    await DataStorage().save_sound_card_status(0)
    logging.info("Finished sound card cycle")

    logging.info("Stopping the stream...")
    card.close()
