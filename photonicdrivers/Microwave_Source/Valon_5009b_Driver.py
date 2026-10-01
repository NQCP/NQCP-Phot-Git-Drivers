
import re
import time

import serial
import serial.tools.list_ports


"""
Driver for the Valon Technology 5009b Dual Frequency Synthesizer (20 MHz - 6.4 GHz).

The 5009b contains two independent sources (1 and 2). Every per-source method takes an
optional `source` argument; if omitted, the driver's current default source is used
(see set_source()). Each per-source command is sent as "Source <n>; <command>" so the
device's sticky source selection never gets out of sync with the driver.

Communication: FTDI virtual COM port, 8N1, default 9600 baud on USB (115200 on the
TTL User Port). Commands are terminated with a carriage return. The device echoes the
command, prints the response lines and finishes with a prompt such as "-1->".

Command summary (see the 5009b Operations Manual, section 4):
              Source  : <1|2>  Select source for subsequent commands
                  ID  : Device ID info
              STATus  : Print status (serial, firmware, VBAT, temperature, ...)
                LOCK  : Display lock state of both sources (LOCK1? / LOCK2? per source)
                DALL  : Dump all synth parameters for both synths
                 RCL  : Recall state from flash
                SAVe  : Save power up synth state to flash
                 RST  : Reset to default factory settings
              CLEans  : Clean all user saved data in flash
                MODe  : <CW|SWEep|LIST>  Set mode
           Frequency  : <n>    Set CW frequency (add '?' to query)
              OFFset  : <n>    Set frequency offset
               FStep  : <n>    Set CW frequency step
                FINC  : Increment CW frequency by FStep
                FDEC  : Decrement CW frequency by FStep
               STARt  : <n>    Set sweep start frequency
                STOP  : <n>    Set sweep stop frequency
                STEP  : <n>    Set sweep step frequency
                RATE  : <ms>   Set sweep step time in milliseconds
               RTIME  : <ms>   Set sweep retrace time in milliseconds
               TMODe  : <AUTO|MANual|EXTernal|EXTStep> Set sweep trigger mode
                 RUN  : [0|1|2|3] Start sweep
                HALT  : [0|1|2|3] Stop sweep
                TRGR  : Start a sweep in manual trigger mode
                LIst  : <n> <freq> [<att>]  Set list mode entry (n = 1..32)
          ATTenuator  : <dB>   Set attenuation (0 to 31.75 dB in 0.25 dB steps)
              PLEVel  : <AUTO|0..63>  Power level before the attenuator
                 OEN  : <0|1>  Disable/enable RF output buffers
                 PDN  : <0|1>  0 = complete power down of the source
             AMDepth  : <dB>   AM modulation depth (0 disables AM)
         AMFrequency  : <f>    AM modulation frequency (0.5 Hz to 10 kHz)
  REFerencefrequency  : <n>    Set (external) reference frequency
                REFS  : <0|1>  Reference source, 0 = internal, 1 = external
             REFTrim  : <0..255> Internal reference trim DAC
                  CP  : <0..15> Charge pump current
                 SDN  : <LN1|LN2|LS1|LS2> Spur mitigation mode
                NAMe  : <name> Source alias name (max 48 characters)
                BAUD  : <baud> Set baud rate
"""


