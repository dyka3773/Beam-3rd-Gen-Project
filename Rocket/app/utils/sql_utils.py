from typing import Iterable
import aiosqlite
from aiosqlite import Row
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

accepted_signal_names = ['LO', 'SOE', 'SODS']


async def add_motor_speed(cursor: aiosqlite.Cursor, motor_speed: int):
    """Adds the motor speed to the database by first checking when the motor speed has been added in the last second.
    If it hasn't been added in the last second, it inserts a new row with the new motor speed. If it has been added in the last second,
    it updates the earliest row with the new motor speed.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.
        motor_speed (int): The motor speed to be added to the database.
    """
    results = await cursor.execute("""
                                    SELECT motor_speed, time 
                                    FROM rocket_data 
                                    WHERE strftime('%s', time) = strftime('%s', 'now')
                                    ORDER BY time DESC
                                """)

    results = await results.fetchall()

    if not results:
        await cursor.execute("""
                                INSERT INTO rocket_data (motor_speed) VALUES (?)
                            """, (motor_speed,))
        logging.debug(f'Added a new row with motor speed: {motor_speed}')
    else:

        # This variable will declare the earliest time in which the motor speed was None.
        earliest_time = None

        for row in results:
            prev_motor_speed, last_time = row

            if prev_motor_speed is not None:
                if earliest_time is not None:
                    await cursor.execute(""" 
                                            UPDATE rocket_data SET motor_speed = ? WHERE time = ?
                                        """, (motor_speed, earliest_time))
                    logging.debug(
                        f"Updated the timestamp '{earliest_time}' with motor speed: {motor_speed}")
                    break
                await cursor.execute("""
                                        INSERT INTO rocket_data (motor_speed) VALUES (?)
                                    """, (motor_speed,))
                logging.debug(
                    f'Added a new row with motor speed: {motor_speed}')
                break
            else:
                earliest_time = last_time
                continue
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET motor_speed = ? WHERE time = ?
                                """, (motor_speed, earliest_time))
            logging.debug(
                f"Updated the timestamp '{earliest_time}' with motor speed: {motor_speed}")


async def add_sound_card_status(cursor: aiosqlite.Cursor, sound_card_status: int):
    """Adds the sound card status to the database by first checking when the sound card status has been added in the last second.
    If it hasn't been added in the last second, it inserts a new row with the new sound card status. If it has been added in the last second,
    it updates the earliest row with the new sound card status.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.
        sound_card_status (int): The sound card status to be added to the database.
    """
    results = await cursor.execute("""
                                    SELECT sound_card_status, time 
                                    FROM rocket_data
                                    WHERE strftime('%s', time) = strftime('%s', 'now')
                                    ORDER BY time DESC
                                """)

    results = await results.fetchall()

    if not results:
        await cursor.execute("""
                                INSERT INTO rocket_data (sound_card_status) VALUES (?)
                            """, (sound_card_status,))
        logging.debug(
            f'Added a new row with sound card status: {sound_card_status}')
    else:

        # This variable will declare the earliest time in which the sound card status was None.
        earliest_time = None

        for row in results:
            prev_sound_card_status, last_time = row

            if prev_sound_card_status is not None:
                if earliest_time is not None:
                    await cursor.execute(""" 
                                            UPDATE rocket_data SET sound_card_status = ? WHERE time = ?
                                        """, (sound_card_status, earliest_time))
                    logging.debug(
                        f"Updated the timestamp '{earliest_time}' with sound card status: {sound_card_status}")
                    break
                await cursor.execute("""
                                        INSERT INTO rocket_data (sound_card_status) VALUES (?)
                                    """, (sound_card_status,))
                logging.debug(
                    f'Added a new row with sound card status: {sound_card_status}')
                break
            else:
                earliest_time = last_time
                continue
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET sound_card_status = ? WHERE time = ?
                                """, (sound_card_status, earliest_time))
            logging.debug(
                f"Updated the timestamp '{earliest_time}' with sound card status: {sound_card_status}")


