from enum import Enum


class PinsEnum(Enum):
    """An enum to store the pins used in the Jetson Nano."""

    LO = 11  # FIXME: Change this later
    SOE = 12  # FIXME: Change this later
    SODS = 13  # FIXME: Change this later
    UART_TX = 8  # These will not be used by the code but it's nice to have them for reference
    UART_RX = 10  # These will not be used by the code but it's nice to have them for reference
