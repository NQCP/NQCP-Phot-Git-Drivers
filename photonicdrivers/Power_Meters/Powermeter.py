from abc import ABC, abstractmethod

class PowerMeter(ABC):

    @abstractmethod
    def get_detector_power(self):
        pass

        