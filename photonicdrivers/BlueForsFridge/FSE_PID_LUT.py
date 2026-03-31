from typing import TypedDict

class PIDParameters(TypedDict):
    P: float
    I: float
    D: float
    max_power: float

# Define temperature thresholds (in Kelvin) and corresponding PID parameters.
# The `get_pid_parameters` function will pick the lowest threshold such that `setpoint <= threshold`.
FSE_PID_LUT: list[tuple[float, PIDParameters]] = [
    (0.05,  {"P": 2e-5 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 0.001}),
    (0.100, {"P": 8e-5 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 0.002}),
    (0.150, {"P": 1e-4 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 0.004}),
    (0.225, {"P": 2e-4 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 0.008}),
    (0.325, {"P": 4e-4 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 0.02}),
    (0.425, {"P": 6e-4 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 0.04}),
    (0.55,  {"P": 1e-3 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 0.08}),
    (0.725, {"P": 2e-3 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 0.1}),
    (0.85,  {"P": 3e-3 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.0,   {"P": 4e-3 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.1,   {"P": 5e-3 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.2,   {"P": 6e-3 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.3,   {"P": 7.5e-3 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.35,  {"P": 1e-2 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.425, {"P": 1.1e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.475, {"P": 1.2e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.525, {"P": 1.3e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.625, {"P": 1.35e-2 * 0.85, "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.675, {"P": 1.4e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.7,   {"P": 1.5e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.75,  {"P": 1.55e-2 * 0.85, "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (1.85,  {"P": 1.6e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (2.0,   {"P": 1.65e-2 * 0.85, "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (2.15,  {"P": 1.75e-2 * 0.85, "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (2.25,  {"P": 1.9e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (2.5,   {"P": 2.2e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (2.75,  {"P": 2.4e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (3.0,   {"P": 2.7e-2 * 0.85,  "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (5.0,   {"P": 3e-2 * 0.85,    "I": 100.0, "D": 0.0, "max_power": 1.0}),
    (float('inf'), {"P": 5e-2 * 0.85, "I": 100.0, "D": 0.0, "max_power": 1.0}),
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
