from Andor_Newton import Andor_Newton
from Andor_Kymera import Andor_Kymera
import matplotlib.pyplot as plt
import numpy as np
from instruments.Implementations.Toptica_CTL950 import Toptica_CTL950
from photonicdrivers.Lasers.Toptica.Toptica_DLC_Pro import Toptica_DLC_PRO_driver
import time
import datetime    
import os
from configparser import ConfigParser

class Andor_Spectrograph():

    def __init__(self, spectrograph: Andor_Kymera, camera: Andor_Newton):
        self.spectrograph: Andor_Kymera = spectrograph
        self.camera: Andor_Newton = camera
        self.calibration = None
        
    def load_settings(self) -> dict:
        pass

    def save_settings(self, settings: dict) -> None:
        pass
    
class Image_Plotter():

    def plot_image(image, calibration = None):

        plt.figure()
        plt.imshow(image, cmap='gray', aspect='auto')
        plt.colorbar()  # Add a colorbar to show the mapping of values to colors
        plt.title("2D Image Representation of 1D Array")
        x_axis_range = [0,1600]
        if calibration is None:
            plt.xlim(x_axis_range)
            plt.xlabel("x axis [pixels]")
        else:
            plt.xlim(x_axis_range)
            plt.xlabel("x axis [nm]")
        plt.ylabel("y axis [pixels]")
        
        plt.ylim([0,200])

class Spectograph_Calibration:

    def __init__(self, pixel_list, wavelength_list, grating, center_wavelength, degree, center_wavelength_list) -> None:
        self.pixel_list = pixel_list
        self.wavelength_list = wavelength_list
        self.grating = grating
        self.center_wavelength = center_wavelength
        self.fit_function = None
        self.degree = 2
        self.center_wavelength_list = center_wavelength_list

    def get_polynomial_degree(self):
        return self.degree
    
    def get_pixel_list(self):
        return self.pixel_list
    
    def get_wavelength_list(self):
        return self.wavelength_list
    
    def get_grating(self):
        return self.grating
    
    def get_center_wavelength(self):
        return self.center_wavelength
    
    def get_center_wavelength_list(self):
        return self.center_wavelength_list
    
    def set_degree(self, degree):
        self.degree = degree
    
    def fit(self, degree):
        coefficients = np.polyfit(self.pixel_list, self.wavelength_list, degree)
        self.fit_function = lambda x: np.polyval(coefficients, x)

    def plot_fit(self):
        plt.figure()
        plt.scatter(self.pixel_list, self.wavelength_list)
        plt.title("calibration plot")

        #plt.xlim(x_axis_range)
        plt.xlabel("x axis [pixels]")
        plt.ylabel("y axis [pixels]")
        fit_xaxis = np.linspace(np.min(self.pixel_list), np.max(self.pixel_list))
        plt.plot(fit_xaxis, self.fit_function(fit_xaxis))

    def polyfit2d(x, y, z, kx=3, ky=3, order=None):
        # '''
        # https://stackoverflow.com/questions/33964913/equivalent-of-polyfit-for-a-2d-polynomial-in-python
        # Two dimensional polynomial fitting by least squares.
        # Fits the functional form f(x,y) = z.

        # Notes
        # -----
        # Resultant fit can be plotted with:
        # np.polynomial.polynomial.polygrid2d(x, y, soln.reshape((kx+1, ky+1)))

        # Parameters
        # ----------
        # x, y: array-like, 1d
        #     x and y coordinates.
        # z: np.ndarray, 2d
        #     Surface to fit.
        # kx, ky: int, default is 3
        #     Polynomial order in x and y, respectively.
        # order: int or None, default is None
        #     If None, all coefficients up to maxiumum kx, ky, ie. up to and including x^kx*y^ky, are considered.
        #     If int, coefficients up to a maximum of kx+ky <= order are considered.

        # Returns
        # -------
        # Return paramters from np.linalg.lstsq.

        # soln: np.ndarray
        #     Array of polynomial coefficients.
        # residuals: np.ndarray
        # rank: int
        # s: np.ndarray

        # '''

        # grid coords
        x, y = np.meshgrid(x, y)
        # coefficient array, up to x^kx, y^ky
        coeffs = np.ones((kx+1, ky+1))

        # solve array
        a = np.zeros((coeffs.size, x.size))

        # for each coefficient produce array x^i, y^j
        for index, (j, i) in enumerate(np.ndindex(coeffs.shape)):
            # do not include powers greater than order
            if order is not None and i + j > order:
                arr = np.zeros_like(x)
            else:
                arr = coeffs[i, j] * x**i * y**j
            a[index] = arr.ravel()

        # do leastsq fitting and return leastsq result
        return np.linalg.lstsq(a.T, np.ravel(z), rcond=None)

    # def poly2Dreco(X, Y, c):
    # return (c[0] + X*c[1] + Y*c[2] + X**2*c[3] + X**2*Y*c[4] + X**2*Y**2*c[5] + 
    #        Y**2*c[6] + X*Y**2*c[7] + X*Y*c[8])



    
