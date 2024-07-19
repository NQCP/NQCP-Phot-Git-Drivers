# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:42:41 2024

@author: dtk791
"""


import pyvisa


rm = pyvisa.ResourceManager()

try:
    santec = rm.open_resource('TCPIP0::10.209.67.181::5000::SOCKET', write_termination = '\n', read_termination='\r')
    print(santec.query('*IDN?'))
except:
    print('Cannot connect to Santec TSL-570.')

#%%
# import time
# import numpy as np