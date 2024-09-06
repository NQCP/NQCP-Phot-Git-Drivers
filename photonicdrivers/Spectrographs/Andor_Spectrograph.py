from Andor_Newton import Andor_Newton
from Andor_Kymera import Andor_Kymera
import matplotlib.pyplot as plt
import numpy as np
from instruments.Implementations.Toptica_CTL950 import Toptica_CTL950
from photonicdrivers.Lasers.Toptica.Toptica_DLC_Pro_Driver import Toptica_DLC_PRO_driver
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

    def __init__(self, pixel_list, wavelength_list, grating, center_wavelength, degree, center_wavelength_list, fit_coeff) -> None:
        self.pixel_list = pixel_list
        self.wavelength_list = wavelength_list
        self.grating = grating
        self.center_wavelength = center_wavelength
        self.fit_function = None
        self.degree = 2
        self.center_wavelength_list = center_wavelength_list
        self.fit_coeff = fit_coeff

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

    def get_fit_coeff(self):
        return self.fit_coeff
    
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



#-#-#-#-#-#-#-# 2 D FIT #-#-#-#-#-#-#-#
def create_design_matrix(x, y, degree):
    """Creates a design matrix for polynomial fitting up to a given degree."""
    columns = []
    for i, j in product(range(degree + 1), repeat=2):
        if i + j <= degree:
            columns.append((x ** i) * (y ** j))
    return np.vstack(columns).T

# Function to fit a polynomial and calculate coefficients
def fit_polynomial(x, y, z, degree):
    """Fits a polynomial to the data and returns the coefficients and covariance matrix."""
    x_flat = x.flatten()
    y_flat = y.flatten()
    z_flat = z.flatten()

    A = create_design_matrix(x_flat, y_flat, degree)
    coefficients, residuals, rank, singular_values = np.linalg.lstsq(A, z_flat, rcond=None)

    # Calculate residual variance and covariance matrix
    residuals = z_flat - (A @ coefficients)
    residual_variance = np.sum(residuals ** 2) / (len(z_flat) - len(coefficients))
    covariance_matrix = residual_variance * np.linalg.inv(A.T @ A)

    return coefficients, covariance_matrix

# Function to calculate the prediction variance
def calculate_prediction_variance(x, y, covariance_matrix, degree):
    """Calculates the prediction variance for given x, y based on the covariance matrix."""
    x_flat = x.flatten()
    y_flat = y.flatten()
    A_pred = create_design_matrix(x_flat, y_flat, degree)
    variance = np.sum(A_pred @ covariance_matrix * A_pred, axis=1)
    return variance

# Function to plot the results
def plot_results(x, y, z, x_grid, y_grid, z_fitted, z_true, z_upper, z_lower):
    """Plots the noisy data, true surface, fitted surface, and confidence intervals."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the data points
    ax.scatter(x.flatten(), y.flatten(), z.flatten(), color='r', label='Data')

    # Plot the true surface
    ax.plot_surface(x_grid, y_grid, z_true, color='g', alpha=0.5, label='True Polynomial Surface')

    # Plot the fitted surface
    ax.plot_surface(x_grid, y_grid, z_fitted, color='b', alpha=0.5, label='Fitted Polynomial Surface')

    # Plot the upper and lower confidence bounds
    ax.plot_surface(x_grid, y_grid, z_upper, color='b', alpha=0.2, linestyle='--', label='Upper Confidence Bound')
    ax.plot_surface(x_grid, y_grid, z_lower, color='b', alpha=0.2, linestyle='--', label='Lower Confidence Bound')

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show legend
    ax.legend()

    # Show the plot
    plt.show()

# Main function to fit polynomial and plot results
def poly2d_fit(x, y, z, degree=3):
    """Main function to fit a polynomial to the given data and plot results."""

    # Fit polynomial to the data
    coefficients, covariance_matrix = fit_polynomial(x, y, z, degree)

    # Create grid for plotting
    x_range = np.linspace(np.min(x), np.max(x), 50)
    y_range = np.linspace(np.min(y), np.max(y), 50)
    x_grid, y_grid = np.meshgrid(x_range, y_range)

    # Flatten the grid for evaluation
    x_grid_flat = x_grid.flatten()
    y_grid_flat = y_grid.flatten()

    # Create the design matrix for the grid
    A_grid = create_design_matrix(x_grid_flat, y_grid_flat, degree)

    # Calculate the fitted z values
    z_grid_flat = A_grid @ coefficients
    z_fitted = z_grid_flat.reshape(x_grid.shape)

    # Calculate the confidence interval for each point on the grid
    variances = calculate_prediction_variance(x_grid, y_grid, covariance_matrix, degree)
    confidence_interval = 1.96 * np.sqrt(variances)  # 95% confidence interval

    # Reshape confidence intervals to match grid shape
    confidence_interval_grid = confidence_interval.reshape(x_grid.shape)

    # Calculate upper and lower confidence bounds
    z_upper = z_fitted + confidence_interval_grid
    z_lower = z_fitted - confidence_interval_grid


    return(x, y, z, x_grid, y_grid, z_fitted, z_fitted, z_upper, z_lower)


    
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
        pixel_matrix = []

        grating = spectrograph.get_grating()
        time.sleep(5)

        for i, center_wavelength in enumerate(center_wavelength_list):
            spectrograph.set_center_wavelength(center_wavelength)
            print("set center wavelength to: ", center_wavelength )
            time.sleep(10)
            
            for j, wavelength in enumerate(laser_wavelength_list):
                print("set laser wavelength: ", wavelength )
                laser.set_wavelength(wavelength)
                time.sleep(5)
                
                y_counts = camera.get_trace()
                x_axis = range(0, np.size(y_counts))
                argmax_ycount = np.argmax(y_counts)
                
                # Store the argmax_ycount value in the matrix at the corresponding position
                pixel_matrix[i, j] = argmax_ycount
                
                max_wavelength = x_axis[argmax_ycount]
                print("the peak: ", max_wavelength)

        #create matrices
        laser_wavelength_matrix = np.tile(laser_wavelength_list, (len(center_wavelength_list), 1) )
        center_wavelength_matrix= np.tile(center_wavelength_list[:, np.newaxis], (1,len(laser_wavelength_list)) )


        return pixel_matrix, laser_wavelength_matrix, center_wavelength_matrix
        





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

    pixel_list, laser_wavelength_list, center_wavelength_list = calibrator.calibrate_2d(laser, spectrograph, camera, 910, 941, 10)
    x, y, z, x_grid, y_grid, z_fitted, z_fitted, z_upper, z_lower = poly2d_fit(pixel_list, center_wavelength_list, pixel_list, degree=3)
    plot_results(x, y, z, x_grid, y_grid, z_fitted, z_fitted, z_upper, z_lower)


        # Example usage
    if __name__ == "__main__":
    # Define example matrices for x, y, and z
    x_range = np.linspace(0, 10, 12)
    y_range = np.linspace(0, 10, 12)
    x, y = np.meshgrid(x_range, y_range)
    
    # Define a true polynomial surface for demonstration
    z = 0.001 * (x ** 3) - 0.01 * (x ** 2) + 0.005 * x * y + 0.0002 * (y ** 3) - 0.02 * (y ** 2) + 0.1 * x - 0.05 * y + 700
    
    # Call the main function with example data
    main(x, y, z)
#____________________________________________________________________________________







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





    