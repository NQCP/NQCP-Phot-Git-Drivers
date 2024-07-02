import toptica.lasersdk.dlcpro.v3_0_1 as toptica

class Toptica_CTL950():  # Developer: Magnus Linnet Madsen

    def get_id(self):
        return "toptica_dlcpro01"

    def __init__(self):
        print("initalising laser")
        self.laser = None

    def __del__(self):
        self.disconnect()

    def connect(self, IP_address='10.209.67.103'):
        self.laser = toptica.DLCpro(toptica.NetworkConnection(IP_address))

    def set_diode(self, enable_bool):
        self.laser.laser1.dl.cc.enabled.set(enable_bool)

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

    def set_wavelength(self, wavelength_nm: float):
        """
        Set wavelength [nm] of the laser
        @param wavelength_nm: wavelength of the laser [nm]
        @return: None
        """

        self.wavelength_nm_set = wavelength_nm
        if wavelength_nm < 910 or wavelength_nm > 980:
            print('ERROR in Toptica->SetWavelength: wavelength range exceeded')
            return None

        self.laser.laser1.ctl.wavelength_set.set(float(wavelength_nm))

        return None

    def get_power(self):
        """
        Return the power [mW] of the laser
        @rtype: float
        @return: power of the laser [mW]
        """
        return self.laser.laser1.ctl.power.power_act.get()

    def set_power(self, power_mW: float):
        """
        Set the power [mW] of the laser
        @param power_mW: power of the laser [mW]
        @return: None
        """
        if power_mW is not None:
            self.power_mW_set = power_mW
            self.laser.laser1.power_stabilization.setpoint.set(power_mW)
        return None

    def get_emission_status(self) -> bool:
        """
        Return a boolean emission status of the Toptica CTL950 laser
        @rtype: bool
        @return: emission status of type (True) if the laser is on and (False) if the laser is off.
        """
        return self.laser.emission.get()

    def get_power_stabilization(self):
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

    def play_welcome(self):
        self.laser.buzzer.play_welcome()


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


if __name__ == "__main__":
    laser = Toptica_CTL950()
    laser.connect()
    laser.set_wavelength(940)
    laser.enable_emission()
    laser.set_power_stabilization(True)
    laser.set_power(1)
