import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import pythonnet
import clr
clr.AddReference('System')
from System import String, Char, Int32, IntPtr,Text, UInt32

from copy import deepcopy
from win32api import GetFileVersionInfo, LOWORD, HIWORD

import time

class ThorlabsPowerMeter():
    
    defaultPath:str=os.path.join(os.path.join(os.path.dirname(__file__),'Thorlabs_DotNet_dll'),'')
    defaultName:str='Thorlabs.TLPM_64.Interop'
    driverVersion:str=''
    resourceCount:int=0
    resourceName:list[str]=[]
    modelName:list[str]=[]
    serialNumber:list[str]=[]
    manufacturer:list[str]=[]
    
    TLPM=None
    deviceNET=None
    
    def __init__(self):
      
        self.resourceNameConnected=None
        
        self.sensorName=None
        self.sensorSerialNumber=None
        self.sensorCalibrationMessage=None
        self.sensorType=None
        self.sensorSubType=None
        self.sensorFlags:str=''
        
        self.averageTimeMax=None
        self.averageTimeMin=None
        self.averageTimeSet=None
        
        self.timeoutValue=None
        
        self.wavelengthMax=None
        self.wavelengthMin=None
        self.wavelengthSet=None
        
        self.powerRangeMax=None
        self.powerRangeMin=None
        self.powerRangeSet=None
        
        self.brightnessMax=None
        self.brightnessMin=None
        self.brightnessSet=None
        
        self.attenuationMax=None
        self.attenuationMin=None
        self.attenuationSet=None
        
        self.meterPowerReading=None
        self.meterPowerUnit=None
        
        self.meterVoltageReading=None
        self.meterVoltageUnit=None
        
        self.darkOffsetVoltage=None
        self.darkOffsetUnit=None
        
        self.isConnected:bool=False
        
    def connect(self,resourceName,ID_Query=True,Reset_Device=True):
        if not self.isConnected:
            try: 
                selfCopy=deepcopy(self)
                selfCopy.TLPM=self.TLPM
                selfCopy.deviceNET=selfCopy.TLPM(resourceName,ID_Query,Reset_Device)
                
                _index=self.resourceName.index(resourceName)
                
                selfCopy.resourceNameConnected=resourceName
                
                selfCopy.isConnected=True
                selfCopy.resourceName=selfCopy.resourceName[_index]
                selfCopy.modelName=selfCopy.modelName[_index]
                selfCopy.serialNumber=selfCopy.serialNumber[_index]
                selfCopy.manufacturer=selfCopy.manufacturer[_index]

                self.isConnected=False
                return selfCopy
            except:
                pass
                
    def connectForce(self,resourceName,ID_Query=True,Reset_Device=True):
        try: 
            selfCopy=deepcopy(self)
            selfCopy.deviceNET=self.TLPM(resourceName,ID_Query,Reset_Device)
            
            _index=self.resourceName.index(resourceName)
            
            selfCopy.resourceNameConnected=resourceName
            
            selfCopy.isConnected=True
            selfCopy.resourceName=selfCopy.resourceName[_index]
            selfCopy.modelName=selfCopy.modelName[_index]
            selfCopy.serialNumber=selfCopy.serialNumber[_index]
            selfCopy.manufacturer=selfCopy.manufacturer[_index]

            self.isConnected=False
            return selfCopy
        except:
            pass
        
    def disconnect(self):
        if self.isConnected:
            try:
                self.deviceNET.Dispose()
                self.isConnected=False
            except:
                pass
        else:
            pass

    def setAverageTime(self,averageTime):
        _,self.averageTimeMin=self.deviceNET.getAvgTime(1)
        _,self.averageTimeMax=self.deviceNET.getAvgTime(2)
        _,self.averageTimeSet=self.deviceNET.getAvgTime(0)
        if self.averageTimeMin<=averageTime and averageTime<=self.averageTimeMax:
            averageTime=averageTime
        else:
            if self.averageTimeMin>averageTime:
                averageTime=self.averageTimeMin
            if averageTime>self.averageTimeMax:
                averageTime=self.averageTimeMax
                
        self.deviceNET.setAvgTime(averageTime)
        self.averageTimeSet=averageTime

           
    def getAverageTime(self):
        self.averageTimeSet=self.deviceNET.getAvgTime(0)  
            
    def setTimeoutValue(self,timeout):
        self.deviceNET.setTimeoutValue(timeout)
        self.timeoutValue=timeout
    
    def getTimeoutValue(self):
        _,self.timeoutValue=self.deviceNET.getTimeoutValue()


    def setWaveLength(self,wavelength):
        _,self.wavelengthMin=self.deviceNET.getWavelength(1)
        _,self.wavelengthMax=self.deviceNET.getWavelength(2)
        _,self.wavelengthSet=self.deviceNET.getWavelength(0)
        
        if (self.wavelengthMin<=wavelength and wavelength<=self.wavelengthMax):
            wavelength=wavelength
        else:
            if self.wavelengthMin>wavelength:
                wavelength=self.wavelengthMin
            if wavelength>self.wavelengthMax:
                wavelength=self.wavelengthMax
                
        self.deviceNET.setWavelength(wavelength)
        self.wavelengthSet=wavelength
        
    def getWaveLength(self):
        _,self.wavelengthSet=self.deviceNET.getWavelength(0)

    def setPowerAutoRange(self,enable:bool):
        self.deviceNET.setPowerAutoRange(enable)

    def setPowerRange(self,maxRange):
        _,self.powerRangeMin=self.deviceNET.getPowerRange(1)
        _,self.powerRangeMax=self.deviceNET.getPowerRange(2)
        _,self.powerRangeSet=self.deviceNET.getPowerRange(0)
        if (self.powerRangeMin<=maxRange and maxRange<=self.powerRangeMax):
            maxRange=maxRange
        else:
            if self.powerRangeMin>maxRange:
                maxRange=self.powerRangeMin

            if maxRange>self.powerRangeMax:
                maxRange=self.powerRangeMax
                
        self.deviceNET.setPowerRange(maxRange)
        self.powerRangeSet=maxRange
        self.logger.info(f'|{self.__class__.__name__}| Set max range to {maxRange}')
    
    def getPowerRange(self):
        self.powerRangeSet=self.deviceNET.getPowerRange(0)
        self.logger.info(f'|{self.__class__.__name__}| Max range was set to {self.powerRangeSet}')
        
    def setDispBrightness(self,brightness):
        self.brightnessMin=0.0
        self.brightnessMax=1.0
        _,self.brightnessSet=self.deviceNET.getDispBrightness()
        
        if (self.brightnessMin<=brightness and brightness<=self.brightnessMax):
            brightness=brightness
        else:
            if self.brightnessMin>brightness:
                brightness=self.brightnessMin
            if brightness>self.brightnessMax:
                brightness=self.brightnessMax

        self.deviceNET.setDispBrightness(brightness)
        self.brightnessSet=brightness

    def getDispBrightness(self):
        self.brightnessSet=self.deviceNET.getDispBrightness()

    def setAttenuation(self,attenuation):
            if self.modelName in {'PM100D', 'PM100A', 'PM100USB', 'PM200', 'PM400'}:
                _,self.attenuationMin=self.deviceNET.getAttenuation(1)
                _,self.attenuationMax=self.deviceNET.getAttenuation(2)
                _,self.attenuationSet=self.deviceNET.getAttenuation(0)
                
                if (self.attenuationMin<=attenuation and attenuation<=self.attenuationMax):
                    attenuation=attenuation
                else:
                    if self.attenuationMin>attenuation:
                        attenuation=self.attenuationMin
                    if attenuation>self.attenuationMax:
                        attenuation=self.attenuationMax

                self.deviceNET.setAttenuation(attenuation)
                self.attenuationSet=attenuation
            else:
                pass

    def getAttenuation(self,attenuation):
        if self.modelName in {'PM100D', 'PM100A', 'PM100USB', 'PM200', 'PM400'}:
            self.attenuationSet=self.deviceNET.getAttenuation(0)
        else:
            pass

    def getSensorInfo(self):
        _description=[Text.StringBuilder(1024),Text.StringBuilder(1024),Text.StringBuilder(1024)]
        _,_type,_subtype,_flag=self.deviceNET.getSensorInfo(_description[0], _description[1], _description[2])
        self.sensorName=_description[0].ToString()
        self.sensorSerialNumber=_description[1].ToString()
        self.sensorCalibrationMessage=_description[2].ToString()

        match _type:
            case 0x00:
                self.sensorType='No sensor'
                match _subtype:
                    case 0x00:
                        self.sensorSubType='No sensor'
                    case _:
                        pass

            case 0x01:
                self.sensorType='Photodiode sensor'
                match _subtype:
                    case 0x01:
                        self.sensorSubType='Photodiode adapter'
                    case 0x02:
                        self.sensorSubType='Photodiode sensor'
                    case 0x03:
                        self.sensorSubType='Photodiode sensor with integrated filter identified by position'
                    case 0x12:
                        self.sensorSubType='Photodiode sensor with temperature sensor'
                    case _:
                        pass
                        
            case 0x02:
                self.sensorType='Thermopile sensor'
                match _subtype:
                    case 0x01:
                        self.sensorSubType='Thermopile adapter'
                    case 0x02:
                        self.sensorSubType='Thermopile sensor'
                    case 0x12:
                        self.sensorSubType='Thermopile sensor with temperature sensor'
                    case _:
                        pass
                            
            case 0x03:
                self.sensorType='Pyroelectric sensor'
                match _subtype:
                    case 0x01:
                        self.sensorSubType='Pyroelectric adapter'
                    case 0x02:
                        self.sensorSubType='Pyroelectric sensor'
                    case 0x12:
                        self.sensorSubType='Pyroelectric sensor with temperature sensor'
                    case _:
                        pass
            case _:
                    pass
            
        _tag= _flag % 16
        match _tag:
            case 0x0000:
                self.sensorFlags+=''
            case 0x0001:
                self.sensorFlags+='Power sensor; '
            case 0x0002:
                self.sensorFlags+='Energy sensor; '
            case _:
                self.sensorFlags+=''
                
        _flag-=_tag
        _tag= _flag % (16*16)
        match _tag:
            case 0x0000:
                self.sensorFlags+=''
            case 0x0010:
                self.sensorFlags+='Responsivity settable; '
            case 0x0020:
                self.sensorFlags+='Wavelength settable; '
            case 0x0040:
                self.sensorFlags+='Time constant settable; '
            case _:
                self.sensorFlags+=''
                
        _flag-=_tag
        _tag= _flag % (16*16*16)
        match _tag:
            case 0x0000:
                self.sensorFlags+=''
            case 0x0100:
                self.sensorFlags+='With Temperature sensor; '
            case _:
                pass
            
                
    def updatePowerReading(self,period:float=0.5):
        _,self.meterPowerReading=self.deviceNET.measPower()
        time.sleep(period)
        _,_unit=self.deviceNET.getPowerUnit()
        match _unit:
            case 0:
                self.meterPowerUnit='W'
            case 1:
                self.meterPowerUnit='dBm'
            case _:
                pass

    def updateVoltageReading(self,period:float=0.5):
        if self.modelName in {'PM100D', 'PM100A', 'PM100USB', 'PM160T', 'PM200', 'PM400'}:
            try:
                _,self.meterVoltageReading=self.deviceNET.measVoltage() 
                time.sleep(period)
                self.meterVoltageUnit='V'
            except:
                self.logger.warning(f'|{self.__class__.__name__}| Wrong sensor type for this operation')
        else:
            self.logger.warning(f'|{self.__class__.__name__}| This power meter model does not support this function')
        
    def darkAdjust(self):
        if self.modelName in {'PM400'}:
            self.deviceNET.startDarkAdjust()
            _,_state=self.deviceNET.getDarkAdjustState()
            while _state:
                _,_state=self.deviceNET.getDarkAdjustState()
        else:
            pass

    def getDarkOffset(self):
        if self.modelName in {'PM400'}:
            _,self.darkOffsetVoltage=self.deviceNET.getDarkOffset()
            self.darkOffsetUnit='V'
        else:
            pass

    @classmethod
    def listDevices(cls,libraryPath:str=defaultPath):
        if libraryPath.upper() not in [path.upper() for path in sys.path]:
            sys.path.extend(libraryPath)
            
        try:
            clr.AddReference(cls.defaultName)
            from Thorlabs.TLPM_64.Interop import TLPM
            cls.TLPM=TLPM
            cls.driverVersion=cls.getVersionNumber(os.path.join(libraryPath,cls.defaultName + '.dll'))
            
        except:
            pass
            
        _description=[Text.StringBuilder(2048),Text.StringBuilder(2048),Text.StringBuilder(2048),Text.StringBuilder(2048)]
        
        _tempInstance=cls.TLPM(IntPtr(0))
        _,cls.resourceCount=_tempInstance.findRsrc()
        if cls.resourceCount<=0:
            pass
        else:
            for i in range(cls.resourceCount):
                _tempInstance.getRsrcName(UInt32(i),_description[0])
                _,_=_tempInstance.getRsrcInfo(UInt32(i), _description[1], _description[2], _description[3])
                
                cls.resourceName.append(deepcopy(_description[0].ToString()))
                cls.modelName.append(deepcopy(_description[1].ToString()))
                cls.serialNumber.append(deepcopy(_description[2].ToString()))
                cls.manufacturer.append(deepcopy(_description[3].ToString()))
        del _tempInstance,_description
        pass
        return cls()
    
    @staticmethod
    def getVersionNumber(filename):
        info = GetFileVersionInfo (filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return ".".join([str(HIWORD (ms)), str(LOWORD (ms)), str(HIWORD (ls)), str(LOWORD (ls))])

if __name__=='__main__':
    _deviceList = ThorlabsPowerMeter.listDevices()
    deviceA=_deviceList.connect(_deviceList.resourceName[0])
    deviceA.getSensorInfo()
    deviceA.setWaveLength(635);                              
    deviceA.setDispBrightness(0.3);                          
    deviceA.setAttenuation(0);                               
    deviceA.setPowerAutoRange(True);                            
    time.sleep(5)                                                    
    deviceA.setAverageTime(0.001)                           
    deviceA.setTimeoutValue(1000)                               
    #deviceA.darkAdjust() # PM400 ONLY                                   
    #deviceA.getDarkOffset() # PM400 ONLY                                
    for i in range(100):
        deviceA.updatePowerReading(0.1)
        print(f'{deviceA.meterPowerReading} {deviceA.meterPowerUnit}')
        #deviceA.updateVoltageReading(0.1)  # PM400 ONLY  
        #print(f'{deviceA.meterVoltageReading} {deviceA.meterVoltageUnit}')  # PM400 ONLY  
                            
    deviceA.disconnect()