#!/usr/bin/env python


import numpy as np
import pyvisa

class Thorlabs_PM100U():

    def __init__(self, resource_manager: pyvisa.ResourceManager, port: str) -> None:
        """Connect to and reset Thorlabs PM101USB"""        
        self.resource_manager = resource_manager
        self.port = port
        self.powerMeter = None
        

    def is_alive(self) -> bool:
        return bool(self.get_idn())

    def get_idn(self) -> str:
        return self._write('*IDN?')

    def get_averaging(self) -> int:
        """Get the averaging"""
        msg = ':SENS:AVER?'
        self._write(msg)
        return int(self._read())

    def set_averaging(self, average: int) -> None:
        """Get the averaging"""
        msg = ':SENS:AVER ' + str(average)
        self._write(msg)

    def set_config_power(self) -> None:
        msg = ':SENS:CONF:POW'
        self._write(msg)

    def set_auto_range(self, auto_range: str ='ON') -> None:
        msg = ':SENS:POW:RANG:AUTO ' + auto_range
        self._write(msg)

    def set_beam(self, beam: str ='MIN') -> None:
        """Set the wavelength in nm"""
        msg = ':SENS:CORR:BEAM ' + beam
        self._write(msg)

    def set_detector_wavelength(self, wavelength_nm: float):
        """Set the wavelength in nm"""
        msg = ':SENS:CORR:WAV ' + str(wavelength_nm)
        self._write(msg)

    def set_units(self, unit: str) -> None:
        """Set the units to W or dBm"""
        msg = ':SENS:POW:UNIT ' + unit
        self._write(msg)

    def get_units(self) -> str:
        """Set the units to W or dBm"""
        msg = ':SENS:POW:UNIT?'
        self._write(msg)
        return self._read()

    def get_detector_power(self) -> float:
        """Get a power measurement"""
        msg = ':READ?'
        self._write(msg)
        return float(self._read())

    def get_detector_wavelength(self) -> float:
        msg = ':SENS:CORR:WAV?'
        self._write(msg)
        return float(self._read())

    def reset(self) -> None:
        """Reset"""
        self._write('*RST')
        
    def connect(self) -> None:
        self.powerMeter = self.resource_manager.open_resource(self.port)

    def disconnect(self) -> None:
        """End communication"""
        self.powerMeter.close()

#################################### PRIVATE METHODS ###########################################

    def _write(self,command: str) -> None:
        self.powerMeter.write(command)

    def _read(self) -> str:
        response = self.powerMeter.read()
        response = response.replace('\n', '').replace('\r', '')
        return response
