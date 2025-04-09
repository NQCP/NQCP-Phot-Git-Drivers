import serial
from photonicdrivers.Abstract.Connectable import Connectable

class VdHB400_Driver(Connectable):
    def __init__(self, port: str):
        self.port = port
        self.connection = None
        
    def connect(self) -> None:
        self.connection = serial.Serial(
            port=self.port,
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=5
        )
        
    def disconnect(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            
    def is_connected(self) -> bool:
        try:
            power_status = self.get_power_status()
            return power_status == "ON" or power_status == "OFF"
        except:
            return False

    def query(self, command: str) -> str:
        if self.connection is None:
            raise ConnectionError("Not connected to the device")
        
        # Send command with CR and LF
        full_command = f"{command}\r\n"
        self.connection.write(full_command.encode())
        
        # Read response
        response = self.connection.readline().decode().strip()
        return response
    
    # Read commands implementation
    
    def get_power_status(self) -> str:
        return self.query("POWER")
    
    def get_pump1_status(self) -> str:
        return self.query("PUMP1")
    
    def get_control_status(self) -> str:
        return self.query("COOL")
    
    def get_temperature_pt1(self) -> float:
        response = self.query("PT1")
        return float(response)
    
    def get_temperature_pt2(self) -> float:
        response = self.query("PT2")
        return float(response)
    
    def get_temperature_pt3(self) -> float:
        response = self.query("PT3")
        return float(response)
    
    def get_temperature_pt4(self) -> float:
        response = self.query("PT4")
        return float(response)
    
    def get_setpoint_temperature(self) -> float:
        response = self.query("SET1")
        return float(response)
    
    def get_interface_software_version(self) -> str:
        return self.query("SWC")
    
    def get_display_software_version(self) -> str:
        return self.query("SWB400")
    
    def get_control_software_version(self) -> str:
        return self.query("SWR203")
    
    def get_flow_rate_df1(self) -> float:
        response = self.query("DF1")
        return float(response)
    
    def get_flow_rate_df2(self) -> float:
        response = self.query("DF2")
        return float(response)
    
    def get_analog_input_output1(self) -> float:
        response = self.query("EA1")
        return float(response)
    
    def get_analog_input_output2(self) -> float:
        response = self.query("EA2")
        return float(response)
    
    def get_analog_input_output3(self) -> float:
        response = self.query("EA3")
        return float(response)
    
    def get_analog_input_output4(self) -> float:
        response = self.query("EA4")
        return float(response)
    
    def get_error_status(self) -> str:
        return self.query("ERR")
