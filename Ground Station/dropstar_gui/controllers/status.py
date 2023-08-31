import asyncio
import numpy as np
import aiosqlite as sql
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# The following functions are used to get the status of each component of the system


async def get_motor_speed() -> int:
    """Gets the motor speed from the db.

    Returns:
        int: The motor speed.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = await db.execute('SELECT motor_speed FROM GS_data ORDER BY time DESC LIMIT 1')
        speed = await result.fetchone()
        speed = speed[0]  # type: ignore

    return speed


async def get_sound_card_status() -> bool:
    """Gets the sound card status from the db.

    Returns:
        bool: The sound card status.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = await db.execute('SELECT sound_card_status FROM GS_data ORDER BY time DESC LIMIT 1')
        status = await result.fetchone()
        status = status[0]  # type: ignore

    return status


async def get_camera_status() -> bool:
    """Gets the camera status from the db.

    Returns:
        bool: The camera status.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = await db.execute('SELECT camera_status FROM GS_data ORDER BY time DESC LIMIT 1')
        status = await result.fetchone()
        status = status[0]  # type: ignore

    return status


async def get_heater_status() -> bool:
    """Gets the heater status from the db.

    Returns:
        bool: The heater status.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = await db.execute('SELECT heater_status FROM GS_data ORDER BY time DESC LIMIT 1')
        status = await result.fetchone()
        status = status[0]  # type: ignore

    return status


async def get_temperature(sensor: str, time: int) -> list[int]:
    """Gets the temperature from the db.

    Args:
        sensor (str): The sensor from which the temperature will be read.
        time (int): The time for which the temperature will be read.

    Returns:
        list: The temperature values for the given time.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        if sensor == 'sensor1':
            col = 'temp_1'
        elif sensor == 'sensor2':
            col = 'temp_2'
        else:
            raise ValueError('Invalid sensor name')

        results = await db.execute(f'''SELECT {col}
                                        FROM GS_data
                                        WHERE time >= DATETIME('now', '-{time} seconds')
                                        ORDER BY time DESC
                                ''')
        temperature = await results.fetchall()

    temperature.reverse()  # type: ignore
    logging.debug(f'Got temperature: {temperature}')

    return temperature  # type: ignore


async def get_pressure(sensor: str, time: int) -> list[int]:
    """Gets the pressure from the db.

    Args:
        sensor (str): The sensor from which the pressure will be read.
        time (int): The time for which the pressure will be read.

    Returns:
        list: The pressure values for the given time.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        if sensor == 'sensor1':
            col = 'pressure_1'
        elif sensor == 'sensor2':
            col = 'pressure_2'
        else:
            raise ValueError('Invalid sensor name')

        results = await db.execute(f'''SELECT {col}
                                        FROM GS_data
                                        WHERE time >= DATETIME('now', '-{time} seconds')
                                        ORDER BY time DESC
                                    ''')
        pressure = await results.fetchall()

    pressure.reverse()  # type: ignore
    logging.debug(f'Got pressure: {pressure}')

    return pressure  # type: ignore


# The following functions are used to check the status of each component of the system. This means that they will check if the component is working properly.
# FIXME: The following functions are just placeholders. In order to implement these, we need to implement the Uplink first.

def check_motor() -> bool:
    """Checks the motor status.

    Returns:
        bool: The motor status.
    """
    return bool(np.random.randint(0, 2))  # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file


def check_sound_card() -> bool:
    """Checks the sound card status.

    Returns:
        bool: The sound card status.
    """
    # time.sleep(1) # FIXME: These sleep calls are here for TESTING purposes. They should be removed when the Uplink is implemented.
    # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file
    return bool(np.random.randint(0, 2))


def check_camera() -> bool:
    """Checks the camera status.

    Returns:
        bool: The camera status.
    """
    # time.sleep(2) # FIXME: These sleep calls are here for TESTING purposes. They should be removed when the Uplink is implemented.
    # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file
    return bool(np.random.randint(0, 2))


def check_heater() -> bool:
    """Checks the heater status.

    Returns:
        bool: The heater status.
    """
    # time.sleep(3) # FIXME: These sleep calls are here for TESTING purposes. They should be removed when the Uplink is implemented.
    # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file
    return bool(np.random.randint(0, 2))


def delete_data() -> bool:
    """Deletes the data from the db.

    Returns:
        bool: The status of the operation.
    """
    return bool(np.random.randint(0, 2))  # FIXME: This is a placeholder. It should be replaced with the actual value which will be read from the csv file
