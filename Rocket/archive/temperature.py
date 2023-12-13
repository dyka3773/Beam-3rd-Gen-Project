import math as mt


def calculate_temperature_reading(voltage_in: float):
    V_t = 5  # Vcc (power supply) voltage from LabJack

    R_k = 10000  # Thermistor's resistance

    # B = 3984  # Beta value

    R_0 = 10000  # Resistance next to the thermistor in ohms

    # These are the ones that need to be calibrated
    A = 1.137946915e-3
    C = 2.326894292e-4
    B = 0.9333051145e-7

    # Steinhart Constants
    A = 0.001129148
    B = 0.000234125
    C = 0.0000000876741

    Vout = voltage_in
    # Calculate Resistance
    Rt = (Vout * R_0) / (V_t - Vout)
    # Rt = 10000 # Used for Testing. Setting Rt=10k should give TempC=25
    # Steinhart - Hart Equation
    TempK = 1 / (A + (B * mt.log(Rt)) + C * mt.pow(mt.log(Rt), 3))
    # Convert from Kelvin to Celsius
    TempC = TempK - 273.15

    return TempC


print(f"This should be around 33.5: {calculate_temperature_reading(2.96)}")
print(calculate_temperature_reading(2.31))
print(calculate_temperature_reading(2.99))
