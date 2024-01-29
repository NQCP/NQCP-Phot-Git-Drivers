import toptica.lasersdk.dlcpro.v3_0_1 as toptica

from Instruments.Savable import Savable


class Toptica_CTL950(Savable):  # Developer: Magnus Linnet Madsen

    def __init__(self, IP_address='192.168.1.100'):
        self.laser = toptica.DLCpro(toptica.NetworkConnection(IP_address))

    def __del__(self):
        self.disconnect()

    def connect(self):
        """
        Opens the connections to the Toptica laser
        """
        self.laser.open()

    def disconnect(self):
        """
        Closes the connections to the Toptica laser
        """
        self.laser.close()

    def get_wavelength(self):
        """
        Returns the wavelength [nm] of the laser
        @rtype: float
        @return: wavelength [nm]
        """
        return self.laser.laser1.ctl.wavelength_act.get()

    def get_wavelength_set(self):
        """
        Returns the wavelength [nm] of the laser
        @rtype: float
        @return: wavelength [nm]
        """
        return self.wavelength_set_nm

    def set_wavelength(self, wavelength_nm: float):
        """
        Set wavelength [nm] of the laser
        @param wavelength_nm: wavelength of the laser [nm]
        @return: None
        """
        self.wavelength_set_nm = wavelength_nm
        return None

    def set_wavelength_set(self, wavelength_nm: float):
        """
        Set wavelength [nm] of the laser
        @param wavelength_nm: wavelength of the laser [nm]
        @return: None
        """
        self.wavelength_set_nm = wavelength_nm
        return None

    def get_power(self):
        """
        Return the power [W] of the laser
        @rtype: float
        @return: power of the laser [W]
        """
        return self.laser.laser1.ctl.power.power_act.get()

    def set_power(self, power_mW: float):
        """
        Set the power [mW] of the laser
        @param power_mW: power of the laser [mW]
        @return: None
        """
        self.power_set = power_mW
        self.set_power_stabilization_status(True)
        self.laser.laser1.power_stabilization.setpoint.set(power_mW)
        return None

    def get_emission_status(self) -> bool:
        """
        Return a boolean emission status of the Toptica CTL950 laser
        @rtype: bool
        @return: emission status of type (True) if the laser is on and (False) if the laser is off.
        """
        return self.laser.emission.get()

    def print_emission_status(self):
        if self.get_emission_status():
            print("Emission status: The Toptica laser is on and emitting light")
        else:
            print("Emission status: The Toptica laser is off and not emitting any light")

    def get_power_stabilization_status(self):
        """
        Return a boolean power stabilization status of the Toptica CTL950 laser
        @rtype: bool
        @return:power stabilization status of type (True) if the stabilization is on and (False) if the stabilization is off.
        """
        return self.laser.laser1.power_stabilization.enabled.get()

    def set_power_stabilization(self, power_stabilization: bool):
        """
        Set the power stabilization of the Toptica CTL950 laser
        :param power_stabilization:
        :return: None
        """
        self.laser.laser1.power_stabilization.enabled.set(power_stabilization)
        return None

    def get_power_stabilization_parameters(self):
        """
        Set the power stabilization of the Toptica CTL950 laser
        :param power_stabilization:
        :return: None
        """
        gain = self.laser.laser1.power_stabilization.gain.all.get()
        p = self.laser.laser1.power_stabilization.gain.p.get()
        i = self.laser.laser1.power_stabilization.gain.i.get()
        d = self.laser.laser1.power_stabilization.gain.d.get()
        return gain, p, i, d

    def set_power_stabilization_parameters(self, p, i, d=0, gain=1):
        """
        Set the power stabilization of the Toptica CTL950 laser
        :return: None
        """
        self.laser.laser1.power_stabilization.gain.all.set(gain)
        self.laser.laser1.power_stabilization.gain.p.set(p)
        self.laser.laser1.power_stabilization.gain.i.set(i)
        self.laser.laser1.power_stabilization.gain.d.set(d)
        return None

    @staticmethod
    def get_min_wavelength():
        """
        :return: Return the minimum wavelength of type integer (int) in units of nano meters [nm] 
        """
        return 910

    @staticmethod
    def get_max_wavelength() -> int:
        """
        :return: Return the maximum wavelength of type integer (int) in units of nano meters [nm] 
        """
        return 980

    @staticmethod
    def get_min_power():
        """
        :return: Return the minimum power of the Toptica CTL950 laser of type integer (int) in units of milli watts [mW] 
        """
        return 0

    @staticmethod
    def get_max_power():
        """
        :return: Return the maximum power of the Toptica CTL950 laser of type integer (int) in units of milli watts [mW] 
        """
        return

    def set_settings(self, settings: dict) -> None:
        self.set_wavelength(settings["wavelength_nm"])
        self.set_power(settings["power_mW"])

    def get_settings(self) -> dict:
        return {
            "wavelength_nm": self.get_wavelength(),
            "power_mW": self.get_power()
        }
