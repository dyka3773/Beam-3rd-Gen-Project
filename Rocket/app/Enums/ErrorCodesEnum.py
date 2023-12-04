from enum import Enum


class ErrorCodesEnum(Enum):
    """An enum to store the error codes and their messages.

    NOTE: The error codes are stored in the database as integers.
    """
    MOTOR_SPEED_ERROR = 1
    SOUND_CARD_ERROR = 2
    CAMERA_ERROR = 3
    HEATER_ERROR = 4
    TEMP_1_ERROR = 5
    PRESSURE_1_ERROR = 6
    TEMP_2_ERROR = 7
    PRESSURE_2_ERROR = 8
    UNKNOWN_ERROR = 9
    OVERHEAT_ERROR = 10
    OVERPRESSURE_ERROR = 11
    TEMP_SENSOR_NULL_ERROR = 12
    CONNECTION_ERROR = 13

    @staticmethod
    def from_value(value: int):
        """Returns the error code from the given value.

        Args:
            value (int): The value of the error code to be returned.

        Returns:
            ErrorCode: The error code with the given value.
        """
        for code in ErrorCodesEnum:
            if code.value == value:
                return code
        return None
