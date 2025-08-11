
from abc import abstractmethod, ABC
from photonicdrivers.Abstract.Connectable import Connectable

class Thorlabs_Power_Meter_Driver(Connectable):

    @abstractmethod
    def get_power(self) -> float:
        pass

    @abstractmethod
    def set_wavelength(self, wavelength_nm: float):
        pass

    @abstractmethod
    def set_auto_range(self, auto_range_bool: bool):
        pass

    @abstractmethod
    def get_wavelength(self) -> float:
        pass

    @abstractmethod
    def set_averaging(self, average: int):
        pass

    @abstractmethod
    def get_averaging(self) -> int:
        pass

    @abstractmethod
    def get_power_unit(self) -> str:
        pass

    @abstractmethod
    def set_power_unit(self, power_unit: str):
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