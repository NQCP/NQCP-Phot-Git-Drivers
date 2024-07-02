# The reader outputs a voltage signal between 0 and 10 V, which corresponds to the pressure range.
# The pressure range is set by shorting pins in the sensor.
# The arduino is connected to a PCB with a 1/2 voltage divider, so it reads a signal between 0 and 5 A
# The voltage is converted to a 10 bit (0 to 1023) signal


import json
from urllib.request import urlopen
import numpy as np 

class arduinoPressureReader:
    def __init__(self, _ip_address_string, _port_string, _pressureRanges_npArray):
        # _pressureRanges_npArray has to be length 4 to match the number of sensors
        print("Initialising arduinoPressureReader class with IP:")


        self.url = "http://" + _ip_address_string +":" + _port_string + "/"
        print(self.url)

        self.pressureRanges = _pressureRanges_npArray # from 0 to 2.5, 6, 10, or 16 bar
        self.voltageDivider = 2
        self.outputVoltage = 10 # V. The sensor outputs 10 V

    def getPressures(self):
        rawDataArray = self.__getRawData()
        a = np.multiply(rawDataArray,5.0/1023) # convert 10 bit signal to raw voltage between 0 and 5 V
        # print(a)
        b = np.multiply(a,self.voltageDivider/self.outputVoltage) # compensate for voltage divider and convert to relative range (0 to 10 V)
        # print(b)
        convertedData = np.round(np.multiply(b, self.pressureRanges),2) # convert to pressure ranges
        return convertedData

        

##################### PRIVATE METHODS ###########################
    def __getRawData(self):
        data_dict = json.loads(urlopen(self.url).read())
        # print(data_dict["channel"])
        # print(type(data_dict["channel"]))

        dataArray = np.array(data_dict["channel"])
        # print(dataArray)

        return dataArray