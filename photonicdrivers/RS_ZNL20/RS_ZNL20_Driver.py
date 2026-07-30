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
        try:
            response = self.identify()
            return response is not None and response != ""
        except:
            return False
        
    def write(self, command: str) -> None:
        self.connection.write(command)

    def query(self, command) -> str:
        return self.connection.query(command)
    
    def reset(self) -> None:
        self.write("*RST")
    
    def identify(self):
        return self.query("*IDN?")
    
    def get_id(self):
        return self.identify()
    
    def status(self) -> int:
        return int(self.query("*STB?"))
    
    def wait(self) -> None:
        """Issue SCPI ``*WAI`` to enforce instrument-side command ordering.

        This does not itself return a completion token to Python. It is useful for
        sequencing commands in the instrument parser but is less explicit than
        ``*OPC?`` for host-side blocking logic.
        """
        self.write("*WAI")
    
    def wait_operation_complete(self) -> int:
        """Block until pending operations complete using SCPI ``*OPC?``.

        Returns:
            int: Typically ``1`` when the instrument reports operation complete.

        Use this after ``start_sweep()`` when you must ensure sweep results are
        ready before reading data.
        """
        result = self.query("*OPC?")
        return int(result)

    def get_power(self) -> float:
        return float(self.query(f"SOUR:POW?"))
    
    def get_frequency_start(self) -> float:
        return float(self.query(f"SENS:FREQ:STAR?"))

    def get_frequency_end(self) -> float:
        return float(self.query(f"SENS:FREQ:STOP?"))
    
    def get_num_sweep_points(self) -> int:
        return int(self.query(f"SENS:SWE:POIN?"))
    
    def get_continuous_sweep(self) -> bool:
        return bool(self.query(f"INIT:CONT?")) 
    
    def get_bandwidth(self) -> float:
        return float(self.query(f"SENS:BAND:RES?"))

    def set_power(self, power_dBm: float) -> None:
        self.write(f"SOUR:POW {power_dBm}dBm")

    def set_power_state(self, enable: bool) -> None:
        self.write(f"OUTP {boolean_str(enable)}")

    def set_frequency_start(self, start: float) -> None:
        self.write(f"SENS:FREQ:STAR {start}")

    def set_frequency_end(self, end: float) -> None:
        self.write(f"SENS:FREQ:STOP {end}")
    
    def set_num_sweep_points(self, points: int) -> None:
        self.write(f"SENS:SWE:POIN {points}")

    def set_continuous_sweep(self, enable: bool) -> None:
        self.write(f"INIT:CONT {boolean_str(enable)}")

    def set_sweep_count(self, sweeps: int) -> None:
        self.write(f"SENS:SWE:COUN {sweeps}")

    def set_bandwidth(self, bandwidth_Hz: float) -> None:
        self.write(f"SENS:BAND:RES {bandwidth_Hz}")

    def start_sweep(self) -> None:
        """Trigger a sweep using ``INIT:IMM`` and return immediately.

        This method does not wait for measurement completion. Call
        ``wait_operation_complete()`` when deterministic blocking is required
        before data readout.
        """
        self.write("INIT:IMM")
    
    def stop_continuous_sweep(self) -> None:
        self.write("INIT:CONT False")
    
    def set_data_format(self) -> None:
        self.write(f"CALC:FORM {format}")

    def sw_channel(self, channel_name: str) -> None:
        self.write(f"INST:SEL '{channel_name}'")

    def select_s_parameter(self, s_param: str) -> None:
        self.write(f"CALC:PAR:MEAS 'Trc1', '{s_param}'")

    def select_s_parameter_list(self, s_param_list: list[str]) -> None:
        for i, s_param in enumerate(s_param_list):
            self.write(f"CALC:PAR:SDEF 'Trc{i+1}', '{s_param}'")
        # print('VNA traces: ' + self.query("CALC:PAR:CAT?"))
    
    def read_formatted_data(self) -> str:
        return self.query("CALC:DATA? FDAT")
    
    def read_formatted_data_complex(self, trace_index: int = 1) -> str:
        self.write(f"CALC:PAR:SEL 'Trc{trace_index}'")
        return self.query("CALC:DATA? SDAT")
    
    def create_channel(self, channel_type: str, channel_name: str) -> None:
        """Channel name must be unique"""
        self.write(f"INST:CRE {channel_type}, '{channel_name}'")

    def list_channel_options(self) -> str:
        return self.query("INST:LIST?")

    def list_traces(self) -> str:
        return self.query("CALC:PAR:CAT?")