async def add_camera_status(cursor: aiosqlite.Cursor, camera_status: int):
    """Adds the camera status to the database by first checking when the camera status has been added in the last second.
    If it hasn't been added in the last second, it inserts a new row with the new camera status. If it has been added in the last second,
    it updates the earliest row with the new camera status.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.
        camera_status (int): The camera status to be added to the database.
    """
    results = await cursor.execute("""
                                    SELECT camera_status, time 
                                    FROM rocket_data
                                    WHERE strftime('%s', time) = strftime('%s', 'now')
                                    ORDER BY time DESC
                                """)

    results = await results.fetchall()

    if not results:
        await cursor.execute("""
                                INSERT INTO rocket_data (camera_status) VALUES (?)
                            """, (camera_status,))
        logging.debug(f'Added a new row with camera status: {camera_status}')
    else:

        # This variable will declare the earliest time in which the camera status was None.
        earliest_time = None

        for row in results:
            prev_camera_status, last_time = row

            if prev_camera_status is not None:
                if earliest_time is not None:
                    await cursor.execute(""" 
                                            UPDATE rocket_data SET camera_status = ? WHERE time = ?
                                        """, (camera_status, earliest_time))
                    logging.debug(
                        f"Updated the timestamp '{earliest_time}' with camera status: {camera_status}")
                    break
                await cursor.execute("""
                                        INSERT INTO rocket_data (camera_status) VALUES (?)
                                    """, (camera_status,))
                logging.debug(
                    f'Added a new row with camera status: {camera_status}')
                break
            else:
                earliest_time = last_time
                continue
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET camera_status = ? WHERE time = ?
                                """, (camera_status, earliest_time))
            logging.debug(
                f"Updated the timestamp '{earliest_time}' with camera status: {camera_status}")


async def add_temp_to_sensor(cursor: aiosqlite.Cursor, temp: float, sensor_num: int):
    """Adds the temperature of a specified sensor to the database by first checking when the temperature of that sensor has been added in the last second.
    If it hasn't been added in the last second, it inserts a new row with the new temperature. If it has been added in the last second,
    it updates the earliest row with the new temperature.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.
        temp (float): The temperature of the sensor to be added to the database.
        sensor_num (int): The number of the sensor to be added to the database.
    """
    results = await cursor.execute("""
                                    SELECT temp_{}, time 
                                    FROM rocket_data 
                                    WHERE strftime('%s', time) = strftime('%s', 'now')
                                    ORDER BY time DESC
                                """.format(sensor_num))
    results = await results.fetchall()

    if not results:
        await cursor.execute("""
                                INSERT INTO rocket_data (temp_{}) VALUES (?)
                            """.format(sensor_num), (temp,))
        logging.debug(
            f'Added a new row with temperature of sensor {sensor_num}: {temp}')
    else:

        # This variable will declare the earliest time in which the temperature of the sensor was None.
        earliest_time = None

        for row in results:
            prev_temp, last_time = row

            if prev_temp is not None:
                if earliest_time is not None:
                    await cursor.execute(""" 
                                            UPDATE rocket_data SET temp_{} = ? WHERE time = ?
                                        """.format(sensor_num), (temp, earliest_time))
                    logging.debug(
                        f"Updated the timestamp '{earliest_time}' with temperature of sensor {sensor_num}: {temp}")
                    break
                await cursor.execute("""
                                        INSERT INTO rocket_data (temp_{}) VALUES (?)
                                    """.format(sensor_num), (temp,))
                logging.debug(
                    f'Added a new row with temperature of sensor {sensor_num}: {temp}')
                break
            else:
                earliest_time = last_time
                continue
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET temp_{} = ? WHERE time = ?
                                """.format(sensor_num), (temp, earliest_time))
            logging.debug(
                f"Updated the timestamp '{earliest_time}' with temperature of sensor {sensor_num}: {temp}")


