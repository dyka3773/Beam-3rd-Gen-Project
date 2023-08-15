import aiosqlite
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s', 
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

accepted_signal_names = ['LO', 'SOE', 'SODS', 'PO']


async def add_motor_speed(cursor: aiosqlite.Cursor, motor_speed: int):
    """Adds the motor speed to the database by first checking if the motor speed exists in the last row.
    If it does, it updates the row with the new motor speed. If it doesn't, it inserts a new row with the new motor speed.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        motor_speed (int): The motor speed to be added to the database.
    """
    result = await cursor.execute("""
                                    SELECT motor_speed, time FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    result = await result.fetchone()
    if result is None:
        await cursor.execute("""
                                INSERT INTO rocket_data (motor_speed) VALUES (?)
                            """, (motor_speed,))
        logging.info(f'Added a new row with motor speed: {motor_speed}')
    else:
        prev_motor_speed, last_time = result
    
        if prev_motor_speed is not None:
            await cursor.execute("""
                                    INSERT INTO rocket_data (motor_speed) VALUES (?)
                                """, (motor_speed,))
            logging.info(f'Added a new row with motor speed: {motor_speed}')
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET motor_speed = ? WHERE time = ?
                                """, (motor_speed, last_time))
            logging.info(f"Updated the timestamp '{last_time}' with motor speed: {motor_speed}")

   
async def add_sound_card_status(cursor: aiosqlite.Cursor, sound_card_status: int):
    """Adds the sound card status to the database by first checking if the sound card status exists in the last row.
    If it does, it updates the row with the new sound card status. If it doesn't, it inserts a new row with the new sound card status.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        sound_card_status (int): The sound card status to be added to the database.
    """
    results = await cursor.execute("""
                                    SELECT sound_card_status, time FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    results = await results.fetchone()
    
    if results is None:
        await cursor.execute("""
                                INSERT INTO rocket_data (sound_card_status) VALUES (?)
                            """, (sound_card_status,))
        logging.info(f'Added a new row with sound card status: {sound_card_status}')
    else:
        prev_sound_card_status, last_time = results
        
        if prev_sound_card_status is not None:
            await cursor.execute("""
                                    INSERT INTO rocket_data (sound_card_status) VALUES (?)
                                """, (sound_card_status,))
            logging.info(f'Added a new row with sound card status: {sound_card_status}')
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET sound_card_status = ? WHERE time = ?
                                """, (sound_card_status, last_time))
            logging.info(f"Updated the timestamp '{last_time}' with sound card status: {sound_card_status}")
    

async def add_camera_status(cursor: aiosqlite.Cursor, camera_status: int):
    """Adds the camera status to the database by first checking if the camera status exists in the last row.
    If it does, it updates the row with the new camera status. If it doesn't, it inserts a new row with the new camera status.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        camera_status (int): The camera status to be added to the database.
    """
    results = await cursor.execute("""
                                    SELECT camera_status, time FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    results = await results.fetchone()
    
    if results is None:
        await cursor.execute("""
                                INSERT INTO rocket_data (camera_status) VALUES (?)
                            """, (camera_status,))
        logging.info(f'Added a new row with camera status: {camera_status}')
    else:
        prev_camera_status, last_time = results
        
        if prev_camera_status is not None:
            await cursor.execute("""
                                    INSERT INTO rocket_data (camera_status) VALUES (?)
                                """, (camera_status,))
            logging.info(f'Added a new row with camera status: {camera_status}')
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET camera_status = ? WHERE time = ?
                                """, (camera_status, last_time))
            logging.info(f"Updated the timestamp '{last_time}' with camera status: {camera_status}")


async def add_heater_status(cursor: aiosqlite.Cursor, heater_status: bool):
    """Adds the heater status to the database by first checking if the heater status exists in the last row.
    If it does, it updates the row with the new heater status. If it doesn't, it inserts a new row with the new heater status.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        heater_status (bool): The heater status to be added to the database.
    """
    results = await cursor.execute("""
                                    SELECT heater_status, time FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    results = await results.fetchone()
    
    if results is None:
        await cursor.execute("""
                                INSERT INTO rocket_data (heater_status) VALUES (?)
                            """, (heater_status,))
        logging.info(f'Added a new row with heater status: {heater_status}')
    else:
        prev_heater_status, last_time = results
        
        if prev_heater_status is not None:
            await cursor.execute("""
                                    INSERT INTO rocket_data (heater_status) VALUES (?)
                                """, (heater_status,))
            logging.info(f'Added a new row with heater status: {heater_status}')
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET heater_status = ? WHERE time = ?
                                """, (heater_status, last_time))
            logging.info(f"Updated the timestamp '{last_time}' with heater status: {heater_status}")
        

