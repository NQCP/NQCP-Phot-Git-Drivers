import clr
import sys

assembly_path = r".\dll_files"  # find .dll file
sys.path.append(assembly_path)
ref = clr.AddReference(r"Santec_FTDI")

import Santec_FTDI as ftdi

class Santec_TSL570():  # Developer: Magnus Linnet Madsen

    def __init__(self, _serial_number):
        # The serial_number of the TSL570 is '24040112'
        print("initalising laser")
        self.serial_number = _serial_number

    def __del__(self):
        self.disconnect()

    def connect(self):
        ftdi.FTD2xx_helper(self.serial_number)

    def disconnect(self):
        """
        Closes the connections to the Toptica laser
        """
        self.laser_controller.close()
    
    def get_idn(self) -> str:
        return self.QueryIdn()
    
    def get_wavelength(self):
        """
        Returns the wavelength [nm] of the laser
        @rtype: float
        @return: wavelength [nm]
        """
        msg = ':WAV?'
        return self.Query(msg)
    
    def set_wavelength(self, wavelength_nm: float):
        """
        Set wavelength [nm] of the laser
        @param wavelength_nm: wavelength of the laser [nm]
        @return: None
        """

        msg = ':WAVelength  ' + str(wavelength_nm) + 'e-9'
        return self.Query(msg)

