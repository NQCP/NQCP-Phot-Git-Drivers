
from abc import abstractmethod, ABC
from photonicdrivers.Abstract.Connectable import Connectable

class Thorlabs_Power_Meter_Driver(Connectable):

    @abstractmethod
    def get_power(self):
        pass

    @abstractmethod
    def set_wavelength(self, wavelength_nm: float):
        pass

    @abstractmethod
    def set_auto_range(auto_range):
        pass

    @abstractmethod
    def get_wavelength(self):
        pass

    @abstractmethod
    def set_averaging(self, average: int):
        pass

    @abstractmethod
    def get_averaging(self):
        pass

    @abstractmethod
    def set_auto_range(self):
        pass

    @abstractmethod
    def get_units(self):
        pass

    @abstractmethod
    def set_units(self, unit):
        pass

    @abstractmethod
    def set_beam(self, beam):
        pass

    @abstractmethod
    def reset(self):
        pass
  
    @abstractmethod
    def zero(self):
        pass