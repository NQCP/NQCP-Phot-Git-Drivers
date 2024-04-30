import numpy as np


def power_W_to_dBm(power_W: float) -> float:
    if power_W == 0:
        return -np.Inf
    else:
        return 10 * np.log10(power_W * 1000)


def power_dBm_to_W(power_dBm: float) -> float:
    return 10 ** (power_dBm / 10) / 1000


def power_to_dB(power_1: float, power_2: float) -> float:
    return 10 * np.log10(power_1 / power_2)
