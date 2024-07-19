from photonicdrivers.Lasers.Toptica.Toptica_DLC_Pro import Toptica_CTL950_driver 

laser = Toptica_CTL950_driver()
laser.connect()
laser.play_welcome()
laser.set_wavelength(940)
laser.set_diode(True)
laser.set_power_stabilization(True)
laser.set_power(1)
# laser.set_diode(False)
laser.disconnect()