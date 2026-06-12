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
        gated_histogram_1 = TimeTagger.Histogram(tagger=self.connection, click_channel=gated_channel_1_number, start_channel=trigger_channel_number, binwidth = bin_width_ps, n_bins=histogram_num_bins)
        gated_histogram_2 = TimeTagger.Histogram(tagger=self.connection, click_channel=gated_channel_2_number, start_channel=trigger_channel_number, binwidth = bin_width_ps, n_bins=histogram_num_bins)
        return gated_g2_correlation, gate_start_channel, gate_stop_channel, gated_channel_1, gated_channel_2, histogram_1, histogram_2, gated_histogram_1, gated_histogram_2
    
    def initialise_check_probe_correlation(self, trigger_channel_number, click_channel_number, global_delay_ps, probe_check_delay_ps, check_laser_width_ps, probe_laser_width_ps,  check_collections_width_ps, probe_collections_width_ps, bin_width_ps, num_bins, histogram_num_bins):
        gate_check_laser_start_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=global_delay_ps)
        gate_check_collection_start_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=global_delay_ps + check_laser_width_ps)
        gate_check_collection_stop_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=global_delay_ps + check_laser_width_ps + check_collections_width_ps)
        gate_check_laser_start_channel_number = gate_check_laser_start_channel.getChannel()
        gate_check_collection_start_channel_number = gate_check_collection_start_channel.getChannel()
        gate_check_collection_stop_channel_number = gate_check_collection_stop_channel.getChannel()

        gate_probe_laser_start_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=global_delay_ps + probe_check_delay_ps)
        gate_probe_collection_start_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=global_delay_ps + probe_check_delay_ps + probe_laser_width_ps)
        gate_probe_collection_stop_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=global_delay_ps + probe_check_delay_ps + probe_laser_width_ps + probe_collections_width_ps)
        gate_probe_laser_start_channel_number = gate_probe_laser_start_channel.getChannel()
        gate_probe_collection_start_channel_number = gate_probe_collection_start_channel.getChannel()
        gate_probe_collection_stop_channel_number = gate_probe_collection_stop_channel.getChannel()
        
        gated_check_channel=TimeTagger.GatedChannel(tagger=self.connection, input_channel=click_channel_number, gate_start_channel=gate_check_laser_start_channel_number, gate_stop_channel=gate_check_collection_stop_channel_number)
        gated_probe_channel=TimeTagger.GatedChannel(tagger=self.connection, input_channel=click_channel_number, gate_start_channel=gate_probe_laser_start_channel_number, gate_stop_channel=gate_probe_collection_stop_channel_number)
        gated_check_collection_channel=TimeTagger.GatedChannel(tagger=self.connection, input_channel=click_channel_number, gate_start_channel=gate_check_collection_start_channel_number, gate_stop_channel=gate_check_collection_stop_channel_number)
        gated_probe_collection_channel=TimeTagger.GatedChannel(tagger=self.connection, input_channel=click_channel_number, gate_start_channel=gate_probe_collection_start_channel_number, gate_stop_channel=gate_probe_collection_stop_channel_number)
        gated_check_channel_number = gated_check_channel.getChannel()
        gated_probe_channel_number = gated_probe_channel.getChannel()
        gated_check_collection_channel_number = gated_check_collection_channel.getChannel()
        gated_probe_collection_channel_number = gated_probe_collection_channel.getChannel()

        gated_check_histogram = TimeTagger.Histogram(tagger=self.connection, click_channel=gated_check_channel, start_channel=gate_check_laser_start_channel, binwidth = bin_width_ps, n_bins=histogram_num_bins)
        gated_probe_histogram = TimeTagger.Histogram(tagger=self.connection, click_channel=gated_probe_channel, start_channel=gate_probe_laser_start_channel, binwidth = bin_width_ps, n_bins=histogram_num_bins)
        gated_check_collection_histogram = TimeTagger.Histogram(tagger=self.connection, click_channel=gated_check_collection_channel, start_channel=gate_check_collection_start_channel, binwidth = bin_width_ps, n_bins=histogram_num_bins)
        gated_probe_collection_histogram = TimeTagger.Histogram(tagger=self.connection, click_channel=gated_probe_collection_channel, start_channel=gate_probe_collection_start_channel, binwidth = bin_width_ps, n_bins=histogram_num_bins)
        gated_check_probe_correlation = TimeTagger.Correlation(tagger=self.connection, channel_1=gated_check_collection_channel_number, channel_2=gated_probe_collection_channel_number, binwidth=bin_width_ps, n_bins=num_bins)

        return gated_check_probe_correlation, gated_check_histogram, gated_probe_histogram, gated_check_collection_histogram, gated_probe_collection_histogram, gate_check_laser_start_channel, gate_check_collection_start_channel, gate_check_collection_stop_channel, gate_probe_laser_start_channel, gate_probe_collection_start_channel, gate_probe_collection_stop_channel, gated_check_channel, gated_probe_channel, gated_check_collection_channel, gated_probe_collection_channel

    def initialize_check_probe(self, trigger_channel_number: int, click_channel_number: int, check_gate_delay_ps: int, check_gate_width_ps: int, probe_gate_delay_ps: int, probe_gate_width_ps: int, bin_width_ps: int, num_bins: int):
        """
        Check-probe measurement with conditional filtering.

        Creates two histograms of time from the laser sync pulse to probe-window detections:
          - probe_histogram: all probe-window detections
          - probe_histogram_conditional: probe-window detections only for shots where a
            check-window detection also occurred (via setConditionalFilter)

        The coincidence window for setConditionalFilter must span at least
        (probe_gate_delay_ps + probe_gate_width_ps - check_gate_delay_ps) to associate
        check and probe detections within the same laser repetition cycle.

        Parameters:
            trigger_channel_number: Laser sync / trigger channel
            click_channel_number: Photon detector channel
            check_gate_delay_ps: Delay from laser sync to check gate opening [ps]
            check_gate_width_ps: Width of check detection gate [ps]
            probe_gate_delay_ps: Delay from laser sync to probe gate opening [ps]
            probe_gate_width_ps: Width of probe detection gate [ps]
            bin_width_ps: Histogram bin width [ps]
            num_bins: Number of histogram bins
        """
        check_gate_start = TimeTagger.DelayedChannel(
            tagger=self.connection,
            input_channel=trigger_channel_number,
            delay=check_gate_delay_ps
        )
        check_gate_stop = TimeTagger.DelayedChannel(
            tagger=self.connection,
            input_channel=trigger_channel_number,
            delay=check_gate_delay_ps + check_gate_width_ps
        )
        probe_gate_start = TimeTagger.DelayedChannel(
            tagger=self.connection,
            input_channel=trigger_channel_number,
            delay=probe_gate_delay_ps
        )
        probe_gate_stop = TimeTagger.DelayedChannel(
            tagger=self.connection,
            input_channel=trigger_channel_number,
            delay=probe_gate_delay_ps + probe_gate_width_ps
        )

        check_detection = TimeTagger.GatedChannel(
            tagger=self.connection,
            input_channel=click_channel_number,
            gate_start_channel=check_gate_start.getChannel(),
            gate_stop_channel=check_gate_stop.getChannel()
        )
        probe_detection = TimeTagger.GatedChannel(
            tagger=self.connection,
            input_channel=click_channel_number,
            gate_start_channel=probe_gate_start.getChannel(),
            gate_stop_channel=probe_gate_stop.getChannel()
        )
        # Separate instance with identical gate so the unconditional histogram is unaffected
        # by the conditional filter applied below.
        probe_detection_conditional = TimeTagger.GatedChannel(
            tagger=self.connection,
            input_channel=click_channel_number,
            gate_start_channel=probe_gate_start.getChannel(),
            gate_stop_channel=probe_gate_stop.getChannel()
        )

        check_ch = check_detection.getChannel()
        probe_ch = probe_detection.getChannel()
        probe_cond_ch = probe_detection_conditional.getChannel()

        # Pass probe_detection_conditional events only when check_detection fired
        self.connection.setConditionalFilter(trigger=[check_ch], filtered=[probe_cond_ch])

        probe_histogram = TimeTagger.Histogram(
            tagger=self.connection,
            start_channel=trigger_channel_number,
            click_channel=probe_ch,
            binwidth=bin_width_ps,
            n_bins=num_bins
        )
        probe_histogram_conditional = TimeTagger.Histogram(
            tagger=self.connection,
            start_channel=trigger_channel_number,
            click_channel=probe_cond_ch,
            binwidth=bin_width_ps,
            n_bins=num_bins
        )

        raw_histogram = TimeTagger.Histogram(
            tagger=self.connection,
            start_channel=trigger_channel_number,
            click_channel=click_channel_number,
            binwidth=bin_width_ps,
            n_bins=3*num_bins
        )

        return (
            probe_histogram,
            probe_histogram_conditional,
            raw_histogram,
            # check_gate_start, check_gate_stop,
            # probe_gate_start, probe_gate_stop,
            # check_detection, probe_detection, probe_detection_conditional
        )

    def initialise_gated_g2_2D_histogram(self, trigger_channel_number, click_1_channel_number, click_2_channel_number, trigger_gate_start_delay_ps, trigger_gate_stop_delay_ps, bin_width_ps, num_bins):
        gate_start_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=trigger_gate_start_delay_ps)
        gate_stop_channel = TimeTagger.DelayedChannel(tagger=self.connection, input_channel=trigger_channel_number, delay=trigger_gate_stop_delay_ps)
        gate_start_channel_number = gate_start_channel.getChannel()
        gate_stop_channel_number = gate_stop_channel.getChannel()
        gated_channel_1=TimeTagger.GatedChannel(tagger=self.connection, input_channel=click_1_channel_number, gate_start_channel=gate_start_channel_number, gate_stop_channel=gate_stop_channel_number)
        gated_channel_2=TimeTagger.GatedChannel(tagger=self.connection, input_channel=click_2_channel_number, gate_start_channel=gate_start_channel_number, gate_stop_channel=gate_stop_channel_number)
        gated_channel_1_number = gated_channel_1.getChannel()
        gated_channel_2_number = gated_channel_2.getChannel()
        gated_g2_2D_histogram = TimeTagger.Histogram2D(tagger=self.connection, start_channel=trigger_channel_number, stop_channel_1=gated_channel_1_number, stop_channel_2=gated_channel_2_number, binwidth_1=bin_width_ps, binwidth_2=bin_width_ps, n_bins_1=num_bins, n_bins_2=num_bins)
        return gated_g2_2D_histogram, gate_start_channel, gate_stop_channel, gated_channel_1, gated_channel_2
    

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
        self.connection.disableLEDs(disabled=True)

    def enable_leds(self) -> None:
        self.connection.disableLEDs(disabled=False)

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
    

