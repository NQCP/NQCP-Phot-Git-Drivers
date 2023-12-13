import os
import time
import sys
import clr # is in the 'pythonnet' package

# get these files by downloading the kinesis software from
# https://www.thorlabs.com/software_pages/viewsoftwarepage.cfm?code=Motion_Control

# once the files are downloaded, the communication protocol can be found in
# C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DotNet_API.chm

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.PiezoCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.KCube.PiezoCLI import *
from System import Decimal  # necessary for real world units


class PiezoKPZ101:
    def __init__(self, _serialNo):
        print("Initialising instance of thorlabs piezo class")
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
    
    def setOutputVoltage(self, voltage):
        self.device.SetOutputVoltage(voltage)

    def getOutputVoltage(self):
        output_voltage = self.device.GetOutputVoltage()
        return output_voltage
        
    def getSerialNumber(self):
        deviceInfo = self._getDeviceInfo()
        print(deviceInfo.Serialnumber)
        return deviceInfo.Serialnumber

    def _getDeviceInfo(self):
        # this function is private. Call get serialnumber instead
        DeviceInfo = self.GetDeviceInfo()
        print(DeviceInfo)
        return DeviceInfo


    def __del__(self):
        # this is the destructor
        print('destructing')
        self.device.Disconnect()