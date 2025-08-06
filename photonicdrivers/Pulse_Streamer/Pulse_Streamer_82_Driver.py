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
        self.sequence: Sequence = None

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
    
    def start_streaming(self):
        """Start streaming."""
        self.driver.stream(seq=self.sequence)
    
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

    def set_digital_pattern(self, channel: int, pattern: tuple):
        """
        Set digital pulse pattern on a channel.

        pattern: list of tuples (duration_ns, state)
        """
        if self.sequence is None:
            self.create_sequence()   
        self.sequence.setDigital(channel, pattern)

    def set_analog_pattern(self, channel: int, pattern: tuple):
        """
        Set analog pulse pattern on a channel.

        pattern: list of tuples (duration_ns, amplitude)
        """
        if self.sequence is None:
            self.create_sequence()   
        self.sequence.setAnalog(channel, pattern)

    
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