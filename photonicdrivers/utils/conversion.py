import math

# Convert power from dBm to mW
def dBm_to_mW(power_dBm):
    """
    Converts power from dBm (decibel-milliwatts) to mW (milliwatts).

    Formula: mW = 10^(dBm / 10)

    Parameters:
        power_dBm (float): Power in dBm.

    Returns:
        float: Power in mW.
    """
    return 10 ** (power_dBm / 10)

# Convert power from mW to dBm
def mW_to_dBm(power_mW):
    """
    Converts power from mW (milliwatts) to dBm (decibel-milliwatts).

    Formula: dBm = 10 * log10(mW)

    Parameters:
        power_mW (float): Power in mW.

    Returns:
        float: Power in dBm.
    """
    return 10 * math.log10(power_mW)

# Convert power from dBm to W
def dBm_to_W(power_dBm):
    """
    Converts power from dBm (decibel-milliwatts) to W (watts).

    Formula: W = mW / 1000

    Parameters:
        power_dBm (float): Power in dBm.

    Returns:
        float: Power in W.
    """
    return mW_to_W(dBm_to_mW(power_dBm))

# Convert power from W to dBm
def W_to_dBm(power_W):
    """
    Converts power from W (watts) to dBm (decibel-milliwatts).

    Formula: dBm = 10 * log10(W * 1000)

    Parameters:
        power_W (float): Power in W.

    Returns:
        float: Power in dBm.
    """
    return mW_to_dBm(W_to_mW(power_W))

# Convert power from mW to W
def mW_to_W(power_mW):
    """
    Converts power from mW (milliwatts) to W (watts).

    Formula: W = mW / 1000

    Parameters:
        power_mW (float): Power in mW.

    Returns:
        float: Power in W.
    """
    return power_mW / 1000

# Convert power from W to mW
def W_to_mW(power_W):
    """
    Converts power from W (watts) to mW (milliwatts).

    Formula: mW = W * 1000

    Parameters:
        power_W (float): Power in W.

    Returns:
        float: Power in mW.
    """
    return power_W * 1000

def convert_power_from_unit_to_unit(power_data, data_unit, conversion_unit):
    if data_unit == conversion_unit:
        return power_data

    if data_unit == "W" and conversion_unit == "dBm":
        return W_to_dBm(power_data)

    if data_unit == "W" and conversion_unit == "mW":
        return W_to_mW(power_data)
    
    if data_unit == "mW" and conversion_unit == "dBm":
        return mW_to_dBm(power_data)

    if data_unit == "mW" and conversion_unit == "W":
        return mW_to_W(power_data)
    
    if data_unit == "dBm" and conversion_unit == "W":
        return dBm_to_W(power_data)
    
    if data_unit == "dBm" and conversion_unit == "mW":
        return dBm_to_mW(power_data)