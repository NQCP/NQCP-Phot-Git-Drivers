import time

import clr  # is in the 'pythonnet' package

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


class PiezoKPZ101_Driver:
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

        # Get Device Information and display description
        device_info = self.device.GetDeviceInfo()
        print(device_info.Description)

        # Start polling and enable
        self.device.StartPolling(250)  #250ms polling rate
        time.sleep(0.25)
        # self.device.EnableDevice()
        # time.sleep(0.25)  # Wait for device to enable

        if not self.device.IsSettingsInitialized():
            self.device.WaitForSettingsInitialized(10000)  # 10 second max wait timeout
            assert self.device.IsSettingsInitialized() is True

        # Load the device configuration - output not valid until after this call
        self.device_config = self.device.GetPiezoConfiguration(self.serialNo)

        # This shows how to obtain the device settings
        self.device_settings = self.device.PiezoDeviceSettings

        # Set the Zero point of the device
        # print("Setting Zero Point")
        # self.device.SetZero()


    def enable(self):
        try:
            self.device.EnableDevice()
        except:
            print("enable failed")
            return 1
        return 0
    
    def disable(self):
        self.device.DisableDevice()
    
    def getConfig(self):
        device_config = self.device.GetPiezoConfiguration(self.serialNo)
        # print(device_config)
        return device_config

    def getMaxVoltage(self):
        max_voltage = self.device.GetMaxOutputVoltage()
        return max_voltage
    
    def setZero(self):
        # set the output of the device to 0 V
        self.device.SetZero()
    
    def setOutputVoltage(self, voltageString):
        # print("setting voltage to [V]:")
        # print(voltageString)
        try:
            voltageFloat = float(voltageString) 
            # Now 'float_value' is guaranteed to be a float
            # You can use 'float_value' in the rest of your function
            # print(f"The input as a float: {voltageFloat}")
        except ValueError:
            print("Error: Input is not a valid float.")

        self.device.SetOutputVoltage(Decimal(voltageFloat))

    def getOutputVoltage(self):
        output_voltage = self.device.GetOutputVoltage()
        return output_voltage
        
    def getStatus(self):
        statusBits = hex(self.device.GetStatusBits())
        print(statusBits)
        ENABLED_MASK = hex(0x80000000) # got this from the documentation. search for GetStatusBits
        print(ENABLED_MASK)
        is_enabled = (int(statusBits,16) & int(ENABLED_MASK,16)) != 0
        print(f"logic = {int(statusBits,16) & int(ENABLED_MASK,16)}")
        if is_enabled:
            print("Device is enabled")
        else:
            print("Device is disabled")
        return statusBits
    
    def getSerialNumber(self):
        deviceInfo = self._getDeviceInfo()
        print(deviceInfo.Serialnumber)
        return deviceInfo.Serialnumber

    def _getDeviceInfo(self):
        # this function is private. Call get serialnumber instead
        DeviceInfo = self.GetDeviceInfo()
        print(DeviceInfo)
        return DeviceInfo

    # destructor
    # it is not recommended to use destructors in most cases in python
    # there is a question of wheter __del__ or __exit__ is the better method
    # def __exit__(self):
    #     # this is the destructor. using exit is more reliable than the del function, where timing is not guaranteed
    #     print('destructing')
    #     self.device.StopPolling()
    #     self.device.Disconnect()