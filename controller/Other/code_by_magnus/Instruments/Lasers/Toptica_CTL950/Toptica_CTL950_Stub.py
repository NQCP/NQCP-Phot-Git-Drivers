

class Toptica_CTL950_Stub:  # Developer: Magnus Linnet Madsen

    def __init__(self, IP_address='192.168.1.100'):
        self.IP_address = IP_address
        self.wavelength_set_nm = 950

    def connect(self):
        """
        (Stub method) Opens the connections to the Toptica laser
        """
        pass

    def disconnect(self):
        """
        (Stub method) Closes the connections to the Toptica laser
        """
        pass

    def get_wavelength(self):
        """
        (Stub method) Returns the wavelength [nm] of the laser
        @rtype: float
        @return: wavelength [nm]
        """
        return self.wavelength_set_nm

    def get_wavelength_set(self):
        """
        (Stub method) Returns the wavelength [nm] of the laser
        @rtype: float
        @return: wavelength [nm]
        """
        return self.wavelength_set_nm

    def set_wavelength(self, wavelength_nm: float):
        """
        (Stub method) Set wavelength [nm] of the laser
        @param wavelength_nm: wavelength of the laser [nm]
        @return: None
        """
        self.wavelength_set_nm = wavelength_nm
        return None

    def set_wavelength_set(self, wavelength_nm: float):
        """
        (Stub method) Set wavelength [nm] of the laser
        @param wavelength_nm: wavelength of the laser [nm]
        @return: None
        """
        self.wavelength_set_nm = wavelength_nm
        return None
