# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:04:04 2020

@author: schaecl
"""

import numpy as np
from matplotlib import pyplot as plt
from lib import ASC500

binPath = "Installer\\ASC500CL-V2.7.13\\"
dllPath = "64bit_lib\\ASC500CL-LIB-WIN64-V2.7.13\\daisybase\\lib\\"

asc500 = ASC500(binPath, dllPath)

asc500.base.startServer()

asc500.base.sendProfile(binPath + '20221019_AFM_Akiyama.ngp')

asc500.data.setDataEnable(1)
asc500.base.setOutputsWaiting(1)

sampTime = 1e-3
average = 0
chnNo = 0
bufSize = 256

asc500.data.configureChannel(chnNo,
                             asc500.base.getConst('CHANCONN_PERMANENT'),
                             asc500.base.getConst('CHANADC_AFMAMPL'),
                             average,
                             sampTime)

print(asc500.data.getChannelConfig(chnNo))

asc500.data.configureDataBuffering(chnNo, bufSize)

#%% Configure scannner

asc500.scanner.configureScanner(xOffset=500e-9,
                                yOffset=500e-9,
                                pxSize=200,
                                columns=100,
                                lines=100,
                                sampTime=sampTime)

#%% Get number of lines and columns

print('Columns {:d}'.format(asc500.scanner.getNumberOfColumns()))
print('Lines {:d}'.format(asc500.scanner.getNumberOfLines()))
print('Pixel size {:.2f} nm'.format(asc500.scanner.getPixelSize() * 1e9))

#%% Get various information about the scan field

print(asc500.scanner.getScannerCoordSystemZero())
print(asc500.scanner.getScannerAbsolutCoordSystem())
print(asc500.scanner.getPositionsXYRel())
sf_centre = asc500.scanner.getScanFieldCentre()
print('The centre of the scan field is {:.2f} x {:.2f} nm'.format(sf_centre[0] * 1e9, sf_centre[1] * 1e9))

#%% Close ASC500

asc500.base.stopServer()