async def add_temp_to_sensor(cursor: aiosqlite.Cursor, temp: float, sensor_num: int):
    """Adds the temperature of a specified sensor to the database by first checking if the temperature of that sensor exists in the last row.
    If it does, it updates the row with the new temperature. If it doesn't, it inserts a new row with the new temperature.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        temp (float): The temperature of the sensor to be added to the database.
        sensor_num (int): The number of the sensor to be added to the database.
    """
    results = await cursor.execute("""
                                    SELECT temp_{}, time FROM rocket_data ORDER BY time DESC LIMIT 1
                                """.format(sensor_num))
    results = await results.fetchone()
    
    if results is None:
        await cursor.execute("""
                                INSERT INTO rocket_data (temp_{}) VALUES (?)
                            """.format(sensor_num), (temp,))
        logging.info(f'Added a new row with temperature of sensor {sensor_num}: {temp}')
    else:
        prev_temp, last_time = results
        
        if prev_temp is not None:
            await cursor.execute("""
                                    INSERT INTO rocket_data (temp_{}) VALUES (?)
                                """.format(sensor_num), (temp,))
            logging.info(f'Added a new row with temperature of sensor {sensor_num}: {temp}')
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET temp_{} = ? WHERE time = ?
                                """.format(sensor_num), (temp, last_time))
            logging.info(f"Updated the timestamp '{last_time}' with temperature of sensor {sensor_num}: {temp}")

        
async def add_pressure_to_sensor(cursor: aiosqlite.Cursor, pressure: float, sensor_num: int):
    """Adds the pressure of a specified sensor to the database by first checking if the pressure of that sensor exists in the last row.
    If it does, it updates the row with the new pressure. If it doesn't, it inserts a new row with the new pressure.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        pressure (float): The pressure of the sensor to be added to the database.
        sensor_num (int): The number of the sensor to be added to the database.
    """
    results = await cursor.execute("""
                                    SELECT pressure_{}, time FROM rocket_data ORDER BY time DESC LIMIT 1
                                """.format(sensor_num))
    results = await results.fetchone()
    
    if results is None:
        await cursor.execute("""
                                INSERT INTO rocket_data (pressure_{}) VALUES (?)
                            """.format(sensor_num), (pressure,))
        logging.info(f'Added a new row with pressure of sensor {sensor_num}: {pressure}')
    else:
        prev_pressure, last_time = results
        
        if prev_pressure is not None:
            await cursor.execute("""
                                    INSERT INTO rocket_data (pressure_{}) VALUES (?)
                                """.format(sensor_num), (pressure,))
            logging.info(f'Added a new row with pressure of sensor {sensor_num}: {pressure}')
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET pressure_{} = ? WHERE time = ?
                                """.format(sensor_num), (pressure, last_time))
            logging.info(f"Updated the timestamp '{last_time}' with pressure of sensor {sensor_num}: {pressure}")


async def add_signal_status(cursor: aiosqlite.Cursor, signal_status: bool, signal_name: str):
    """Adds the status of a specified signal to the database by first checking if the status of that signal exists in the last row.
    If it does, it updates the row with the new status. If it doesn't, it inserts a new row with the new status.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        signal_status (bool): The status of the signal to be added to the database.
        signal_name (str): The name of the signal to be added to the database. Accepted values: LO, SOE, SODS, PO
    """    
    if signal_name not in accepted_signal_names:
        raise ValueError(f'Invalid signal name. Accepted values: {accepted_signal_names}')
    
    results = await cursor.execute("""
                                    SELECT {}_signal, time FROM rocket_data ORDER BY time DESC LIMIT 1
                                """.format(signal_name))
    results = await results.fetchone()
    
    if results is None:
        await cursor.execute("""
                                INSERT INTO rocket_data ({}_signal) VALUES (?)
                            """.format(signal_name), (signal_status,))
        logging.info(f'Added a new row with {signal_name} signal status: {signal_status}')
    else:
        prev_signal_status, last_time = results
        
        if prev_signal_status is not None:
            await cursor.execute("""
                                    INSERT INTO rocket_data ({}_signal) VALUES (?)
                                """.format(signal_name), (signal_status,))
            logging.info(f'Added a new row with {signal_name} signal status: {signal_status}')
        else:
            await cursor.execute("""
                                    UPDATE rocket_data SET {}_signal = ? WHERE time = ?
                                """.format(signal_name), (signal_status, last_time))
            logging.info(f"Updated the timestamp '{last_time}' with {signal_name} signal status: {signal_status}")


