
from abc import abstractmethod, ABC
class Thorlabs_Power_Meter_Driver(ABC):

    @abstractmethod
    def connect(self):
        """
        Establishes a connection to the power meter.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Disconnects from the power meter.

        Raises:
            NotImplementedError: This method must be overridden in a subclass.
        """
        pass

    @abstractmethod
    def get_detector_power(self):
        pass

    @abstractmethod
    def set_wavelength(self):
        pass

    @abstractmethod
    def get_wavelength(self):
        pass

    @abstractmethod
    def set_averaging(self):
        pass

    @abstractmethod
    def get_averaging(self):
        pass