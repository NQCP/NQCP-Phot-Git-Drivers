from pylablib.devices.Thorlabs.elliptec import ElliptecMotor
from photonicdrivers.Abstract.Connectable import Connectable

class Elliptec_Driver(Connectable):
    """
    Class for controlling ELL14 rotation stage.
    """

    def __init__(self, port, addresses):
        """
        Initializes the ELL14 instance with the specified port and address.

        Args:
            port (str): The connection port for the rotation stage.
            address (str): The address of the rotation stage (default is 'all'). Must be between 0 and 15. Addresses above 10 represent letters (A, B, C, D, E, F) but cannot be used.
        """
        self.port = port
        self.addresses = addresses
        self.driver: ElliptecMotor = None

    def connect(self) -> None:
        """
        Establishes a connection to the ELL6 rotation stage.
        """
        self.driver = ElliptecMotor(conn=self.port, addrs=self.addresses)

    def disconnect(self) -> None:
        """
        Closes the connection to the ELL6 rotation stage.
        """
        self.driver.close()
        self.driver = None

    def is_connected(self) -> bool:
        """
        Checks if a connection to the ELL6 rotation stage is established.

        Returns:
            bool: True if connected, False otherwise.
        """
        try:
            self.driver.get_full_status()
            return True
        except Exception:
            return False

    def get_address(self) -> list:
        """
        Retrieves the connected addresses for the rotation stage.

        Returns:
            list: List of connected addresses.
        """
        return self.driver.get_connected_addrs()
    

    def get_position(self, address) -> float:
        return self.driver.get_position(addr=address)

    def move_to(self, position: int, address) -> None:
        self.driver.move_to(position=position, addr=address)

    def move_by(self, angle: float, address) -> None:
        self.driver.move_by(distance=angle, addr=address)

    def home(self, address=None) -> None:
        self.driver.home(addr=address)
  
  




