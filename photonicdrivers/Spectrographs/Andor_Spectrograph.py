from photonicdrivers.Spectrographs.Andor_Kymera import Andor_Kymera
from photonicdrivers.Spectrographs.Andor_Newton import Andor_Newton

class Andor_Spectrograph():

    def __init__(self, spectrograph: Andor_Kymera, camera: Andor_Newton):
        self.spectrograph: Andor_Kymera = spectrograph
        self.camera: Andor_Newton = camera
        self.calibration = None
        
    def load_settings(self) -> dict:
        pass

    def save_settings(self, settings: dict) -> None:
        pass

    def load_calibration(path):
        pass

    def calibration(pixel_list, center_wavelength):
        return
