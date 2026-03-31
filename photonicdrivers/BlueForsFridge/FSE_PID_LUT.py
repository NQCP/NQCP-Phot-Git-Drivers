from typing import TypedDict

class PIDParameters(TypedDict):
    P: float
    I: float
    D: float
    max_power: float

# Define temperature thresholds (in Kelvin) and corresponding PID parameters.
# The `get_pid_parameters` function will pick the lowest threshold such that `setpoint <= threshold`.
FSE_PID_LUT: list[tuple[float, PIDParameters]] = [
    (1.5, {"P": 0.005, "I": 100.0, "D": 0.0, "max_power": 0.020}),
    (1.0, {"P": 0.003, "I": 100.0, "D": 0.0, "max_power": 0.002}),
    (0.1, {"P": 0.001, "I": 50.0,  "D": 0.0, "max_power": 0.0005}),
    # Add more mapping tuples by hand here as needed:
    # (threshold, {"P": ..., "I": ..., "D": ..., "max_power": ...}),
]

def get_pid_parameters(setpoint: float) -> PIDParameters:
    """Return the PID parameters for a given setpoint based on FSE_PID_LUT."""
    if not FSE_PID_LUT:
        return {"P": 0.0, "I": 0.0, "D": 0.0, "max_power": 0.0}

    # Ensure they are sorted from lowest to highest threshold
    sorted_lut = sorted(FSE_PID_LUT, key=lambda x: x[0])
    
    for threshold, params in sorted_lut:
        if setpoint <= threshold:
            return params
            
    # Fallback to the highest threshold if the setpoint is higher than all defined values
    return sorted_lut[-1][1]
        
    return {"P": 0.0, "I": 0.0, "D": 0.0, "max_power": 0.0}
