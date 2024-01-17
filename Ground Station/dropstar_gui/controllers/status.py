import aiosqlite as sql
import logging

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
        try:
            speed = speed[0]  # type: ignore
        except TypeError:
            speed = -1

    return speed


async def get_sound_card_status() -> bool:
    """Gets the sound card status from the db.

    Returns:
        bool: The sound card status.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = await db.execute('SELECT sound_card_status FROM GS_data ORDER BY time DESC LIMIT 1')
        status = await result.fetchone()
        try:
            status = status[0]  # type: ignore
        except TypeError:
            status = False

    return status


async def get_camera_status() -> bool:
    """Gets the camera status from the db.

    Returns:
        bool: The camera status.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = await db.execute('SELECT camera_status FROM GS_data ORDER BY time DESC LIMIT 1')
        status = await result.fetchone()
        try:
            status = status[0]  # type: ignore
        except TypeError:
            status = False

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
        elif sensor == 'sensor3':
            col = 'temp_3'
        else:
            raise ValueError('Invalid sensor name')

        results = await db.execute(f'''SELECT {col}
                                        FROM GS_data
                                        WHERE time >= DATETIME('now', '-{time} seconds')
                                        ORDER BY time DESC
                                ''')
        temperature = await results.fetchall()

    temp_list = [x for (x,) in temperature]
    temp_list.reverse()

    logging.debug(f'Got temperature: {temp_list}')

    if len(temp_list) == 0:
        temp_list = [-1]

    return temp_list


async def get_LO_signal() -> bool:
    """Gets the LO signal status from the db.

    Returns:
        bool: The LO signal status.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = db.execute(
            'SELECT LO_signal FROM GS_data ORDER BY time DESC LIMIT 1')
        status = await result
        status = await status.fetchone()
        try:
            status = status[0]  # type: ignore
        except TypeError:
            status = False

    return status


async def get_SOE_signal() -> bool:
    """Gets the SOE signal status from the db.

    Returns:
        bool: The SOE signal status.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = db.execute(
            'SELECT SOE_signal FROM GS_data ORDER BY time DESC LIMIT 1')
        status = await result
        status = await status.fetchone()
        try:
            status = status[0]  # type: ignore
        except TypeError:
            status = False

    return status


async def get_SODS_signal() -> bool:
    """Gets the SODS signal status from the db.

    Returns:
        bool: The SODS signal status.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = db.execute(
            'SELECT SODS_signal FROM GS_data ORDER BY time DESC LIMIT 1')
        status = await result
        status = await status.fetchone()
        try:
            status = status[0]  # type: ignore
        except TypeError:
            status = False

    return status


async def get_errors() -> int | None:
    """Gets the error code from the db.

    Returns:
        int: The error code.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = db.execute(
            'SELECT error_code FROM GS_data ORDER BY time DESC LIMIT 1')
        error_code = await result
        error_code = await error_code.fetchone()
        try:
            error_code = error_code[0]  # type: ignore
        except TypeError:
            error_code = None

    return error_code


async def get_led_status() -> int | None:
    """Gets the led status from the db.

    Returns:
        int: The led status.
    """
    async with sql.connect('file:GS_data.db?mode=ro', timeout=10, isolation_level=None, uri=True) as db:
        result = db.execute(
            'SELECT led_status FROM GS_data ORDER BY time DESC LIMIT 1')
        status = await result
        status = await status.fetchone()
        try:
            status = status[0]  # type: ignore
        except TypeError:
            status = None

    return status
