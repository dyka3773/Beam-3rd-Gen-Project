import numpy as np
import time
import logging
import sqlite3 as sql

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_motor_speed() -> int:
    return np.random.randint(0,255)

def get_sound_card_status() -> bool:
    return bool(np.random.randint(0,2))

def get_camera_status() -> bool:
    return bool(np.random.randint(0,2))

def get_heater_status() -> bool:
    return bool(np.random.randint(0,2))

def get_temperature() -> int:    
    return np.random.randint(-50,100)

def get_pressure() -> float:
    return np.random.randint(8,32)/16

def generate_db():
    
    time_passed = 0

    interval = 1/3 # 3Hz
        
    with sql.connect('GS_data.db', timeout=10) as db:
        cursor = db.cursor()
        cursor.executescript('''
            DROP TABLE IF EXISTS GS_data;
            
            CREATE TABLE IF NOT EXISTS GS_data (
                time DATETIME DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
                motor_speed INTEGER,
                sound_card_status BOOLEAN,
                camera_status BOOLEAN,
                heater_status BOOLEAN,
                temp_1 REAL,
                pressure_1 REAL,
                temp_2 REAL,
                pressure_2 REAL,
                PRIMARY KEY (time)
            );
        ''')
        db.commit()
        logging.info('Created table GS_data')
        
        while time_passed < 600:
            cursor.executemany('''
                INSERT INTO GS_data (MOTOR_SPEED, SOUND_CARD_STATUS, CAMERA_STATUS, HEATER_STATUS, TEMP_1, PRESSURE_1, TEMP_2, PRESSURE_2)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);''', [(
                    get_motor_speed(),
                    get_sound_card_status(),
                    get_camera_status(),
                    get_heater_status(),
                    get_temperature(),
                    get_pressure(),
                    get_temperature(),
                    get_pressure()
                )]
            )
            db.commit()
            logging.info('Inserted row')
            
            time.sleep(interval)
            time_passed += interval


if __name__ == '__main__':
    generate_db()