import logging
from functools import cache
import serial
import sqlite3 as sql

from telecoms.telecom_util import coalesce_data, get_previous_row_values

port = "COM5"  # NOTE: This port may change depending on the computer


def receive_data():
    """Receives data from the serial port and saves it in a database.
    """
    logging.info("Creating database")
    create_db()

    logging.info("Starting receiver thread")
    connection = serial.Serial(port, baudrate=38400, timeout=0.33)

    data_has_been_received = False

    while True:
        try:
            data = connection.readline()
            if data:
                logging.info(f"Received data: {data}")
                try:
                    insert_data_in_db(deserialize_data(data))
                except Exception as e:
                    logging.error(f"Error in inserting data: {e}")

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
    deserialized_data = data.decode().split(',')

    def omit_none_values(x):
        return x if x != 'None' else None

    def omit_values_with_endline(x):
        if x is None:
            return x
        if x.endswith('\n'):
            return x[:-1]
        return x

    try:
        deserialized_data = map(omit_values_with_endline, deserialized_data)
        deserialized_data = map(omit_none_values, deserialized_data)
    except Exception as e:
        logging.error(f"Error in deserializing data: {e}")
        raise e

    return tuple(deserialized_data)


def insert_data_in_db(data: tuple):
    """Inserts the data into the database.

    Args:
        data (tuple): The data to be inserted into the database.
    """
    with sql.connect('GS_data.db', timeout=10) as db:
        cursor = db.cursor()
        try:
            previous_row = get_previous_row_values(cursor)
            coalesced_data = coalesce_data(data, previous_row)
        except Exception as e:
            logging.error(f"Error in coalescing data: {e}")
            raise e
        cursor.execute('''
            INSERT INTO GS_DATA (
                time,
                motor_speed,
                sound_card_status,
                camera_status,
                temp_1,
                temp_2,
                temp_3,
                LO_signal,
                SOE_signal,
                SODS_signal,
                error_code,
                led_status
            ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', coalesced_data)
        db.commit()
        logging.info(f'Inserted data: {coalesced_data} in the database')


def create_db():
    """Creates the database 
    """
    with sql.connect('GS_data.db', timeout=10) as db:
        cursor = db.cursor()
        cursor.executescript('''
                DROP TABLE IF EXISTS GS_DATA;
                
                -- TODO: Add contraints in the values of the columns where needed

                CREATE TABLE GS_DATA (
                    time DATETIME,
                    motor_speed INTEGER,        -- The speed of the motor. Possible values: 0 = OFF, 1 = ON
                    sound_card_status INTEGER,  -- The status of the sound card. Possible values: 0 = FINISHED, 1 = STANDBY, 2 = RECORDING, 3 = ERROR
                    camera_status INTEGER,      -- The status of the camera. Possible values: 0 = FINISHED, 1 = STANDBY, 2 = RECORDING, 3 = ERROR
                    temp_1 REAL,                -- The temperature of the first sensor in (Celsius?)
                    temp_2 REAL,                -- The temperature of the second sensor in (Celsius?)
                    temp_3 REAL,                -- The temperature of the sound card sensor in (Kelvin)
                    -- Add sensors here if needed
                    LO_signal BOOLEAN,          -- The status of the LO signal. Possible values: 0 = OFF, 1 = ON
                    SOE_signal BOOLEAN,         -- The status of the SOE signal. Possible values: 0 = OFF, 1 = ON
                    SODS_signal BOOLEAN,        -- The status of the SODS signal. Possible values: 0 = OFF, 1 = ON
                    error_code INTEGER,         -- The error code of the system in case of an error. Possible values: TBD
                    led_status INTEGER         -- The status of the LED. Possible values: 0 = OFF, 1 = ON
                );
            ''')
        db.commit()
        logging.info('Created table GS_data')
