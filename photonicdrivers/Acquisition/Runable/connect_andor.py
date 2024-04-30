from photonicdrivers.Instruments.Implementations.Spectrographs import Andor

andor = Andor()
andor.connect()
print(andor.get_id())
andor.disconnect()