from configparser import RawConfigParser
config = ConfigParser()

class Spectrograph_Calibration_Loader():

    def load_calibration(self, path):
        # Create a ConfigParser object
        config = ConfigParser()

        # Open and read the .cfg file
        config.read(path)

        # Accessing the values
        degree = int(config.get('Manual X-Calibration', 'Type'))
        number_of_points = int(config.get('Manual X-Calibration', 'Number'))
        center_wavelength = float(config.get('Manual X-Calibration', 'Center_Wavelength'))
        grating = int(config.get('Manual X-Calibration', 'Grating'))

        # Initialize empty lists for x and y coordinates
        pixel_list = []
        wavelength_list = []

        # Extract the points and split them into x and y coordinates
        for i in range(1, number_of_points + 1):
            point_str = config.get('Manual X-Calibration', f'Point{i}')
            x, y = map(int, point_str.split(','))
            pixel_list.append(x)
            wavelength_list.append(y)

        # Perform a polynomial fit (degree 1 for linear, 2 for quadratic, etc.)
        coefficients = np.polyfit(pixel_list, wavelength_list, degree)
        
        # Create a lambda function that represents the polynomial
        calibration = lambda x: np.polyval(coefficients, x)
        return Spectograph_Calibration(pixel_list, wavelength_list, grating, center_wavelength, degree)
    
    def save_calibration(self, path, calibration):
        # Ensure the path ends with .cfg
        if not path.endswith('.cfg'):
            path += '.cfg'

        # Ensure the directory exists
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Manually write the configuration data to the file
        with open(path, 'w') as file:
            file.write('[Manual X-Calibration]\n')
            file.write(f'Type={calibration.get_polynomial_degree()}\n')
            file.write(f'Center_Wavelength={calibration.get_center_wavelength()}\n')
            file.write(f'Grating={calibration.get_grating()}\n')
            file.write(f'Number={len(calibration.get_pixel_list())}\n')
            for i, (x, y) in enumerate(zip(calibration.get_pixel_list(), calibration.get_wavelength_list()), start=1):
                file.write(f'Point{i}={x},{y}\n')

        print(f"Calibration data saved to {path}")

