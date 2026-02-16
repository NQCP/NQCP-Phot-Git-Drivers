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
        # To do any measurements, the TimeTagger must first have initalised a counter
        return TimeTagger.Counter(tagger=self.connection, channels=channelList, binwidth=bin_width_ps, n_values=num_bins)

    def initialise_correlation(self, channel_1: int, channel_2: int, bin_width_ps: int, num_bins: int) -> None:
        # To do any measurements, the TimeTagger must first have initalised a counter
        return TimeTagger.Correlation(tagger=self.connection, channel_1=channel_1, channel_2=channel_2, binwidth=bin_width_ps, n_bins=num_bins)

    def initialise_histogram(self, start_channel: int, click_channel: int, bin_width_ps: int, num_bins: int) -> None:
        # To do any measurements, the TimeTagger must first have initalised a counter
        return TimeTagger.Histogram(tagger=self.connection, click_channel=click_channel, start_channel=start_channel, binwidth = bin_width_ps, n_bins=num_bins)

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
    
    def get_time_tag_data(self, channel: int, acquisition_time_ps: int = 1e12, n_max_events: int = 10_000_000) -> TimeTagStreamBuffer :
        # return self.connection.
        stream = TimeTagger.TimeTagStream(tagger=self.connection, n_max_events=n_max_events, channel=channel)
        stream.startFor(acquisition_time_ps)
        return stream.getData()