class Valon_5009b_Driver():

    SOURCES = (1, 2)
    BAUD_RATES = (9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600)
    MODES = ("CW", "SWEEP", "LIST")
    TRIGGER_MODES = ("AUTO", "MANUAL", "EXTERNAL", "EXTSTEP")
    SPUR_MODES = ("LN1", "LN2", "LS1", "LS2")
    _UNIT_TO_MHZ = {"HZ": 1e-6, "KHZ": 1e-3, "MHZ": 1.0, "GHZ": 1e3}

    def __init__(self, port: str = "COM11", baud_rate: int = 9600, timeout: float = 1.0,
                 source: int = 1, data_saver=None):
        self.port = port
        self.baud_rate = baud_rate  # The 5009b USB port defaults to 9600 baud
        self.timeout = timeout
        self.source = self._check_source(source)
        self.connection = None
        self.data_saver = data_saver

    # ------------------------------------------------------------------ #
    # Connection
    # ------------------------------------------------------------------ #

    @staticmethod
    def list_ports():
        """Return the COM ports that look like FTDI/Valon USB UARTs."""
        return [p.device for p in serial.tools.list_ports.comports()
                if "USB" in (p.description or "") or "FTDI" in (p.manufacturer or "")]

    def connect(self, port_name=None, baud_rate=None, timeout=None):
        if port_name is None:
            port_name = self.port
        if baud_rate is None:
            baud_rate = self.baud_rate
        if timeout is None:
            timeout = self.timeout

        self.port = port_name
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.connection = serial.Serial(port_name, baud_rate, timeout=timeout)
        # Flush any stale prompt left in the device buffer
        self._query("")
        print(f"Serial port {port_name} opened successfully at {baud_rate} baud.")

    def disconnect(self):
        if self.connection and self.connection.is_open:
            self.connection.close()

    def close_serial_port(self):
        self.disconnect()

    def is_connected(self) -> bool:
        return self.connection is not None and self.connection.is_open

    def set_baud_rate(self, baud_rate: int):
        """Change the device baud rate and reconnect at the new rate.

        The new rate is not persistent unless save() is called afterwards.
        """
        if baud_rate not in self.BAUD_RATES:
            raise ValueError(f"Invalid baud rate {baud_rate}. Use one of {self.BAUD_RATES}.")
        self._send(f"BAUD {baud_rate}")
        time.sleep(0.1)
        self.connection.baudrate = baud_rate
        self.baud_rate = baud_rate
        self._query("")

    # ------------------------------------------------------------------ #
    # Low level communication
    # ------------------------------------------------------------------ #

    def _send(self, command):
        if not self.is_connected():
            raise RuntimeError("Valon 5009b is not connected.")
        self.connection.reset_input_buffer()
        self.connection.write(f"{command}\r".encode())

    def _read(self):
        """Read until the device prompt ("-1->" / "-2->") or until timeout."""
        response_bytes = self.connection.read_until(b"->")
        response = response_bytes.decode(errors="replace")
        lines = [line.strip() for line in response.replace("\r", "\n").split("\n")]
        # Drop empty lines and the trailing prompt
        return [line for line in lines if line and not re.fullmatch(r"-\d*->", line)]

    def _query(self, command):
        """Send a command and return the response lines (without the echo and the prompt)."""
        self._send(command)
        lines = self._read()
        if lines and lines[0].replace(" ", "").lower() == command.replace(" ", "").lower():
            lines = lines[1:]
        return lines

    def _source_command(self, command, source=None):
        return f"Source {self._get_source(source)}; {command}"

    def _write(self, command, source=None):
        """Send a (per-source if source is not False) command and consume the response."""
        if source is not False:
            command = self._source_command(command, source)
        return "\n".join(self._query(command))

    def send_command(self, command):
        """Send a raw command and return the device response as a string."""
        return "\n".join(self._query(command))

    def _query_value(self, command, keyword, source=None):
        """Query a value and return the tokens following `keyword` in the response.

        Responses look like "F 2440 MHz; // Act 2440 MHz" or "ATT 15.0; // dB".
        """
        if source is not False:
            command = self._source_command(command, source)
        lines = self._query(command)
        for line in lines:
            tokens = line.split("//")[0].replace(";", " ").split()
            upper = [t.upper() for t in tokens]
            if keyword.upper() in upper:
                index = upper.index(keyword.upper())
                if index + 1 < len(tokens):
                    return tokens[index + 1:]
        raise RuntimeError(f"No valid {keyword} response found: {lines}")

    def _query_float(self, command, keyword, source=None):
        return float(self._query_value(command, keyword, source)[0])

    def _query_frequency_MHz(self, command, keyword, source=None):
        tokens = self._query_value(command, keyword, source)
        value = float(tokens[0])
        unit = tokens[1].upper() if len(tokens) > 1 else "MHZ"
        return value * self._UNIT_TO_MHZ.get(unit, 1.0)

    def _check_source(self, source):
        if source not in self.SOURCES:
            raise ValueError(f"Invalid source {source}. Use 1 or 2.")
        return source

    def _get_source(self, source=None):
        return self.source if source is None else self._check_source(source)

    # ------------------------------------------------------------------ #
    # General
    # ------------------------------------------------------------------ #

    def get_id(self):
        return self.send_command("ID")

    def get_status(self):
        return self.send_command("STATus")

    def get_all_parameters(self):
        """Dump all parameters of both sources (DALL)."""
        return self.send_command("DALL")

    def set_source(self, source: int):
        """Set the default source used when no source argument is given."""
        self.source = self._check_source(source)

    def get_source(self) -> int:
        return self.source

    def save(self):
        """Save the current state of both sources to flash (restored on power up)."""
        return self.send_command("SAVe")

    def recall(self):
        """Recall the state of both sources from flash."""
        return self.send_command("RCL")

    def reset(self):
        """Reset both sources to factory default settings (reference trim is kept)."""
        return self.send_command("RST")

    def cleanse(self):
        """Erase all user data in flash, including source names."""
        return self.send_command("CLEanse")

    # ------------------------------------------------------------------ #
    # Lock / power
    # ------------------------------------------------------------------ #

    def get_lock_status(self):
        """Return the raw lock status string of both sources."""
        return self.send_command("LOCK?")

    def is_locked(self, source=None) -> bool:
        """Return True if the PLL of the given source is locked."""
        response = self.send_command(f"LOCK{self._get_source(source)}?").lower()
        if "unlock" in response or "not locked" in response:
            return False
        if "lock" in response:
            return True
        raise RuntimeError(f"No valid LOCK response found: {response}")

    def set_synth_power(self, enabled: bool, source=None):
        """Power the source up (True) or completely down (False) using PDN."""
        self._write(f"PDN {1 if enabled else 0}", source)

    def get_synth_power(self, source=None) -> bool:
        return self._query_value("PDN?", "PDN", source)[0] == "1"

    def set_output_enabled(self, enabled: bool, source=None):
        """Enable or disable the RF output buffer (OEN). Disabled reduces output by ~30-50 dB."""
        self._write(f"OEN {1 if enabled else 0}", source)

    def get_output_enabled(self, source=None) -> bool:
        return self._query_value("OEN?", "OEN", source)[0] == "1"

    # ------------------------------------------------------------------ #
    # Output level
    # ------------------------------------------------------------------ #

    def set_attenuation_dB(self, attenuation_dB, source=None):
        """Set the output attenuator, 0 to 31.75 dB in 0.25 dB steps (15 dB ~ 0 dBm)."""
        if not 0 <= attenuation_dB <= 31.75:
            raise ValueError("Attenuation must be between 0 and 31.75 dB.")
        attenuation_dB = round(attenuation_dB * 4) / 4
        self._write(f"ATT {attenuation_dB:.2f}", source)

    def get_attenuation_dB(self, source=None):
        return self._query_float("ATT?", "ATT", source)

    def set_power_level(self, level="AUTO", source=None):
        """Set the power level before the attenuator: 'AUTO' (leveled) or 0..63."""
        if isinstance(level, str):
            if level.upper() != "AUTO":
                raise ValueError("Power level must be 'AUTO' or an integer 0..63.")
            level = "AUTO"
        elif not 0 <= int(level) <= 63:
            raise ValueError("Power level must be 'AUTO' or an integer 0..63.")
        self._write(f"PLEV {level}", source)

    def get_power_level(self, source=None):
        value = self._query_value("PLEV?", "PLEV", source)[0]
        return value if value.upper() == "AUTO" else int(value)

    def set_am_depth_dB(self, depth_dB, source=None):
        """Set AM modulation depth (0 to 31.75 dB). 0 disables AM."""
        if not 0 <= depth_dB <= 31.75:
            raise ValueError("AM depth must be between 0 and 31.75 dB.")
        self._write(f"AMD {depth_dB}", source)

    def get_am_depth_dB(self, source=None):
        return self._query_float("AMD?", "AMD", source)

    def set_am_frequency_Hz(self, frequency_Hz, source=None):
        """Set AM modulation frequency (0.5 Hz to 10 kHz, square wave)."""
        if not 0.5 <= frequency_Hz <= 10e3:
            raise ValueError("AM frequency must be between 0.5 Hz and 10 kHz.")
        self._write(f"AMF {frequency_Hz} Hz", source)

    def get_am_frequency_Hz(self, source=None):
        tokens = self._query_value("AMF?", "AMF", source)
        unit = tokens[1].upper() if len(tokens) > 1 else "HZ"
        return float(tokens[0]) * self._UNIT_TO_MHZ.get(unit, 1e-6) * 1e6

    # ------------------------------------------------------------------ #
    # CW frequency
    # ------------------------------------------------------------------ #

    def set_frequency_MHz(self, frequency_MHz, source=None):
        if not 20 <= frequency_MHz <= 6400:
            raise ValueError("Frequency must be between 20 and 6400 MHz.")
        self._write(f"F {frequency_MHz} MHz", source)

    def get_frequency_MHz(self, source=None):
        return self._query_frequency_MHz("F?", "F", source)

    def set_frequency_offset_MHz(self, offset_MHz, source=None):
        self._write(f"OFFset {offset_MHz} MHz", source)

    def get_frequency_offset_MHz(self, source=None):
        return self._query_frequency_MHz("OFFset?", "OFFSET", source)

    def set_frequency_step_MHz(self, step_MHz, source=None):
        """Set the CW step used by increment_frequency()/decrement_frequency()."""
        self._write(f"FSTEP {step_MHz} MHz", source)

    def get_frequency_step_MHz(self, source=None):
        return self._query_frequency_MHz("FSTEP?", "FSTEP", source)

    def increment_frequency(self, source=None):
        self._write("FINC", source)

    def decrement_frequency(self, source=None):
        self._write("FDEC", source)

    # ------------------------------------------------------------------ #
    # Mode
    # ------------------------------------------------------------------ #

    def set_mode(self, mode, source=None):
        """Set the mode: 'CW', 'SWEep' or 'LIST'."""
        if mode.upper() not in self.MODES and mode.upper() != "SWE":
            raise ValueError(f"Invalid mode {mode}. Use CW, SWEep or LIST.")
        self._write(f"MODe {mode}", source)

    def set_mode_cw(self, source=None):
        """Set the source to CW (single tone) mode."""
        self.set_mode("CW", source)

    def set_mode_sweep(self, source=None):
        """Set the source to sweep mode. Start, stop, step and rate must also be set."""
        self.set_mode("SWEep", source)

    def set_mode_list(self, source=None):
        """Set the source to LIST mode (entry selected by the USER PORT pins)."""
        self.set_mode("LIST", source)

    def get_mode(self, source=None):
        return self._query_value("MODe?", "MODE", source)[0].upper()

    # ------------------------------------------------------------------ #
    # Sweep
    # ------------------------------------------------------------------ #

    def set_sweep_start_frequency_MHz(self, start_freq_MHz, source=None):
        self._write(f"STARt {start_freq_MHz} MHz", source)

    def get_sweep_start_frequency_MHz(self, source=None):
        return self._query_frequency_MHz("STARt?", "START", source)

    def set_sweep_stop_frequency_MHz(self, stop_freq_MHz, source=None):
        self._write(f"STOP {stop_freq_MHz} MHz", source)

    def get_sweep_stop_frequency_MHz(self, source=None):
        return self._query_frequency_MHz("STOP?", "STOP", source)

    def set_sweep_step_MHz(self, step_MHz, source=None):
        self._write(f"STEP {step_MHz} MHz", source)

    def get_sweep_step_MHz(self, source=None):
        return self._query_frequency_MHz("STEP?", "STEP", source)

    def set_sweep_rate_ms(self, rate_ms, source=None):
        """Set the dwell time per sweep step (0.1 ms to 1 s)."""
        self._write(f"RATE {rate_ms}", source)

    def get_sweep_rate_ms(self, source=None):
        return self._query_float("RATE?", "RATE", source)

    def set_sweep_retrace_time_ms(self, retrace_time_ms, source=None):
        self._write(f"RTIME {retrace_time_ms}", source)

    def get_sweep_retrace_time_ms(self, source=None):
        return self._query_float("RTIME?", "RTIME", source)

    def set_trigger_mode(self, trigger_mode="AUTO", source=None):
        """Set the sweep trigger mode: AUTO, MANual, EXTernal or EXTStep."""
        if not any(m.startswith(trigger_mode.upper()) for m in self.TRIGGER_MODES):
            raise ValueError(f"Invalid trigger mode {trigger_mode}. Use AUTO, MANual, EXTernal or EXTStep.")
        self._write(f"TMODe {trigger_mode}", source)

    def get_trigger_mode(self, source=None):
        return self._query_value("TMODe?", "TMODE", source)[0].upper()

    def start_sweep(self, source=None):
        """Start the sweep of the given source (RUN).

        Before calling this, ensure:
        - The source is in sweep mode (set_mode_sweep())
        - Start/stop frequency, step and rate are set
        """
        self._write(f"RUN {self._get_source(source)}", source=False)

    def start_sweep_both(self):
        """Start the sweep of both sources simultaneously."""
        self._write("RUN 3", source=False)

    def stop_sweep(self, source=None):
        """Stop the sweep of the given source (HALT)."""
        self._write(f"HALT {self._get_source(source)}", source=False)

    def stop_sweep_both(self):
        self._write("HALT 3", source=False)

    def trigger_sweep(self, source=None):
        """Trigger a single sweep in MANual trigger mode."""
        self._write("TRGR", source)

    # ------------------------------------------------------------------ #
    # List mode
    # ------------------------------------------------------------------ #

    def set_list_entry(self, index: int, frequency_MHz, attenuation_dB=None, source=None):
        """Set LIST entry `index` (1..32). Use save() to keep the list after power down."""
        if not 1 <= index <= 32:
            raise ValueError("List index must be between 1 and 32.")
        command = f"LIST {index} {frequency_MHz} MHz"
        if attenuation_dB is not None:
            command += f" {attenuation_dB}"
        self._write(command, source)

    def get_list(self, source=None):
        """Return the raw LIST table of the given source."""
        return self._write("LIST?", source)

    # ------------------------------------------------------------------ #
    # Reference and configuration
    # ------------------------------------------------------------------ #

    def get_reference_source(self):
        value = self._query_value("REFS?", "REFS", source=False)[0]
        return "internal" if value == "0" else "external"

    def set_reference_source(self, source: str):
        if source.lower() == "internal":
            self._write("REFS 0", source=False)
        elif source.lower() == "external":
            self._write("REFS 1", source=False)
        else:
            raise ValueError("Invalid reference source. Use 'internal' or 'external'.")

    def get_reference_frequency_MHz(self):
        return self._query_frequency_MHz("REF?", "REF", source=False)

    def set_reference_frequency_MHz(self, frequency_MHz):
        """Set the external reference frequency (10 to 100 MHz). Internal is fixed at 10 MHz."""
        if not 10 <= frequency_MHz <= 100:
            raise ValueError("Reference frequency must be between 10 and 100 MHz.")
        self._write(f"REF {frequency_MHz} MHz", source=False)

    def get_reference_trim(self) -> int:
        return int(self._query_float("REFT?", "REFT", source=False))

    def set_reference_trim(self, value: int):
        """Trim the internal VCTCXO (0..255, ~+-10 ppm range)."""
        if not 0 <= int(value) <= 255:
            raise ValueError("Reference trim must be between 0 and 255.")
        self._write(f"REFT {int(value)}", source=False)

    def set_spur_mode(self, mode="LN1", source=None):
        """Set the spur mitigation mode: LN1 (default), LN2, LS1 or LS2."""
        if mode.upper() not in self.SPUR_MODES:
            raise ValueError(f"Invalid spur mode {mode}. Use one of {self.SPUR_MODES}.")
        self._write(f"SDN {mode.upper()}", source)

    def get_spur_mode(self, source=None):
        return self._query_value("SDN?", "SDN", source)[0].upper()

    def set_charge_pump(self, value: int, source=None):
        """Set the 4-bit charge pump current (0..15, optimum 8)."""
        if not 0 <= int(value) <= 15:
            raise ValueError("Charge pump must be between 0 and 15.")
        self._write(f"CP {int(value)}", source)

    def get_charge_pump(self, source=None) -> int:
        return int(self._query_float("CP?", "CP", source))

    def set_name(self, name: str, source=None):
        """Set the alias name of the source (max 48 characters)."""
        if len(name) > 48:
            raise ValueError("Name must be at most 48 characters.")
        self._write(f"NAMe {name}", source)

    def get_name(self, source=None):
        return self._write("NAMe?", source)


if __name__ == "__main__":
    print("Available ports:", Valon_5009b_Driver.list_ports())
    valon = Valon_5009b_Driver(port="COM11")
    valon.connect()
    print(valon.get_id())

    for src in Valon_5009b_Driver.SOURCES:
        print(f"Source {src}: {valon.get_frequency_MHz(src)} MHz, "
              f"ATT {valon.get_attenuation_dB(src)} dB, "
              f"mode {valon.get_mode(src)}, locked {valon.is_locked(src)}")

    valon.disconnect()
