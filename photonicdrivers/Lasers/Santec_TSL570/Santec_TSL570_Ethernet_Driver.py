"""
Santec TSL-570 tunable laser driver, over ethernet.

Section references in this module point to the TSL-570 operation manual
(TSL-570-M-E-v1.5, chapter 6 = detailed operation, 7.4 = command reference), which
lives at:
    N:/SCI-NBI-NQCP/Phot/manualsEtc/SANTEC TSL570/USB stick contents/TSL-570/Product Manual/
"""

from photonicdrivers.Abstract.Connectable import Connectable
import pyvisa
import logging

SPEED_OF_LIGHT_M_PER_S = 299792458.0

# Command sets, see ":SYSTem:COMMunicate:CODe" in manual chapter 7.4.
# The unit of every value the laser sends and accepts depends on this setting:
#   Legacy: wavelengths in nm, frequencies in THz
#   SCPI:   wavelengths in m,  frequencies in Hz
# This driver assumes the laser is in SCPI mode.
COMMAND_SET_LEGACY = 0
COMMAND_SET_SCPI = 1

# Modulation sources, see ":AM:SOURce" in manual chapter 7.4.
MODULATION_SOURCE_COHERENCE_CONTROL = 0
MODULATION_SOURCE_INTENSITY_MODULATION = 1
MODULATION_SOURCE_FREQUENCY_MODULATION = 3

# Fine-tuning limits, see manual chapter 6.1.
# The fine-tuning value is a unitless number that spans roughly 10 GHz in total
# (about 80 pm around 1550 nm) with a resolution below 1 MHz. Increasing the value
# shifts the output to a SHORTER wavelength, i.e. to a HIGHER optical frequency.
FINE_TUNING_MIN = -100.00
FINE_TUNING_MAX = 100.00
FINE_TUNING_STEP = 0.01
FINE_TUNING_RANGE_HZ = 10e9

# Frequency modulation ("Frequency Mod." external modulation) specifications, see
# manual chapter 6.3.2. The signal is applied to the "ANALOG INPUT" BNC connector on
# the rear panel. Exceeding the input voltage range may damage the laser.
FREQUENCY_MODULATION_INPUT_MIN_V = -1.2
FREQUENCY_MODULATION_INPUT_MAX_V = 1.2
FREQUENCY_MODULATION_DEPTH_HZ_PER_V = 5e9
FREQUENCY_MODULATION_BANDWIDTH_HZ = 100.0
FREQUENCY_MODULATION_INPUT_IMPEDANCE_OHM = 4700.0

# Intensity modulation specifications, see manual chapter 6.3.1.
INTENSITY_MODULATION_INPUT_MIN_V = -2.0
INTENSITY_MODULATION_INPUT_MAX_V = 0.0
INTENSITY_MODULATION_BANDWIDTH_HZ = 400e3
INTENSITY_MODULATION_INPUT_IMPEDANCE_OHM = 100.0

# Smallest step of the ":WAVelength:FREQuency" command, see manual chapter 7.4.
FREQUENCY_SET_STEP_HZ = 10e6


def wavelength_nm_to_frequency_Hz(wavelength_nm: float) -> float:
    """
    Converts a vacuum wavelength [nm] to an optical frequency [Hz].
    """
    return SPEED_OF_LIGHT_M_PER_S / (wavelength_nm * 1e-9)


def frequency_Hz_to_wavelength_nm(frequency_Hz: float) -> float:
    """
    Converts an optical frequency [Hz] to a vacuum wavelength [nm].
    """
    return SPEED_OF_LIGHT_M_PER_S / frequency_Hz * 1e9


