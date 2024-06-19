from grafanaLogger import GrafanaLogger

import tkinter as tk
from tkinter import ttk
import random
import threading
import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# User ID and API Key for Grafana account created with Peter Granum's email
# The logging class is set up to log to this account by default, so the arguments are only added here for demonstration
USER_ID = 1545635
API_KEY = "glc_eyJvIjoiMTEwODkyOCIsIm4iOiJzdGFjay05MTU0MjEtaW50ZWdyYXRpb24tbnFjcHBob3QiLCJrIjoiaDg5NnJiMTlQZTI2NzhWQmxVZDJ3SXlNIiwibSI6eyJyIjoicHJvZC1ldS1ub3J0aC0wIn19"

LOGGING_INTERVAL = 1 # IN SECONDS

class RandomNumberLogger:
    def __init__(self, root):
        self.root = root
        self.root.title("loggingmyvar")
        self.running = False

        self.create_widgets()

        self.data = []

        # self.stop_button = ttk.Button(root, text="Stop", command=self.stop_generating, state=tk.NORMAL)
        # self.stop_button.pack(pady=10)

        # self.log_box = tk.Text(root, height=10, width=50)
        # self.log_box.pack(pady=10)

        self.logger = GrafanaLogger(USER_ID,API_KEY)

        self.running = True
        self.thread = threading.Thread(target=self.readAndLogData)
        self.thread.start()

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.stopRunning)

        
    def create_widgets(self):

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stopRunning)
        self.stop_button.grid(row=0, column=0, pady=10, padx=5)

        self.variable_label = tk.Label(self.root, text="variableTitle")
        self.variable_label.grid(row=1, column=0, pady=5, padx=5)

        self.variable_entry = tk.Entry(self.root, width=20)
        self.variable_entry.grid(row=2, column=0, pady=5, padx=5)

        self.time_label = tk.Label(self.root, text="Last Updated Time")
        self.time_label.grid(row=1, column=1, pady=5, padx=5)

        self.time_entry = tk.Entry(self.root, width=20)
        self.time_entry.grid(row=2, column=1, pady=5, padx=5)

        # Create the matplotlib figure and axes
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, pady=10, padx=5)

    def stopRunning(self):
        print("stopping")
        self.running = False
        self.stop_button.config(state=tk.DISABLED)
        self.root.quit() # quit
        # self.root.destroy()  # Close the Tkinter window and end the program

    def readAndLogData(self):
        while self.running:

            # Generate a random number to simulate data acquisition
            random_number = random.randint(0, 100)
            current_time = datetime.now()

            self.variable_entry.delete(0, tk.END) # clear the field
            self.variable_entry.insert(0, random_number) # enter new value

            self.time_entry.delete(0, tk.END)
            self.time_entry.insert(0, current_time)

            # Update plot
            self.data.append((current_time, random_number))
            self.update_plot()

            # Remove data points older than 5 minutes
            self.data = [(time, value) for time, value in self.data if time >= datetime.now() - timedelta(seconds=5)]

            # Log the data to Grafana
            self.logger.log('myVarRand',random_number)

            time.sleep(LOGGING_INTERVAL)

    def update_plot(self):
        times = [point[0] for point in self.data]
        values = [point[1] for point in self.data]

        self.ax.clear()
        self.ax.plot(times, values, marker='o')
        self.ax.set_title('Random Numbers in the Last 5 Minutes')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Value')
        self.ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: datetime.fromtimestamp(x).strftime('%H:%M:%S')))
        self.fig.autofmt_xdate()

        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberLogger(root)
    print("1")
    root.mainloop()
    print("2")