class Spectrograph_Calibrator():

    def __init__(self) -> None:
        pass

    def calibrate(self, laser: Toptica_CTL950, spectrograph: Andor_Kymera, camera: Andor_Newton, lower_limit, higher_limit, steps):
        # Connect to Toptica Laser
                    
        wavelength_list = np.arange(lower_limit, higher_limit, steps)
        time.sleep(5)
        laser.set_wavelength(wavelength_list[0])
        pixel_list = []

        grating = spectrograph.get_grating()
        center_wavelength = spectrograph.get_center_wavelength()

        for wavelength in wavelength_list:
            print("actual wavelength: ",wavelength )
            laser.set_wavelength(wavelength)
            time.sleep(5)
            y_counts = camera.get_trace()
            x_axis = range(0,np.size(y_counts))
            argmax_ycount = np.argmax(y_counts)
            pixel_list.append(argmax_ycount)
            max_wavelength = x_axis[argmax_ycount]
            print("the peak: ", max_wavelength)

        return Spectograph_Calibration(pixel_list, wavelength_list,grating, center_wavelength, 2)
    
    def calibrate_2d(self, laser: Toptica_CTL950, spectrograph: Andor_Kymera, camera: Andor_Newton, lower_limit, higher_limit, steps):
        
        laser_wavelength_list = np.arange(lower_limit, higher_limit, steps)
        center_wavelength_list = np.arange(800, 1050, 50)


        time.sleep(5)
        laser.set_wavelength(laser_wavelength_list[0])
        spectrograph.set_center_wavelength(center_wavelength_list[0])
        pixel_list = []

        grating = spectrograph.get_grating()
        time.sleep(5)

        for center_wavelength in center_wavelength_list:
            spectrograph.set_center_wavelength(center_wavelength)
            print("set center wavelength to: ", center_wavelength )
            time.sleep(10)
            for wavelength in laser_wavelength_list:
                print("set laser wavelength: ", wavelength )
                laser.set_wavelength(wavelength)
                time.sleep(5)
                y_counts = camera.get_trace()
                x_axis = range(0,np.size(y_counts))
                argmax_ycount = np.argmax(y_counts)
                pixel_list.append(argmax_ycount)
                max_wavelength = x_axis[argmax_ycount]
                print("the peak: ", max_wavelength)


        return Spectograph_Calibration(pixel_list, laser_wavelength_list,grating, center_wavelength, 2, center_wavelength_list)
        





if __name__ == "__main__":
    laser_driver_ip_adress = '10.209.67.103'
    laser_driver = Toptica_DLC_PRO_driver(ip_address=laser_driver_ip_adress)
    laser = Toptica_CTL950(laser_driver)
    laser.connect()
    laser.enable_diode()
    laser.set_power_stabilization(True)
    laser.set_power(1)
    laser.set_wavelength(910)

    spectrograph: Andor_Kymera = Andor_Kymera()
    camera: Andor_Newton = Andor_Newton()

    spectrograph.connect()
    camera.connect()
    camera.cooler_on()
    camera.set_temperature(-60)
    camera.set_exposure_time_s(0.05)

    spectrograph.set_center_wavelength(750)

    center_wavelength = spectrograph.get_center_wavelength()
    print("center_wavelength: ", center_wavelength)

    #spectrograph.set_grating(1)

    grating = spectrograph.get_grating()
    print("grating used: ", grating)

    andor_spectrograph: Andor_Spectrograph = Andor_Spectrograph(spectrograph=spectrograph,camera=camera)
    calibrator = Spectrograph_Calibrator()

    # calibration = calibrator.calibrate(laser, spectrograph, camera, 910, 961, 10)
    # calibration.fit(2)
    # calibration.plot_fit()
    # loader = Spectrograph_Calibration_Loader()

    # now = datetime.datetime.now()
    # formatted_time = now.strftime("%Y-%m-%d-%H-%M-%S")    # Format the date and time as a string

    # # Define the path using the formatted date and time
    # path = "N:\\SCI-NBI-NQCP\\Phot\\byHardware\\Spectrograph\\Calibration\\" + formatted_time + ".cfg" 

    calibration = calibrator.calibrate_2d(laser, spectrograph, camera, 910, 941, 10)


    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d-%H-%M-%S")    # Format the date and time as a string

    # Define the path using the formatted date and time
    path = "N:\\SCI-NBI-NQCP\\Phot\\byHardware\\Spectrograph\\Calibration\\" + formatted_time + ".cfg" 


    loader = Spectrograph_Calibration_Loader()
    loader.save_calibration(path, calibration)
    # calibration_loaded = loader.load_calibration(path)
    # calibration.fit(2)
    # calibration.plot_fit()

    plt.show()

    laser.disconnect()





    