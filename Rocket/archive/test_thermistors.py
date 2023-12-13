import time
import u3

SCAN_FREQUENCY = 48000  # Hz


def calibrate_temperature_reading(voltage_in: float):
    V_t = 5  # Vcc (power supply) voltage from LabJack

    R_k = 10000  # Thermistor's resistance

    T_0 = 298.15  # Room temperature in Kelvin

    B = 3984  # Beta value

    R_0 = 1000  # Resistance next to the thermistor in ohms

    R_measured = (voltage_in/V_t)*R_k  # Calculated resistance of thermistor

    # Final temperature in Celsius.
    therm_temp = ((T_0*B)/(B+T_0*math.log(R_measured/R_0))-273.15)

    return therm_temp


card = u3.U3()
card.configU3()
card.getCalibrationData()
card.configIO(FIOAnalog=3)

card.streamConfig(
    NumChannels=3,
    PChannels=[2],
    NChannels=[31],
    Resolution=3,
    ScanFrequency=SCAN_FREQUENCY
)

try:
    card.streamStart()

    for data_batch in card.streamData():
        if data_batch is not None:

            print(f"AIN2: {data_batch['AIN2']}")
            print(
                f"Temperature? : {calibrate_temperature_reading(data_batch['AIN2'])}")
            r_aio2 = sum(data_batch['AIN2'])/len(data_batch['AIN2'])

            print(f"ain2 average: {r_aio2}")
            print(
                f"Temperature average? : {calibrate_temperature_reading(r_aio2)}")
except KeyboardInterrupt as e:
    print("exiting...")
finally:
    card.streamStop()
    card.close()
