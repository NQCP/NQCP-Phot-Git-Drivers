from abc import ABC, abstractmethod


class Savable(ABC):

    @abstractmethod
    def get_settings(self) -> dict:
        """
        Returns the settings of the Savable
        :return: settings of type (dict)
        """
        pass

    @abstractmethod
    def set_settings(self, settings: dict) -> None:
        """
        Sets the settings of the Savable
        :param settings: set the settings (dict) of the (Savable)
        """
        pass

    @abstractmethod
    def get_is_connected(self) -> None:
        """
        Sets the settings of the Savable
        :param settings: set the settings (dict) of the (Savable)
        """
        pass
