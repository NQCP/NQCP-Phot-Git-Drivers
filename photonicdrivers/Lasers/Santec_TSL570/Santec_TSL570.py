import clr
import sys

assembly_path = r".\dll_files"  # find .dll file
sys.path.append(assembly_path)
ref = clr.AddReference(r"Santec_FTDI")

import Santec_FTDI as ftdi

class Santec_TSL570_driver():  # Developer: Magnus Linnet Madsen

    def __init__(self, _serial_number='24040112'):
        # The serial_number of the TSL570 is '24040112'
        print("initalising laser")
        self.serial_number = _serial_number

    def connect(self):
        self.laser = ftdi.FTD2xx_helper(self.serial_number)
        print("connecting to laser")
        
    def disconnect(self):
        """
        Closes the connections to the laser
        """
        print("closing laser")
        self.laser.CloseUsbConnection()
    
    def get_idn(self):
        idn_query = self.laser.QueryIdn()
        print('\n' + idn_query)
    
    def get_wavelength(self):
        """
        Returns the wavelength [nm] of the laser
        @rtype: float
        @return: wavelength [nm]
        """
        msg = ':WAV?'
        return self.laser.Query(msg)
    
    def set_wavelength(self, wavelength_nm: float):
        """
        Set wavelength [nm] of the laser
        @param wavelength_nm: wavelength of the laser [nm]
        @return: None
        """

        msg = ':WAVelength  ' + str(wavelength_nm) + 'e-9'
        self.laser.Write(msg)
        
        
    def set_power(self, power_dBm: float):
        """
        Set power [dBm] of the laser
        """
        power_dBm_decimal = '{:.2e}'.format(power_dBm)
        msg = ':POW ' + str(power_dBm_decimal) 
        self.laser.Write(msg)
        
    def get_power(self, power_dBm: float):
        """
        Get power [dBm] of the laser
        """
        msg = ':POW?' 
        return self.laser.Query(msg)
        
    def set_emission_status(self, emission: int):
        """
        Set laser emission ON or OFF 
        """
        msg = ':POW:STAT ' + str(emission) 
        self.laser.Write(msg)
        
    def get_emission_status(self):
        """
        Set laser emission ON or OFF 
        """
        msg = ':POW:STAT?'
        return self.laser.Query(msg)
        

