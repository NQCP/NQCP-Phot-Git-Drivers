import matplotlib.pyplot as plt

from Instruments.Lasers.Toptica_CTL950.Toptica_CTL950 import Toptica_CTL950

toptica_laser = Toptica_CTL950(IP_address='192.168.1.100')
toptica_laser.connect()
toptica_laser.set_wavelength(950)
plt.pause(2)
toptica_laser.disconnect()