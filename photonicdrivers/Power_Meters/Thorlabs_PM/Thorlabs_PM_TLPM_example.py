import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

from Thorlabs_PM_TLPM import ThorlabsPowerMeter
import time

if __name__=='__main__':
    _deviceList = ThorlabsPowerMeter.listDevices()
    logger=_deviceList.logger
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
        logger.info(f'|{__name__}| {deviceA.meterPowerReading} {deviceA.meterPowerUnit}')
        #deviceA.updateVoltageReading(0.1)  # PM400 ONLY  
        #logger.info(f'|{__name__}| {deviceA.meterVoltageReading} {deviceA.meterVoltageUnit}')  # PM400 ONLY  
    logger.info(f'|{__name__}| Done')                       
    deviceA.disconnect()