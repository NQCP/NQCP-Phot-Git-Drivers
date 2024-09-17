import numpy as np

from loguru import logger
import math

def str_is_number(str):
    try:
        num = float(str)
        if math.isnan(num):
            return False
        elif math.isinf(num):
            return False

        return True 
    except Exception as exception:
        logger.debug(exception)
        return False
    
    
def get_average(number_average, list):
        # Ensure the slice size is valid
        if number_average <= 0 or number_average > len(list):
            return 0, 0

        last_acquired = list[-number_average:]

        # Filter out NaN and inf values
        last_acquired = [x for x in last_acquired if np.isfinite(x)]

        if len(last_acquired) == 0:
            # Handle the case where all values were NaN or inf
            mean = 0
            standard_deviation = 0
            relative_standard_deviation = 0
        else:
            try:
                mean = np.mean(last_acquired)
                standard_deviation = np.std(last_acquired)
                relative_standard_deviation = standard_deviation/mean
            except Exception as e:
                # Log or handle the exception if needed
                mean = 0
                standard_deviation = 0
                relative_standard_deviation = 0

        return mean, standard_deviation