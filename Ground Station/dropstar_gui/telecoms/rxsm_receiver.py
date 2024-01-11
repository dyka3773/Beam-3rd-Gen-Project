import logging
from functools import cache
import serial
import sqlite3 as sql

port = "COM6"  # NOTE: This port may change depending on the computer


def receive_data():
    """Receives data from the serial port and saves it in a database.
    """
    logging.info("Creating database")
    create_db()

    logging.info("Starting receiver thread")
    connection = serial.Serial(port, baudrate=38400, timeout=0.33)

    data_has_been_received = False

    try:
        while True:
            data = connection.readline()
            if data:
                logging.info(f"Received data: {data}")
                insert_data_in_db(deserialize_data(data))

                data_has_been_received = True
            else:
                if not data_has_been_received:
                    logging.warning(
                        "No data received. Experiment is probably still off or there is something wrong in the connection...")
                logging.debug("No data received")
    except Exception as e:
        logging.error(f"Error in receiving data: {e}")


@cache
def deserialize_data(data: bytes) -> tuple:
    """Deserializes the data received from the serial port.

    Args:
        data (bytes): The data received from the serial port.

    Returns:
        tuple: The deserialized data.
    """
    return tuple(data.decode().split(','))


def insert_data_in_db(data: tuple):
    """Inserts the data into the database.

    Args:
        data (tuple): The data to be inserted into the database.
    """
    with sql.connect('GS_data.db', timeout=10) as db:
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO GS_DATA (
                motor_speed,
                sound_card_status,
                camera_status,
                temp_1,
                temp_2,
                temp_3,
                LO_signal,
                SOE_signal,
                SODS_signal,
                error_code
            ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        db.commit()
        logging.info(f'Inserted data: {data} in the database')


def create_db():
    """Creates the database 
    """
    with sql.connect('GS_data.db', timeout=10) as db:
        cursor = db.cursor()
        cursor.executescript('''
                DROP TABLE IF EXISTS GS_DATA;
                
                -- TODO: Add contraints in the values of the columns where needed

                CREATE TABLE GS_DATA (
                    time DATETIME DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
                    motor_speed INTEGER,        -- The speed of the motor in (rpm?)
                    sound_card_status INTEGER,  -- The status of the sound card. Possible values: 0 = OFF, 1 = ON, 2 = RECORDING, 3 = ERROR
                    camera_status INTEGER,      -- The status of the camera. Possible values: 0 = OFF, 1 = ON, 2 = RECORDING, 3 = ERROR
                    temp_1 REAL,                -- The temperature of the first sensor in (Celsius?)
                    temp_2 REAL,                -- The temperature of the second sensor in (Celsius?)
                    temp_3 REAL,                -- The temperature of the sound card sensor in (Kelvin)
                    -- Add sensors here if needed
                    LO_signal BOOLEAN,          -- The status of the LO signal. Possible values: 0 = OFF, 1 = ON
                    SOE_signal BOOLEAN,         -- The status of the SOE signal. Possible values: 0 = OFF, 1 = ON
                    SODS_signal BOOLEAN,        -- The status of the SODS signal. Possible values: 0 = OFF, 1 = ON
                    error_code INTEGER,         -- The error code of the system in case of an error. Possible values: TBD
                    PRIMARY KEY (time)
                );
            ''')
        db.commit()
        logging.info('Created table GS_data')
