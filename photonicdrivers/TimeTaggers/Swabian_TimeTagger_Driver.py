import TimeTagger
from TimeTagger import TimeTagStreamBuffer
import time
from photonicdrivers.Abstract.Connectable import Connectable

# https://www.swabianinstruments.com/static/documentation/TimeTagger/tutorials/TimeTaggerRPC.html
# If the "Time Tagger Lab" software is installed, code example can be found here C:\Program Files\Swabian Instruments\Time Tagger\examples

# For manufacturer drivers associated with TimeTaggerLab version <2.17.4,  the TimeTagger module uses an older version of numpy. 
# I got it to work with 1.26 (the highest 1.x version)

class Swabian_TimeTagger_Driver(Connectable):
    def __init__(self, serialNumber: str=None, serverIP: str=None, serverPort: str=None, connection_type: str=None) -> None:
        self.serialNumber = serialNumber

        self.serverIP = serverIP
        self.serverPort = serverPort

        self.connection_type = connection_type
        self.connection = None

    ###################### HIGH LEVEL FUNCTIONS ######################

    def print_all_trigger_levels(self):
        print("Trigger levels for channels [V]:")
        for channelNo in range(1, 13):
            print(self.getTriggerLevel(channelNo), end=', ')
        print("")

    ###################### LOW LEVEL FUNCTIONS ######################

    def connect(self, _connectionType: str=None) -> None:
        """Use provided connection type or fall back to connection type given in constructor"""
        connection_type = _connectionType if _connectionType is not None else self.connection_type

        if connection_type == 'USB':

            if self.serialNumber != None:
                print("Connecting via USB to TimeTagger with serial number " + self.serialNumber)
                self.connection = TimeTagger.createTimeTagger(self.serialNumber)

            else:
                print("Connecting via USB to the first TimeTagger available")
                self.connection = TimeTagger.createTimeTagger()
                

        elif connection_type == 'Network':
            self.connection = TimeTagger.createTimeTaggerNetwork(self.serverIP + ":" + self.serverPort)

        else:
            print('ERROR - connectionType has not been defined. Valid argument values are <USB> or <Network>')

    def disconnect(self) -> None:
        TimeTagger.freeTimeTagger(self.connection)
        self.connection = None

    def is_connected(self):
        try:
            return bool(self.getSerial())
        except:
            return False

    def initialise_counter(self, channelList: list[int], bin_width_ps: int, num_bins: int) -> None:
        return TimeTagger.Counter(tagger=self.connection, channels=channelList, binwidth=bin_width_ps, n_values=num_bins)

    def initialise_delayed_counter(self, channel, bin_width_ps: int, num_bins: int, delay_ps: int) -> None:
        self.delayed_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=channel, delay=delay_ps)
        self.delayed_channel_number = self.delayed_channel.getChannel()
        return TimeTagger.Counter(tagger=self.connection, channels=self.delayed_channel_number, binwidth=bin_width_ps, n_values=num_bins)


    def initialise_correlation(self, channel_1: int, channel_2: int, bin_width_ps: int, num_bins: int) -> None:
        return TimeTagger.Correlation(tagger=self.connection, channel_1=channel_1, channel_2=channel_2, binwidth=bin_width_ps, n_bins=num_bins)

    def initialise_histogram(self, start_channel: int, click_channel: int, bin_width_ps: int, num_bins: int) -> None:
        return TimeTagger.Histogram(tagger=self.connection, click_channel=click_channel, start_channel=start_channel, binwidth = bin_width_ps, n_bins=num_bins)

    def initialise_frequency_stability(self, channel: int, steps: list[int], average: int = 1000, trace_len: int = 1000):
        return TimeTagger.FrequencyStability(tagger=self.connection, channel=channel, steps=steps, average=average, trace_len=trace_len)

    def initialise_frequency_counter(self, channels: list[int], sampling_interval_ps: int, fitting_window_ps: int, n_values: int = 0):
        return TimeTagger.FrequencyCounter(tagger=self.connection, channels=channels, sampling_interval=sampling_interval_ps, fitting_window=fitting_window_ps, n_values=n_values)

    def initialize_2d_histogram(self, stop_channel_1: int, stop_channel_2: int, start_channel: int, bin_width_1_ps: int, bin_width_2_ps: int, num_bins_1: int, num_bins_2: int) -> None:
        return TimeTagger.Histogram2D(tagger=self.connection, start_channel=start_channel, stop_channel_1=stop_channel_1, stop_channel_2=stop_channel_2, binwidth_1=bin_width_1_ps, binwidth_2=bin_width_2_ps, n_bins_1=num_bins_1, n_bins_2=num_bins_2)

    def initialise_delayed_histogram(self, start_channel: int, click_channel: int, bin_width_ps: int, num_bins: int, delay_ps: int) -> None:
        self.delayed_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=start_channel, delay=delay_ps)
        self.delayed_channel_number = self.delayed_channel.getChannel()
        self.delayed_histogram = TimeTagger.Histogram(tagger=self.connection, click_channel=click_channel, start_channel=self.delayed_channel_number, binwidth = bin_width_ps, n_bins=num_bins)
        return self.delayed_histogram

    def initialise_gated_lifetime_histogram(self, trigger_channel_number, click_channel_number, trigger_gate_start_delay_ps, trigger_gate_stop_delay_ps, bin_width_ps, num_bins):
        self.gate_start_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=trigger_gate_start_delay_ps)
        self.gate_stop_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=trigger_gate_stop_delay_ps)
        self.gate_start_channel_number = self.gate_start_channel.getChannel()
        self.gate_stop_channel_number = self.gate_stop_channel.getChannel()
        self.gated_channel=TimeTagger.GatedChannel(tagger=self.connection, input_channel=click_channel_number, gate_start_channel=self.gate_start_channel_number, gate_stop_channel=self.gate_stop_channel_number)
        self.gated_channel_number = self.gated_channel.getChannel()
        print("Gated channel number: ", self.gated_channel_number, " gate start channel number: ", self.gate_start_channel_number, " gate stop channel number: ", self.gate_stop_channel_number)
        self.gated_life_time_histogram = TimeTagger.Histogram(tagger=self.connection, start_channel=trigger_channel_number, click_channel=self.gated_channel_number, binwidth=bin_width_ps, n_bins=num_bins)
        return self.gated_life_time_histogram

    def initialise_gated_g2_correlation(self, trigger_channel_number, click_1_channel_number, click_2_channel_number, trigger_gate_start_delay_ps, trigger_gate_stop_delay_ps, bin_width_ps, num_bins, histogram_num_bins):
        gate_start_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=trigger_gate_start_delay_ps)
        gate_stop_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=trigger_gate_stop_delay_ps)
        gate_start_channel_number = gate_start_channel.getChannel()
        gate_stop_channel_number = gate_stop_channel.getChannel()
        gated_channel_1=TimeTagger.GatedChannel(tagger=self.connection, input_channel=click_1_channel_number, gate_start_channel=gate_start_channel_number, gate_stop_channel=gate_stop_channel_number)
        gated_channel_2=TimeTagger.GatedChannel(tagger=self.connection, input_channel=click_2_channel_number, gate_start_channel=gate_start_channel_number, gate_stop_channel=gate_stop_channel_number)
        gated_channel_1_number = gated_channel_1.getChannel()
        gated_channel_2_number = gated_channel_2.getChannel()
        gated_g2_correlation = TimeTagger.Correlation(tagger=self.connection, channel_1=gated_channel_1_number, channel_2=gated_channel_2_number, binwidth=bin_width_ps, n_bins=num_bins)
        histogram_1 = TimeTagger.Histogram(tagger=self.connection, click_channel=click_1_channel_number, start_channel=trigger_channel_number, binwidth = bin_width_ps, n_bins=histogram_num_bins)
        histogram_2 = TimeTagger.Histogram(tagger=self.connection, click_channel=click_2_channel_number, start_channel=trigger_channel_number, binwidth = bin_width_ps, n_bins=histogram_num_bins)
        return gated_g2_correlation, gate_start_channel, gate_stop_channel, gated_channel_1, gated_channel_2, histogram_1, histogram_2
    

    def getSerial(self) -> str:
        return self.connection.getSerial()
    
    def scanTimeTaggers(self) -> None:
        print("Serial numbers of all available TimeTaggers:")
        print(TimeTagger.scanTimeTagger())

    def setTestSignal(self, channelNo: int, status: bool) -> None:
        self.connection.setTestSignal(channelNo,status)
        
    
    def reset(self):
        # Reset the Time Tagger to the start-up state
        print("The reset function clims to not exist for the time tagger network. Setup and better function")
        # self.connection.reset()

    def set_trigger_level(self, channel: int, voltage: float) -> None:
        self.connection.setTriggerLevel(channel,voltage)

    def get_trigger_level(self, channel: int) -> float:
        return self.connection.getTriggerLevel(channel)
    
    def set_dead_time(self, channel: int, dead_time_ps: int) -> None:
        self.connection.setDeadtime(channel, dead_time_ps) 

    def get_dead_time(self, channel: int) -> int:
        return self.connection.getDeadtime(channel)
    
    def set_input_hysteresis(self, channel: int, hysteresis_mV: int) -> None:
        """
        Allowed hysteresis values: 1, 20, 70
        """
        self.connection.setInputHysteresis(channel, hysteresis_mV)

    def get_input_hysteresis(self, channel: int) -> int:
        return self.connection.getInputHysteresis(channel)
    
    def auto_calibration(self) -> list[float]:
        return self.connection.autoCalibration()
    
    def disable_leds(self) -> None:
        self.connection.disableLEDs()

    def set_input_channel_delay(self, channel: int, delay_ps: int) -> None:
        self.connection.setInputDelay(channel, delay_ps)

    def get_input_channel_delay(self, channel: int) -> int:
        return self.connection.getInputDelay(channel)
    
    def set_event_divider(self, channel: int, divider: int) -> None:
        """
        Set the event divider for a channel. Only every Nth event will be recorded.
        This reduces USB bandwidth but means timestamps represent every Nth signal period.
        
        Parameters:
            channel: Input channel number
            divider: Divider value (1 = no division, 100 = every 100th event)
        """
        self.connection.setEventDivider(channel, divider)

    def get_event_divider(self, channel: int) -> int:
        """
        Get the current event divider setting for a channel.
        
        Returns:
            The divider value (1 = no division)
        """
        return self.connection.getEventDivider(channel)
    
    def get_time_tag_data(self, channels: list[int], acquisition_time_ps: int = 1e12, n_max_events: int = 10_000_000) -> TimeTagStreamBuffer :
        stream = TimeTagger.TimeTagStream(tagger=self.connection, n_max_events=n_max_events, channels=channels)
        stream.startFor(acquisition_time_ps)
        stream.waitUntilFinished()
        return stream.getData()

    def set_conditional_channel(self, trigger_channel: int, filtered_channels_list: list[int]) -> None:
        "Set a conditional filter on the Time Tagger. Only events on the trigger channel that coincide with events on the filtered channels will be recorded."
        self.connection.setConditionalFilter(trigger=trigger_channel, filtered=filtered_channels_list)

    def get_conditional_filter_filtered(self) -> list[int]:
        "Get the current filtered channels for a given trigger channel. Returns an empty list if no conditional filter is set for that trigger channel."
        return self.connection.getConditionalFilterFiltered()
    
    def get_conditional_filter_trigger(self) -> list[int]:
        "Get the current trigger channels that have conditional filters set. Returns an empty list if no conditional filters are set."
        return self.connection.getConditionalFilterTrigger()
    
    def get_delayed_channel_number(self, channel: int, delay_ps: int) -> int:
        self.delayed_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=channel, delay=delay_ps)
        return self.delayed_channel.getChannel()

    def get_gated_channel_number(self, channel: int, gate_start_channel: int, gate_stop_channel: int) -> int:
        self.gated_channel = TimeTagger.GatedChannel(tagger=self.connection, input_channel=channel, gate_start_channel=gate_start_channel, gate_stop_channel=gate_stop_channel)
        return self.gated_channel.getChannel()
    
    def get_channel_list(self):
        return self.connection.getChannelList()
    
    def get_channel_number_scheme(self):
        return self.connection.getChannelNumberScheme()
    

