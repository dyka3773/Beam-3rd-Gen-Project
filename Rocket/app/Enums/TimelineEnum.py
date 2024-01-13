from enum import Enum


class TimelineEnum(Enum):
    """An enum to store the timeline of the rocket."""

    POWER_ON = -600  # Power on everything
    LANDING = 390   # This is estimated on the REXUS 29 & 30 flight profile that landed at 391 & 402 respectively
    SODS_ON = -100  # Camera and I-VED start recording
    SODS_OFF = 380  # Switch off everything
    SOE_ON = 86     # Switch off the motor
    SOE_OFF = 191   # The end of microgravity
    LIFT_OFF = 0
    START_MOTOR = 66    # 64 in Electrical's PCB
    START_OF_MICROGRAVITY = 72

    @property
    def adapted_value(self):
        return self.value + 600
