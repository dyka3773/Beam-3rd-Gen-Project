import numpy as np


# The folloring functions are used to get the status of each component of the system

# FIXME: The following functions are just placeholders. They should be replaced with the actual functions which will read the values from the csv file

def get_motor_speed() -> int:
    """Gets the motor speed from the CSV file.

    Returns:
        int: The motor speed.
    """
    return np.random.randint(0,255) # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file

def get_sound_card_status() -> bool:
    """Gets the sound card status from the CSV file.

    Returns:
        bool: The sound card status.
    """
    return bool(np.random.randint(0,2)) # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file

def get_camera_status() -> bool:
    """Gets the camera status from the CSV file.

    Returns:
        bool: The camera status.
    """
    return bool(np.random.randint(0,2)) # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file

def get_heater_status() -> bool:
    """Gets the heater status from the CSV file.

    Returns:
        bool: The heater status.
    """
    return bool(np.random.randint(0,2)) # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file

def get_temperature(sensor: str, time: int) -> list:
    """Gets the temperature from the CSV file.

    Args:
        sensor (str): The sensor from which the temperature will be read.
        time (int): The time for which the temperature will be read.

    Returns:
        list: The temperature values for the given time.
    """
    
    temperature = [np.random.randint(-50,100) for _ in range(time)]
    
    return temperature # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file

def get_pressure(sensor: str, time: int) -> list:
    """Gets the pressure from the CSV file.

    Args:
        sensor (str): The sensor from which the pressure will be read.
        time (int): The time for which the pressure will be read.

    Returns:
        list: The pressure values for the given time.
    """
    
    pressure = [np.random.randint(8,32)/16 for _ in range(time)]
    
    return pressure # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file


# TODO: Add the functions to send commands to the components.

# The following functions are used to check the status of each component of the system. This means that they will check if the component is working properly.

def check_motor() -> bool:
    """Checks the motor status.

    Returns:
        bool: The motor status.
    """
    return bool(np.random.randint(0,2)) # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file

def check_sound_card() -> bool:
    """Checks the sound card status.

    Returns:
        bool: The sound card status.
    """
    return bool(np.random.randint(0,2)) # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file

def check_camera() -> bool:
    """Checks the camera status.

    Returns:
        bool: The camera status.
    """
    return bool(np.random.randint(0,2)) # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file

def check_heater() -> bool:
    """Checks the heater status.

    Returns:
        bool: The heater status.
    """
    return bool(np.random.randint(0,2)) # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file

def delete_data() -> bool:
    """Deletes the data from the CSV file.
    
    Returns:
        bool: The status of the operation.
    """
    return bool(np.random.randint(0,2)) # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file