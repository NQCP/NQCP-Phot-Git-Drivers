import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a Tkinter window
root = tk.Tk()
root.title("Matplotlib Plot in Tkinter")

# Create a Matplotlib figure and subplot
fig, ax = plt.subplots()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Matplotlib Plot in Tkinter')

# Initialize an empty line object
line, = ax.plot([], [], 'bo-', label='Dynamic Data')

# Set up the axes limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)


# Function to update the plot
def update_plot():
    # Generate new data points
    x_data = np.linspace(0, 10, 10)  # Example: Linearly spaced x values
    y_data = np.random.randint(0, 20, 10)  # Example: Random y values

    # Update the plot with new data points
    line.set_xdata(x_data)
    line.set_ydata(y_data)

    # Redraw the plot
    canvas.draw()


# Create a canvas to embed Matplotlib plot in Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a button to trigger plot update
update_button = tk.Button(root, text="Update Plot", command=update_plot)
update_button.pack(side=tk.BOTTOM)

# Run the Tkinter event loop
root.mainloop()