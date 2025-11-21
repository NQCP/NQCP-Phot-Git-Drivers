import socket
import time

from photonicdrivers.Abstract.Connectable import Connectable


class AMI430_PS_Driver(Connectable):
    """
    Driver for the American Magnetics Inc. Model 430 Power Supply
    Communication via TCP/IP socket connection.

    All commands are sent as a query. If the command ends with a '?', a response is expected.
    If the command does not end with a '?', the function returns 0 upon successful sending to avoid a timeout waiting for a response.
    """

    def __init__(self, ip_address: str, port: int = 7180) -> None:
        self.ip_address = ip_address
        self.port = port
        self.timeout = 10
        self.termination_char = "\n"

    def connect(self) -> None:
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.settimeout(self.timeout)
        self.connection.connect((self.ip_address, self.port))

        # Read and discard the "Hello" message
        hello_msg = self.connection.recv(1024).decode("utf-8")
        print(f"Connected: {hello_msg.strip()}")

        self.unit = self.get_unit()

    def disconnect(self) -> None:
        self.connection.close()

    def is_connected(self) -> bool:
        try:
            self.get_id()
            return True
        except Exception:
            return False

    def get_id(self) -> str:
        return self.__query("*IDN?")

    def set_control_remote(self) -> str:
        return self.__query("SYSTem:REMote")

    def set_control_local(self) -> str:
        return self.__query("SYSTem:LOCal")

    def get_unit(self) -> str:
        """
        Returns "kG" for kilogauss or "T" for tesla
        """
        response = self.__query("FIELD:UNITS?")
        return "T" if response == "1" else "kG"

    def set_unit(self, unit: str) -> str:
        """
        Unit options are kG or T.
        """
        if unit == "kG":
            response = self.__query("CONFigure:FIELD:UNITS 0")
        elif unit == "T":
            response = self.__query("CONFigure:FIELD:UNITS 1")
        else:
            warning_str = f"Unit must be kG or T, not {unit}"
            print(warning_str)
            return warning_str

        self.unit = self.get_unit()
        return response

    def get_limit(self) -> str:
        """
        Returns the current limit (used as both upper and lower limit for 4-quadrant supplies)
        """
        return self.__query("CURRent:LIMit?")

    def set_limit(self, limit: float, unit: str):
        """
        Note: AMI 430 uses Current Limit which functions as both positive and negative limit.
        unit: should be A
        """
        if unit != "A":
            warning_str = f"Limit must be set in amperes (A), not {unit}"
            print(warning_str)
            return warning_str
        return self.__query(f"CONFigure:CURRent:LIMit {limit}")

    def ramp_up(self, wait_while_ramping: bool = True) -> str:
        """
        Ramps to the target setpoint
        """
        response = self.__query("RAMP")
        if wait_while_ramping:
            self.__wait_for_state([2, 8])  # HOLDING or AT ZERO
        return response

    def ramp_down(self, wait_while_ramping: bool = True) -> str:
        """
        Manually ramps down
        """
        response = self.__query("DECR")
        if wait_while_ramping:
            print("Manual ramp down - will continue until limit or stopped")
        return response

    def ramp_to_zero(self, wait_while_ramping: bool = True) -> str:
        """
        Ramps to zero current
        """
        response = self.__query("ZERO")
        if wait_while_ramping:
            self.__wait_for_state([8])  # AT ZERO
        return response

    def pause(self) -> str:
        """
        Pauses ramping at current field/current
        """
        return self.__query("PAUSE")

    def get_sweep_mode(self) -> str:
        """
        Returns ramping state:
        1=RAMPING, 2=HOLDING, 3=PAUSED, 4=MANUAL UP, 5=MANUAL DOWN,
        6=ZEROING, 7=QUENCH, 8=AT ZERO, 9=HEATING SWITCH, 10=COOLING SWITCH, 11=RAMPDOWN
        and its corresponding code
        """
        state_code = self.__query("STATE?")
        state_map = {
            "1": "RAMPING to target",
            "2": "HOLDING at target",
            "3": "PAUSED",
            "4": "MANUAL UP",
            "5": "MANUAL DOWN",
            "6": "ZEROING CURRENT",
            "7": "QUENCH detected",
            "8": "AT ZERO",
            "9": "HEATING switch",
            "10": "COOLING switch",
            "11": "RAMPDOWN active",
        }
        return state_map.get(state_code, f"Unknown state: {state_code}"), state_code

    def __wait_for_state(self, target_states: list, timeout: float = 600):
        """
        Wait for the magnet to reach one of the target states
        """
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                print(f"Timeout waiting for state {target_states}")
                break

            state = self.__query("STATE?")
            print(f"Current state: {self.get_sweep_mode()}\r", end="")

            if int(state) in target_states:
                break

            time.sleep(0.5)

    def get_current(self) -> float:
        """
        Returns the magnet current in A
        """
        response = self.__query("CURRent:MAGnet?")
        return float(response)

    def set_current_target(self, current_A: float) -> str:
        """
        Sets the target current in amperes
        """
        return self.__query(f"CONFigure:CURRent:TARGet {current_A}")

    def get_current_target(self) -> float:
        """
        Returns the target current in amperes
        """
        response = self.__query("CURRent:TARGet?")
        return float(response)

    def get_field(self) -> float:
        """
        Returns the magnet field in kG or T (depending on unit setting)
        """
        response = self.__query("FIELD:MAGnet?")
        return float(response)

    def set_field_target(self, field: float) -> str:
        """
        Sets the target field in kG or T (depending on unit setting)
        """
        return self.__query(f"CONFigure:FIELD:TARGet {field}")

    def get_field_target(self) -> float:
        """
        Returns the target field in kG or T (depending on unit setting)
        """
        response = self.__query("FIELD:TARGet?")
        return float(response)

    def get_magnet_voltage(self) -> float:
        """
        Returns the magnet voltage in V
        """
        response = self.__query("VOLTage:MAGnet?")
        return float(response)

    def get_supply_voltage(self) -> float:
        """
        Returns the supply voltage in V
        """
        response = self.__query("VOLTage:SUPPly?")
        return float(response)

    def set_ramp_rate_current(
        self, segment: int, rate: float, upper_bound: float
    ) -> str:
        """
        Sets ramp rate for a segment in A/s or A/min (depending on rate units)
        segment: 1 to number of configured segments
        rate: ramp rate
        upper_bound: upper current bound for this segment in A
        """
        return self.__query(
            f"CONFigure:RAMP:RATE:CURRent {segment},{rate},{upper_bound}"
        )

    def get_ramp_rate_current(self, segment: int) -> str:
        """
        Returns ramp rate and upper bound for specified segment
        """
        return self.__query(f"RAMP:RATE:CURRent:{segment}?")

    def set_ramp_rate_field(self, segment: int, rate: float, upper_bound: float) -> str:
        """
        Sets ramp rate for a segment in kG/s, kG/min, T/s, or T/min
        segment: 1 to number of configured segments
        rate: ramp rate
        upper_bound: upper field bound for this segment
        """
        return self.__query(f"CONFigure:RAMP:RATE:FIELD {segment},{rate},{upper_bound}")

    def get_ramp_rate_field(self, segment: int) -> str:
        """
        Returns ramp rate and upper bound for specified segment
        """
        return self.__query(f"RAMP:RATE:FIELD:{segment}?")

    def get_coil_constant(self) -> float:
        """
        Returns the coil constant in kG/A or T/A (depending on field units)
        """
        response = self.__query("COILconst?")
        return float(response)

    def set_coil_constant(self, value: float) -> str:
        """
        Sets the coil constant in kG/A or T/A (depending on field units)
        """
        return self.__query(f"RAMP {value}")

    def get_persistent_switch_state(self) -> str:
        """
        Returns "0" if switch heater is OFF, "1" if ON
        """
        return self.__query("PSwitch?")

    def set_persistent_switch(self, state: int) -> str:
        """
        Turns persistent switch heater ON (1) or OFF (0)
        """
        if state not in [0, 1]:
            warning_str = "State must be 0 (OFF) or 1 (ON)"
            print(warning_str)
            return warning_str
        return self.__query(f"PSwitch {state}")

    def get_quench_state(self) -> str:
        """
        Returns "0" if no quench, "1" if quench detected
        """
        return self.__query("QUench?")

    def reset_quench(self) -> str:
        """
        Clears quench condition
        """
        return self.__query("QUench 0")

    def get_error(self) -> str:
        """
        Returns next error from error buffer
        """
        return self.__query("SYSTem:ERRor?")

    def get_error_count(self) -> str:
        """
        Returns number of errors in buffer
        """
        return self.__query("SYSTem:ERRor:COUNt?")

    def send_custom_command(self, command: str) -> str:
        return self.__query(command)

    def get_all_settings(self) -> dict:
        settings = {
            "ID": self.get_id(),
            "Unit": self.get_unit(),
            "Limit": self.get_limit(),
            "Current": self.get_current(),
            "Current_Target": self.get_current_target(),
            "Field": self.get_field(),
            "Field_Target": self.get_field_target(),
            "Magnet_Voltage_V": self.get_magnet_voltage(),
            "Supply_Voltage_V": self.get_supply_voltage(),
            "Coil_Constant": self.get_coil_constant(),
            "Persistent_Switch_State": self.get_persistent_switch_state(),
            "Quench_State": self.get_quench_state(),
            "Sweep_Mode": self.get_sweep_mode(),
            "RampRate_Current_Segment1": self.get_ramp_rate_current(1),
            "RampRate_Field_Segment1": self.get_ramp_rate_field(1),
        }
        return settings

    ################################ PRIVATE METHODS ################################

    def __query(self, command_str: str) -> str:
        command = f"{command_str}{self.termination_char}"
        self.connection.sendall(command.encode("utf-8"))

        if not command_str.endswith("?"):
            return 0

        # Wait for response
        time.sleep(0.1)

        response_raw = self.connection.recv(4096)
        response = response_raw.decode("utf-8").strip()

        return response
