from abc import ABC, abstractmethod


class Instrument(ABC):

    @abstractmethod
    def load_settings(self) -> dict:
        """
        Returns the settings of the Savable
        :return: settings of type (dict)
        """
        pass

    @abstractmethod
    def save_settings(self) -> None:
        """
        Sets the settings of the Savable
        """
        pass

    @abstractmethod
    def get_id(self) -> None:
        pass

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass
