
import serial

"""
                 RUN  : Start sweep function
                HALT  : Stop sweep function
              Source  : [1]  Set synth number for subsequent commands
                TRGR  : Start a sweep in manual trigger mode
                DALL  : Dump all synth parameters for both synths
                LOCK  : Display lock
                  LK  : ...
                  ID  : Device ID info
                Help  : Help
                 RCL  : Recall state from flash
                 RST  : Reset to default factory settings
              CLEans  : Clean all user saved data in flash.
          ATTenuator  : <dB>   Set attenuation (0 to 31.5 dB) (add '?' to query)
         AMFrequency  : <freq> Set AM modulation frequency
             AMDepth  : <dB>   Set AM modulation depth in dB
                 PDN  : <0|1>  0=complete power down of synthesizer
              PLEVel  : <n>  Relative power control (0 to 63)
               POWER  : <n>  Set output power in dBm
                 PWR  : ...
                 OEN  : <0|1>  disable/enable RF output buffers
                MODe  : <CW|SWEep|LIST>  Set mode
           Frequency  : <n>    Set frequency (add '?' to query)
                  CW  : <n>    Set frequency
              OFFset  : <n>    Set frequency offset
       FREQUENCYStep  : <n>    Set frequency step
               FStep  : ...
  FREQUENCYINCrement  : Increment frequency
                FINC  : ...
  FREQUENCYDECrement  : Decrement frequency
                FDEC  : ...
                LIst  : <n> <freq> <power>   Set list mode parameter
  REFerencefrequency  : <n>    Set reference frequency (add '?' to query)
         REGisterset  : <reg> <val>   Set a register value
                REFS  : <0|1>  Set reference source, 0=internal, 1=external
     REFERENCESource  : ...
             REFTrim  : <v>    Set reference DAC value (add '?' to query)
              REFT10  : <v>    Set reference DAC, range -511 to +512
                 SDN  : <LN1|LN2|LS1|LS2> Spur mitigation mode
           MASH_seed  : <n>    Write value to MASH_SEED.  0 or OFF disables
                SAVe  : Save power up synth state
               STARt  : <n> Set sweep start frequency
                STOP  : <n> Set sweep stop frequency
                STEP  : <n> Set sweep step frequency
                RATE  : <n> Set sweep step time period in milliseconds
               RTIME  : <n> Set sweep retrace time period in milliseconds
           SWEEPLIST  : <n> Display sweep frequencies
               TMODe  : <AUTO|MANual|EXTernal|EXTStep> Set sweep trigger mode
              STATus  : Print status
                NAMe  : Print synth name
                BAUD  : <baud> Set baud rate
                TEST  : <n> Test code, internal use only...
                 ETH  : [set_ip <ip_addr>]
              EEPROM  : Read the EEPROM
                KNOB  : <func> <inc>   Set RPG knob functionality
         UPTS_OFFSET  : <n>  uP temp offset deg C
"""

import time
class Valon_5019_Driver():
    def __init__(self, port: str = "COM3", data_saver=None):
        self.port = port
        self.baud_rate = 115200 # The Valon 5019 requires a baud rate of 115200
        self.connection = None
        self.data_saver = data_saver

    def is_connected(self) -> bool:
        return self.connection is not None and self.connection.is_open
    
    def disconnect(self):        
        if self.connection and self.connection.is_open:
            self.connection.close()

    def connect(self, port_name='COM3', baud_rate=115200, timeout=0.1): # Has to baud rate of 115200 for the Valone 5019

        try:
            self.connection = serial.Serial(port_name, baud_rate, timeout=timeout)
            self.connection.setDTR(False)
            self.connection.flushInput()
            self.connection.setDTR(True)
            print(f"Serial port {port_name} opened successfully.")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")

    def close_serial_port(self):
        if self.connection and self.connection.is_open:
            self.connection.close()

    def send_command(self, command, delay=0.1):
        try:
            # Clear the input buffer
            self.connection.reset_input_buffer()

            # Send the command with a carriage return
            command_with_cr = f"{command}\r"
            self.connection.write(command_with_cr.encode())

            # Introduce a delay before reading the response
            time.sleep(delay)

            # Read the response with a timeout
            response_bytes = self.connection.read(1024)  # Adjust the buffer size as needed

            # Decode and print the response
            response = response_bytes.decode().strip()
            print(f"Response from device: {response}")
        except serial.SerialException as e:
            print(f"Error communicating with the device: {e}")

    def _write(self, command):
        if self.connection and self.connection.is_open:
            command_with_cr = f"{command}\r"
            self.connection.write(command_with_cr.encode())

    def _read(self, num_bytes=1024, delay=0.1):
        if self.connection and self.connection.is_open:
            time.sleep(delay)
            response_bytes = self.connection.read(num_bytes)
            response = response_bytes.decode().strip()
            return response
        return None
    
    def _query(self, command, num_bytes=1024, delay=0.1):
        self._write(command)
        return self._read(num_bytes=num_bytes, delay=delay)

    def is_locked(self):
        response = self._query("PDN?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("PDN"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    return parts[1] == "1"

        raise RuntimeError(f"No valid LOCK response found: {response}")
    
    def get_lock_status(self):
        response = self._query("LOCK?")
        return response

        raise RuntimeError(f"No valid LOCK response found: {response}")
    def set_lock(self, lock_state):
        self._query(f"PDN {1 if lock_state else 0}")

    def get_power_dBm(self):
        response = self._query("PWR?")

        lines = response.splitlines()

        for line in lines:
            line = line.strip()

            if line.startswith("PWR"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    try:
                        return float(parts[1])
                    except ValueError:
                        pass

        raise RuntimeError(f"No valid PWR response found: {response}")

    def set_power_dBm(self, power_dBm):
        self._write(f"PWR {power_dBm}")

    def get_frequency_MHz(self):
        response = self._query("FREQ?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("F"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    try:
                        return float(parts[1])
                    except ValueError:
                        pass

        raise RuntimeError(f"No valid frequency response found: {response}")
    
    def set_frequency_MHz(self, frequency_MHz):
        self._write(f"FREQ {frequency_MHz}")

    def set_mode(self, mode):
        self._write(f"MODe {mode}") # CW, SWEep, or LIST

    def get_mode(self):
        response = self._query("MODe?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("MODE"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    return parts[1]

        raise RuntimeError(f"No valid mode response found: {response}")
    
    def start_sweep(self):
        self._query("RUN")
    
    def stop_sweep(self):
        self._query("HALT")

    def set_frequency_step_MHz(self, step_MHz):
        self._query(f"FREQUENCYStep {step_MHz}")

    def get_frequency_step_MHz(self):
        response = self._query("FREQUENCYStep?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("FSTEP"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    try:
                        return float(parts[1])
                    except ValueError:
                        pass

        raise RuntimeError(f"No valid frequency step response found: {response}")
    
    def get_sweep_step_MHz(self):
        response = self._query("STEP?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("STEP"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    try:
                        return float(parts[1])
                    except ValueError:
                        pass

        raise RuntimeError(f"No valid step response found: {response}")
    
    def get_sweep_start_frequency_MHz(self):
        response = self._query("START?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("START"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    try:
                        return float(parts[1])
                    except ValueError:
                        pass

        raise RuntimeError(f"No valid start sweep frequency response found: {response}")
    
    def get_sweep_stop_frequency_MHz(self):
        response = self._query("STOP?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("STOP"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    try:
                        return float(parts[1])
                    except ValueError:
                        pass

        raise RuntimeError(f"No valid stop sweep frequency response found: {response}")
    
    def get_sweep_rate_ms(self):
        response = self._query("RATE?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("RATE"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    try:
                        return float(parts[1])
                    except ValueError:
                        pass

        raise RuntimeError(f"No valid sweep rate response found: {response}")

    def get_sweep_retrace_time_ms(self):
        response = self._query("RTIME?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("RTIME"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    try:
                        return float(parts[1])
                    except ValueError:
                        pass

        raise RuntimeError(f"No valid sweep retrace time response found: {response}")

    def get_trigger_mode(self):
        response = self._query("TMODe?")

        for line in response.splitlines():
            line = line.strip()

            if line.startswith("TMODe"):
                parts = line.replace(";", "").split()
                if len(parts) >= 2:
                    return parts[1]

        raise RuntimeError(f"No valid trigger mode response found: {response}")
    
    def set_sweep_start_frequency_MHz(self, start_freq_MHz):
        self._query(f"START {start_freq_MHz}")
    
    def set_sweep_stop_frequency_MHz(self, stop_freq_MHz):
        self._query(f"STOP {stop_freq_MHz}")
    
    def set_sweep_rate_ms(self, rate_ms):
        self._query(f"RATE {rate_ms}")
    
    def set_sweep_step_MHz(self, step_MHz):
        self._query(f"STEP {step_MHz}")

    def set_sweep_retrace_time_ms(self, retrace_time_ms):
        self._query(f"RTIME {retrace_time_ms}")

    def set_trigger_mode(self, trigger_mode = "AUTO"):
        self._query(f"TMODe {trigger_mode}") # AUTO, MANual, EXTernal, or EXTStep