import pyvisa
from serial import Serial
from time import sleep

from photonicdrivers.Abstract.Connectable import Connectable

class Picus_Driver(Connectable):

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
            self.connection.read_termination = self.termination_character
            self.connection.write_termination = self.termination_character
            print("Successfully connected to Picus laser via pyvisa using port: " + self.port)

        elif self.connectionType == "serial":
            self.connection = Serial(port=self.port, timeout = 3)
            print("Successfully connected to Picus laser via serial using port: " + self.port)    

        else:
            print("No connection method defined")

    def disconnect(self):
        # both the pyvisa and serial libraries have "close" command
        self.connection.close()

    def is_connected(self) -> bool:
        return bool(self.getRuntimeAmplifier())
        
    def getRuntimeAmplifier(self):
        self._write("Measure:Runtime:Amplifier?")
        return self._read()

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
        if self.connectionType == "pyvisa":
            self.connection.write(command)
            
        elif self.connectionType == "serial":
            command = command + self.termination_character
            self.connection.write(command.encode())
        else:
            print("No connection method defined")        

    def _read(self) -> str:
        response = None

        if self.connectionType == "pyvisa":
            response = self.connection.read()
            response = response.replace('\n', '').replace('\r', '')

        elif self.connectionType == "serial":
            response = self.connection.readline().decode()

        else:
            print("No connection method defined")

        return response