class Santec_TSL570_driver(Connectable):
    def __init__(
        self,
        ip_address: str,
        port_number: str,
        resource_manager: pyvisa.ResourceManager = None,
        prints_enabled=False,
    ):
        self.prints_enabled = prints_enabled
        if resource_manager is not None:
            self.resource_manager = resource_manager
        else:
            self.resource_manager = pyvisa.ResourceManager()
        self.ip_address = ip_address
        self.port_number = port_number

    def connect(self):
        """
        Connects to laser
        """
        try:
            self.laser = self.resource_manager.open_resource(
                f"TCPIP0::{self.ip_address}::{self.port_number}::SOCKET",
                write_termination="\n",
                read_termination="\r",
            )
            if self.prints_enabled:
                logging.info("Succesfully connected to laser.")
        except Exception as e:
            if self.prints_enabled:
                logging.error(f"Couldn't connect to the laser due to the error: {e}")
            else:
                raise

    def disconnect(self):
        """
        Closes the connections to laser
        """
        self.laser.close()
        if self.prints_enabled:
            print("Connection to laser closed.")

    def is_connected(self):
        try:
            return bool(self.get_idn() is not None)
        except Exception as e:
            if self.prints_enabled:
                logging.error(f"Couldn't get ID due to the error: {e}")
            return False

    def get_idn(self):
        """
        Retrieves the identification string of the Santec TSL-570 laser.
        """
        return_msg = self.laser.query("*IDN?")
        return_msg_split = return_msg.split(",")
        manufacturer = return_msg_split[0]
        model = return_msg_split[1]
        serial_number = return_msg_split[2]
        firmware_version = return_msg_split[3]
        if self.prints_enabled:
            print("Identification string returned:")
            print(f"- Manufacturer: {manufacturer}")
            print(f"- Model: {model}")
            print(f"- Serial number: {serial_number}")
            print(f"- Firmware version: {firmware_version}")
        else:
            return manufacturer, model, serial_number, firmware_version

    def get_wavelength(self) -> float:
        """
        Gets and returns the current set wavelength

        Args:
            None
        Returns:
            float: wavelength in nm
        """
        msg = ":WAV?"
        return_msg = self.laser.query(msg)
        wavelength_in_nm = float(return_msg) * 1e9
        return wavelength_in_nm

    def get_wavelength_nm(self) -> float:
        """
        Gets and returns the current set wavelength [nm].

        Unit-explicit alias of get_wavelength(), which also returns nm. Prefer this
        one: the matching setter set_wavelength() takes metres, not nm.

        Args:
            None
        Returns:
            float: wavelength in nm
        """
        return self.get_wavelength()

    def set_wavelength_nm(self, wavelength_nm: float) -> None:
        """
        Set wavelength [nm] of the laser.

        Unit-explicit wrapper around set_wavelength(), which takes metres.

        Args:
            wavelength_nm (float): wavelength in nm
        Returns:
            None
        """
        self.set_wavelength(wavelength_nm * 1e-9)

    def get_frequency_Hz(self) -> float:
        """
        Gets and returns the current set optical frequency [Hz].

        Uses the laser's native ":FREQuency?" command rather than converting the
        wavelength by hand, so the value matches what the laser computes internally.
        In SCPI command set mode the laser answers in Hz.

        Args:
            None
        Returns:
            float: optical frequency in Hz
        """
        msg = ":FREQ?"
        return_msg = self.laser.query(msg)
        frequency_in_Hz = float(return_msg)
        return frequency_in_Hz

    def get_frequency_MHz(self) -> float:
        """
        Gets and returns the current set optical frequency [MHz].

        Args:
            None
        Returns:
            float: optical frequency in MHz
        """
        return self.get_frequency_Hz() * 1e-6

    def get_frequency_GHz(self) -> float:
        """
        Gets and returns the current set optical frequency [GHz].

        Args:
            None
        Returns:
            float: optical frequency in GHz
        """
        return self.get_frequency_Hz() * 1e-9

    def get_frequency_THz(self) -> float:
        """
        Gets and returns the current set optical frequency [THz].

        Args:
            None
        Returns:
            float: optical frequency in THz
        """
        return self.get_frequency_Hz() * 1e-12

    def set_frequency_Hz(self, frequency_Hz: float) -> None:
        """
        Set the optical frequency [Hz] of the laser.

        The laser tunes in steps of 10 MHz (see ":FREQuency" in the manual). Use
        fine-tuning or external frequency modulation for finer steps.

        Args:
            frequency_Hz (float): optical frequency in Hz
        Returns:
            None
        """
        msg = ":FREQuency " + "{:.12g}".format(frequency_Hz)
        self.laser.write(msg)

    def set_frequency_MHz(self, frequency_MHz: float) -> None:
        """
        Set the optical frequency [MHz] of the laser.

        Args:
            frequency_MHz (float): optical frequency in MHz
        Returns:
            None
        """
        self.set_frequency_Hz(frequency_MHz * 1e6)

    def set_frequency_GHz(self, frequency_GHz: float) -> None:
        """
        Set the optical frequency [GHz] of the laser.

        Args:
            frequency_GHz (float): optical frequency in GHz
        Returns:
            None
        """
        self.set_frequency_Hz(frequency_GHz * 1e9)

    def set_frequency_THz(self, frequency_THz: float) -> None:
        """
        Set the optical frequency [THz] of the laser.

        Args:
            frequency_THz (float): optical frequency in THz
        Returns:
            None
        """
        self.set_frequency_Hz(frequency_THz * 1e12)

    def get_wavelength_unit(self) -> str:
        
        """
        OBS not sure if this code work!!
        Check!

        Get wavelength unit of the laser wavelength [nm]

        Args:
            None
        Returns:
            str: wavelength unit of the laser
        """
        msg = ":WAV:UNIT?"
        return_msg = self.laser.query(msg)
        return return_msg

    def get_power(self) -> float:
        """
        Get power [dBm] of the laser

        Args:
            None
        Returns:
            float: power of the laser
        """
        msg = ":POW?"
        return_msg = self.laser.query(msg)
        power_value = float(return_msg)
        return power_value

    def get_power_unit(self) -> str:
        """
        Get power unit of the laser power [dBm or mW]

        Args:
            None
        Returns:
            str: power unit of the laser

        """
        msg = ":POW:UNIT?"
        return_msg = self.laser.query(msg)
        if return_msg:
            return "dBm"
        else:
            return "mW"

    def set_power_unit(self, unit: str) -> None:
        """
        OBS: This code has not been tested!

        Set power unit of the laser power [dBm or mW]

        Args:
            unit (str): Desired unit, either 'dBm' or 'mW'
        """
        unit = unit.strip().lower()
        if unit == "dbm":
            cmd = ":POW:UNIT DBM"
        elif unit == "mw":
            cmd = ":POW:UNIT MW"
        else:
            raise ValueError("Invalid unit. Must be 'dBm' or 'mW'.")

        self.laser.write(cmd)

    def get_emission_status(self) -> int:
        """
        Get laser emission status

        Args:
            None
        Returns:
            int: 1 if laser is ON, 0 if laser is OFF
        """
        msg = ":POW:STAT?"
        return_msg = self.laser.query(msg)
        emission_status = int(return_msg)
        return emission_status

    def get_operation_status(self) -> int:
        """
        Get laser operation status, that is, if a command is in operation

        Args:
            None
        Returns:
            int: 0 if laser is in operation, 1 if laser is not in operation
        """
        msg = "*OPC?"
        return_msg = self.laser.query(msg)
        operation_status = int(return_msg)
        return operation_status

    def set_wavelength(self, wavelength_m: float) -> None:
        """
        Set wavelength [m] of the laser

        Args:
            wavelength_nm (float): wavelength in m
        Returns:
            None
        """

        msg = ":WAVelength  " + str(wavelength_m) # + "e-9"
        self.laser.write(msg)

    def set_wavelength_unit(self, unit: str):
        """
        Set the unit the laser shows on its own display: 'nm' or 'THz'.

        This only changes the front panel display. It does not change the unit used
        over the communication interface, which is fixed by the command set (see
        ":SYSTem:COMMunicate:CODe").

        Args:
            unit (str): Desired display unit, either 'nm' or 'THz'
        Returns:
            None
        """
        unit = unit.strip().lower()
        if unit == "nm":
            unit_int = 0
        elif unit == "thz":
            unit_int = 1
        else:
            raise ValueError("Invalid unit. Must be 'nm' or 'THz'.")

        cmd = ":WAV:UNIT " + str(unit_int)
        self.laser.write(cmd)

    def get_command_set(self) -> int:
        """
        Get the command set the laser is using.

        The command set decides which units the laser uses on the communication
        interface. This driver assumes SCPI mode (wavelengths in m, frequencies in Hz).

        Args:
            None
        Returns:
            int: 0 for Legacy, 1 for SCPI
        """
        msg = ":SYST:COMM:COD?"
        return_msg = self.laser.query(msg)
        return int(return_msg)

    def set_command_set(self, command_set: int) -> None:
        """
        Set the command set of the laser.

        Args:
            command_set (int): 0 for Legacy, 1 for SCPI
        Returns:
            None
        """
        if command_set not in [COMMAND_SET_LEGACY, COMMAND_SET_SCPI]:
            raise ValueError("Invalid command set. Must be 0 (Legacy) or 1 (SCPI).")
        msg = ":SYST:COMM:COD " + str(command_set)
        self.laser.write(msg)

    ####################### FINE-TUNING (manual chapter 6.1) #######################

    def get_fine_tuning(self) -> float:
        """
        Get the current fine-tuning value.

        The value is unitless and spans about 10 GHz in total (roughly 80 pm around
        1550 nm) over its -100 to +100 range, with a resolution below 1 MHz.

        Args:
            None
        Returns:
            float: fine-tuning value in the range -100.00 to +100.00
        """
        msg = ":WAV:FIN?"
        return_msg = self.laser.query(msg)
        return float(return_msg)

    def set_fine_tuning(self, fine_tuning_value: float) -> None:
        """
        Set the fine-tuning value, which puts the laser into fine-tuning mode.

        Increasing the value shifts the output to a SHORTER wavelength, i.e. to a
        HIGHER optical frequency.

        While fine-tuning is active the closed-loop wavelength control of the laser is
        stopped, so the output may drift with the environment. Call
        disable_fine_tuning() or set the wavelength again to restart closed-loop
        control.

        Args:
            fine_tuning_value (float): fine-tuning value, -100.00 to +100.00, step 0.01
        Returns:
            None
        """
        if not FINE_TUNING_MIN <= fine_tuning_value <= FINE_TUNING_MAX:
            raise ValueError(
                f"Invalid fine-tuning value. Must be between {FINE_TUNING_MIN} and {FINE_TUNING_MAX}."
            )
        msg = ":WAV:FIN " + "{:.2f}".format(fine_tuning_value)
        self.laser.write(msg)

    def disable_fine_tuning(self) -> None:
        """
        Terminate fine-tuning operation and restart closed-loop wavelength control.

        Args:
            None
        Returns:
            None
        """
        msg = ":WAV:FIN:DIS"
        self.laser.write(msg)

    ####################### MODULATION (manual chapter 6.2 and 6.3) #######################

    def get_modulation_source(self) -> int:
        """
        Get the selected modulation source.

        Args:
            None
        Returns:
            int: 0 for coherence control, 1 for intensity modulation,
                 3 for frequency modulation
        """
        msg = ":AM:SOUR?"
        return_msg = self.laser.query(msg)
        return int(return_msg)

    def set_modulation_source(self, source: int) -> None:
        """
        Select the modulation source.

        Intensity modulation and frequency modulation are both driven by an external
        analog signal on the rear panel "ANALOG INPUT" BNC connector. Frequency
        modulation is the one that fine tunes the wavelength; see chapter 6.3.2 of the
        manual for the input voltage range and the modulation depth.

        The source only takes effect once modulation is enabled with
        set_modulation_state(True).

        Args:
            source (int): 0 for coherence control, 1 for intensity modulation,
                          3 for frequency modulation
        Returns:
            None
        """
        valid_sources = [
            MODULATION_SOURCE_COHERENCE_CONTROL,
            MODULATION_SOURCE_INTENSITY_MODULATION,
            MODULATION_SOURCE_FREQUENCY_MODULATION,
        ]
        if source not in valid_sources:
            raise ValueError(
                "Invalid modulation source. Must be 0 (coherence control), "
                "1 (intensity modulation) or 3 (frequency modulation)."
            )
        msg = ":AM:SOUR " + str(source)
        self.laser.write(msg)

    def get_modulation_state(self) -> bool:
        """
        Get whether the modulation function of the laser output is enabled.

        Args:
            None
        Returns:
            bool: True if modulation is enabled, False otherwise
        """
        msg = ":AM:STAT?"
        return_msg = self.laser.query(msg)
        return bool(int(return_msg))

    def set_modulation_state(self, enabled: bool) -> None:
        """
        Enable or disable the modulation function of the laser output.

        With frequency modulation selected, enabling modulation stops the closed-loop
        wavelength control, so the output frequency may drift with the environment.
        This is why external fine tuning is normally used together with a wavemeter.

        Args:
            enabled (bool): True to enable modulation, False to disable it
        Returns:
            None
        """
        msg = ":AM:STAT " + str(int(bool(enabled)))
        self.laser.write(msg)

    def set_frequency_modulation_enabled(self, enabled: bool) -> None:
        """
        Put the laser into (or out of) external frequency modulation mode.

        This is the mode used to fine tune the optical frequency with an external
        analog voltage on the rear panel "ANALOG INPUT" connector, at about
        5 GHz/V over a -1.2 V to +1.2 V input range (manual chapter 6.3.2).

        Never apply a voltage outside that range: it may damage the laser.

        Args:
            enabled (bool): True to select frequency modulation and enable modulation,
                            False to disable modulation
        Returns:
            None
        """
        if enabled:
            self.set_modulation_source(MODULATION_SOURCE_FREQUENCY_MODULATION)
            self.set_modulation_state(True)
        else:
            self.set_modulation_state(False)

    def get_coherence_control(self) -> bool:
        """
        Get the coherence control status.

        Coherence control broadens the spectral linewidth of the output, which
        suppresses power fluctuations caused by interference. It must be off for
        narrow-linewidth fine tuning.

        Args:
            None
        Returns:
            bool: True if coherence control is on, False otherwise
        """
        msg = ":COHC?"
        return_msg = self.laser.query(msg)
        return bool(int(return_msg))

    def set_coherence_control(self, enabled: bool) -> None:
        """
        Set the coherence control status.

        Args:
            enabled (bool): True to turn coherence control on, False to turn it off
        Returns:
            None
        """
        msg = ":COHC " + str(int(bool(enabled)))
        self.laser.write(msg)

    def set_power(self, power_dBm: float):
        """
        Set power [dBm] of the laser
        """
        power_dBm_decimal = "{:.2e}".format(power_dBm)
        msg = ":POW " + str(power_dBm_decimal)
        self.laser.write(msg)

    def set_emission_status(self, emission: bool):
        """
        Set laser emission ON or OFF: emission = True to turn ON laser, emission = False to turn OFF laser

        Args:
            emission (bool): True to turn ON laser, False to turn OFF laser
        Returns:
            None
        """
        if emission:
            emission_int = 1
        else:
            emission_int = 0
        msg = ":POW:STAT " + str(emission_int)
        self.laser.write(msg)

    def start_single_sweep(self):
        """
        Start a single sweep of the laser

        Args:
            None
        Returns:
            None
        """
        msg = ":WAV:SWE: 1"
        self.laser.write(msg)

    def get_sweep_status(self) -> int:
        """
        Get the current sweep status of the laser

        Args:
            None
        Returns:
            int: 1 if sweep is running, 0 if sweep is stopped
        """
        msg = ":WAV:SWE?"
        return_msg = self.laser.query(msg)
        sweep_status = int(return_msg)
        return sweep_status

    def get_sweep_cycles(self) -> int:
        """
        Get the number of sweep cycles for the laser

        Args:
            None
        Returns:
            int: Number of sweep cycles
        """
        msg = ":WAV:SWE:CYCL?"
        return_msg = self.laser.query(msg)
        sweep_cycles = int(return_msg)
        return sweep_cycles

    def set_sweep_cycles(self, cycles: int):
        """
        Set the number of sweep cycles for the laser

        Args:
            cycles (int): Number of sweep cycles
        """
        msg = ":WAV:SWE:CYCL " + str(cycles)
        self.laser.write(msg)


    def start_repeating_sweep(self):
        """
        Start a repeating sweep of the laser

        Args:
            None
        Returns:
            None
        """
        msg = ":WAV:SWE:REP"
        self.laser.write(msg)

    def set_sweep_start(self, start_wavelength_nm: float):
        """
        Set the start wavelength of the sweep in nm

        Args:
            start_wavelength_nm (float): Start wavelength in nm
        Returns:
            None
        """

        msg = ":WAV:SWE:STAR " + str(start_wavelength_nm * 1e-9)
        self.laser.write(msg)

    def set_sweep_stop(self, stop_wavelength_nm: float):
        """
        Set the stop wavelength of the sweep in nm

        Args:
            stop_wavelength_nm (float): Stop wavelength in nm
        Returns:
            None
        """
        msg = ":WAV:SWE:STOP " + str(stop_wavelength_nm * 1e-9)
        self.laser.write(msg)

    def get_sweep_start(self) -> float:
        """
        Get the start wavelength of the sweep in nm

        Args:
            None
        Returns:
            float: Start wavelength in nm
        """
        msg = ":WAV:SWE:STAR?"
        return_msg = self.laser.query(msg)
        start_wavelength_nm = float(return_msg) * 1e9
        return start_wavelength_nm

    def get_sweep_stop(self) -> float:
        """
        Get the stop wavelength of the sweep in nm

        Args:
            None
        Returns:
            float: Stop wavelength in nm
        """
        msg = ":WAV:SWE:STOP?"
        return_msg = self.laser.query(msg)
        stop_wavelength_nm = float(return_msg) * 1e9
        return stop_wavelength_nm

    def set_sweep_start_frequency_Hz(self, start_frequency_Hz: float):
        """
        Set the start frequency of the sweep in Hz

        Note that the start frequency corresponds to the stop wavelength, since
        frequency and wavelength run in opposite directions.

        Args:
            start_frequency_Hz (float): Start frequency in Hz
        Returns:
            None
        """
        msg = ":FREQ:SWE:STAR " + "{:.12g}".format(start_frequency_Hz)
        self.laser.write(msg)

    def get_sweep_start_frequency_Hz(self) -> float:
        """
        Get the start frequency of the sweep in Hz

        Args:
            None
        Returns:
            float: Start frequency in Hz
        """
        msg = ":FREQ:SWE:STAR?"
        return_msg = self.laser.query(msg)
        return float(return_msg)

    def set_sweep_stop_frequency_Hz(self, stop_frequency_Hz: float):
        """
        Set the stop frequency of the sweep in Hz

        Args:
            stop_frequency_Hz (float): Stop frequency in Hz
        Returns:
            None
        """
        msg = ":FREQ:SWE:STOP " + "{:.12g}".format(stop_frequency_Hz)
        self.laser.write(msg)

    def get_sweep_stop_frequency_Hz(self) -> float:
        """
        Get the stop frequency of the sweep in Hz

        Args:
            None
        Returns:
            float: Stop frequency in Hz
        """
        msg = ":FREQ:SWE:STOP?"
        return_msg = self.laser.query(msg)
        return float(return_msg)

    def set_sweep_step_frequency_Hz(self, step_frequency_Hz: float):
        """
        Set the step of the step sweep mode in Hz

        Args:
            step_frequency_Hz (float): Step size in Hz
        Returns:
            None
        """
        msg = ":FREQ:SWE:STEP " + "{:.12g}".format(step_frequency_Hz)
        self.laser.write(msg)

    def get_sweep_step_frequency_Hz(self) -> float:
        """
        Get the step of the step sweep mode in Hz

        Args:
            None
        Returns:
            float: Step size in Hz
        """
        msg = ":FREQ:SWE:STEP?"
        return_msg = self.laser.query(msg)
        return float(return_msg)

    def get_sweep_frequency_range_Hz(self) -> tuple[float, float]:
        """
        Get the minimum and maximum configurable sweep frequency in Hz

        Args:
            None
        Returns:
            tuple[float, float]: (minimum frequency, maximum frequency) in Hz
        """
        minimum_frequency_Hz = float(self.laser.query(":FREQ:SWE:RANG:MIN?"))
        maximum_frequency_Hz = float(self.laser.query(":FREQ:SWE:RANG:MAX?"))
        return minimum_frequency_Hz, maximum_frequency_Hz

    def set_sweep_speed(self, speed_nm_per_s: float):
        """
        Set the sweep speed of the laser in nm/s

        Args:
            speed_nm_per_s (float): Sweep speed in nm/s [1,2,4,10,20,50,100,200]
        Returns:
            None
        """
        if speed_nm_per_s not in [1, 2, 4, 10, 20, 50, 100, 200]:
            raise ValueError(
                "Invalid sweep speed. Must be one of the following: [1, 2, 4, 10, 20, 50, 100, 200] nm/s"
            )
        msg = ":WAV:SWE:SPD: " + str(speed_nm_per_s)
        self.laser.write(msg)

    def get_sweep_speed(self) -> float:
        """
        Get the sweep speed of the laser in nm/s

        Args:
            None
        Returns:
            float: Sweep speed in nm/s
        """
        msg = ":WAV:SWE:SPD?"
        return_msg = self.laser.query(msg)
        sweep_speed_nm_per_s = float(return_msg)
        return sweep_speed_nm_per_s

    def set_sweep_mode(self, mode: int):
        """
        Set the sweep mode of the laser

        Args:
            mode (int): 0 for step sweep mode one way, 1 for continuous sweep mode one way, 2 for step sweep mode two way, 3 for continuous sweep mode two way
        Returns:
            None
        """
        if mode not in [0, 1, 2, 3]:
            raise ValueError("Invalid mode. Must be 0, 1, 2, or 3.")
        msg = ":WAV:SWE:MOD " + str(mode)
        self.laser.write(msg)

    def get_sweep_mode(self):
        """
        Get the current sweep mode of the laser

        Args:
            None
        Returns:
            int: 0 for step sweep mode one way, 1 for continuous sweep mode one way, 2 for step sweep mode two way, 3 for continuous sweep mode two way
            str: Description of the current sweep mode
        """
        msg = ":WAV:SWE:MOD?"
        return_msg = self.laser.query(msg)
        if return_msg == 0:
            return 0, "Step sweep mode and One way"
        elif return_msg == 1:
            return 1, "Continuous sweep mode and One way"
        elif return_msg == 2:
            return 2, "Step sweep mode and Two way"
        elif return_msg == 3:
            return 3, "Continuous sweep mode and Two way"
        else:
            raise ValueError("Invalid sweep mode received from the laser: {}".format(return_msg))
        

    ####################### BLANKET FUNCTIONS #######################

    def write(self, message: str):
        """
        Write a message to the laser

        Args:
            message (str): message to write
        Returns:
            None
        """
        self.laser.write(message)

    def query(self, message: str):
        """
        Query a message to the laser
        """
        return self.laser.query(message)

    def read(self):
        """
        Read a message from the laser
        """
        return self.laser.read()


if __name__ == "__main__":


    # Check if the driver works
    from time import sleep

    rm = pyvisa.ResourceManager()
    santec = Santec_TSL570_driver(
        resource_manager = rm,
        ip_address="10.209.69.95",
        port_number="5000")
    santec.connect()
    santec.get_idn()

    # check all getter methods
    print("Wavelength [nm]: ", santec.get_wavelength())
    print("Power unit: ", santec.get_power_unit())
    print("Power: ", santec.get_power())
    print("Emission status: ", santec.get_emission_status())

    # check all setter methods
    santec.set_wavelength(1270.41)
    print("Operation status:", santec.get_operation_status())
    sleep_time = 0.01
    sleep(sleep_time)
    print(f"Operation status after {sleep_time}s sleep:", santec.get_operation_status())
    print("Wavelength [nm]: ", santec.get_wavelength())

    santec.set_power(-10)
    sleep_time = 0.1
    sleep(sleep_time)
    print("Power: ", santec.get_power())
    santec.set_emission_status(True)

    santec.disconnect()
    print("\nDone.")
