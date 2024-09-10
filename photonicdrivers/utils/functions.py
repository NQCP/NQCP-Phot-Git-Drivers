
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