from math import log


def convert_thermistor_values(voltage1: float) -> float:
    """Kanei convert ta voltages twn thermistors se thermokrasies 
        To voltage που παιρνουμε ειναι της αντίστασης όχι του θερμίστορ
    Args:
        thermistor_value (float): to ekastote voltage apo to ekastote thermistor
    """
    r0 = 10000  # temperature at 25 Celcious
    B = 3984  # Beta value

    Rth = (5 - voltage1) / 43.6e-5
    TK = 1 / ((log(Rth/r0) / B)+(1/298.15))
    T = TK - 273.5

    return T
