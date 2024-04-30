# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:28:44 2024

@author: cvk331
"""


from urllib.request import urlopen
import json
import time

url = "http://10.209.67.135/"
while 1:
    data = json.loads(urlopen(url).read())
    print (data["channel"][0])
    print (data["channel"][1])
    print (data["channel"][2])
    print (data["channel"][3])
    time.sleep(1)



