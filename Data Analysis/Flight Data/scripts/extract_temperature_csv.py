import pandas as pd
from math import log

def convert_thermistor_values(thermistor_value: float) -> float:
    """Kanei convert ta voltages twn thermistors se thermokrasies 
        To voltage που παιρνουμε ειναι της αντίστασης όχι του θερμίστορ
    Args:
        thermistor_value (float): to ekastote voltage apo to ekastote thermistor
    """
    if (not thermistor_value) or (pd.isna(thermistor_value)):
        return None
    
    r0 = 10000  # temperature at 25 Celcious
    B = 3984  # Beta value

    T: float = 0

    try:
        Rth = (5 - thermistor_value) / 43.6e-5

        print(f"Rth: {Rth}")
        print(f"thermistor_value: {thermistor_value}")
        print(f"Rth/r0: {Rth/r0}")

        TK = 1 / ((log(Rth/r0) / B)+(1/298.15))
        T = TK - 273.5
    except Exception as e:
        print("Error in converting thermistor values")
        print(e)
    return T

def main():
    # Read the data from the csv file 
    df = pd.read_csv(
        'rocket_data.csv',
        usecols=[0, 4, 5, 6],
        names=['time', 'right_thermistor', 'left_thermistor', 'sound_card_temp'],
        header=0
    )
    
    # Apply the conversion function to the thermistor values for each row
    df['right_thermistor'] = df['right_thermistor'].apply(convert_thermistor_values)
    df['left_thermistor'] = df['left_thermistor'].apply(convert_thermistor_values)
    
    # Drop the rows with NaN values in all the temperature columns
    df.dropna(subset=['right_thermistor', 'left_thermistor', 'sound_card_temp'], how='all', inplace=True)
    
    # Save the data to a new csv file
    df.to_csv('temperature_data.csv', index=False)    
    
if __name__ == '__main__':
    main()