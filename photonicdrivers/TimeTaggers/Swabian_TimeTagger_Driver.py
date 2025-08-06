import TimeTagger
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

        self.counter = None
        self.histogram = None

    ###################### HIGH LEVEL FUNCTIONS ######################

    def printAllTriggerLevels(self):
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

    def initialiseCounter(self, channelList: list[int], binwidth_ps: int, n_bins: int) -> None:
        # To do any measurements, the TimeTagger must first have initalised a counter
        self.counter = TimeTagger.Counter(tagger=self.connection, channels=channelList, binwidth=binwidth_ps, n_values=n_bins)

    def initialiseHistogram(self, channel1: int, channel2: int, binwidth_ps: int, n_bins: int) -> None:
        # To do any measurements, the TimeTagger must first have initalised a counter
        self.histogram = TimeTagger.Correlation(tagger=self.connection, channel_1=channel1, channel_2=channel2, binwidth=binwidth_ps, n_bins=n_bins)

    def getSerial(self) -> str:
        return self.connection.getSerial()
    
    def scanTimeTaggers(self) -> None:
        print("Serial numbers of all available TimeTaggers:")
        print(TimeTagger.scanTimeTagger())

    def setTestSignal(self, channelNo: int, status: bool) -> None:
        self.connection.setTestSignal(channelNo,status)

    def countForTime(self, time_ps: int) -> int:
        if self.counter is None: 
            print("TimeTagger Counter not inialised") 
            return None
        else:
            self.counter.startFor(capture_duration=time_ps)
            self.counter.waitUntilFinished()
            counts = self.counter.getDataTotalCounts()
            return counts
        
    def getHistogramSnapshot(self, int_time_s: float):
        # return an array with size (number of channel in counter)x(number of bins) with counts per bin
        if self.histogram is None: 
            print("TimeTagger Histogram not inialised") 
            return None
        else:
            self.histogram.startFor(capture_duration=int_time_s * 1e12)
            self.histogram.waitUntilFinished()
            counts = self.histogram.getData()
            times = self.histogram.getIndex()
            return counts, times

        
    
    def reset(self):
        # Reset the Time Tagger to the start-up state
        print("The reset function clims to not exist for the time tagger network. Setup and better function")
        # self.connection.reset()

    def setTriggerLevel(self, channelNo: int, voltage: float) -> None:
        self.connection.setTriggerLevel(channelNo,voltage)

    def getTriggerLevel(self, channelNo: int) -> float:
        return self.connection.getTriggerLevel(channelNo)