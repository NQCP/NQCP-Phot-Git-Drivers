#!/usr/bin/env python


import numpy as np
import pyvisa

class Thorlabs_PM100U():

    def __init__(self, resource_manager, port):
        """Connect to and reset Thorlabs PM101USB"""

        self.meter = None
        self.detector_power_get = None
        self.detector_wavelength_set = None
        self.averaging_set = None
        self.resource_manager = resource_manager
        self.port = port
        

    def is_alive(self):
        is_alive = self.meter.write('*IDN?')
        if is_alive != 0:
            print("Thorlabs detector " + self.port + " is alive")
        return is_alive

    def zero(self):
        """Zero the sensor"""
        # msg = ':INIT'
        # self.meter.write(msg)
        msg = ':SENS:CORR:COLL:ZERO'
        self.meter.write(msg)
        wait = 0
        while (not wait):
            self.meter.write('*OPC?')
            wait = self.meter.read()

    def get_averaging(self):
        """Get the averaging"""
        msg = ':SENS:AVER?'
        self.meter.write(msg)
        message = self.meter.read()
        print(int(message.replace('\n', '').replace('\r', '')))
        return int(message.replace('\n', '').replace('\r', ''))

    def set_averaging(self, average):
        """Get the averaging"""
        msg = ':SENS:AVER %s' % (str(int(average)))
        self.averaging_set = int(average)
        self.meter.write(msg)

    def set_config_power(self):
        msg = ':SENS:CONF:POW'
        self.meter.write(msg)

    def set_auto_range(self, auto_range='ON'):
        msg = ':SENS:POW:RANG:AUTO %s' % (str(auto_range))
        self.meter.write(msg)

    def set_beam(self, beam='MIN'):
        """Set the wavelength in nm"""
        msg = ':SENS:CORR:BEAM %s' % (str(beam))
        self.meter.write(msg)

    def set_detector_wavelength(self, wavelength_nm):
        """Set the wavelength in nm"""
        self.set_detector_wavelength_set(wavelength_nm)
        msg = ':SENS:CORR:WAV %s' % (str(self.detector_wavelength_set))
        self.meter.write(msg)

    def set_units(self, unit_str):
        """Set the units to W or dBm"""
        msg = ':SENS:POW:UNIT %s' % (unit_str)
        self.meter.write(msg)

    def get_units(self):
        """Set the units to W or dBm"""
        msg = ':SENS:POW:UNIT?'
        self.meter.write(msg)
        return self.meter.read().replace('\n', '').replace('\r', '')

    def get_detector_power(self):
        """Get a power measurement"""
        power_res = 2e1
        msg = ':READ?'
        power_list = []
        while (power_res > 1e1):
            for index in range(0, 1):
                self.meter.write(msg)
                power_str = self.meter.read()
                power = float(power_str[0:-1])
                if power < 0:
                    power = 1e-12
                power_list.append(power)
            print(power_list)
            power_res = np.median(power_list)
        self.detector_power_get = power_res
        return power_res

    def get_detector_wavelength(self):
        msg = ':SENS:CORR:WAV?'
        self.meter.write(msg)
        self.meter.write(msg)
        wavelength_str = self.meter.read()

        return float(wavelength_str.replace('\n', '').replace('\r', ''))

    def reset(self):
        """Reset"""
        self.meter.write('*RST')
        self.meter.write('*CLS')

    def connect(self) -> None:
        self.meter = self.resource_manager.open_resource(self.port)
        self.is_alive()
        self.set_beam()
        self.set_auto_range()
        self.meter.write(':CONF:POW')  # configure for power

    def disconnect(self):
        """End communication"""

        try:
            self.meter.close()
        except Exception as error:
            print(error)

if __name__ == "__main__":
    resource_manager = pyvisa.ResourceManager()
    print(resource_manager.list_resources())
    power_meter = Thorlabs_PM100U(resource_manager, 'USB0::0x1313::0x8078::P0045344::0::INSTR')
    power_meter.connect()
    print(power_meter.get_detector_power())
    print(power_meter.get_detector_wavelength())
    print(power_meter.get_units())
    print(power_meter.get_averaging())
    power_meter.disconnect()


