import socket
from instruments.Abstract.Identifiable import Identifiable
from photonicdrivers.Abstract.Connectable import Connectable
#import Santec_FTDI as ftdi
from enum import Enum
import math

# Methods taken from: https://github.com/santec-corporation/python-samples/tree/main/samples/mpm_instrument
# for socket questions, see qdac2 instruments

#ip = "192.168.1.161" # static IP for Santec MPM-220, MAC address 3C 6F 45 10 11 64
#ip = "10.209.69.171" # KU IT registered IP

class santec_MPM220_driver(Identifiable, Connectable):

    def __init__(self, ip_adress: str = "192.168.1.161",port: int = 5000,  timeout: int = 2) -> None:

        # self.serial_number = 25020089
        self.port = port
        self.ip_adress = ip_adress
        self.timeout = timeout
        self.socket = None
    

    #========== Identifiable ==========
    def get_id(self) -> str:
        return self._query('*IDN?')  

    #========== Connectable ==========
    def connect(self):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)
        self.socket.connect((self.ip_adress, self.port))

    def disconnect(self):

        if self.socket:
            self.socket.close()

    def is_connected(self) -> bool:
        return self.socket is not None
    
    #========== Private methods ==========

    def _query(self,cmd: str) -> str:
        
        self._write(cmd)
        response = self._read()    
        return response

    def _write(self, cmd: str) -> None:
        
        if not self.socket:
            raise ConnectionError("Not connected. Can't send command")
        self.socket.sendall((cmd + "\n").encode("ascii"))
        # self.socket.sendall(b"*IDN?\n")

    def _read(self) -> str:
        
        if not self.socket:
            raise ConnectionError("Not connected. Can't read response")
        response = self.socket.recv(4096).decode("ascii").strip()
        #response = self.socket.recv(1024).decode()
        return response

    #======================== driver commands #========================#
    #========== Instrument info  ==========
    def get_error_info(self):
        """
        Check Error information.

        Response:
            <value>,<string>
            <value>: Error Code
            <string>: Summary of content for Error
        """
        error_value, error_message = self._query('ERR?').split(',')
        error_code = ErrorCode(int(error_value))
        return error_code, error_message

    def get_modules(self):
        """
        Check recognition of Module for MPM-210H.
        
        Response:
            <value0>, <value1>, <value2>, <value3>, <value4>
            value0: Module0
            value1: Module1
            value2: Module2
            value3: Module3
            value4: Module4
            0: Module is not recognized.
            1: Module is recognized.

        Example:
            IDIS?
            Response: 1,1,1,1,1
        """
        return self._query('IDIS?')

    def get_module_information(self, module: int):
        """
        Identification query of a module type.

        Parameters: <module >: 0,1,2,3,4

        Response:
            <value0>,<value1>,<value2>,<Value3>
            value0: Company (Santec)
            value1: Product code (MPM-211,MPM-212,MPM-
            213,MPM-215)
            value2: Serial number
            value3: Firmware version

        Example:
            MMVER? 0
            Response : Santec,MPM-211,00000000M211,Ver1.11
        """
        return self._query(f'MMVER? {module}')

    def get_gpib_address(self):
        """Get the current GPIB address."""
        return self._query('ADDR?')

    def set_gpib_address(self, value: str):
        """
        Set the GPIB address.

        Parameters:
            <value>: GPIB address value, range 1 to 31
        """
        self._write(f'ADDR {value}')

    def get_gateway_address(self):
        """Get the current Gateway Address."""
        return self._query('GW?')

    def set_gateway_address(self, address: str):
        """
        Set the Gateway address.

        Parameters:
            <address>: Gateway address in the format 'www.xxx.yyy.zzz'
        """
        self._write(f'GW {address}')

    def get_subnet_mask(self):
        """Get the current Subnet Mask."""
        return self._query('SUBNET?')

    def set_subnet_mask(self, address: str):
        """
        Set the Subnet Mask.

        Parameters:
            <address>: Subnet mask in the format 'www.xxx.yyy.zzz'
        """
        self._write(f'SUBNET {address}')

    def get_ip_address(self):
        """Get the current IP address."""
        return self._query('IP?')

    def set_ip_address(self, address: str):
        """
        Set the IP address.

        Parameters:
            <address>: IP address in the format www.xxx.yyy.zzz (0 ~ 255)
        """
        self._write(f'IP {address}')
    
    #========== Instrument info  ==========
    def perform_zeroing(self):
        """
        Before measuring optical power, run Zeroing to delete
        electrical DC offset. Please be careful with the incidence of light
        into Optic Port. When using the current meter module,
        the MPM-213, please remove the BNC cable from the
        MPM-213. This command action takes about 3 sec, so
        please run other commands at least 3 sec later.
        """
        self._write('ZERO')

    def get_input_trigger(self):
        """Get the current input trigger setting."""
        return self._query('TRIG?')

    def set_input_trigger(self, value: int):
        """
        Set the input trigger.

        Parameters:
            value: 0 - Internal trigger, 1 - External trigger
        """
        self._write(f'TRIG {value}')


    #========== Modes  ==========
    def get_measurement_mode(self):
        """Get the current measurement mode."""
        return self._query('WMOD?')

    def set_measurement_mode(self, mode: str):
        """
        Set the measurement mode.

        Parameters:
            mode: One of the supported modes:
                - CONST1: Constant Wavelength, No Auto Gain, SME mode
                - SWEEP1: Sweep Wavelength, No Auto Gain, SME mode
                - CONST2: Constant Wavelength, Auto Gain, SME mode
                - SWEEP2: Sweep Wavelength, Auto Gain, SME mode
                - FREE-RUN: Constant Wavelength, No Auto Gain, First Hardware Trigger Start (CME mode)
        """
        if mode not in ["CONST1", "SWEEP1", "CONST2", "SWEEP2", "FREE-RUN"]:
            raise ValueError("Invalid mode. Supported modes: CONST1, SWEEP1, CONST2, SWEEP2, FREE-RUN")
        self._write(f'WMOD {mode}')

    def get_power_mode(self):
        """Get the current power mode (Auto or Manual)."""
        return self._query('AUTO?')

    def set_power_mode(self, value):
        """
        Set the power mode (Auto or Manual).

        Parameters:
            value: 0 for Manual range, 1 for Auto range
        """
        if value not in [0, 1]:
            raise ValueError("Invalid value. It must be 0 (Manual range) or 1 (Auto range).")
        self._write(f'AUTO {value}')

    def get_power_mode_for_each_channel(self, module_number):
        """Get the power mode (Auto or Manual) for a specific module."""
        return self._query(f'DAUTO? {module_number}')

    def set_power_mode_for_each_channel(self, module_number, range_value):
        """
        Set the power mode (Auto or Manual) for each channel.

        Parameters:
            value: A tuple (module, range_mode)
            module: Module number (0 to 5)
            range_mode: 0 for Manual range, 1 for Auto range
        """
        if range_value not in [0, 1]:
            raise ValueError("Invalid value. It must be 0 (Manual range) or 1 (Auto range).")
        self._write(f'DAUTO {module_number},{range_value}')


    #========== Measurements  ========== 
        
    def start_measurement(self):
        """Command to start measuring."""
        self._write('MEAS')

    def stop_measurement(self):
        """Command to stop measuring."""
        self._write('STOP')

    def get_power_of_single_module(self, module):
        
        """
        Get the optical power or electrical current for each channel of the selected module.

        Syntax:
            READ? <module>

        Parameters:
            <module>: Module Number (0, 1, 2, 3, 4)

        Response:
            <module>: Module Number (0, 1, 2, 3, 4)
            Response: <value1>,<value2>,<value3>,<value4>
            value1: Optical power of port 1
            value2: Optical power of port 2
            value3: Optical power of port 3
            value4: Optical power of port 4

        Example:
            READ? 0
            Response: -20.123,-20.454,-20.764,-20.644
        """
        response = self._query(f'READ? {module}').split(',')
        return response

    def get_wavelength(self):
        """Get the current wavelength in Constant Wavelength Measurement Mode (CONST1, CONST2)."""
        return self._query('WAV?')

    def set_wavelength(self, value: float):
        """
        Set the wavelength for Constant Wavelength Measurement Mode (CONST1, CONST2).

        Parameters:
            value: Wavelength in nm (1250.000 ~ 1630.000)
        """
        if not 1250.000 <= value <= 1630.000:
            raise ValueError("Wavelength must be between 1250.000 and 1630.000 nm.")
        self._write(f'WAV {value}')

    def get_wavelength_for_each_channel(self):
        """Get the wavelength for a specific module and channel in Constant Wavelength Measurement Mode."""
        return self._query('DWAV?')

    def set_wavelength_for_each_channel(self, values: tuple):
        """
        Set the wavelength for a specific module and channel in Constant Wavelength Measurement Mode.

        Parameters:
            values: A tuple containing the following values:
                - value1: Module number (0-5), where 5 sets all channels and modules to the same wavelength
                - value2: Channel number (1-4)
                - value3: Wavelength in nm (1250.000 ~ 1630.000)
        """
        value1, value2, value3 = values
        if not 0 <= value1 <= 5:
            raise ValueError("Module value must be between 0 and 5.")
        if not 1 <= value2 <= 4:
            raise ValueError("Channel value must be between 1 and 4.")
        if not 1250.000 <= value3 <= 1630.000:
            raise ValueError("Wavelength must be between 1250.000 and 1630.000 nm.")

        self._write(f'DWAV {value1},{value2},{value3}')

    def get_sweep_wavelength_and_step(self):
        """Get the current sweep wavelength settings (start, stop, step)."""
        return self._query('WSET?')

    def set_sweep_wavelength_and_step(self, values: tuple):
        """
        Set the sweep wavelength parameters.

        Parameters:
            values: A tuple containing the following values:
                - start: Start wavelength (1250 ~ 1630 nm)
                - stop: Stop wavelength (1250 ~ 1630 nm)
                - step: Step wavelength (0.001 ~ 10 nm)
        """
        start, stop, step = values
        if not 1250 <= start <= 1630:
            raise ValueError("Start wavelength must be between 1250 and 1630 nm.")
        if not 1250 <= stop <= 1630:
            raise ValueError("Stop wavelength must be between 1250 and 1630 nm.")
        if not 0.001 <= step <= 10:
            raise ValueError("Step wavelength must be between 0.001 and 10 nm.")
        if stop <= start:
            raise ValueError("Stop wavelength must be greater than start wavelength.")

        self._write(f'WSET {start},{stop},{step}')

    def get_sweep_speed(self):
        """Get the current wavelength sweep speed."""
        return self._query('SPE?')

    def set_sweep_speed(self, speed: float):
        """
        Set the wavelength sweep speed.

        Parameters:
            speed: Sweep speed in nm/sec (0.001 ~ 200).

        Raises:
            ValueError: If the speed is out of the valid range (0.001 to 200).
        """
        if not 0.001 <= speed <= 200:
            raise ValueError("Sweep speed must be between 0.001 and 200 nm/sec.")
        self._write(f'SPE {speed}')

    def get_dynamic_range(self):
        """Get the current TIA gain setting."""
        return self._query('LEV?')

    def set_dynamic_range(self, dynamic_range: int):
        """
        Set the TIA gain for measuring modes like CONST1, SWEEP1, FREERUN, and AUTO1.

        Parameters:
            range: 1 to 5 for MPM-215 or 1 to 4 for MPM-213.
        """
        if dynamic_range not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid range. Valid values are 1, 2, 3, 4, or 5.")
        self._write(f'LEV {dynamic_range}')

    def get_dynamic_range_set2(self):
        """Get TIA Gain for CONST1, SWEEP1, FREERUN, AUTO1 measuring mode for each channel."""

        def get_gain(value1, value2):
            return self._query(f'DLEV? {value1},{value2}')

        return get_gain

    def set_dynamic_range_set2(self, values):
        """
        Set TIA Gain for CONST1, SWEEP1, FREERUN, AUTO1 measuring mode for each channel.

        Parameters:
            values: A tuple containing (value1: module, value2: channel, value3: gain)
            value1: Module 0, 1, 2, 3, 4, 5
            value2: Channel 1, 2, 3, 4
            value3: Gain 1, 2, 3, 4, 5
        """
        value1, value2, value3 = values
        if value3 not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid gain value. Valid values are 1, 2, 3, 4, or 5.")
        self._write(f'DLEV {value1},{value2},{value3}')

    def get_average_time(self):
        """Get the average time."""
        return self._query('AVG?')

    def set_average_time(self, time):
        """
        Set the average time.

        Parameters:
            time: A value between 0.01 and 10000.00 (in ms).
        """
        if not (0.01 <= time <= 10000.00):
            raise ValueError("Invalid time value. It must be between 0.01 and 10000.00 ms.")
        self._write(f'AVG {time}')

    def get_average_time_set2(self):
        """Get the average time (set2)."""
        return self._query('FGSAVG?')

    def set_average_time_set2(self, value):
        """
        Set the average time (set2).

        Parameters:
            value: A value between 0.01 and 10000.00 (in ms).
        """
        if not (0.01 <= value <= 10000.00):
            raise ValueError("Invalid value. It must be between 0.01 and 10000.00 ms.")
        self._write(f'FGSAVG {value}')

    def get_power_unit(self):
        """Get the current measuring unit for optical power or electrical current."""
        return self._query('UNIT?')

    def set_power_unit(self, value):
        """
        Set the measuring unit for optical power or electrical current.

        Parameters:
            value: 0 for dBm/dBmA, 1 for mW/mA
        """
        if value not in [0, 1]:
            raise ValueError("Invalid value. It must be 0 (for dBm/dBmA) or 1 (for mW/mA).")
        self._write(f'UNIT {value}')

    def get_wavelength_to_be_calibrated(self, module, index):
        """
        Get the wavelength that should be calibrated for the given module and index.

        Parameters:
            <module>: Module Number (0, 1, 2, 3, 4)
            <index>: Wavelength set order (1, 2, 3... 18, 19, 20)

        Response:
            <value>: Wavelength in nm

        Example:
            CWAV? 0,1
            Response: 1250

        Returns:
            float: Wavelength in nm to be calibrated.
        """
        response = self._query(f'CWAV? {module},{index}')
        return float(response)

    def get_power_calibration_of_calibrated_wavelength(self, module, channel, index):
        """
        Get the power calibration value of the wavelength from the "CWAV?" command index.

        Parameters:
            <module>: Module Number (0, 1, 2, 3, 4)
            <channel>: Port number (1, 2, 3, 4)
            <index>: Wavelength set order (1, 2, 3...18, 19)

        Response:
            <value>: Optical power offset in dB (float)

        Example:
            CWAVPO? 0,1,1
            Response: 0.904640

        Returns:
            float: Optical power offset in dB.
        """
        response = self._query(f'CWAVPO? {module},{channel},{index}')
        return float(response)

    def get_logging_status(self):
        """
        Gets the latest measuring status and logging points.

        Response:
            <value1>,<value2>
                <value1>: Status
                    0 – Measuring is still in process.
                    1 – Measurement completed.
                    -1 – The measurement is forcibly stopped.
                <value2>: Measured logging point

        Example Response: 1,100
        """
        status, count = self.connection._query('STAT?').split(',')
        return int(status), int(count)

    def get_logging_data_point(self):
        """Get the current measurement logging point in CONST1/CONST2/FREE-RUN measuring mode."""
        response = self._query('LOGN?')
        return int(response)

    def set_logging_data_point(self, value: int):
        """
        Set measurement logging point in CONST1/CONST2/FREE-RUN measuring mode.
        Refer to the 5.6.3 Measurement logging setting (LOGN).

        Syntax:
            LOGN <value>

        Parameters:
            value: 1 ~ 1,000,000

        Default value: 1

        Example: LOGN 100
        """
        if not (1 <= value <= 1000000):
            raise ValueError("Measurement data point must be between 1 and 1,000,000.")
        self._write(f'LOGN {value}')

    def get_logging_data(self, module_no: int, channel_no: int):
        """
        Read out the logging logg.
        This command is not available for RS-232 communication.

        Example:    LOGG? 0,1`
        """
        try:
            count = self.get_logging_data_point()

            expected_size = count * 4 + (2 + 1 + int(math.log10(count)))
            return self.connection._query_binary_values(f'LOGG? {module_no},{channel_no}',
                                                    data_points=expected_size)

        except Exception as e:
            print(f"Error while fetching logging data (query_binary_values): {e}")



