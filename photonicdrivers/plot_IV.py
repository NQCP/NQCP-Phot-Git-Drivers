import matplotlib.pyplot as plt
import numpy as np

# Example data
voltage = np.arange(-600,1800,100)
print(voltage)
current = np.array([-5.80e-08,
                    -4.00e-09,
                    -3.00e-10,
                    1.00e-10,
                    0,
                    0,
                    0, 
                    1.00e-10,
                    1.00e-10,
                    1.00e-10,
                    2.00e-10,
                    3.50e-10,
                    7.00e-10,
                    1.20e-09,
                    2.30e-09,
                    4.00e-09,
                    6.70e-09,
                    1.09e-08,
                    1.70e-08,
                    2.58e-08,
                    3.83e-08,
                    5.48e-08,
                    7.67e-08,
                    0.106E-06])*1000

voltage = np.array([-1,
                    -0.9,
                    -0.8,
                    -0.7,
                    -0.6,
                    -0.5,
                    -0.4,
                    -0.3,
                    -0.25,
                    -0.2,
                    -0.15,
                    -0.1,
                    -0.05,
                    0,
                    0.1,
                    0.2,
                    0.3,
                    0.4,
                    0.45,
                    0.5,
                    0.55,
                    0.6,
                    0.65,
                    0.7,
                    0.75])*1000

current = np.array([-0.18,
                    -0.140,
                    -0.107,
                    -0.079,
                    -0.056,
                    -0.039,
                    -0.024,
                    -0.0139,
                    -0.00987,
                    -0.00675,
                    -0.0043,
                    -0.0025,
                    -0.00114,
                    0.000001,
                    0.0032,
                    0.0106,
                    0.0276,
                    0.0905,
                    0.203,
                    0.5820,
                    1.74,
                    5.78,
                    15.9,
                    37.7,
                    70.5])*10**(-6)

# Create a new figure
plt.figure()

# Plot with log scale for the current
plt.plot(voltage, np.abs(current), marker='o')

# Set the y-axis to log scale
plt.yscale('log')

# Set labels and title
plt.xlabel('Voltage [mV]')
plt.ylabel('Current [A]')
plt.title('IV Curve in Logarithmic Scale for Current')

# Show grid
plt.grid(True, which="both", ls="--")


# Create a new figure
plt.figure()

# Plot with log scale for the current
plt.plot(voltage, current, marker='o')


# Set labels and title
plt.xlabel('Voltage [mV]')
plt.ylabel('Current [A]')
plt.title('IV Curve in Linear Scale for Current')

# Show grid
plt.grid(True, which="both", ls="--")

# Show the plot
plt.show()