async def add_signal_status(cursor: aiosqlite.Cursor, signal_status: bool, signal_name: str):
    """Adds the status of a specified signal to the database by first checking when the status of that signal has been added in the last second.
    If it hasn't been added in the last second, it inserts a new row with the new signal status. If it has been added in the last second,
    it updates the earliest row with the new signal status.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.
        signal_status (bool): The status of the signal to be added to the database.
        signal_name (str): The name of the signal to be added to the database. Accepted values: LO, SOE, SODS, PO
    """
    if signal_name not in accepted_signal_names:
        raise ValueError(
            f'Invalid signal name. Accepted values: {accepted_signal_names}')

    results = await cursor.execute("""
                                    SELECT {}_signal, time 
                                    FROM rocket_data 
                                    WHERE strftime('%s', time) = strftime('%s', 'now')
                                    ORDER BY time DESC
                                """.format(signal_name))
    results = await results.fetchall()

    if not results:
        await cursor.execute("""
                                INSERT INTO rocket_data ({}_signal) VALUES (?)
                            """.format(signal_name), (signal_status,))
        logging.debug(
            f'Added a new row with {signal_name} signal status: {signal_status}')
    else:

        # This variable will declare the earliest time in which the signal status was None.
        earliest_time = None

        for row in results:
            prev_signal_status, last_time = row

            if prev_signal_status is not None:
                if earliest_time is not None:
                    await cursor.execute(""" 
                                            UPDATE rocket_data SET {}_signal = ? WHERE time = ?
                                        """.format(signal_name), (signal_status, earliest_time))
                    logging.debug(
                        f"Updated the timestamp '{earliest_time}' with {signal_name} signal status: {signal_status}")
                    break
                await cursor.execute("""
                                        INSERT INTO rocket_data ({}_signal) VALUES (?)
                                    """.format(signal_name), (signal_status,))
                logging.debug(
                    f'Added a new row with {signal_name} signal status: {signal_status}')
                break
            else:
                earliest_time = last_time
                continue
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET {}_signal = ? WHERE time = ?
                                """.format(signal_name), (signal_status, earliest_time))
            logging.debug(
                f"Updated the timestamp '{earliest_time}' with {signal_name} signal status: {signal_status}")


async def add_error_code(cursor: aiosqlite.Cursor, error_code: int):
    """Adds the given error code to the database.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.
        error_code (int): The error code to be added to the database.
    """
    await cursor.execute("""
                            INSERT INTO rocket_data (error_code) VALUES (?)
                        """, (error_code,))
    logging.debug(f'Added a new row with error code: {error_code}')


async def add_led_status(cursor: aiosqlite.Cursor, led_status: int):
    """Adds the status of the LED to the database.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.
        led_status (int): The status of the LED. Possible values: 0 = OFF, 1 = ON
    """
    results = await cursor.execute("""
                                    SELECT led_status, time
                                    FROM rocket_data
                                    WHERE strftime('%s', time) = strftime('%s', 'now')
                                    ORDER BY time DESC
                                """)
    results = await results.fetchall()

    if not results:
        await cursor.execute("""
                                INSERT INTO rocket_data (led_status) VALUES (?)
                            """, (led_status,))
        logging.debug(f'Added a new row with LED status: {led_status}')
    else:

        # This variable will declare the earliest time in which the LED status was None.
        earliest_time = None

        for row in results:
            prev_led_status, last_time = row

            if prev_led_status is not None:
                if earliest_time is not None:
                    await cursor.execute(""" 
                                                UPDATE rocket_data SET led_status = ? WHERE time = ?
                                            """, (led_status, earliest_time))
                    logging.debug(
                        f"Updated the timestamp '{earliest_time}' with LED status: {led_status}")
                    break
                await cursor.execute("""
                                            INSERT INTO rocket_data (led_status) VALUES (?)
                                        """, (led_status,))
                logging.debug(f'Added a new row with LED status: {led_status}')
                break
            else:
                earliest_time = last_time
                continue
        else:
            await cursor.execute("""
                                        UPDATE rocket_data SET led_status = ? WHERE time = ?
                                    """, (led_status, earliest_time))
            logging.debug(
                f"Updated the timestamp '{earliest_time}' with LED status: {led_status}")


async def get_motor_speed(cursor: aiosqlite.Cursor) -> int | None:
    """Returns the motor speed from the database.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.

    Returns:
        int: The motor speed from the database.
    """
    results = await cursor.execute("""
                                    SELECT motor_speed FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    results = await results.fetchone()
    speed = results[0] if results is not None else None
    return speed


async def get_sound_card_status(cursor: aiosqlite.Cursor) -> int | None:
    """Returns the sound card status from the database.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.

    Returns:
        int: The sound card status from the database.
    """
    results = await cursor.execute("""
                                    SELECT sound_card_status FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    results = await results.fetchone()
    status = results[0] if results is not None else None
    return status


async def get_error_code(cursor: aiosqlite.Cursor) -> int | None:
    """Returns the error code from the database.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.

    Returns:
        int: The error code from the database.
    """
    results = await cursor.execute("""
                                    SELECT error_code FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    results = await results.fetchone()
    error_code = results[0] if results is not None else None
    return error_code


async def get_last_row_of_all_data(cursor: aiosqlite.Cursor) -> aiosqlite.Row | None:
    """Returns the last row of all data from the database.

    Args:
        cursor (aiosqlite.Cursor): The cursor of the database.

    Returns:
        tuple: The last row of all data from the database.
    """
    results = await cursor.execute("""
                                    SELECT * FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    results = await results.fetchone()
    return results
