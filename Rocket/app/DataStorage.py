import logging
import sqlite3 as sql
from sql import sql_utils as sqlu

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s', 
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

class DataStorage:
    """A class to store data in a database.
    
    NOTE: It follows the singleton design pattern so that only one instance of the class can be created.
    """
    
    _instance = None
    
    db_filename : str = 'rocket.db'
    
    def __new__(cls, *args, **kwargs):
        """This function is called before __init__ and is used to create a singleton class.
        
        NOTE: It also initializes the database if the class hasn't been instantiated before.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._create_db() # Create the database if it doesn't exist
        return cls._instance

    def _create_db(self):
        """Creates the database 
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            db.executescript('''
                    DROP TABLE IF EXISTS ROCKET_DATA;

                    -- TODO: Add contraints in the values of the columns where needed

                    CREATE TABLE ROCKET_DATA (
                        time DATETIME DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
                        motor_speed INTEGER,        -- The speed of the motor in (rpm?)
                        sound_card_status INTEGER,  -- The status of the sound card. Possible values: 0 = OFF, 1 = ON, 2 = RECORDING, 3 = ERROR
                        camera_status INTEGER,      -- The status of the camera. Possible values: 0 = OFF, 1 = ON, 2 = RECORDING, 3 = ERROR
                        heater_status BOOLEAN,      -- The status of the heater. Possible values: 0 = OFF, 1 = ON
                        temp_1 REAL,                -- The temperature of the first sensor in (Celsius?)
                        temp_2 REAL,                -- The temperature of the second sensor in (Celsius?)
                        -- Add sensors here if needed
                        pressure_1 REAL,            -- The pressure of the first sensor in (atm?)
                        pressure_2 REAL,            -- The pressure of the second sensor in (atm?)
                        -- Add sensors here if needed
                        LO_signal BOOLEAN,          -- The status of the LO signal. Possible values: 0 = OFF, 1 = ON
                        SOE_signal BOOLEAN,         -- The status of the SOE signal. Possible values: 0 = OFF, 1 = ON
                        SODS_signal BOOLEAN,        -- The status of the SODS signal. Possible values: 0 = OFF, 1 = ON
                        PO_signal BOOLEAN,          -- The status of the PO signal. Possible values: 0 = OFF, 1 = ON. (It should always be 1)
                        error_code INTEGER,         -- The error code of the system in case of an error. Possible values: TBD
                        PRIMARY KEY (time)
                    );
                ''')
            
            db.commit()
            
            logging.info('Created table ROCKET_DATA')
            
    def save_motor_speed(self, motor_speed: int):
        """Adds the speed of the motor to the database.
        
        Args:
            motor_speed (int): The speed of the motor in (rpm?)
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            sqlu.add_motor_speed(cursor, motor_speed)
            db.commit()
            
    def save_sound_card_status(self, sound_card_status: int):
        """Adds the status of the sound card to the database.
        
        Args:
            sound_card_status (int): The status of the sound card. Possible values: 0 = OFF, 1 = ON, 2 = RECORDING, 3 = ERROR
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            sqlu.add_sound_card_status(cursor, sound_card_status)
            db.commit()
            
    def save_camera_status(self, camera_status: int):
        """Adds the status of the camera to the database.
        
        Args:
            camera_status (int): The status of the camera. Possible values: 0 = OFF, 1 = ON, 2 = RECORDING, 3 = ERROR
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            sqlu.add_camera_status(cursor, camera_status)
            db.commit()
    
    def save_heater_status(self, heater_status: bool):
        """Adds the status of the heater to the database.
        
        Args:
            heater_status (bool): The status of the heater. Possible values: 0 = OFF, 1 = ON
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            sqlu.add_heater_status(cursor, heater_status)
            db.commit()
    
    def save_temperature_of_sensor(self, temp: float, sensor_num: int):
        """Adds the temperature of a specified sensor to the database.
        
        Args:
            temp (float): The temperature of the sensor to be added to the database.
            sensor_num (int): The number of the sensor to be added to the database.
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            sqlu.add_temp_to_sensor(cursor, temp, sensor_num)
            db.commit()
            
    def save_pressure_of_sensor(self, pressure: float, sensor_num: int):
        """Adds the pressure of a specified sensor to the database.
        
        Args:
            pressure (float): The pressure of the sensor to be added to the database.
            sensor_num (int): The number of the sensor to be added to the database.
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            sqlu.add_pressure_to_sensor(cursor, pressure, sensor_num)
            db.commit()
            
    def save_status_of_signal(self, status: bool, signal_name: str):
        """Adds the status of a specified signal to the database.
        
        Args:
            status (bool): The status of the signal to be added to the database.
            signal_name (str): The name of the signal to be added to the database.
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            sqlu.add_signal_status(cursor, status, signal_name)
            db.commit()
            
    def save_error_code(self, error_code: int):
        """Adds the error code of the system to the database.
        
        Args:
            error_code (int): The error code of the system to be added to the database.
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            sqlu.add_error_code(cursor, error_code)
            db.commit()
            
    def get_motor_speed(self):
        """Gets the speed of the motor from the database.
        
        Returns:
            int: The speed of the motor in (rpm?)
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            speed = sqlu.get_motor_speed(cursor)
            db.commit()
        
        return speed
    
    def get_sound_card_status(self):
        """Gets the status of the sound card from the database.
        
        Returns:
            int: The status of the sound card. Possible values: 0 = OFF, 1 = ON, 2 = RECORDING, 3 = ERROR
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            status = sqlu.get_sound_card_status(cursor)
            db.commit()
        
        return status
    
    def get_camera_status(self):
        """Gets the status of the camera from the database.
        
        Returns:
            int: The status of the camera. Possible values: 0 = OFF, 1 = ON, 2 = RECORDING, 3 = ERROR
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            status = sqlu.get_camera_status(cursor)
            db.commit()
        
        return status
    
    def get_heater_status(self):
        """Gets the status of the heater from the database.
        
        Returns:
            bool: The status of the heater. Possible values: 0 = OFF, 1 = ON
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            status = sqlu.get_heater_status(cursor)
            db.commit()
        
        return status
    
    def get_temperature_of_sensor(self, sensor_num: int):
        """Gets the temperature of a specified sensor from the database.
        
        Args:
            sensor_num (int): The number of the sensor to get the temperature from.
        
        Returns:
            float: The temperature of the specified sensor.
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            temp = sqlu.get_temp_of_sensor(cursor, sensor_num)
            db.commit()
        
        return temp
    
    def get_pressure_of_sensor(self, sensor_num: int):
        """Gets the pressure of a specified sensor from the database.
        
        Args:
            sensor_num (int): The number of the sensor to get the pressure from.
        
        Returns:
            float: The pressure of the specified sensor.
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            pressure = sqlu.get_pressure_of_sensor(cursor, sensor_num)
            db.commit()
        
        return pressure
    
    def get_status_of_signal(self, signal_name: str):
        """Gets the status of a specified signal from the database.
        
        Args:
            signal_name (str): The name of the signal to get the status from.
        
        Returns:
            bool: The status of the specified signal.
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            status = sqlu.get_status_of_signal(cursor, signal_name)
            db.commit()
        
        return status
    
    def get_error_code(self):
        """Gets the error code of the system from the database.
        
        Returns:
            int: The error code of the system.
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            error_code = sqlu.get_error_code(cursor)
            db.commit()
        
        return error_code
    
    def get_first_row_of_all_data(self):
        """Gets the first row of all the data from the database.
        
        Returns:
            tuple: The first row of all the data from the database.
        """
        with sql.connect(self.db_filename, timeout=10) as db:
            cursor = db.cursor()
            data = sqlu.get_first_row_of_all_data(cursor)
            db.commit()
        
        return data        