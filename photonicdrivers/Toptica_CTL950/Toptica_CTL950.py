import json

import nest_asyncio
import toptica.lasersdk.dlcpro.v2_4_0 as toptica
import time


class Toptica_CTL950:  # developer: Fabian Ruf, Magnus Madsen

    def __init__(self, settings_path, IP_address='192.168.1.100'):
        self.settings_path = settings_path
        nest_asyncio.apply()
        self.laser = toptica.DLCpro(toptica.NetworkConnection(IP_address))
        self.laser.open()
        self.onoff = True
        self.is_alive()
        self.power_set = None
        self.power_on_off = None
        self.wavelength_set = None

        self.load_settings()

    def __enter__(self):
        return self

    def is_alive(self):
        is_alive = True
        if is_alive != 0:
            print("Toptica Laser is alive")

    def get_emission_status(self) -> bool:
        """
        Return the emission statu (True) on and (False) off
        @rtype: bool
        @return: emission status (True) on and (False) off
        """
        return self.laser.emission.get()

    def print_emission_status(self):
        if self.get_emission_status():
            print("Emission status: The Toptica laser is on and emitting light")
        else:
            print("Emission status: The Toptica laser is off and not emitting any light")

    def get_power_stabilization_status(self):
        return self.laser.laser1.power_stabilization.enabled.get()

    def set_power_stabilization_status(self, enabled=True):
        self.laser.laser1.power_stabilization.enabled.set(enabled)
        return None

    def get_power_stabilization_parameters(self):
        gain = self.laser.laser1.power_stabilization.gain.all.get()
        p = self.laser.laser1.power_stabilization.gain.p.get()
        i = self.laser.laser1.power_stabilization.gain.i.get()
        d = self.laser.laser1.power_stabilization.gain.d.get()
        return gain, p, i, d

    def set_power_stabilization_parameters(self, p, i, d=0, gain=1):
        self.laser.laser1.power_stabilization.gain.all.set(gain)
        self.laser.laser1.power_stabilization.gain.p.set(p)
        self.laser.laser1.power_stabilization.gain.i.set(i)
        self.laser.laser1.power_stabilization.gain.d.set(d)
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

    def get_wavelength(self):
        """
        Returns the wavelength [nm] of the laser
        @rtype: float
        @return: wavelength [nm]
        """
        return self.laser.laser1.ctl.wavelength_act.get()

    def get_wavelength_set(self):
        return self.wavelength_set

    def get_power_set(self):
        return self.power_set

    def set_wavelength(self, wavelength_nm: float):
        """
        Set wavelength [nm] of the laser
        @param wavelength_nm: wavelength of the laser [nm]
        @return: None
        """

        delta = 0.01
        t = 0
        delta_t = 0.05
        t_wait = delta_t
        t_max = 10
        self.wavelength_set = wavelength_nm
        if wavelength_nm < 910 or wavelength_nm > 980:
            print('ERROR in Toptica->SetWavelength: wavelength range exceeded')
            return None

        self.laser.laser1.ctl.wavelength_set.set(float(wavelength_nm))

        while abs(self.get_wavelength() - wavelength_nm) > delta:
            time.sleep(delta_t)
            t = t + delta_t;

            if t > t_max:
                print('ERROR in Toptica->SetWavelength: max time exceeded')
                break

        time.sleep(t_wait)
        t = t + t_wait;
        print(wavelength_nm, t, abs(self.get_wavelength() - wavelength_nm), sep=' --- ')

        return None

    def get_current(self):
        """
        Return the current [mA] of the laser
        @rtype: float
        @return: power of the laser [mA]
        """
        return self.laser.laser1.dl.cc.current_act.get()

    def set_current(self, current_mA: float):
        """
        Set the current [mA] of the laser
        @param current: current of the laser [mA]
        @return: None
        """
        if current_mA > 160:
            print('ERROR in Toptica->SetWavelength: current range exceeded')
            return None

        self.laser.laser1.dl.cc.current_set.set(float(current_mA))
        return None

    def toggle_laser(self):
        if self.onoff:
            self.power_on_off = self.power_set
            self.set_power(0)
            self.onoff = not self.onoff
        else:
            self.set_power(self.power_on_off)
            self.onoff = not self.onoff

    def close(self):
        """
        Closes the connection to the laser
        """
        self.save_settings()
        self.laser.close()

    def open(self):
        """
        Opens the connection to the laser
        """
        self.laser.open()
        self.load_settings()

    def get_name(self):
        return "Toptica Laser"

    def load_settings(self):
        with open(self.settings_path, "r") as text_file:
            settings_dict = json.load(text_file)
            self.wavelength_set = settings_dict["wavelength"]
            self.power_on_off = settings_dict["power"]
            self.set_wavelength(self.wavelength_set)
            self.set_power(self.power_on_off)

    def save_settings(self):
        dictionary = {
            "wavelength": self.wavelength_set,
            "power": self.power_on_off
        }

        with open(self.settings_path, "w") as text_file:
            json.dump(dictionary, text_file)

    def get_min_wavelength(self):
        return 910

    def get_max_wavelength(self):
        return 980

    def get_min_power(self):
        return 0

    def get_max_power(self):
        return 80