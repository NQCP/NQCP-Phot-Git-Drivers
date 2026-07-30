"""
Python wrapper for the Time Tagger X fast feedback coincidence logic.
"""

from Swabian.TimeTagger import Countrate, TimeTagger
import numpy as np

class FastFeedbackCoincidences():
    """
    Class to control the fast feedback coincidence logic module of the Time Tagger X.

    The output is generated when a user-defined coincidence condition on the input channels is met. The length of the coincidence window as well as the output pulse length can be configured. The coincidence window ends with the event on the trigger channel. In total, two coincidence patterns, one for each output channel, can be configured. They run simultaneously but on the same trigger channel and same coincidence window size. For each output channel the user has to define a list of input channels which are considered by the module and another list of input channels which defines the coincidence pattern. A boolean is set to discriminate between exclusive or inclusive coincidences within the considered (active) channels. An exclusive coincidence only triggers an output pulse if there are only events on the coincidence channels but no events on all other active channels.
     
    The output can be used to trigger other devices, e.g. an Pulse Streamer, with a trigger to output latency below 90 ns."""

    def __init__(self, tagger: TimeTagger, triggerChannel: int, outputChannel1: int, activeChannels1: list, coincidenceGroup1: list, exclusiveCoincidence1: bool = False, outputChannel2: int = None, activeChannels2: list = None, coincidenceGroup2: list = None, exclusiveCoincidence2: bool = False, coincidenceWindow: int = 1000, outputPulseLength1: int = 10000, outputPulseLength2: int = 10000):
        """
        Parameters
        ----------
        tagger: TimeTagger object
            The Time Tagger object to control the fast feedback logic.
        triggerChannel: int
            The input channel that serves as the trigger for the coincidence logic. The coincidence window ends with the event on this channel.
        outputChannel1: int
            The output channel that should be used for the coincidence group 1 (1 or 2).
        activeChannels1: list of int
            List of input channels which are considered for the coincidence group 1.
        coincidenceGroup1: list of int
            The input channels that are included in the first coincidence condition. The output pulse is generated when an event on the trigger channel coincides with an event on any of the channels in this group within the coincidence window.
        exclusiveCoincidence1: bool, optional
            If True, an exclusive coincidence event is considered. The output pulse is only generated if there are no events on any of the active channels outside the coincidence group 1 within the coincidence window. Default is False (inclusive coincidence).
        outputChannel2: int
            The output channel that should be used for the coincidence group 2 (1 or 2).
        activeChannels2: list of int
            List of input channels which are considered for the coincidence group 2.
        coincidenceGroup2: list of int
            The input channels that are included in the second coincidence condition. The output pulse is generated when an event on the trigger channel coincides with an event on any of the channels in this group within the coincidence window.
        exclusiveCoincidence2: bool, optional
            If True, an exclusive coincidence event is considered. The output pulse is only generated if there are no events on any of the active channels outside the coincidence group 2 within the coincidence window. Default is False (inclusive coincidence).
        coincidenceWindow: int, optional
            The size of the coincidence window in units of ps in the range from 1 ps to 715 µs with 1 ps resolution. Default is 1000 ps. 
        outputPulseLength1: int, optional
            The length of the output pulse for the first output channel in units of ps in the range from 667 ps to 21.8 µs with 667 ps resolution. Default is 10000 ps.
        outputPulseLength2: int, optional
            The length of the output pulse for the second output channel in units of ps in the range from 667 ps to 21.8 µs with 667 ps resolution. Default is 10000 ps.
        """
        # Set class parameters. Channel numbers are in official TT format (-20 to 20).
        self.tagger = tagger
        self.availableChannels = self.tagger.getChannelList()
        self.triggerChannel = triggerChannel
        self.outputChannel1 = outputChannel1
        self.outputChannel2 = outputChannel2
        self.activeChannels1 = activeChannels1
        self.activeChannels2 = activeChannels2
        self.coincidenceGroup1 = coincidenceGroup1
        self.coincidenceGroup2 = coincidenceGroup2
        self.exclusiveCoincidence1 = exclusiveCoincidence1
        self.exclusiveCoincidence2 = exclusiveCoincidence2
        self.coincidenceWindow = coincidenceWindow
        self.outputPulseLength1 = outputPulseLength1
        self.outputPulseLength2 = outputPulseLength2
        
        # Perform checks
        self.checkLicense()
        self.checkInputChannels()

        # Set FPGA parameters
        self._writeParams(0x0, 1) # Set muxer to coincidence logic
        self._writeParams(0x1, 1) # Set muxer to coincidence logic
        self.setTriggerChannel(triggerChannel)
        self.setCoincidenceWindow(coincidenceWindow)
        self.setOutputPulseLength(outputChannel1, outputPulseLength1)
        self.setOutputPulseLength(outputChannel2, outputPulseLength2)
        self.setCoincidenceGroup(outputChannel1, activeChannels1, coincidenceGroup1, exclusiveCoincidence1)
        if coincidenceGroup2:
            self.setCoincidenceGroup(outputChannel2, activeChannels2, coincidenceGroup2, exclusiveCoincidence2)

    def _writeParams(self, addr: int, data: int):
        self.tagger.factoryAccess(0xAF4321FE, 0xF0070000 + 0x2000 + 4*(addr), data , 2**32-1, use_wb=True)

    def _convertChannelNumber(self, channel: int):
        if channel in self.availableChannels:
            if 1 <= channel <= 20:
                return channel - 1
            elif -20 <= channel <= -1:
                return abs(channel) + 19
        else:
            raise ValueError(f"Invalid channel number: {channel}. Please select a channel from the available channels: {self.availableChannels}")
        
    def checkLicense(self):
        """
        Check if the Time Tagger has a Fast Feedback license.
        """
        if not self.tagger.getDeviceLicense()[0]['fast feedback']:
            raise ValueError("Please ask for a Fast Feedback license.")

    def checkInputChannels(self):
        """
        Check if there are input signals on the trigger as well as active channels. The method also enables the LEDs of the respective channels.
        """
        channels = [self.triggerChannel] + self.activeChannels1
        if self.activeChannels2 is not None:
            channels += self.activeChannels2
        channels = list(set(channels))  # remove duplicates
        self.countrate = Countrate(self.tagger, channels)
        self.countrate.start()
        rates = self.countrate.getData()
        if not any(rates):
            raise ValueError("No input signals on trigger and active channels.")

    def setTriggerChannel(self, channel: int):
        """
        Parameters
        ----------
        channel: int
            Trigger channel for coincidence group.
        """
        ch = self._convertChannelNumber(channel)
        self._writeParams(0x10, ch)
        self.checkInputChannels()  # update LEDs
        self.triggerChannel = channel

    def setCoincidenceWindow(self, window: int):
        """
        Parameters
        ----------
        window: int
            Length of the coincidence window in ps (from 1 ps to 715 µs with 1 ps resolution).
        """
        self.coincidenceWindow = window
        win = int(np.round(window * 3))  # window size in units of 0.33 ps
        if win == 0:
            raise ValueError("Coincidence window size too small. Please select a value between 1 ps and 715 us.")
        elif win > 715*3e6:
            raise ValueError("Coincidence window size too large. Please select a value between 1 ps and 715 us.")
        else:
            self._writeParams(0x11, win)
        
    def setOutputPulseLength(self, channel: int, pulseLength: int):
        """
        Parameters
        ----------
        channel: int
            Aux output channel number to assign the pulse length to (1 or 2).
        pulselength: int
            Output pulse length in ps (from 667 ps to 21.8 µs with 667 ps resolution).
        """
        if channel == self.outputChannel1:
            self.outputPulseLength1 = pulseLength
        elif channel == self.outputChannel2:
            self.outputPulseLength2 = pulseLength
        elif channel is None:
            pass
        else:
            raise ValueError("Output channel must be 1 or 2")
        length = int(pulseLength * 0.0015) # pulse length in units of 667 ps
        if length == 0:
            raise ValueError("Output pulse length too short. Please select a value between 667 ps and 21.8 us.")
        elif length > 21.8e6*0.0015:
            raise ValueError("Output pulse length too large. Please select a value between 667 ps and 21.8 us.")
        if channel == 1:
            self._writeParams(0x12, length)
        elif channel == 2:
            self._writeParams(0x13, length)
        elif channel is None:
            pass
        else:
            raise ValueError("Output must be 1 or 2")

    def setCoincidenceGroup(self, outputChannel: int, activeChannels: list, group: list, exclusive: bool = False):
        """
        Parameters
        ----------
        outputChannel: int
            Aux output channel to assign the coincidence pattern to (1 or 2).
        activeChanels: list of int
            List of input channels which are considered for the coincidence logic.
        group: list of int
            List of input channels which form the coincidence group.
        exclusive: bool
            Whether to consider inclusive or exclusive coincidences. Default is False (inclusive coincidences).
        """
        if outputChannel == self.outputChannel1:
            self.activeChannels1 = activeChannels
            self.coincidenceGroup1 = group
            self.exclusiveCoincidence1 = exclusive
        elif outputChannel == self.outputChannel2:
            self.activeChannels2 = activeChannels
            self.coincidenceGroup2 = group
            self.exclusiveCoincidence2 = exclusive
        else:
            raise ValueError("Output channel must be 1 or 2")
        
        # Create channel masks
        active_chs_Rising = 0
        active_chs_Falling = 0
        state_Rising = 0
        state_Falling = 0
        channels = list(set(group + [self.triggerChannel]))
        for channel in channels:
            ch = self._convertChannelNumber(channel)
            if 0 <= ch <= 19:
                state_Rising |= (1 << ch)
            elif 20 <= ch <= 39:
                state_Falling |= (1 << (ch-20))
        if exclusive:
            for channel in activeChannels:
                ch = self._convertChannelNumber(channel)
                if 0 <= ch <= 19:
                    active_chs_Rising |= (1 << ch)
                elif 20 <= ch <= 39:
                    active_chs_Falling |= (1 << (ch-20))
        else:
            active_chs_Rising = state_Rising
            active_chs_Falling = state_Falling

        # Assign masks to output channel
        if outputChannel == 1:
            self._writeParams(0x14, active_chs_Rising)
            self._writeParams(0x15, active_chs_Falling)
            self._writeParams(0x18, state_Rising)
            self._writeParams(0x19, state_Falling)
        elif outputChannel == 2:
            self._writeParams(0x16, active_chs_Rising)
            self._writeParams(0x17, active_chs_Falling)
            self._writeParams(0x1a, state_Rising)
            self._writeParams(0x1b, state_Falling)
        else:
            raise ValueError("Output channel must be 1 or 2.")
        self.checkInputChannels()  # Update LEDs
        
    def disableOutputs(self):
        """
        Disable the output channels and reset the fast feedback module.
        """
        # Stop countrate measurement (initialize LEDs)
        self.countrate.stop()

        # Stop coincidence logic by enabling only trigger channel with low state mask
        trigger_mask = 0
        ch = self._convertChannelNumber(self.triggerChannel)
        if 0 <= ch <= 19:
            trigger_mask |= (1 << ch)
        elif 20 <= ch <= 39:
            trigger_mask |= (1 << (ch - 20))
        self._writeParams(0x14, trigger_mask)
        self._writeParams(0x15, trigger_mask)
        self._writeParams(0x16, trigger_mask)
        self._writeParams(0x17, trigger_mask)
        self._writeParams(0x18, 0)
        self._writeParams(0x19, 0)
        self._writeParams(0x1a, 0)
        self._writeParams(0x1b, 0)