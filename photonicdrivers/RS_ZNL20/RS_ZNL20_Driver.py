import pyvisa
from photonicdrivers.Abstract.Connectable import Connectable

def boolean_str(val:  bool) -> str:
    return "ON" if val else "OFF"

class RS_ZNL20_Driver(Connectable):
    def __init__(self, ip_address: str, port=5025):
        self.ip_address = ip_address
        self.port = port
        self.resource_manager = pyvisa.ResourceManager()
        self.connection: pyvisa.resources.Resource | None = None

    def connect(self) -> None:
        resource_string = f"TCPIP::{self.ip_address}::{self.port}::SOCKET"

        connection = self.resource_manager.open_resource(resource_string, timeout=5 * 10 ** 3)
        connection.read_termination = '\n'
        connection.write_termination = '\n'
        connection.timeout = 60 * 10 ** 3 # 60 seconds
        self.connection = connection
        
    def disconnect(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def is_connected(self) -> bool:
        success = False
        try:
            response = self.identify()
            if response is not None and response != "":
                success = True
        finally:
            return success
        
    def write(self, command: str) -> None:
        self.connection.write(command)

    def query(self, command) -> str:
        return self.connection.query(command)
    
    def reset(self) -> None:
        self.write("*RST")
    
    def identify(self):
        return self.query("*IDN?")
    
    def status(self) -> int:
        return int(self.query("*STB?"))
    
    def wait(self) -> None:
        """Fire and forget synchronization of the device. Will not process further commands until all previous are done"""
        self.write("*WAI")
    
    def wait_operation_complete(self) -> int:
        """Wait for the operation complete to be written to output buffer"""
        result = self.query("*OPC?")
        return int(result)
    
    def set_power(self, power_dBm: float) -> None:
        self.write(f"SOUR:POW {power_dBm}dBm")
    
    def set_power_state(self, enable: bool) -> None:
        self.write(f"OUTP {boolean_str(enable)}")

    def set_frequency_start(self, start: float) -> None:
        self.write(f"SENS:FREQ:STAR {start}")

    def set_frequency_end(self, end: float) -> None:
        self.write(f"SENS:FREQ:STOP {end}")
    
    def set_sweep_points(self, points: int) -> None:
        self.write(f"SENS:SWE:POIN {points}")

    def set_continuous_sweep(self, enable: bool) -> None:
        self.write(f"INIT:CONT {boolean_str(enable)}")

    def set_sweep_count(self, sweeps: int) -> None:
        self.write(f"SENS:SWE:COUN {sweeps}")

    def start_sweep(self) -> None:
        self.write("INIT:IMM")
    
    def set_data_format(self) -> None:
        self.write(f"CALC:FORM {format}")

    def select_channel(self, channel_name: str) -> None:
        self.write(f"INST:SEL '{channel_name}'")

    def select_s_parameter(self, s_param: str) -> None:
        self.write(f"CALC:PAR:MEAS 'Trc1', '{s_param}'")
    
    def read_formatted_data(self) -> str:
        return self.query("CALC:DATA? FDAT")
    
    def create_channel(self, channel_type: str, channel_name: str) -> None:
        """Channel name must be unique"""
        self.write(f"INST:CRE {channel_type}, '{channel_name}'")

    def list_channel_options(self) -> str:
        return self.query("INST:LIST?")

    def list_traces(self) -> str:
        return self.query("CALC:PAR:CAT?")
