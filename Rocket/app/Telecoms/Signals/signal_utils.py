try:
    import Jetson.GPIO as GPIO  # type: ignore
except ImportError:
    # This is for testing purposes only so that the tests can run on a non-Jetson device

    class GPIO:
        """A mock class for the GPIO module."""

        BOARD = "BOARD"
        HIGH = "HIGH"
        LOW = "LOW"
        IN = "IN"

        @staticmethod
        def setmode(x):
            """A mock method for the setmode method."""
            pass

        @staticmethod
        def setup(x, y):
            """A mock method for the setup method."""
            pass

        @staticmethod
        def input(x):
            """A mock method for the input method."""
            return False

from Enums.PinsEnum import PinsEnum

LO_pin = PinsEnum.LO.value
SOE_pin = PinsEnum.SOE.value
SODS_pin = PinsEnum.SODS.value

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LO_pin, GPIO.IN)
GPIO.setup(SOE_pin, GPIO.IN)
GPIO.setup(SODS_pin, GPIO.IN)


def get_signals() -> tuple[bool, bool, bool]:
    """Gets the signals from the RXSM.

    Returns:
        tuple[bool, bool, bool]: A tuple containing the signals from the RXSM.
    """
    # NOTE: With Dimitris' PCB these should be inverted
    LO_pin_state = GPIO.input(LO_pin) != GPIO.HIGH
    SOE_pin_state = GPIO.input(SOE_pin) != GPIO.HIGH
    SODS_pin_state = GPIO.input(SODS_pin) != GPIO.HIGH

    return LO_pin_state, SOE_pin_state, SODS_pin_state


def get_status_of_signal(signal: PinsEnum) -> bool:
    """Gets the status of the given signal.

    Args:
        signal (PinsEnum): The signal to get the status of.

    Returns:
        bool: The status of the given signal.
    """
    return GPIO.input(signal.value) != GPIO.HIGH
