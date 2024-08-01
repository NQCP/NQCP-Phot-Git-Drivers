import TimeTagger
import time

# https://www.swabianinstruments.com/static/documentation/TimeTagger/tutorials/TimeTaggerRPC.html
# If the "Time Tagger Lab" software is installed, code example can be found here C:\Program Files\Swabian Instruments\Time Tagger\examples

# For manufacturer drivers associated with TimeTaggerLab version <2.17.4,  the TimeTagger module uses an older version of numpy. 
# I got it to work with 1.26 (the highest 1.x version)

class SwabianTimeTagger():
    def __init__(self, serialNumber: str=None, serverIP: str=None, serverPort: str=None) -> None:
        self.serialNumber = serialNumber

        self.serverIP = serverIP
        self.serverPort = serverPort

        self.connectionType = None
        self.connection = None

        self.counter = None

    ###################### HIGH LEVEL FUNCTIONS ######################

    def printAllTriggerLevels(self):
        print("Trigger levels for channels [V]:")
        for channelNo in range(1, 13):
            print(self.getTriggerLevel(channelNo), end=', ')
        print("")

    ###################### LOW LEVEL FUNCTIONS ######################

    def connect(self, _connectionType) -> None:
        self.connectionType = _connectionType

        if self.connectionType == 'USB':

            if self.serialNumber != None:
                print("Connecting via USB to TimeTagger with serial number " + self.serialNumber)
                self.connection = TimeTagger.createTimeTagger(self.serialNumber)

            else:
                print("Connecting via USB to the first TimeTagger available")
                self.connection = TimeTagger.createTimeTagger()
                

        elif self.connectionType == 'Network':
            print("Connecting via network to server with IP " + self.serverIP + " and port " + self.serverPort)
            self.connection = TimeTagger.createTimeTaggerNetwork(self.serverIP + ":" + self.serverPort)

        else:
            print('ERROR in SwabianTimeTagger - connectionType has not been defined. Valid argument values are <USB> or <Network>')

    def disconnect(self) -> None:
        print("Disconnecting TimeTagger")
        TimeTagger.freeTimeTagger(self.connection)#

    def initialiseCounter(self, channelList: list[int], binwidth_ps: int, n_bins: int) -> None:
        self.counter = TimeTagger.Counter(tagger=self.connection, channels=channelList, binwidth=binwidth_ps, n_values=n_bins)

    def getSerial(self) -> str:
        return self.connection.getSerial()
    
    def scanTimeTaggers(self) -> None:
        print("Serial numbers of all available TimeTaggers:")
        print(TimeTagger.scanTimeTagger())

    def setTestSignal(self, channelNo: int, status: bool) -> None:
        self.connection.setTestSignal(channelNo,status)

    def countForTime(self, time_ps: int):
        # iteratorbase = TimeTagger.IteratorBase()
        counter = TimeTagger.Counter(tagger=self.connection, channels=[6], binwidth=int(1e9), n_values=1000)
        counter.startFor(capture_duration=time_ps)
        counter.waitUntilFinished()
        data = counter.getDataTotalCounts()
        return data

    def countHistogram(self, channelList: list[int], binwidth_ps: int, n_bins: int) -> TimeTagger.Counter:        
        time_s = binwidth_ps/1e12*n_bins
        print("Starting counting measurement. Measurement will take " + str(time_s) + " seconds. Wait before reading the data.")

        # returns counts per bin
        counter = self.countHistogram_noWait(channelList,binwidth_ps,n_bins)

        time.sleep(time_s)
        return counter

    def countHistogram_noWait(self, channelList, binwidth_ps: int, n_bins: int) -> TimeTagger.Counter:
        # This function returns a complicated class. The "Counter.getData()" contains 0's and is available immediately, but 
        # it does not contain meaningful data until the measurement time has passed.
        # The array acts like a FIFO - the default setting is that the counter keeps overwriting data.

        counter = TimeTagger.Counter(tagger=self.connection, channels=channelList, binwidth=binwidth_ps, n_values=n_bins)
        
        return counter
    
    def reset(self):
        # Reset the Time Tagger to the start-up state
        print("The reset function clims to not exist for the time tagger network. Setup and better function")
        # self.connection.reset()

    def setTriggerLevel(self, channelNo: int, voltage: float) -> None:
        self.connection.setTriggerLevel(channelNo,voltage)

    def getTriggerLevel(self, channelNo: int) -> float:
        return self.connection.getTriggerLevel(channelNo)