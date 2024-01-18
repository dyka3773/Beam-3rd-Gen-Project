import aiosqlite as sql
import logging
import datetime

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


async def get_temperature(sensor: str, time: int) -> tuple[list[int], list[float]]:
    """Gets the temperature from the db.

    Args:
        sensor (str): The sensor from which the temperature will be read.
        time (int): The time for which the temperature will be read.

    Returns:
        tuple[list[float], list[float]]: A list of tuples containing the time and temperature.
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

        # This query gets the last 180 temperature readings which we assume is about 1 minute of data because we have 3.3 Hz sampling rate
        results = await db.execute(f'''SELECT time, {col}
                                        FROM GS_data
                                        WHERE {col} IS NOT NULL
                                        ORDER BY time DESC
                                        LIMIT 180
                                ''')
        time_to_temperature = await results.fetchall()  # This is a list of tuples

    # I need to convert the list of tuples into a tuple of lists
    # I think this is returning a tuple of tuples instead of a tuple of lists but I'm not sure
    temp_tuple = tuple(zip(*time_to_temperature))
    if len(temp_tuple) == 0:
        return ([], [])

    temp_tuple = (list(temp_tuple[0]), list(temp_tuple[1]))

    # I need to reverse the lists so that the time is in ascending order
    temp_tuple[0].reverse()
    temp_tuple[1].reverse()

    returned_times = []
    returned_temps = []

    for time_before_format, temp in zip(temp_tuple[0], temp_tuple[1]):
        formated_time = datetime.datetime.strptime(
            time_before_format, '%Y-%m-%d %H:%M:%S.%f')
        returned_times.append(formated_time)
        returned_temps.append(temp)

    temp_tuple = (returned_times, returned_temps)

    logging.debug(f'Got times: {temp_tuple[0]}')
    logging.debug(f'Got temperatures: {temp_tuple[1]}')
    return temp_tuple  # type: ignore


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