async def add_error_code(cursor: aiosqlite.Cursor, error_code: int):
    """Adds the given error code to the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        error_code (int): The error code to be added to the database.
    """
    await cursor.execute("""
                            INSERT INTO rocket_data (error_code) VALUES (?)
                        """, (error_code,))
    logging.info(f'Added a new row with error code: {error_code}')
    
    
async def get_motor_speed(cursor: aiosqlite.Cursor) -> int | None:
    """Returns the motor speed from the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
    
    Returns:
        int: The motor speed from the database.
    """
    result = await cursor.execute("""
                                    SELECT motor_speed FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    result = await result.fetchone()
    speed = result[0] if result is not None else None
    return speed
    

async def get_sound_card_status(cursor: aiosqlite.Cursor) -> int | None:
    """Returns the sound card status from the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
    
    Returns:
        int: The sound card status from the database.
    """
    result = await cursor.execute("""
                                    SELECT sound_card_status FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    result = await result.fetchone()
    status = result[0] if result is not None else None
    return status
    

async def get_camera_status(cursor: aiosqlite.Cursor) -> int | None:
    """Returns the camera status from the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
    
    Returns:
        int: The camera status from the database.
    """
    result = await cursor.execute("""
                                    SELECT camera_status FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    result = await result.fetchone()
    status = result[0] if result is not None else None
    return status
    

async def get_heater_status(cursor: aiosqlite.Cursor) -> bool | None:
    """Returns the heater status from the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
    
    Returns:
        bool: The heater status from the database.
    """
    result = await cursor.execute("""
                                    SELECT heater_status FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    result = await result.fetchone()
    status = bool(result[0]) if result is not None else None
    return status
    

async def get_temp_of_sensor(cursor: aiosqlite.Cursor, sensor_num: int) -> float | None:
    """Returns the temperature of the specified sensor from the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        sensor_num (int): The number of the sensor to be added to the database.
    
    Returns:
        float: The temperature of the specified sensor from the database.
    """
    result = await cursor.execute("""
                                    SELECT temp_{} FROM rocket_data ORDER BY time DESC LIMIT 1
                                """.format(sensor_num))
    result = await result.fetchone()
    temp = result[0] if result is not None else None
    return temp
    

async def get_pressure_of_sensor(cursor: aiosqlite.Cursor, sensor_num: int) -> float | None:
    """Returns the pressure of the specified sensor from the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        sensor_num (int): The number of the sensor to be added to the database.
    
    Returns:
        float: The pressure of the specified sensor from the database.
    """
    result = await cursor.execute("""
                                    SELECT pressure_{} FROM rocket_data ORDER BY time DESC LIMIT 1
                                """.format(sensor_num))
    result = await result.fetchone()
    
    pressure = result[0] if result is not None else None
    return pressure
    

async def get_status_of_signal(cursor: aiosqlite.Cursor, signal_name: str) -> bool | None:
    """Returns the status of the specified signal from the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
        signal_name (str): The name of the signal to be added to the database. Accepted values: LO, SOE, SODS, PO
    
    Returns:
        bool: The status of the specified signal from the database.
    """
    
    if signal_name not in accepted_signal_names:
        raise ValueError(f'Invalid signal name. Accepted values: {accepted_signal_names}')
    
    result = await cursor.execute("""
                                    SELECT {}_signal FROM rocket_data ORDER BY time DESC LIMIT 1
                                """.format(signal_name))
    result = await result.fetchone()
    
    return bool(result[0]) if result is not None else None
    

async def get_error_code(cursor: aiosqlite.Cursor) -> int | None:
    """Returns the error code from the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
    
    Returns:
        int: The error code from the database.
    """
    result = await cursor.execute("""
                                    SELECT error_code FROM rocket_data ORDER BY time DESC LIMIT 1
                                """)
    result = await result.fetchone()
    error_code = result[0] if result is not None else None
    return error_code


async def get_first_row_of_all_data(cursor: aiosqlite.Cursor) -> aiosqlite.Row | None:
    """Returns the first row of all data from the database.
    
    Args:
        cursor (sqlite3.Cursor): The cursor of the database.
    
    Returns:
        tuple: The first row of all data from the database.
    """
    results = await cursor.execute("""
                                    SELECT * FROM rocket_data ORDER BY time ASC LIMIT 1
                                """)
    results = await results.fetchone()
    return results