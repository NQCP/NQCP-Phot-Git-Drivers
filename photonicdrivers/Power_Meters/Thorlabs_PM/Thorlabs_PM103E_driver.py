
from anyvisa import AnyVisa
import numpy as np
from photonicdrivers.utils.execution_time import execution_time

"""
Class for interfacing with Thorlab powermeters.
Supported models: PM103E
Supported units: {'W', 'mW', 'dBm'}
Anyvisa: Navigate to the folder with the anyvisa .whl file and write "pip install anyvisa-0.3.0-py3-none-any.whl"


TCPIP0::10.209.67.184::PM103E-4E_M01027537::INSTR
TCPIP0::10.209.67.196::PM103E-A0_M01080977::INSTR
"""



class Thorlabs_PM103E_driver():

    def __init__(self, port: str) -> None:
        """Connect to and reset Thorlabs PM101USB"""     
        self.port = port 
        self.power_meter = None
        self.is_connected = False
        

#################################### HIGH LEVEL METHODS ###########################################

    def get_median_power(self, n_median: int=10) -> float:
        # The instanteneous power measurement can be unstable, so it can be useful to use the median over multiple measurements if outliers is present
        measurements = np.zeros(n_median)
        for j in range(n_median):
            measurements[j] = self.get_detector_power()
        return np.median(measurements)

    def get_average_power(self, n_averages: int=10) -> float:
        # The instanteneous power measurement can be unstable, so it is better to average over multiple measurements. Conider using the median method.
        measurements = np.zeros(n_averages)
        for j in range(n_averages):
            measurements[j] = self.get_detector_power()
        return np.mean(measurements)

        
#################################### LOW LEVEL METHODS ###########################################

    def connect(self) -> None:
        """
        Opens the connections to the Thorlabs detector
        """
        if self.is_connected is False:
            self.power_meter = AnyVisa.TL_Open(self.port)
            self.power_meter.open()
            self.power_meter.write("CONF:POW")
            self.is_connected = True

    def disconnect(self) -> None:
        """
        Closes the connections to the Thorlabs detector
        """

        self.power_meter.close()

    def is_alive(self) -> bool:
        """
        Returns a boolean specifing wether the a connection to the device is established
        @rtype: boolean
        @return: is alive boolean
        """
        
        try:
            return self.get_idn()
        except ConnectionError:
            return False
        except Exception as exception:
            pass

    def get_idn(self) -> str:
        """
        Returns the response from the *IDN? command
        @rtype: string
        @return: response from the *IDN? command 
        """
        
        return self._query("*IDN?")

    def get_averaging(self) -> int:
        """
        Get the number of averaging of the detector
        @rtype: integer
        @return: the number of averaging of the detector
        """
        msg = ':SENS:AVER?'
        self._write(msg)
        return int(self._read())

    def set_averaging(self, average: int) -> None:
        """
        Set the number of averaging of the detector 
        @param average:
        @return: None
        """
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
        return self._query(msg)
    
    def get_detector_power(self) -> float:
        """Get a power measurement"""
        msg = "MEAS:SCAL:POW?"
        return self._query(msg)

    def get_detector_wavelength(self) -> float:
        msg = ':SENS:CORR:WAV?'
        return float(self._query(msg))

    def reset(self) -> None:
        """Reset"""
        self._write('*RST') 

    def get_auto_range(self):
        resp = self._query("SENS:POW:RANG:AUTO?")
        self.auto_range = bool(int(resp))
        return self.auto_range
    
    def set_auto_range(self, auto = True):
        if auto:
            self._write("SENS:POW:RANG:AUTO ON") # turn on auto range
        else:
            self._write("SENS:POW:RANG:AUTO OFF") # turn off auto range

    def get_zero_magnitude(self):
        resp = self._query("SENS:CORR:COLL:ZERO:MAGN?")
        self.zero_magnitude = float(resp)
        return self.zero_magnitude
        
    def get_zero_state(self): 
        resp = self._query("SENS:CORR:COLL:ZERO:STAT?")
        self.zero_state = bool(int(resp))
        return self.zero_state
    
    def run_zero(self):
        return self._write("SENS:CORR:COLL:ZERO:INIT")

#################################### PRIVATE METHODS ###########################################

    def _write(self,command: str) -> None:
        try:
            return self.power_meter.write(command)
        except Exception as exception:
            raise ConnectionError("An error occurred while writing to the power meter") from exception

    def _read(self) -> None:
        try:
            return self.power_meter.read()
        except Exception as exception:
            raise ConnectionError("An error occurred while reading the power meter") from exception
    
    def _query(self, command: str):
        try:
            return self.power_meter.query(command)
        except Exception as exception:
            raise ConnectionError("An error occurred while querying the power meter") from exception
