

from Code.Instruments.Implementations.Spectrographs.Andor import Andor

andor = Andor()
andor.connect()
print(andor.get_id())
andor.disconnect()



