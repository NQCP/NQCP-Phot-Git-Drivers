# https://www.swabianinstruments.com/static/documentation/PulseStreamer/

from photonicdrivers.Abstract.Connectable import Connectable
from pulsestreamer import PulseStreamer, Sequence, OutputState, Sequence, ClockSource, TriggerRearm, TriggerStart, findPulseStreamers

#import the device detection
from pulsestreamer import findPulseStreamers

# import enum types
from pulsestreamer import TriggerStart

import time 
import numpy as np
    
HIGH = 1
LOW = 0
HIGH = 1
LOW = 0

class Pulse_Streamer_82_Driver(Connectable):
    def __init__(self, ip_address='pulsestreamer'):
        self.ip_address = ip_address
        self.driver: PulseStreamer = None

    def connect(self) -> None:
        self.driver = PulseStreamer(self.ip_address)
    
    def disconnect(self) -> None:
        self.driver = None
    
    def is_connected(self) -> bool:
        try:
            self.get_serial_number()
            return True
        except Exception:
            return False
        
    def get_serial_number(self):
        return self.driver.getSerial()
    
    def get_temperature(self):
        return self.driver.getTemperature()
    
    def reset(self):
        """Reset the pulse streamer to default state."""
        self.driver.reset()
    
    def is_streaming(self):
        """Check if the device is streaming."""
        return self.driver.isStreaming()
    
    def has_finished(self):
        return self.driver.hasFinished()

    def create_sequence(self):
        """Create a new empty sequence object."""
        return self.driver.createSequence()

    def set_trigger(self, trigger_type=TriggerStart.SOFTWARE):
        """Set the trigger type."""
        self.driver.setTrigger(trigger_type)

    def get_analog_calibration(self):
        return self.driver.getAnalogCalibration()
    
    def is_streaming(self):
        return self.driver.isStreaming()

    def has_finished(self):
        return self.driver.hasFinished()

    def has_sequence(self):
        return self.driver.hasSequence()

    def start(self):
        return self.driver.startNow()

    def get_temperature(self):
        return self.driver.getTemperature()

    def get_underflow(self):
        return self.driver.getUnderflow()

    def get_debug_register(self):
        return self.driver.getDebugRegister()

    def select_clock(self, source):
        if not isinstance(source, ClockSource):
            raise TypeError("source must be an instance of ClockSource Enum")
        return self.driver.selectClock(source.value)

    def get_clock(self):
        return ClockSource(self.driver.getClock())

    def set_square_wave_125MHz(self, channels=[]):
        return self.driver.setSquareWave125MHz(self.chans_to_mask(channels))

    def get_firmware_version(self):
        return self.driver.getFirmwareVersion()

    def get_hardware_version(self):
        return self.driver.getHardwareVersion()

    def get_supply_state(self):
        return self.driver.getSupplyState()

    def get_FPGAID(self):
        return self.driver.getFPGAID()

    def set_trigger(self, start, rearm=TriggerRearm.AUTO):
        if not isinstance(start, TriggerStart):
            raise TypeError("start must be an instance of TriggerStart Enum")
        if not isinstance(rearm, TriggerRearm):
            raise TypeError("rearm must be an instance of TriggerRearm Enum")
        return self.driver.setTrigger(start.value, rearm.value)

    def get_trigger_start(self):
        return TriggerStart(self.driver.getTriggerStart())

    def get_trigger_rearm(self):
        return TriggerRearm(self.driver.getTriggerRearm())

    def set_hostname(self, hostname):
        return self.driver.setHostname(hostname)

    def get_hostname(self):
        return self.driver.getHostname()

    def set_network_configuration(self, dhcp, ip='', netmask='', gateway='', testmode=True):
        return self.driver.setNetworkConfiguration(dhcp, ip, netmask, gateway, testmode)

    def get_network_configuration(self, permanent=False):
        return self.driver.getNetworkConfiguration(permanent)

    def apply_network_configuration(self):
        return self.driver.applyNetworkConfiguration()

    def rearm(self):
        return self.driver.rearm()

    def chans_to_mask(self, channels: list[int]) -> int:
        """Helper: convert a list of channel numbers to a bitmask."""
        return sum(1 << ch for ch in channels)

    def check_version(self) -> bool:
        """Determine if device supports version >= 1.1 behavior."""
        try:
            self.driver.getFPGAID()
            return True
        except Exception:
            return False
        
    def get_debug_register(self):
        return self.driver.getDebugRegister()
    
    def stream(self, sequence: Sequence, number_runs: int = -1):
        self.driver.stream(seq=sequence, n_runs=number_runs)
    
    def force_final(self):
        self.driver.forceFinal()

    ##################### ANALOG OUTPUT ###########################
    # The Pulse Streamer 8/2 has no built-in function generators - analog waveforms are built as
    # (duration_ns, voltage_V) step lists and set on a Sequence with setAnalog(). See the
    # Pulse_Streamer instrument wrapper for generators that produce those lists. The methods below
    # only expose the vendor analog calls that were missing from this driver.

    def create_output_state(self, digital_channels: list = None, A0: float = 0.0, A1: float = 0.0):
        """Build an OutputState describing a static output of the Pulse Streamer 8/2.

        Passthrough to PulseStreamer.createOutputState, which is itself just
        OutputState(digi=..., A0=..., A1=...). Exposed here so callers can build one without
        importing the vendor package.

        Args:
            digital_channels: Digital channels to drive HIGH. Must be a list of ints - OutputState
                raises TypeError on anything else. None means no channels high.
            A0: Analog channel 0 level in volts, within +/-1 V.
            A1: Analog channel 1 level in volts, within +/-1 V.

        Returns:
            OutputState: Suitable for set_analog_constant().

        Raises:
            AssertionError: From OutputState if a voltage is outside +/-1 V or a digital channel is
                outside 0..7.
        """
        if digital_channels is None:
            digital_channels = []
        return self.driver.createOutputState(digital_channels, A0, A1)

    def set_analog_constant(self, output_state=None):
        """Drive a static output state immediately, replacing any streamed sequence.

        Passthrough to PulseStreamer.constant.

        NOTE this is not "hold a DC level alongside the sequence": constant() clears the client's
        sequence bookkeeping, so whatever was streaming stops and the uploaded sequence is
        discarded. To put a DC level *inside* a sequence, use the Pulse_Streamer instrument's
        set_analog_dc() instead.

        Args:
            output_state: OutputState to hold, as returned by create_output_state(). None means all
                outputs at zero.
        """
        if output_state is None:
            output_state = OutputState([])
        return self.driver.constant(output_state)

    def set_analog_calibration(self, dc_offset_a0: float = 0.0, dc_offset_a1: float = 0.0,
                               slope_a0: float = 1.0, slope_a1: float = 1.0):
        """Write the analog output calibration to the device.

        Passthrough to PulseStreamer.setAnalogCalibration, the inverse of the existing
        get_analog_calibration(). The vendor call does no validation and the values persist on the
        device, so read the current values with get_analog_calibration() before changing them.

        Args:
            dc_offset_a0: DC offset correction for A0, in volts.
            dc_offset_a1: DC offset correction for A1, in volts.
            slope_a0: Gain correction for A0. 1.0 is uncorrected.
            slope_a1: Gain correction for A1. 1.0 is uncorrected.
        """
        return self.driver.setAnalogCalibration(dc_offset_a0, dc_offset_a1, slope_a0, slope_a1)