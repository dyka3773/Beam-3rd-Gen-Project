import pandas as pd

import sys

name_list = [
    "time",
    "Thermal_Sensor_1",
    "Thermal_Sensor_2", 
    "Thermal_Sensor_3", 
    "Pressure_Sensor_1", 
    "Pressure_Sensor_2", 
    "Pressure_Sensor_3", 
    "Motor_Status", 
    "Heater_Status", 
    "Sound_Card_Status", 
    "Camera_Status", 
    "Error"
]
data_list = [
    0,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b00000000, 
    True, 
    True, 
    0b00000000, 
    0b00000000, 
]

list = []
float_list = []
boolean_list = []
byte_list = []

for i in range(3*60*9):
    list.append(data_list)
    float_list.append(data_list[1])
    boolean_list.append(data_list[8])
    byte_list.append(data_list[7])



df = pd.DataFrame(list, columns=name_list)
df.to_csv("Mock_Collective_CSV.csv")




for i in name_list:
    if i == "time":
        continue
    elif i == "Thermal_Sensor_1" or i == "Thermal_Sensor_2" or i == "Thermal_Sensor_3" or i == "Pressure_Sensor_1" or i == "Pressure_Sensor_2" or i == "Pressure_Sensor_3":
        s = pd.Series(float_list, name=i)
    elif i == "Motor_Status" or i == "Camera_Status" or i == "Error":
        s = pd.Series(byte_list, name=i)
    else :
        s = pd.Series(boolean_list, name=i)

    s.to_csv(f"Mock_{i}_CSV.csv", index=False)