
from photonicdrivers.Spectrographs.Andor_Kymera import Andor_Kymera
from photonicdrivers.Spectrographs.Andor_Newton import Andor_Newton
import matplotlib.pyplot as plt
import numpy as np
from instruments.Implementations.Toptica_CTL950 import Toptica_CTL950
from photonicdrivers.Lasers.Toptica.Toptica_DLC_Pro_Driver import Toptica_DLC_PRO_Driver
import time
import datetime    
import os
from configparser import ConfigParser
from mpl_toolkits.mplot3d import Axes3D
from itertools import product

class Andor_Spectrograph():

    def __init__(self, spectrograph: Andor_Kymera, camera: Andor_Newton):
        self.spectrograph: Andor_Kymera = spectrograph
        self.camera: Andor_Newton = camera
        self.calibration = None
        
    def load_settings(self) -> dict:
        pass

    def save_settings(self, settings: dict) -> None:
        pass


# if __name__ == "__main__":
#     laser_driver_ip_adress = '10.209.67.103'
#     laser_driver = Toptica_DLC_PRO_Driver(ip_address=laser_driver_ip_adress)
#     laser = Toptica_CTL950(laser_driver)
#     laser.connect()
#     laser.enable_diode()
#     laser.set_power_stabilization(True)
#     laser.set_power(1)
#     laser.set_wavelength(910)

#     spectrograph: Andor_Kymera = Andor_Kymera()
#     camera: Andor_Newton = Andor_Newton()

#     spectrograph.connect()
#     camera.connect()
#     camera.cooler_on()
#     camera.set_temperature(-60)
#     camera.set_exposure_time_s(0.05)

#     spectrograph.set_center_wavelength(750)

#     center_wavelength = spectrograph.get_center_wavelength()
#     print("center_wavelength: ", center_wavelength)

#     #spectrograph.set_grating(1)

#     grating = spectrograph.get_grating()
#     print("grating used: ", grating)

#     andor_spectrograph: Andor_Spectrograph = Andor_Spectrograph(spectrograph=spectrograph,camera=camera)
#     calibrator = Spectrograph_Calibrator()

#     # calibration = calibrator.calibrate(laser, spectrograph, camera, 910, 961, 10)
#     # calibration.fit(2)
#     # calibration.plot_fit()
#     # loader = Spectrograph_Calibration_Loader()

#     # now = datetime.datetime.now()
#     # formatted_time = now.strftime("%Y-%m-%d-%H-%M-%S")    # Format the date and time as a string

#     # # Define the path using the formatted date and time
#     # path = "N:\\SCI-NBI-NQCP\\Phot\\byHardware\\Spectrograph\\Calibration\\" + formatted_time + ".cfg" 

#     pixel_list, laser_wavelength_list, center_wavelength_list = calibrator.calibrate_2d(laser, spectrograph, camera, 910, 941, 10)
#     x, y, z, x_grid, y_grid, z_fitted, z_fitted, z_upper, z_lower = poly2d_fit(pixel_list, center_wavelength_list, pixel_list, degree=3)
#     plot_results(x, y, z, x_grid, y_grid, z_fitted, z_fitted, z_upper, z_lower)


#         # Example usage
#     if __name__ == "__main__":
    # Define example matrices for x, y, and z
    # x_range = np.linspace(0, 10, 12)
    # y_range = np.linspace(0, 10, 12)
    # x, y = np.meshgrid(x_range, y_range)
    
    # Define a true polynomial surface for demonstration
    # z = 0.001 * (x ** 3) - 0.01 * (x ** 2) + 0.005 * x * y + 0.0002 * (y ** 3) - 0.02 * (y ** 2) + 0.1 * x - 0.05 * y + 700
    
    # Call the main function with example data
    # main(x, y, z)
#____________________________________________________________________________________







    # now = datetime.datetime.now()
    # formatted_time = now.strftime("%Y-%m-%d-%H-%M-%S")    # Format the date and time as a string

    # Define the path using the formatted date and time
    # path = "N:\\SCI-NBI-NQCP\\Phot\\byHardware\\Spectrograph\\Calibration\\" + formatted_time + ".cfg" 


    # loader = Spectrograph_Calibration_Loader()
    # loader.save_calibration(path, calibration)
    # calibration_loaded = loader.load_calibration(path)
    # calibration.fit(2)
    # calibration.plot_fit()

    # plt.show()

    # laser.disconnect()