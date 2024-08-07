# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:42:41 2024

@author: dtk791
"""

from photonicdrivers.Lasers.Santec_TSL570 import Santec_TSL570  


laser = Santec_TSL570.Santec_TSL570_driver()
laser.connect()

wl_now = laser.get_wavelength()
print(wl_now)