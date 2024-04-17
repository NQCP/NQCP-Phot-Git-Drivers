from Instruments.Spectrographs.Andor import Andor

andor = Andor()
andor.connect()
print(andor.get_id())
andor.disconnect()



