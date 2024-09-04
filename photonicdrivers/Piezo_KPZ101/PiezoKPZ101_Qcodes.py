from qcodes import validators as vals
from qcodes.instrument import (
    Instrument,
)
#from qcodes.logger import start_all_logging

############################################################################

import sys
import clr

# get these files by downloading the kinesis software from
# https://www.thorlabs.com/software_pages/viewsoftwarepage.cfm?code=Motion_Control

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.PiezoCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.PiezoCLI import *


class PiezoKPZ101_QCodes(Instrument):
    def __init__(self, _serialNo, **kwargs):
        print("Initialising instance of thorlabs piezo class")
        super().__init__(**kwargs)


        DeviceManagerCLI.BuildDeviceList()
        self.serialNo = _serialNo
        # print(self.serialNo)
        print(DeviceManagerCLI.BuildDeviceList())
        serialNumbers = DeviceManagerCLI.GetDeviceList(KCubePiezo.DevicePrefix)
        print(serialNumbers)
        self.device = KCubePiezo.CreateKCubePiezo(self.serialNo)
        self.device.Connect(self.serialNo)

    def enable(self):
        try:
            self.device.EnableDevice()
        except:
            print("enable failed")
            return 1
        return 0
    
    def getConfig(self):
        device_config = self.device.GetPiezoConfiguration(self.serialNo)
        # print(device_config)
        return device_config

    def getMaxVoltage(self):
        max_voltage = self.device.GetMaxOutputVoltage()
        return max_voltage
        

    def __del__(self):
        # this is the destructor
        print('destructing')
        self.device.Disconnect()