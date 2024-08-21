"""Miscellaneous helper functions for the elliptec package."""
from .errcodes import error_codes


def is_null_or_empty(msg):
    """Checks if message is empty or null."""
    if not msg.endswith(b"\r\n") or (len(msg) == 0):
        return True
    else:
        return False


def parse(msg, debug=True):
    """Parses the message from the controller."""
    if is_null_or_empty(msg):
        if debug:
            print("Parse: Status/Response may be incomplete!")
            print("Parse: Message:", msg)
        return None
    msg = msg.decode().strip()
    code = msg[1:3]
    try:
        _ = int(msg[0], 16)
    except ValueError as exc:
        raise ValueError(f"Invalid Address: {msg[0]}.") from exc
    addr = msg[0]

    if code.upper() == "IN":
        info = {
            "Address": addr,
            "Motor Type": int(msg[3:5], 16),
            "Serial No.": msg[5:13],
            "Year": msg[13:17],
            "Firmware": msg[17:19],
            "Thread": is_metric(msg[19]),
            "Hardware": msg[20],
            "Range": (int(msg[21:25], 16)),
            "Pulse/Rev": (int(msg[25:], 16)),
        }
        return info

    elif code.upper() in ["PO", "BO", "HO", "GJ"]:
        pos = msg[3:]
        return (addr, code, (s32(int(pos, 16))))

    elif code.upper() == "GS":
        errcode = msg[3:]
        return (addr, code, str(int(errcode, 16)))

    elif code.upper() in ["I1", "I2"]:
        # Info about motor

        # Period=14740000/frequency for backward and forward motor movements
        # And 1 Amp of current is equal to 1866 points (1 point is 0.54 mA circa)

        info = {
            "Address": addr,
            "Loop": msg[3],  # The state of the loop setting (1 = ON, 0 = OFF)
            "Motor": msg[4],  # The state of the motor (1 = ON, 0 = OFF)
            "Current": int(msg[5:9], 16) / 1866,  # 1866 points is 1 amp
            "Ramp up": int(msg[9:13], 16),  # PWM increase every ms
            "Ramp down": int(msg[13:17], 16),  # PWM decrease every ms
            "Forward period": int(msg[17:21], 16),  # Forward period value
            "Backward period": int(msg[21:25], 16),  # Backward period value
            "Forward frequency": 14740000 / int(msg[17:21], 16),  # Calculated forward frequency
            "Backward frequency": 14740000 / int(msg[21:25], 16),  # Calculated forward frequency
        }
        return info

    else:
        return (addr, code, msg[3:])


def is_metric(num):
    """Checks if thread is metric or imperial."""
    if num == "0":
        thread_type = "Metric"
    elif num == "1":
        thread_type = "Imperial"
    else:
        thread_type = None

    return thread_type


def s32(value):
    """Convert 32bit signed hex to int."""
    return -(value & 0x80000000) | (value & 0x7FFFFFFF)


def error_check(status):
    """Checks if there is an error."""
    if not status:
        print("Status is None")
    elif isinstance(status, dict):
        print("Status is a dictionary.")
    elif status[1] == "GS":
        if status[2] != "0":  # is there an error?
            err = error_codes[status[2]]
            print(f"ERROR: {err}")
        else:
            print("Status OK")
    elif status[1] == "PO":
        print("Status OK (position)")
    else:
        print("Other status:", status)


def move_check(status):
    """Checks if the move was successful."""
    if not status:
        print("Status is None")
    elif status[1] == "GS":
        error_check(status)
    elif (status[1] == "PO") or (status[1] == "BO"):
        print("Move Successful.")
    else:
        print(f"Unknown response code {status[1]}")
