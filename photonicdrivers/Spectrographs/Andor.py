
from photonicdrivers.Controller.Instruments.Settings.Console_Controller import Console_Controller
from pyAndorSpectrograph.spectrograph import ATSpectrograph


class Andor():

    def __init__(self):
        Console_Controller.print_message("Initialising Spectrograph")
        self.device_index = 0
        self.spectrograph = ATSpectrograph()  # Load the ATSpectrograph library

    def load_settings(self) -> dict:
        pass

    def save_settings(self, settings: dict) -> None:
        pass

    def get_id(self) -> None:
        (ret, serial) = self.spectrograph.GetSerialNumber(self.device_index, 64)
        Console_Controller.print_message("Function get_id returned {}".format(self.spectrograph.GetFunctionReturnDescription(ret, 64)[1]))
        Console_Controller.print_message("\tSerial No: {}".format(serial))
        return serial

    def connect(self) -> None:
        shm = self.spectrograph.Initialize("")
        Console_Controller.print_message("Function connect returned {}".format(self.spectrograph.GetFunctionReturnDescription(shm, 64)[1]))

    def disconnect(self) -> None:
        ret = self.spectrograph.Close()
        Console_Controller.print_message("Function disconnet returned {}".format(self.spectrograph.GetFunctionReturnDescription(ret, 64)[1]))
