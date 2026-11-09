import socket
from photonicdrivers.Abstract.Connectable import Connectable

class Keithley2450_Driver(Connectable):

    def __init__(self, ip_address, port=5025):
        """
        Initialize the Keithley 2450 SourceMeter driver.

        :param ip_address: IP address of the Keithley 2450.
        :param port: Port number for SCPI communication (default is 5025).
        """
        self.ip_address = ip_address
        self.port = port
        self.socket = None

    def connect(self):
        """
        Establish a connection to the Keithley 2450.
        """
        if self.socket:
            print("Already connected.")
            return
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(10)  # Set a timeout for connection attempts

        try:
            self.socket.connect((self.ip_address, self.port))
            print(f"Connected to {self.ip_address}:{self.port}")
        except socket.timeout:
            print("Connection timed out.")
            self.socket = None
        except socket.error as e:
            print(f"Socket error: {e}")
            self.socket = None

    def disconnect(self):
        """
        Close the connection to the Keithley 2450.
        """
        if self.socket:
            self.socket.close()
            self.socket = None
            print("Connection closed.")

    def is_connected(self):
        try:
            print(self.identify())
            return True
        except: 
            return False

    def write(self, command):
        """
        Send an SCPI command to the Keithley 2450

        :param command: SCPI command to send.
        """
        if not self.socket:
            raise RuntimeError("Not connected to the device.")
        
        try:
            self.socket.sendall(command.encode('ascii') + b'\n')
        except socket.error as e:
            print(f"Socket error: {e}")
            return None

    def query(self, command):
        """
        Send an SCPI command to the Keithley 2450 and receive the response.

        :param command: SCPI command to send.
        :return: Response from the Keithley 2450.
        """
        if not self.socket:
            raise RuntimeError("Not connected to the device.")
        
        try:
            # A stale reply left in the socket (an earlier query whose answer was never read) shifted every later
            # answer by one (2026-11-09: :OUTP:STAT? returned the *IDN? string). Drop it, then read one whole line.
            self._drain()
            self.socket.sendall(command.encode('ascii') + b'\n')
            return self._read_line().decode('ascii').strip()
        except socket.error as e:
            print(f"Socket error on query '{command}': {e}")
            return None

    def _drain(self):
        """Discard any bytes already waiting in the socket (non-blocking)."""
        timeout = self.socket.gettimeout()
        self.socket.settimeout(0.0)
        try:
            while True:
                try:
                    chunk = self.socket.recv(4096)
                except (BlockingIOError, socket.timeout):
                    break
                if not chunk:
                    break
                print(f"Keithley2450: discarded a stale reply {chunk[:80]!r}")
        finally:
            self.socket.settimeout(timeout)

    def _read_line(self) -> bytes:
        """Read until the newline that ends an SCPI reply (a reply can arrive in several pieces)."""
        data = b""
        while not data.endswith(b"\n"):
            chunk = self.socket.recv(4096)
            if not chunk:
                break
            data += chunk
        return data
    
    def read(self):
        """
        Receive a response from Keithley 2450

        :return: Response from the Keithley 2450.
        """
        if not self.socket:
            raise RuntimeError("Not connected to the device.")
        
        try:
            response = self.socket.recv(4096)  # Adjust buffer size if needed
            return response.decode('ascii').strip()
        except socket.error as e:
            print(f"Socket error on read: {e}")
            return None

    def identify(self):
        """
        Query the Keithley 2450 for its identification information.

        :return: Identification string.
        """
        return self.query("*IDN?")
    

    def measure_voltage(self):
        """
        Measure voltage in Volts
        """
        return self.query(":MEAS:VOLT?")

    def measure_current(self):
        """
        Measure current in Amps
        """
        return self.query(":MEAS:CURR?")
    
    def set_voltage(self,value):
        """
        Set output voltage in Volts
        """
        self.write(f":SOUR:VOLT:LEV:IMM:AMPL {str(value)}")

    def set_current(self,value):
        """
        Set output current in amps
        """
        self.write(f":SOUR:CURR:LEV:IMM:AMPL {str(value)}")

    def set_output(self, value):
        """
        Start/stop output
        Value: 0 (off) or 1 (on)
        """
        self.write(f":OUTP:STAT {str(value)}")

    def set_voltage_output_range(self,value):
        """
        Set output voltage range in volts
        """
        self.write(f":SOUR:VOLT:RANG {str(value)}")

    def set_current_output_range(self,value):
        """
        Set output current range in amps
        """
        self.write(f":SOUR:CURR:RANG {str(value)}")
    
    def set_voltage_output_limit(self,value):
        """
        Set voltage limit in volts
        """
        self.write(f":SOUR:CURR:VLIM {str(value)}")

    def set_current_output_limit(self,value):
        """
        Set current limit in amps
        """
        self.write(f":SOUR:VOLT:ILIM {str(value)}")

    def set_voltage_measurement_range(self,value):
        """
        Set measurement voltage range in volts
        """
        self.write(f":SENS:VOLT:RANG {str(value)}")

    def set_current_measurement_range(self,value):
        """
        Set measurement current range in amps
        """
        self.write(f":SENS:CURR:RANG {str(value)}")

    def get_voltage_source_level(self):
        """
        Get voltage source level in volts
        """
        return self.query(":SOUR:VOLT:LEV:IMM:AMPL?")

    def get_current_source_level(self):
        """
        Get current source level in amps
        """
        return self.query(":SOUR:CURR:LEV:IMM:AMPL?")
    
    def get_voltage_output_limit(self):
        """
        Get voltage limit in volts
        """
        return self.query(":SOUR:CURR:VLIM?")
    
    def get_current_output_limit(self):
        """
        Get current limit in amps
        """
        return self.query(":SOUR:VOLT:ILIM?")

    def get_voltage_output_range(self):
        """
        Get output voltage range in volts
        """
        return self.query(":SOUR:VOLT:RANG?")

    def get_current_output_range(self):
        """
        Get output current range in amps
        """
        return self.query(":SOUR:CURR:RANG?")
    
    def get_voltage_measurement_range(self):
        """
        Get measurement voltage range in volts
        """
        return self.query(":SENS:VOLT:RANG?")

    def get_current_measurement_range(self):
        """
        Get measurement current range in amps
        """
        return self.query(":SENS:CURR:RANG?")

    # ------------------------------------------------------------------------------------------------------------
    # Hardware-timed operation (added 2026-11-09): source lists, list sweeps, trigger-model templates and reading
    # buffers. The instrument steps the source and takes the readings itself, so the timing does not depend on
    # the LAN round trip of one SCPI command per level. SCPI syntax from the Model 2450 Reference Manual,
    # section 6 (:SOURce:LIST, :SOURce:SWEep:<function>:LIST, :TRIGger:LOAD, :TRACe); the buffer element names as
    # in QCoDeS' Keithley_2450 driver. NOT YET TESTED ON THE INSTRUMENT - see photonicdrivers/Keithley/README.md.
    # ------------------------------------------------------------------------------------------------------------

    MAX_LIST_VALUES_PER_COMMAND = 100   # :SOURce:LIST:<function>[:APPend] takes at most 100 values per command
    MAX_LIST_VALUES = 2500              # one source list holds at most 2500 values
    BUFFER_ELEMENTS = {"reading": "READ", "source": "SOUR", "relative_time": "REL", "seconds": "SEC",
                       "fractional_seconds": "FRAC", "status": "STAT", "source_status": "SOURSTAT",
                       "unit": "UNIT", "source_unit": "SOURUNIT"}
    STRING_ELEMENTS = ("status", "source_status", "unit", "source_unit")
    # Newer firmware: :TRIG:LOAD "DurationLoop", ...; manual rev B (2013): :TRIG:LOAD:LOOP:DUR ... Which one this
    # unit takes is not known yet (README).
    TRIGGER_LOAD_SYNTAXES = ("named", "legacy")

    @staticmethod
    def _on_off(value) -> str:
        return "ON" if bool(value) else "OFF"

    @staticmethod
    def _function(function: str) -> str:
        names = {"voltage": "VOLT", "volt": "VOLT", "current": "CURR", "curr": "CURR"}
        key = str(function).strip().lower()
        if key not in names:
            raise ValueError(f"function must be 'voltage' or 'current', got {function!r}")
        return names[key]

    def set_source_function(self, function: str):
        """Source voltage or current: 'voltage' / 'current'."""
        self.write(f":SOUR:FUNC {self._function(function)}")

    def set_sense_function(self, function: str):
        """Measure current or voltage: 'current' / 'voltage'."""
        self.write(f':SENS:FUNC "{self._function(function)}"')

    def set_measurement_nplc(self, nplc: float, function: str = "current"):
        """Integration time in power-line cycles, 0.01 to 10 (0.01 NPLC = 0.2 ms at 50 Hz)."""
        if not 0.01 <= float(nplc) <= 10:
            raise ValueError(f"nplc must be within 0.01..10, got {nplc}")
        self.write(f":SENS:{self._function(function)}:NPLC {float(nplc)}")

    def get_measurement_nplc(self, function: str = "current"):
        return self.query(f":SENS:{self._function(function)}:NPLC?")

    def set_measurement_autozero(self, on: bool, function: str = "current"):
        """Autozero at every reading (on) or not (off: faster; the zero drifts with time and temperature)."""
        self.write(f":SENS:{self._function(function)}:AZER {self._on_off(on)}")

    def set_measurement_autorange(self, on: bool, function: str = "current"):
        self.write(f":SENS:{self._function(function)}:RANG:AUTO {self._on_off(on)}")

    def set_source_readback(self, on: bool, function: str = "voltage"):
        """On: the buffer's 'source' element is the measured output, not the programmed level."""
        self.write(f":SOUR:{self._function(function)}:READ:BACK {self._on_off(on)}")

    def set_source_delay(self, delay_s: float, function: str = "voltage"):
        """Fixed delay after the source changes, before the reading (s)."""
        if float(delay_s) < 0:
            raise ValueError(f"delay_s must be >= 0, got {delay_s}")
        self.write(f":SOUR:{self._function(function)}:DEL {float(delay_s)}")

    def set_source_delay_auto(self, on: bool, function: str = "voltage"):
        self.write(f":SOUR:{self._function(function)}:DEL:AUTO {self._on_off(on)}")

    def set_source_list(self, values, function: str = "voltage"):
        """Replace the source list (configuration list VoltCustomSweepList / CurrCustomSweepList) with `values`,
        sent in commands of at most 100 values (the first replaces the list, the rest append). At most 2500."""
        values = [float(v) for v in values]
        if not values:
            raise ValueError("the source list is empty")
        if len(values) > self.MAX_LIST_VALUES:
            raise ValueError(f"at most {self.MAX_LIST_VALUES} values in a source list, got {len(values)}")
        f = self._function(function)
        n = self.MAX_LIST_VALUES_PER_COMMAND
        for i in range(0, len(values), n):
            chunk = ", ".join(repr(v) for v in values[i:i + n])
            self.write(f":SOUR:LIST:{f} {chunk}" if i == 0 else f":SOUR:LIST:{f}:APP {chunk}")

    def get_source_list_points(self, function: str = "voltage") -> int:
        return int(float(self.query(f":SOUR:LIST:{self._function(function)}:POIN?")))

    def configure_list_sweep(self, start_index: int = 1, delay_s: float = 0.0, count: int = 1,
                             fail_abort: bool = True, buffer_name: str = "defbuffer1", function: str = "voltage"):
        """Load the trigger model with a sweep through the source list: at every list value the source is set,
        `delay_s` waited (0, or 50 us to 10000 s; added to the source delay) and one reading stored in
        `buffer_name`; `count` passes through the whole list (0 = until aborted). Starts only with initiate()."""
        if not (float(delay_s) == 0 or 50e-6 <= float(delay_s) <= 10000):
            raise ValueError(f"delay_s must be 0 or within 50e-6..10000 s, got {delay_s}")
        if not 0 <= int(count) <= 268435455:
            raise ValueError(f"count must be within 0..268435455, got {count}")
        self.write(f":SOUR:SWE:{self._function(function)}:LIST {int(start_index)}, {float(delay_s)}, {int(count)}, "
                   f"{self._on_off(fail_abort)}, \"{buffer_name}\"")

    def _check_trigger_load_syntax(self, syntax: str):
        if syntax not in self.TRIGGER_LOAD_SYNTAXES:
            raise ValueError(f"syntax must be one of {self.TRIGGER_LOAD_SYNTAXES}, got {syntax!r}")

    def load_duration_loop(self, duration_s: float, delay_s: float = 0.0, buffer_name: str = "defbuffer1",
                           syntax: str = "named"):
        """Load the trigger model 'read continuously for duration_s' (0 to 100000 s; delay_s before each
        reading). The source stays where it is. Starts only with initiate()."""
        self._check_trigger_load_syntax(syntax)
        if not 0 <= float(duration_s) <= 100000:
            raise ValueError(f"duration_s must be within 0..100000, got {duration_s}")
        if syntax == "named":
            self.write(f':TRIG:LOAD "DurationLoop", {float(duration_s)}, {float(delay_s)}, "{buffer_name}"')
        else:
            self.write(f':TRIG:LOAD:LOOP:DUR {float(duration_s)}, {float(delay_s)}, "{buffer_name}"')

    def load_simple_loop(self, count: int, delay_s: float = 0.0, buffer_name: str = "defbuffer1",
                         syntax: str = "named"):
        """Load the trigger model 'take `count` readings, delay_s before each'. Starts only with initiate()."""
        self._check_trigger_load_syntax(syntax)
        if int(count) < 1:
            raise ValueError(f"count must be >= 1, got {count}")
        if syntax == "named":
            self.write(f':TRIG:LOAD "SimpleLoop", {int(count)}, {float(delay_s)}, "{buffer_name}"')
        else:
            self.write(f':TRIG:LOAD:LOOP:SIMP {int(count)}, {float(delay_s)}, "{buffer_name}"')

    def initiate(self):
        """Start the loaded trigger model (a sweep or a loop)."""
        self.write(":INIT")

    def abort(self):
        """Stop the trigger model. The source level and the output state are not changed by this."""
        self.write(":ABOR")

    def get_trigger_state(self) -> str:
        """The trigger model's state: the first field of :TRIG:STAT? (e.g. 'IDLE', 'RUNNING', 'WAITING',
        'ABORTED', 'FAILED')."""
        reply = self.query(":TRIG:STAT?")
        return reply.split(";")[0].strip().upper() if reply else reply

    def clear_buffer(self, buffer_name: str = "defbuffer1"):
        self.write(f':TRAC:CLE "{buffer_name}"')

    def set_buffer_size(self, points: int, buffer_name: str = "defbuffer1"):
        """Resize the buffer (this clears it)."""
        self.write(f':TRAC:POIN {int(points)}, "{buffer_name}"')

    def get_buffer_size(self, buffer_name: str = "defbuffer1") -> int:
        return int(float(self.query(f':TRAC:POIN? "{buffer_name}"')))

    def get_buffer_count(self, buffer_name: str = "defbuffer1") -> int:
        """The number of readings in the buffer now."""
        return int(float(self.query(f':TRAC:ACT? "{buffer_name}"')))

    def get_buffer_data(self, start: int, end: int, elements=("reading", "relative_time"),
                        buffer_name: str = "defbuffer1", chunk: int = 500) -> dict:
        """Readings start..end (1-based, inclusive) as {element: [values]}, read in pieces of `chunk` readings.
        Elements: keys of BUFFER_ELEMENTS - 'reading' (A or V), 'source' (V or A), 'relative_time' (s since the
        buffer's first reading), ...; the STRING_ELEMENTS come back as strings, the rest as floats."""
        codes = [self.BUFFER_ELEMENTS[e] for e in elements]
        out = {e: [] for e in elements}
        first = int(start)
        while first <= int(end):
            last = min(int(end), first + int(chunk) - 1)
            reply = self.query(f':TRAC:DATA? {first}, {last}, "{buffer_name}", {", ".join(codes)}')
            fields = [x.strip() for x in (reply or "").split(",")]
            expected = (last - first + 1) * len(codes)
            if len(fields) != expected:
                raise RuntimeError(f"buffer read {first}..{last}: {len(fields)} fields, expected {expected}")
            for k, element in enumerate(elements):
                column = fields[k::len(codes)]
                out[element].extend(column if element in self.STRING_ELEMENTS else [float(x) for x in column])
            first = last + 1
        return out

    def get_next_error(self) -> str:
        """The oldest entry of the error queue ('0,"No error"' when it is empty)."""
        return self.query(":SYST:ERR:NEXT?")