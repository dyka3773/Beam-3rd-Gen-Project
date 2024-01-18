from math import exp, log


def theoretic_resistance(T: float):

    r0 = 10000  # temperature at 25 Celcious
    B = 3984  # Beta value
    TK = T + 273.5
    # θεωρητικη τιμη αντιστασης
    resistance_th = r0 * exp(B*((1/TK)-(1/298.15)))

    return resistance_th


def convert_volt_temp(voltage1: float):

    r0 = 10000  # temperature at 25 Celcious
    B = 3984  # Beta value

    Rth = (5 - voltage1) / 43.6e-5
    TK = 1 / ((log(Rth/r0) / B)+(1/298.15))
    T = TK - 273.5

    return T
