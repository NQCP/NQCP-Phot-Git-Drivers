

import serial
from photonicdrivers.Abstract.Connectable import Connectable
"C:\Users\Public\Documents\NKT Photonics\SDK\Examples\DLL_Example_Python\NKTPDLL.dll"

import ctypes

# Load the DLL
dll_path = r"C:\Users\Public\Documents\NKT Photonics\SDK\Examples\DLL_Example_Python\NKTPDLL.dll"

nktp_dll = ctypes.CDLL(dll_path)

import NKTPDLL as NKT 

class SuperK_Driver(Connectable):
    """
    A driver class for controlling an NKT Photonics SuperK COMPACT laser
    via a USB (COM port) serial connection.

    Attributes:
        port (str): The COM port used to connect to the laser (e.g., 'COM5').
        baudrate (int): The baud rate for the serial connection.
        ser (serial.Serial): The active serial connection object.
    """

    def __init__(self, port='COM5', baudrate=115200, timeout=1):
        """
        Initializes the SuperK driver with serial communication parameters.

        Args:
            port (str): The COM port for the laser (default 'COM5').
            baudrate (int): Baud rate for serial communication (default 115200).
            timeout (float): Timeout for serial read/write (default 1 second).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def connect(self):
        """
        Opens the serial connection to the laser.
        """
        self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)

    def disconnect(self):
        """
        Closes the serial connection to the laser.
        """
        if self.ser and self.ser.is_open:
            self.ser.close()

    def is_connected(self):
        """
        Checks whether the serial connection is open.

        Returns:
            bool: True if connected, False otherwise.
        """
        return self.ser is not None and self.ser.is_open

    def _send_command(self, command: str) -> str:
        """
        Sends a command to the laser and reads the response.

        Args:
            command (str): The command string to send.

        Returns:
            str: The response from the laser.
        """
        if not self.is_connected():
            raise ConnectionError("Not connected to SuperK laser.")

        # Ensure command ends with newline
        cmd = command.strip() + "\r\n"
        self.ser.write(cmd.encode('ascii'))

        response = self.ser.readline().decode('ascii').strip()
        return response

    ###### BASIC CONTROL ######

    def set_laser_enabled(self, enable_bool: bool):
        """
        Enables or disables the laser emission.

        Args:
            enable_bool (bool): True to enable emission, False to disable it.
        """
        cmd = "L=1" if enable_bool else "L=0"
        self._send_command(cmd)

    def get_laser_enabled(self) -> bool:
        """
        Retrieves the laser emission status.

        Returns:
            bool: True if emission is on, False otherwise.
        """
        return self._send_command("L?") == "1"

    def set_shutter(self, open_bool: bool):
        """
        Opens or closes the shutter.

        Args:
            open_bool (bool): True to open shutter, False to close it.
        """
        cmd = "S=1" if open_bool else "S=0"
        self._send_command(cmd)

    def get_shutter(self) -> bool:
        """
        Retrieves the shutter status.

        Returns:
            bool: True if shutter is open, False otherwise.
        """
        return self._send_command("S?") == "1"

    def get_power(self) -> float:
        """
        Retrieves the current laser power.

        Returns:
            float: Current power in milliwatts (mW).
        """
        response = self._send_command("P?")
        try:
            return float(response)
        except ValueError:
            return 0.0

    def set_power(self, power_mW: float):
        """
        Sets the laser output power.

        Args:
            power_mW (float): Desired power in milliwatts (mW).
        """
        self._send_command(f"P={power_mW:.2f}")

    def get_errors(self) -> str:
        """
        Retrieves any error messages from the laser.

        Returns:
            str: Error message string, or '0' if no error.
        """
        return self._send_command("ERR?")

    ###### UTILITY ######

    def get_status(self) -> dict:
        """
        Retrieves the overall status of the laser.

        Returns:
            dict: A dictionary containing emission, shutter, power, and errors.
        """
        return {
            "connected": self.is_connected(),
            "emission": self.get_laser_enabled(),
            "shutter": self.get_shutter(),
            "power_mW": self.get_power(),
            "errors": self.get_errors()
        }
