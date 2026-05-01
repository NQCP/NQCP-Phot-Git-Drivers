
from Andor import Andor

andor = Andor()
andor.connect()
print(andor.is_connected())
andor.disconnect()