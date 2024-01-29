import json

from Instruments.Settings.Console_Controller import Console_Controller
from Instruments.Settings.Savable import Savable


class Settings_Controller:

    def __init__(self, savable: Savable):
        """
        :param savable: The savable to use for saving or loading settings
        """
        self.savable = savable

    def save_settings(self, folder_path: str, file_name: str):
        """
        Saves the settings of the savable object
        :param folder_path: folder path to save the settings file
        :param file_name: file name to save the settings
        :return:
        """

        try:
            if self.savable is None:
                raise ConnectionError("Savable is None")

            if not self.savable.get_is_connected():
                raise ConnectionError("Savable is not connceted")

            path = self.get_settings_path(folder_path, file_name)
            settings = self.savable.get_settings()
            self.__save_settings(settings, path)
            Console_Controller.print_message("Successfully saved settings")
        except Exception as error:
            Console_Controller.print_message(error)

    def load_settings(self, folder_path: str, file_name: str):
        """
        Loads the settings of the savable object from the folder path and file name
        :param folder_path: folder path to load the settings
        :param file_name: file name to load the settings
        :return:
        """
        try:
            if self.savable is None:
                raise ConnectionError("Savable is None")

            if not self.savable.get_is_connected():
                raise ConnectionError("Savable is not connected")

            path = self.get_settings_path(folder_path, file_name)
            settings = self.__load_settings(path)
            self.savable.set_settings(settings)
            Console_Controller.print_message("Successfully loaded settings")
        except Exception as error:
            Console_Controller.print_message(error)

    @staticmethod
    def __save_settings(settings: dict, path: str) -> None:
        """
        Saves settings at the path
        :param settings: settings to be saved
        :param path: path to save the settings
        :return:
        """
        with open(path, "w") as text_file:
            json.dump(settings, text_file)

    @staticmethod
    def __load_settings(path: str) -> dict:
        with open(path, "r") as text_file:
            settings = json.load(text_file)
        return settings

    @staticmethod
    def get_settings_path(folder_path: str, file_name: str) -> str:
        return folder_path + file_name
