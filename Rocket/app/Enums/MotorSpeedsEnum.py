from enum import Enum


class MotorSpeedsEnum(Enum):
    """An enum to store the motor_util speeds."""

    STOP = 0
    FULL_SPEED = 255


class MotorPWMSpeeds(Enum):
    """An enum to store the motor_util speeds."""

    STOP = 65535
    HALF_SPEED = 32768
    FULL_SPEED = 0
