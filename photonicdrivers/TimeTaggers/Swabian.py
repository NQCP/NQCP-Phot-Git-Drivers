import TimeTagger


# https://www.swabianinstruments.com/static/documentation/TimeTagger/tutorials/TimeTaggerRPC.html
# If the "Time Tagger Lab" software is installed, code example can be found here C:\Program Files\Swabian Instruments\Time Tagger\examples

# For manufacturer drivers associated with TimeTaggerLab version <2.17.4,  the TimeTagger module uses an older version of numpy. 
# I got it to work with 1.26 (the highest 1.x version)

class SwabianTimeTagger():
    def __init__(self, _serialNumber: str=None, _serverIP: str=None, _serverPort: str=None) -> None:
        self.serialNumber = _serialNumber

        self.serverIP = _serverIP
        self.serverPort = _serverPort

        self.connectionType = None
        self.connection = None

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
        TimeTagger.freeTimeTagger(self.connection)

    def getSerial(self) -> str:
        return self.connection.getSerial()
    
    def scanTimeTaggers(self) -> None:
        print("Serial numbers of all available TimeTaggers:")
        print(TimeTagger.scanTimeTagger())

    def setTestSignal(self, channelNo: int, status: bool) -> None:
        self.connection.setTestSignal(channelNo,status)

    def count(self, channelList, binwidth_ps: int, n_bins: int) -> TimeTagger.Counter:
        time_s = binwidth_ps/1e12*n_bins
        print("Starting counting measurement. Measurement will take " + time_s + " seconds.")

        counter = TimeTagger.Counter(tagger=self.connection, channels=channelList, binwidth=binwidth_ps, n_values=n_bins)
        return counter
