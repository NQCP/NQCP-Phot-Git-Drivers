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
                    0.106E-06])

# Create a new figure
plt.figure()

# Plot with log scale for the current
plt.plot(voltage, current, marker='o')

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