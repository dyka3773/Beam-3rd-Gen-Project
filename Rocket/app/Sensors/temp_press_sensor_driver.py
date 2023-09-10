import random  # TODO: Remove this line


def read_temp(sensor_id: int) -> float:
    """Reads the temperature from the sensor.

    Args:
        sensor_id (int): The id of the sensor.

    Returns:
        float: The temperature read from the sensor.
    """
    # TODO: Implement this function
    return random.uniform(-50, 100)


def read_pressure(sensor_id: int) -> float:
    """Reads the pressure from the sensor.

    Args:
        sensor_id (int): The id of the sensor.

    Returns:
        float: The pressure read from the sensor.
    """
    # TODO: Implement this function
    return random.uniform(0.5, 2)
