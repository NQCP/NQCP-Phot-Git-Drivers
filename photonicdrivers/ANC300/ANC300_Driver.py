import pyvisa
from photonicdrivers.Abstract.Connectable import Connectable

class ANC300_Driver(Connectable):
    """
    Driver for the AttoCube ANC300 Piezo Positioning Electronic
    
    Common parameters across methods:
    - axis_id: Axis ID (1-7)
    - frequency: Frequency in Hz (1-10000)
    - voltage: Voltage in volts (0-150)
    - steps: Number of steps or "c" for continuous
    - trigger_num: Trigger number (1-7) or "off"
    - filter_setting:
        - ANM300: "16", "160", "off"
        - ANM200: "1.6", "16", "160", "1600"
    - mode: Operating mode (gnd, inp, cap, stp, off, stp+, stp-)
    
    Connection strings:
    - USB: 'ASRL<port>::INSTR'
    - Ethernet: 'TCPIP::<ip address>::7230::SOCKET'
    """

    def __init__(self, resource_string, timeout=5000):
        self.resource_string = resource_string
        self.timeout = timeout
        self.resource_manager = pyvisa.ResourceManager()
        self.connection = None
        
    def connect(self) -> None:
        self.connection = self.resource_manager.open_resource(self.resource_string, timeout=self.timeout, read_termination="\r\n", write_termination="\r\n")
        self.set_echo(False)
        
    def disconnect(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            
    def is_connected(self) -> bool:
        try:
            return self.get_version() is not None
        except:
            return False
            
    def query(self, command: str) -> str:
        self.connection
        return self.connection.query(command)

    def write(self, command: str) -> None:
        self.connection.write(command)
        res: str = self.connection.read()
        if res.strip() != "OK":
            raise Exception(f"ANC300 returned error {res}")

    def move_steps(self, axis_id: int, voltage: float, count: int, direction: str, steps: int, frequency: int, wait=True):
        self.set_step_voltage(axis_id, voltage)
        self.set_frequency(axis_id, frequency)
        self.step(axis_id, direction, steps, wait)


    def help(self) -> str:
        return self.query("help")

    def set_echo(self, enabled: bool) -> None:
        state = "on" if enabled else "off"
        self.query(f"echo {state}")

    # Basic information commands
    def get_version(self) -> str:
        return self.query("ver")
    
    def get_controller_serial(self) -> str:
        return self.query("getcser")
    
    def get_axis_serial(self, axis_id: int) -> str:
        return self.query(f"getser {axis_id}")
    
    def send_feature_code(self, code: str) -> str:
        return self.query(f"setfc {code}")
    
    # Mode commands

    def set_ground(self, axis_id: int) -> None:
        """Ground mode. Should follow most operations"""
        self.set_mode(axis_id, "gnd")

    def set_mode(self, axis_id: int, mode: str) -> None:
        self.write(f"setm {axis_id} {mode}")
    
    def get_mode(self, axis_id: int) -> str:
        return self.query(f"getm {axis_id}")
    
    # Parameter settings
    def set_frequency(self, axis_id: int, frequency: int) -> None:
        self.write(f"setf {axis_id} {frequency}")
    
    def get_frequency(self, axis_id: int) -> int:
        return self.query(f"getf {axis_id}")
    
    def set_step_voltage(self, axis_id: int, voltage: float) -> None:
        self.write(f"setv {axis_id} {voltage}")
    
    def get_step_voltage(self, axis_id: int) -> float:
        return self.query(f"getv {axis_id}")
    
    def set_offset_voltage(self, axis_id: int, voltage: float) -> None:
        self.write(f"seta {axis_id} {voltage}")
    
    def get_offset_voltage(self, axis_id: int) -> float:
        return self.query(f"geta {axis_id}")
    
    # Input controls
    def set_ac_in(self, axis_id: int, enabled: bool) -> None:
        state = "on" if enabled else "off"
        self.write(f"setaci {axis_id} {state}")
    
    def get_ac_in(self, axis_id: int) -> bool:
        return self.query(f"getaci {axis_id}")
    
    def set_dc_in(self, axis_id: int, enabled: bool) -> None:
        state = "on" if enabled else "off"
        self.write(f"setdci {axis_id} {state}")
    
    def get_dc_in(self, axis_id: int) -> bool:
        return self.query(f"getdci {axis_id}")
    
    # Filter settings
    def set_filter(self, axis_id: int, filter_setting: str) -> None:
        self.write(f"setfil {axis_id} {filter_setting}")
    
    def get_filter(self, axis_id: int) -> str:
        return self.query(f"getfil {axis_id}")
    
    # Stepping commands
    
    def step_wait(self, axis_id: int) -> None:
        """Wait until the device has moved specified number of steps"""
        self.write(f"stepw {axis_id}")

    def step(self, axis_id: int, direction: str, steps: int = 1, wait=True):
        if direction == "u":
            self.step_up(axis_id, steps=steps, wait=wait)
        elif direction == "d":
            self.step_down(axis_id, steps=steps, wait=wait)
        else:
            raise ValueError(f"'{direction}' is not a valid stepping direction")
        
    def step_up(self, axis_id: int, steps: int = 1, wait=True) -> None:
        self.write(f"stepu {axis_id} {steps}")
        if wait:
            self.step_wait()


    def step_down(self, axis_id: int, steps: int = 1, wait=True) -> None:
        self.write(f"stepd {axis_id} {steps}")
        if wait:
            self.step_wait()
    
    def continuous_step_up(self, axis_id: int) -> None:
        self.step_up(axis_id, "c", wait=False)
    
    def continuous_step_down(self, axis_id: int) -> None:
        self.step_down(axis_id, "c", wait=False)
     
    def stop(self, axis_id: int, set_ground: bool=True) -> None:
        self.write(f"stop {axis_id}")
        if set_ground:
            self.set_mode(axis_id, "gnd")
    
    # Measurement commands
    def measure_capacitance(self, axis_id: int) -> float:
        self.set_mode(axis_id, "cap")
        self.query(f"capw {axis_id}")  # Wait for measurement to complete
        return self.query(f"getc {axis_id}")
    
    def get_output_voltage(self, axis_id: int) -> float:
        return self.query(f"geto {axis_id}")
    
    # Pattern commands
    def set_pattern_up(self, axis_id: int, pattern: list) -> None:
        pattern_str = " ".join(str(int(val)) for val in pattern)
        self.write(f"setpu {axis_id} {pattern_str}")
    
    def get_pattern_up(self, axis_id: int) -> list:
        return self.query(f"getpu {axis_id}")
    
    def set_pattern_down(self, axis_id: int, pattern: list) -> None:
        pattern_str = " ".join(str(int(val)) for val in pattern)
        self.write(f"setpd {axis_id} {pattern_str}")
    
    def get_pattern_down(self, axis_id: int) -> list:
        return self.query(f"getpd {axis_id}")
    
    # Trigger commands
    def set_trigger_up(self, axis_id: int, trigger_num: int) -> None:
        self.write(f"settu {axis_id} {trigger_num}")
    
    def get_trigger_up(self, axis_id: int) -> str:
        return self.query(f"gettu {axis_id}")
    
    def set_trigger_down(self, axis_id: int, trigger_num: int) -> None:
        self.write(f"settd {axis_id} {trigger_num}")
    
    def get_trigger_down(self, axis_id: int) -> str:
        return self.query(f"gettd {axis_id}")
    
    def set_output_trigger(self, trigger_num: int, state: int) -> None:
        self.write(f"setto {trigger_num} {state}")
    
    def get_output_trigger(self, trigger_num: int) -> int:
        return self.query(f"getto {trigger_num}")
