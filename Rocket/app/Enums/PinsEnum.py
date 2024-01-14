from enum import Enum


class PinsEnum(Enum):
    """An enum to store the pins used in the Jetson Nano."""

    LO = 16  # This is in Electrical's PCB
    SOE = 18  # This is in Electrical's PCB
    SODS = 22  # This is in Electrical's PCB
    # LO = 21  # This is in Jim's PCB
    # SOE = 15    # This is in Jim's PCB
    # SODS = 11   # This is in Jim's PCB
    UART_TX = 8  # These will not be used by the code but it's nice to have them for reference
    UART_RX = 10  # These will not be used by the code but it's nice to have them for reference
    LED_HEALTH = 16  # This is in Jim's PCB
    MOTOR_HEATH = 38  # This is in Jim's PCB
    JETSON_HEATH = 22   # This is in Jim's PCB
    LED_CONTROL = 31  # This is in Jim's PCB
    MOTOR_CONTROL = 32  # This is in Jim's PCB
