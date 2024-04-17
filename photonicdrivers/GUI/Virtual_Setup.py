import json
import threading

import numpy as np
import pyvisa as visa
from matplotlib import pyplot as plt

from GUI.functions import *
from Instruments.Abstract import Instrument


class Virtual_Setup:
    def __init__(self):
        self.instrument_list = []

    def add_instrument(self, instrument: Instrument):
        self.instrument_list.append(instrument)

    def save_setup(self):
        pass

