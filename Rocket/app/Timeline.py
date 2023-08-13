from enum import Enum

class Timeline(Enum):
    """An enum to store the timeline of the rocket."""
    
    POWER_ON = -600 # Power on everything
    LANDING = 600
    SODS_ON = -100  # Camera and I-VED start recording 
    SODS_OFF = 550  # Switch off everything
    SOE_ON = 73     # Switch off the motor
    SOE_OFF = 191   # The end of microgravity
    LIFT_OFF = 0
    START_MOTOR = 51
    START_OF_MICROGRAVITY = 71