import pyvisa


class RigolDHO924S_Driver:
    """Driver for the Rigol DHO924S Oscilloscope over TCP/IP using PyVISA"""
    def __init__(self, ip_address: str) -> None:
        self.ip_address = ip_address
        self.resource_manager = pyvisa.ResourceManager()
        self.connection: pyvisa.resources.Resource | None = None

    def connect(self) -> None:
        """Connect to the scope via TCP/IP and set a 1 second timeout"""
        resource_string = f"TCPIP::{self.ip_address}::INSTR"

        connection = self.resource_manager.open_resource(
            resource_string, timeout=1 * 10**3
        )
        connection.timeout = 1 * 10**3  # 1 second
        self.connection = connection

    def disconnect(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def is_connected(self) -> bool:
        """Check if the connection to the scope is active
        
        Returns:
            bool: True if connected, False otherwise
        """
        try:
            response = self.identify()
            return response is not None and response != ""
        except Exception:
            return False

    def write(self, command: str) -> None:
        self.connection.write(command)

    def query(self, command) -> str:
        return self.connection.query(command)

    def reset(self) -> None:
        """Restores the instrument to its factory default settings."""
        self.write("*RST")

    def identify(self):
        """
        The query returns RIGOL TECHNOLOGIES,<model>,<serial number>,<software version>.    
            • <model>: indicates the model number of the instrument.
            • <serial number>: indicates the serial number of the instrument.
            • <software version>: indicates the software version of the instrument.

        Returns:
            str: Identification string of the instrument
        """
        return self.query("*IDN?")

    def wait(self) -> None:
        """
        Waits for all the pending operations to complete before executing any additional commands
        """
        self.write("*WAI")

    def wait_operation_complete(self) -> int:
        """
        Queries whether the current operation is finished.

        Returns:
            int: 1 if operation is complete, 0 otherwise
        """
        result = self.query("*OPC?")
        return int(result)
    
    def run(self) -> None:
        """
        Starts the acquisition process.
        """
        self.write(":RUN")
    
    def stop(self) -> None:
        """
        Stops the acquisition process.
        """
        self.write(":STOP")

    def single(self) -> None:
        """
        Sets the oscilloscope to single acquisition mode.
        """
        self.write(":SINGle")
