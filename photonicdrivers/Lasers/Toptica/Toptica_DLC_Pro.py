import toptica.lasersdk.dlcpro.v3_0_1 as toptica

class Toptica_DLC_PRO_driver():  # Developer: Magnus Linnet Madsen

    def __init__(self, ip_address = '10.209.67.103'):
        # The IP of the Toptica CTL in KK4 is '10.209.67.103'
        self.ip_address = ip_address
        self.laser_controller = toptica.DLCpro(toptica.NetworkConnection(self.ip_address))

    def __del__(self):
        self.disconnect()

    def connect(self):
        self.laser_controller.open()

    def set_scan_mode(self, enable_bool):
        self.laser_controller.laser1.scan.enabled.set(enable_bool)

    def get_scan_mode(self):
        self.laser_controller.laser1.scan.enabled.get()

    def set_scan_amplitude(self, scan_amplitude):
        self.laser_controller.laser1.scan.amplitude.set(scan_amplitude)

    def get_scan_amplitude(self):
        self.laser_controller.laser1.scan.amplitude.get()

    def set_scan_offset(self, offset):
        self.laser_controller.laser1.scan.offset.set(offset)

    def get_scan_offset(self):
        self.laser_controller.laser1.scan.offset.get()

    def set_wide_scan_continuous_mode(self, enable_bool):
        self.laser_controller.laser1.wide_scan.continuous_mode.set(enable_bool)

    def get_wide_scan_continuous_mode(self):
        self.laser_controller.laser1.wide_scan.continuous_mode.get()

    def set_wide_scan_offset(self, offset):
        self.laser_controller.laser1.wide_scan.offset(offset)

    def get_wide_scan_offset(self):
        self.laser_controller.laser1.wide_scan.offset.get()

    def set_wide_scan_amplitude(self, amplitude):
        self.laser_controller.laser1.wide_scan.amplitude(amplitude)

    def get_wide_scan_amplitude(self):
        self.laser_controller.laser1.wide_scan.amplitude.get()

    def get_wide_scan_begin(self):
        self.laser_controller.laser1.wide_scan.scan_end()

    def get_wide_scan_begin(self):
        self.laser_controller.laser1.wide_scan.scan_begin()

    def disconnect(self):
        """
        Closes the connections to the Toptica laser
        """
        self.laser_controller.close()

    def set_diode(self, enable_bool):
        self.laser_controller.laser1.dl.cc.enabled.set(enable_bool)

    def get_wavelength(self):
        """
        Returns the wavelength [nm] of the laser
        @rtype: float
        @return: wavelength [nm]
        """
        return self.laser_controller.laser1.ctl.wavelength_act.get()

    def set_wavelength(self, wavelength_nm: float):
        """
        Set wavelength [nm] of the laser
        @param wavelength_nm: wavelength of the laser [nm]
        @return: None
        """

        self.laser_controller.laser1.ctl.wavelength_set.set(float(wavelength_nm))

        return None

    def get_power(self):
        """
        Return the power [mW] of the laser
        @rtype: float
        @return: power of the laser [mW]
        """
        return self.laser_controller.laser1.ctl.power.power_act.get()

    def set_power(self, power_mW: float):
        """
        Set the power [mW] of the laser
        @param power_mW: power of the laser [mW]
        @return: None
        """
        if power_mW is not None:
            self.power_mW_set = power_mW
            self.laser_controller.laser1.power_stabilization.setpoint.set(power_mW)
        return None

    def get_emission_status(self) -> bool:
        """
        Return a boolean emission status of the Toptica CTL950 laser
        @rtype: bool
        @return: emission status of type (True) if the laser is on and (False) if the laser is off.
        """
        return self.laser_controller.emission.get()

    def get_power_stabilization(self):
        """
        Return a boolean power stabilization status of the Toptica CTL950 laser
        @rtype: bool
        @return:power stabilization status of type (True) if the stabilization is on and (False) if the stabilization is off.
        """
        return self.laser_controller.laser1.power_stabilization.enabled.get()

    def set_power_stabilization(self, power_stabilization: bool):
        """
        Set the power stabilization of the Toptica CTL950 laser
        :param power_stabilization:
        :return: None
        """
        self.laser_controller.laser1.power_stabilization.enabled.set(power_stabilization)
        return None

    def play_welcome(self):
        """
        Playes a small bib bib bib song from the CTL
        """
        self.laser_controller.buzzer.play_welcome()


    def get_power_stabilization_parameters(self):
        """
        Set the power stabilization of the Toptica CTL950 laser
        :param power_stabilization:
        :return: None
        """
        gain = self.laser_controller.laser1.power_stabilization.gain.all.get()
        p = self.laser_controller.laser1.power_stabilization.gain.p.get()
        i = self.laser_controller.laser1.power_stabilization.gain.i.get()
        d = self.laser_controller.laser1.power_stabilization.gain.d.get()
        return gain, p, i, d

    def set_power_stabilization_parameters(self, p, i, d=0, gain=1):
        """
        Set the power stabilization of the Toptica CTL950 laser
        :return: None
        """
        self.laser_controller.laser1.power_stabilization.gain.all.set(gain)
        self.laser_controller.laser1.power_stabilization.gain.p.set(p)
        self.laser_controller.laser1.power_stabilization.gain.i.set(i)
        self.laser_controller.laser1.power_stabilization.gain.d.set(d)
        return None
