from Code.Instruments.Abstract.Abstract import Instrument


class Virtual_Setup:
    def __init__(self):
        self.instrument_list = []

    def add_instrument(self, instrument: Instrument):
        self.instrument_list.append(instrument)

    def save_setup(self):
        pass

