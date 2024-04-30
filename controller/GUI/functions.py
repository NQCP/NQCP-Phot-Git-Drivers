import numpy as np


def power_W_to_dBm(power_W):
    if power_W == 0:
        return -np.Inf
    else:
        return 10 * np.log10(power_W * 1000)

def power_dBm_to_W(power_dBm):
    return 10 ** (power_dBm / 10) / 1000

def power_to_dB(power_1, power_2):
    return 10 * np.log10(power_1 / power_2)


def get_float_from_string(str, original_step):
    if str == '':
        return original_step
    else:
        return float(str)