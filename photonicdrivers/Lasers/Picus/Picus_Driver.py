import pyvisa
from serial import Serial

class Picus_Driver():

    def __init__(self, _resource_manager: pyvisa.ResourceManager=None, _port: str=None, _connectionMethod=None) -> None:
        self.resource_manager = _resource_manager
        self.port = _port
        self.baud_rate = 115200
        self.data_bits = 8
        self.parity = "None"
        self.stop_bits = 1
        self.termination_character = "\n"

        self.connectionType = _connectionMethod
        self.connection = None
        
#################################### HIGH LEVEL METHODS ##########################################



#################################### LOW LEVEL METHODS ###########################################

    def connect(self):
        if self.connectionType == "pyvisa":
            self.connection = self.resource_manager.open_resource(self.port)
            print("Successfully connected to Picos laser")
        elif self.connectionType == "serial":
            self.connection = Serial(port='COM5', timeout = 3)
        else:
            print("No connection method defined")

    def disconnect(self):
        self.connection.close()

    def getEnabledState(self) -> bool:
        self._write("Laser:Enable?")
        return bool(int(self._read()))
    
    def getWavelength(self) -> float:
        self._write("Laser:Wavelength?")
        return float(self._read())
    
    def setEnabledState(self, state: bool) -> None:
        self._write("Laser:Enable" + str(int(state)))

    def setWavelength(self, wavelength_nm: float) -> None:
        self._write("Laser:Wavelength" + str(wavelength_nm))


#################################### PRIVATE METHODS ###########################################

    def _write(self,command: str) -> None:
        cmd = command + self.termination_character
        # print(cmd)

        if self.connectionType == "pyvisa":
            self.write(cmd)
        elif self.connectionType == "serial":
            self.connection.write(cmd.encode())
        else:
            print("No connection method defined")
        

    def _read(self) -> str:
        # response = self.powerMeter.read()
        # response = response.replace('\n', '').replace('\r', '')
        response = None

        if self.connectionType == "pyvisa":
            self.connection.read()
        elif self.connectionType == "serial":
            response = self.connection.readline().decode()
        else:
            print("No connection method defined")

        return response