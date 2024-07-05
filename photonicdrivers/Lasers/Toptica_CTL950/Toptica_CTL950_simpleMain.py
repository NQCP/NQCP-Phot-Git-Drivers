from Toptica_CTL950 import Toptica_CTL950 

laser = Toptica_CTL950()
laser.connect()
laser.play_welcome()
laser.set_wavelength(940)
laser.set_diode(True)
laser.set_power_stabilization(True)
laser.set_power(1)
# laser.set_diode(False)
laser.disconnect()