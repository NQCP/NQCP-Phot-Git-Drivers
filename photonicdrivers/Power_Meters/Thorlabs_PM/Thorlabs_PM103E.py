
from anyvisa import AnyVisa
import numpy as np
from photonicdrivers.utils.execution_time import execution_time
"""
Class for interfacing with Thorlab powermeters.
Supported models: PM103E
Supported units: {'W', 'mW', 'dBm'}
Anyvisa: Navigate to the folder with the anyvisa .whl file and write "pip install anyvisa-0.3.0-py3-none-any.whl
"""


class Thorlabs_PM103E():

    def __init__(self, port: str = "TCPIP0::10.209.67.184::PM5020_07::INSTR") -> None:
        """Connect to and reset Thorlabs PM101USB"""     
        self.resource_manager = AnyVisa   
        self.port = port 
        self.power_meter = None
        

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

    @execution_time
    def connect(self) -> None:
        """
        Opens the connections to the Thorlabs detector
        """

        self.power_meter = self.resource_manager.TL_Open(self.port)
        self.power_meter.open()
        self.power_meter.write("CONF:POW")

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
        return bool(self.get_idn())

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
    
    @execution_time
    def get_detector_power(self) -> float:
        """Get a power measurement"""
        self.power_meter.write("ABOR") #aborts any ongoing measurments
        self.power_meter.write("INIT")
        res = float(self.power_meter.query("FETCH?"))
        return res

    def get_detector_wavelength(self) -> float:
        msg = ':SENS:CORR:WAV?'
        return float(self._query(msg))

    def reset(self) -> None:
        """Reset"""
        self._write('*RST') 

#################################### PRIVATE METHODS ###########################################

    def _write(self,command: str) -> None:
        self.power_meter.write(command)

    def _read(self) -> None:
        return self.power_meter.read()
    
    def _query(self, command: str) -> None:
        return self.power_meter.query(command)


if __name__ == "__main__":

    detector = Thorlabs_PM103E("TCPIP0::10.209.67.184::PM5020_07::INSTR")
    detector.connect()
    print(detector.get_idn())
    print(detector.get_detector_power())
    print(detector.get_detector_power())
    print(detector.get_detector_power())
    detector.disconnect()