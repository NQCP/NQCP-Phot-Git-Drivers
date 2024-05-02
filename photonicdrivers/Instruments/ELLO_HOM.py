# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:39:54 2024

@author: NQCP_
"""

#Check this link for more info https://gitlab.com/ptapping/thorlabs-elliptec/-/blob/main/doc/source/usage.rst?ref_type=heads

#import serial
import numpy as np
from thorlabs_elliptec import ELLx, ELLError, ELLStatus, list_devices


#Open COM port
#ser = serial.Serial('COM5', 9600, timeout=0)
#ser.close()
stage = ELLx(vid=0x0403, pid=0x6015)

# Move device to the home position
stage.home()

# Move device by 45.0 degrees from home 
list_degrees = np.linspace(0,360,61)

for i in list_degrees:
    stage.move_absolute(i)
    
    stage.wait()


