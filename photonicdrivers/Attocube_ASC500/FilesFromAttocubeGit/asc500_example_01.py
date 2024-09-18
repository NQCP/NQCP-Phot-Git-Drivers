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

asc500.base.sendProfile(binPath + 'afm.ngp')

asc500.data.setDataEnable(1)

sampTime = 1e-3
average = 0
chnNo = 0
bufSize = 256
expTime = sampTime # Counter exposure time

asc500.data.configureChannel(chnNo,
                             asc500.base.getConst('CHANCONN_PERMANENT'),
                             asc500.base.getConst('CHANADC_COUNTER'),
                             average,
                             sampTime)

print(asc500.data.getChannelConfig(chnNo))

asc500.data.configureDataBuffering(chnNo, bufSize)

asc500.data.setCounterExposureTime(expTime)
print("Exposure time ", asc500.data.getCounterExposureTime())

#%% Poll data

while True:
    # Wait until buffer is full
    if asc500.data.waitForFullBuffer(chnNo) != 0:
        break

out = \
asc500.data.getDataBuffer(chnNo,
                          0,
                          bufSize)

#%% Close ASC500

asc500.base.stopServer()

#%% Check data

print("Frame number: ", out[0])
print("Index       : ", out[1])
print("Data size   : ", out[2])
print("Meta data   : ", out[4])
counts = np.asarray(out[3][:])
print("Data        :\n", counts)

#%% Plot counts

plt.figure(0)

plt.scatter(np.arange(bufSize) * sampTime * 1e3,
            counts)
plt.xlabel('Time / ms')
plt.ylabel('Counts / 1')
