import numpy as np
from pylablib.devices.Thorlabs.elliptec import ElliptecMotor
import serial
from photonicdrivers.Abstract.Connectable import Connectable
import pylablib.devices.Thorlabs.elliptec as ello

class ELL6(Connectable):
    """
    Class for controlling ELL6 rotation stage.
    """

    def __init__(self, port, address="all"):
        """
        Initializes the ELL6 instance with the specified port and address.

        Args:
            port (str): The connection port for the rotation stage.
            address (int): The new address to set, must be between 0 and 15.
                          Addresses above 10 represent letters (A, B, C, D, E, F) but cannot be used.
        """
        self.port = port
        self.address = address
        self.rotation_mount: ElliptecMotor = None

    def connect(self) -> None:
        """
        Establishes a connection to the ELL6 rotation stage.
        """
        try:
            self.rotation_mount = ElliptecMotor(conn=self.port, addrs=self.address)
        except Exception:
            print("Unable to connect")

    def disconnect(self) -> None:
        """
        Closes the connection to the ELL6 rotation stage.
        """
        self.rotation_mount.close()

    def is_connected(self) -> bool:
        """
        Checks if a connection to the ELL6 rotation stage is established.

        Returns:
            bool: True if connected, False otherwise.
        """
        try:
            self.rotation_mount.get_full_status()
            return True
        except Exception:
            return False

    def get_position(self) -> float:
        """
        Retrieves the current position of the ELL6 rotation stage.

        Returns:
            float: The current position.
        """
        return self.rotation_mount.get_position()

    def move_to_position(self, position: int) -> None:
        """
        Moves the rotation stage to a specific position (0 or 1).

        Args:
            position (int): The target position, must be either 0 or 1.

        Raises:
            ValueError: If the position is not 0 or 1.
        """
        if position not in [0, 1]:
            raise ValueError("Position must be either 0 or 1.")
        self.rotation_mount.move_to(position)

    def set_address(self, address: int) -> None:
        """
        Sets a new address for the ELL6 rotation stage.

        Args:
            address (int): The new address to set, must be between 0 and 15.
                          Addresses above 10 represent letters (A, B, C, D, E, F) but cannot be used.

        Raises:
            ValueError: If the address is not within the valid range (0 to 15).
        """
        if not (0 <= address <= 15):
            raise ValueError("Address must be a number between 0 and 15.")
        self.rotation_mount.set_default_addr(address)

    def get_address(self) -> list:
        """
        Retrieves the connected addresses for the rotation stage.

        Returns:
            list: List of connected addresses.
        """
        return self.rotation_mount.get_connected_addrs()
  
class ELL14(Connectable):
    """
    Class for controlling ELL14 rotation stage.
    """

    def __init__(self, port, address="all"):
        """
        Initializes the ELL14 instance with the specified port and address.

        Args:
            port (str): The connection port for the rotation stage.
            address (str): The address of the rotation stage (default is 'all'). Must be between 0 and 15. Addresses above 10 represent letters (A, B, C, D, E, F) but cannot be used.
        """
        self.port = port
        self.address = address
        self.rotation_mount: ElliptecMotor = None

    def connect(self) -> None:
        """
        Establishes a connection to the ELL14 rotation stage.
        """
        try:
            self.rotation_mount = ElliptecMotor(conn=self.port, addrs=self.address)
        except Exception:
            print("Unable to connect")

    def disconnect(self) -> None:
        """
        Closes the connection to the ELL14 rotation stage.
        """
        self.rotation_mount.close()

    def is_connected(self) -> bool:
        """
        Checks if a connection to the ELL14 rotation stage is established.

        Returns:
            bool: True if connected, False otherwise.
        """
        try:
            self.rotation_mount.get_full_status()
            return True
        except Exception:
            return False

    def set_address(self, address: int) -> None:
        """
        Sets a new address for the ELL14 rotation stage.

        Args:
            address (int): The new address to set, must be between 0 and 15.
                          Addresses above 10 represent letters (A, B, C, D, E, F) but cannot be used.

        Raises:
            ValueError: If the address is not within the valid range (0 to 15).
        """
        if not (0 <= address <= 15):
            raise ValueError("Address must be a number between 0 and 15.")
        self.rotation_mount.set_default_addr(address)

    def get_address(self) -> list:
        """
        Retrieves the connected addresses for the rotation stage.

        Returns:
            list: List of connected addresses.
        """
        return self.rotation_mount.get_connected_addrs()

    def move_to(self, angle: float) -> None:
        """
        Moves the rotation stage to a specific angle.

        Args:
            angle (float): The target angle in degrees.
        """
        if angle < -360:
            angle = np.mod(angle, -360)
        if angle > 360:
            angle = np.mod(angle, 360)
        self.rotation_mount.move_to(angle)

    def move_by(self, angle: float) -> None:
        """
        Moves the rotation stage by a specified angle.

        Args:
            angle (float): The angle to move by, in degrees.
        """
        self.rotation_mount.move_by(angle)

    def home(self) -> None:
        """
        Homes the rotation stage, returning it to the reference position.
        """
        self.rotation_mount.home()

    def get_position(self) -> float:
        """
        Retrieves the current position of the rotation stage.

        Returns:
            float: The current position in degrees.
        """
        return self.rotation_mount.get_position()

class ELLB(Connectable):
    pass

if __name__ == "__main__":

    slider_mount = ELL6(port="COM10", address=[10])
    slider_mount.connect()
    print(slider_mount.get_address())
    print(slider_mount.is_connected())
    print(slider_mount.move_to(1))
    print(slider_mount.get_position())
    slider_mount.disconnect()
    print(slider_mount.is_connected())

# if __name__ == "__main__":

#     slider_mount = ELL6(port="COM10", address=[10])
#     slider_mount.connect()
#     print(slider_mount.get_address())
#     print(slider_mount.is_connected())
#     print(slider_mount.move_to(1))
#     print(slider_mount.get_position())
#     slider_mount.disconnect()
#     print(slider_mount.is_connected())

    
# if __name__ == "__main__":

#     rotation_mount = ELL14(port="COM9", address=[5])
#     rotation_mount.connect()
#     print(rotation_mount.get_address())
#     print(rotation_mount.get_position())    
#     print(rotation_mount.is_connected())
#     rotation_mount.move_to(90)
#     rotation_mount.move_by(90)
#     rotation_mount.disconnect()
#     print(rotation_mount.is_connected())