class ErrorCode(Enum):
    NO_ERROR = 0
    INVALID_CHARACTER = -101
    INVALID_SEPARATOR = -103
    DATA_TYPE_ERROR = -104
    PARAMETER_NOT_ALLOWED = -108
    MISSING_PARAMETER = -109
    COMMAND_HEADER_ERROR = -110
    UNDEFINED_HEADER = -113
    SETTING_CONFLICT = -221
    DATA_OUT_OF_RANGE = -222
    PROGRAM_RUNNING = -284
    DEVICE_SPECIFIC_ERROR = -300
    NOT_MEASUREMENT_MODULE = -301
    QUEUE_OVERFLOW = -350
    QUEUE_EMPTY = -351
    UPP_COMM_HEADER_ERROR = 101
    UPP_COMM_RSP_NO = 103
    UPP_COMM_MODULE_MISMATCHED = 104
    TCPIP_COMM_ERROR = 110
    GPIB_TX_NOT_COMPLETED = 116
    GPIB_TX_TIMER_EXPIRED = 117
    MC_TRIG_ERROR = 120
    SEM_NOT_EXIST = 210

    @staticmethod
    def get_error_description(error_code):
        error_descriptions = {
            ErrorCode.NO_ERROR: "No error",
            ErrorCode.INVALID_CHARACTER: "Invalid character. This occurs when unacceptable characters are received for Command or Parameter. Unacceptable characters: '%', '&', '$', '#', '~'.",
            ErrorCode.INVALID_SEPARATOR: "Invalid separator. This occurs when an unacceptable character is received as a separator between the Command and the Parameter. Unacceptable characters: '`', ';'.",
            ErrorCode.DATA_TYPE_ERROR: "Data type error. This occurs when the Parameter is not an acceptable data type.",
            ErrorCode.PARAMETER_NOT_ALLOWED: "Parameter not allowed. This occurs when the number of parameters in the corresponding command is more or less than expected.",
            ErrorCode.MISSING_PARAMETER: "Missing parameter. This occurs when the number of characters in the Parameter is longer than 18.",
            ErrorCode.COMMAND_HEADER_ERROR: "Command header error. This occurs when the number of characters in the Command is longer than 13.",
            ErrorCode.UNDEFINED_HEADER: "Undefined Header. This occurs when an unsupported command is received.",
            ErrorCode.SETTING_CONFLICT: "Setting conflict. This occurs when one of the following setup commands (other than STOP or STAT?) was received before measurement using 'MEAS' command is completed: AVG, LEV, LOGN, AUTO, WAVE, WMOD, WSET, SPE, LOOP, UNIT.",
            ErrorCode.DATA_OUT_OF_RANGE: "Data out of range. This occurs when the parameter is outside the acceptable value.",
            ErrorCode.PROGRAM_RUNNING: "Program currently running. This occurs when the mainframe delivers new commands to the module before the process of delivering commands to the module and receiving responses is completed.",
            ErrorCode.DEVICE_SPECIFIC_ERROR: "Device specific error. This occurs when the GPIB Address number that you are trying to set exceeds 32.",
            ErrorCode.NOT_MEASUREMENT_MODULE: "Is not Measurement Module. This occurs when user attempts to deliver a command to a module (slot) that is not installed.",
            ErrorCode.QUEUE_OVERFLOW: "Queue overflow. This occurs when the Queue space used for communication between internal Tasks is full, and there is no space to store information.",
            ErrorCode.QUEUE_EMPTY: "Queue empty. This occurs when there is no message in the Queue space used for communication between internal Tasks.",
            ErrorCode.UPP_COMM_HEADER_ERROR: "uPP Comm. Header Error. This occurs when the Headers of the Packet used to send and receive data between the mainframe and the module are different.",
            ErrorCode.UPP_COMM_RSP_NO: "uPP Comm. Rsp No. This occurs when the mainframe sends data information to the module but does not receive a response.",
            ErrorCode.UPP_COMM_MODULE_MISMATCHED: "uPP Comm. Module Mismatched. This occurs when the mainframe receives information from a different module than the one that sent the data.",
            ErrorCode.TCPIP_COMM_ERROR: "TCPIP Comm. Error. This occurs when all data to be transferred is not sent in TCP/IP communication.",
            ErrorCode.GPIB_TX_NOT_COMPLETED: "GPIB Tx not completed. This occurs when no event is delivered to the internal GPIB Task used for GPIB communication.",
            ErrorCode.GPIB_TX_TIMER_EXPIRED: "GPIB Tx Timer Expired. This occurs when all data to be transferred is not sent in GPIB communication.",
            ErrorCode.MC_TRIG_ERROR: "MC Trig. Error. This occurs when the mainframe does not receive a measurement completion signal (H/W signal) from the module after the measurement command was delivered to the module.",
            ErrorCode.SEM_NOT_EXIST: "not exist SEM. This occurs when an unregistered message is delivered between internal tasks.",
        }
        return error_descriptions.get(error_code, "Unknown error")

if __name__ == "__main__":
    
    # Example usage    
    driver = santec_MPM220_driver(port=5000, ip_adress="192.168.1.161")
    driver.connect()
    print(driver.get_id())
    print(driver.get_modules())
    print(driver.get_module_information(0))
    print(driver.get_wavelength())
    print(driver.get_measurement_mode())
    print(driver.get_power_mode())

    # Measure 



