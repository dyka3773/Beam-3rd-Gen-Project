import csv
import numpy as np
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_motor_speed() -> int:
    return np.random.randint(0,255)

def get_sound_card_status() -> bool:
    return bool(np.random.randint(0,2))

def get_camera_status() -> bool:
    return bool(np.random.randint(0,2))

def get_heater_status() -> bool:
    return bool(np.random.randint(0,2))

def get_temperature() -> list:    
    return np.random.randint(-50,100)

def get_pressure() -> list:
    return np.random.randint(8,32)/16


def generate_data():
    cols =[
        'time', 
        'motor_speed', 
        'sound_card_status', 
        'camera_status', 
        'heater_status', 
        'temp_1', 
        'pressure_1', 
        'temp_2', 
        'pressure_2'
    ]
    
    time_passed = 0
    interval = 1/3 # 3Hz
    
    with open('GS_data.csv', 'w', newline='') as csvfile:
        
        writer = csv.DictWriter(csvfile, fieldnames=cols)
        
        writer.writeheader()
        logging.info(f'Wrote header: {cols}')
        
        while time_passed < 600:
            row = {
                'time': time_passed,
                'motor_speed': get_motor_speed(),
                'sound_card_status': get_sound_card_status(),
                'camera_status': get_camera_status(),
                'heater_status': get_heater_status(),
                'temp_1': get_temperature(),
                'pressure_1': get_pressure(),
                'temp_2': get_temperature(),
                'pressure_2': get_pressure()
            }
            
            writer.writerow(row)
            logging.info(f'Wrote row: {row}')
            
            time.sleep(interval)
            
            time_passed += interval


if __name__ == '__main__':
    generate_data()