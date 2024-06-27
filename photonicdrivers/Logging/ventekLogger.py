import sys
import os

from grafanaLogger import GrafanaLogger
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Instruments/Implementations/ventekController')))
from iSMA_MAC36 import iSMA_MAC36

import tkinter as tk
from tkinter import ttk
import threading
import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# User ID and API Key for Grafana account created with Peter Granum's email
# The logging class is set up to log to this account by default, so the arguments are only added here for demonstration
USER_ID = 1545635
API_KEY = "glc_eyJvIjoiMTEwODkyOCIsIm4iOiJzdGFjay05MTU0MjEtaW50ZWdyYXRpb24tbnFjcHBob3QiLCJrIjoiaDg5NnJiMTlQZTI2NzhWQmxVZDJ3SXlNIiwibSI6eyJyIjoicHJvZC1ldS1ub3J0aC0wIn19"

LOGGING_INTERVAL = 2 # in seconds
PLOT_TIME_PERIOD = 300 # in seconds


# Define the Modbus server IP address and port
SERVER_HOST = '10.209.67.120'  # Change this to your Modbus server IP address
SERVER_PORT = 502           # Change this to your Modbus server port
# Define the Modbus slave ID
SLAVE_ID = 10  # Change this to your Modbus slave ID
# Define the Modbus register address to read
REGISTER_ADDRESS = 0
   

class VentekLogger:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventek Logger")
        self.running = False

        self.create_widgets()

        self.dataArray = []

        self.logger = GrafanaLogger(USER_ID,API_KEY)
        self.controller = iSMA_MAC36(SERVER_HOST,SERVER_PORT,SLAVE_ID)

        self.running = True
        self.thread = threading.Thread(target=self.readAndLogData)
        self.thread.start()

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.stopRunning)

        
    def create_widgets(self):

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stopRunning)
        self.stop_button.grid(row=0, column=0, pady=10, padx=5)

        self.variable_label = tk.Label(self.root, text="KK4 temperature")
        self.variable_label.grid(row=1, column=0, pady=5, padx=5)

        self.variable_entry = tk.Entry(self.root, width=20)
        self.variable_entry.grid(row=2, column=0, pady=5, padx=5)

        self.variable2_label = tk.Label(self.root, text="Compressor room")
        self.variable2_label.grid(row=3, column=0, pady=5, padx=5)

        self.variable2_entry = tk.Entry(self.root, width=20)
        self.variable2_entry.grid(row=4, column=0, pady=5, padx=5)

        self.time_label = tk.Label(self.root, text="Last Updated Time")
        self.time_label.grid(row=1, column=1, pady=5, padx=5)

        self.time_entry = tk.Entry(self.root, width=20)
        self.time_entry.grid(row=2, column=1, pady=5, padx=5)

        # Create the matplotlib figure and axes
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, pady=10, padx=5)

    def stopRunning(self):
        print("stopping")

        # Closing hardware connections
        self.controller.closeConnection()

        # Stopping the program
        self.running = False
        self.stop_button.config(state=tk.DISABLED)
        self.root.quit() # quit
        # self.root.destroy()  # Close the Tkinter window and end the program

    def readAndLogData(self):
        while self.running:            
            self.KK4Info = self.controller.queryKK4Info()
            
            self.current_time = datetime.now()

            # Update the indicator fields
            self.variable_entry.delete(0, tk.END) # clear the field
            self.variable_entry.insert(0, self.KK4Info.IBI01_TT001) # enter new value

            self.variable2_entry.delete(0, tk.END) # clear the field
            self.variable2_entry.insert(0, self.KK4Info.IBI02_TT001) # enter new value

            self.time_entry.delete(0, tk.END)
            self.time_entry.insert(0, self.current_time.strftime('%H:%M:%S'))

            # Update plot            
            self.update_plot()

            # Log the data to Grafana
            # print(1)
            self.logger.log('KK4Temp',self.KK4Info.IBI01_TT001)
            self.logger.log('KK4cTemp',self.KK4Info.IBI02_TT001)
            self.logger.log('KK4bTemp',self.KK4Info.IBI03_TT001)

            self.logger.log('KK4Setpoint',self.KK4Info.IBI01_ACT_SP)
            self.logger.log('KK4cSetpoint',self.KK4Info.IBI02_ACT_SP)
            self.logger.log('KK3bSetpoint',self.KK4Info.IBI03_ACT_SP)

            self.logger.log('KK4Fancoil',self.KK4Info.IBI01_FC)
            self.logger.log('KK4cFancoil',self.KK4Info.IBI02_FC)
            self.logger.log('KK3bFancoil',self.KK4Info.IBI03_FC)
            # print(2)

            time.sleep(LOGGING_INTERVAL)

    def update_plot(self):
        # Unpack data
        KK4_temp = self.KK4Info.IBI01_TT001
        KK4c_temp = self.KK4Info.IBI02_TT001
        KK3b_temp = self.KK4Info.IBI03_TT001

        # Storing data in array
        self.dataArray.append((self.current_time, KK4_temp, KK4c_temp, KK3b_temp))
        
        # Remove data points older than 5 minutes
        self.dataArray = [(time, KK4_temp, KK4c_temp, KK3b_temp) for time, KK4_temp, KK4c_temp, KK3b_temp in self.dataArray if time >= datetime.now() - timedelta(seconds=PLOT_TIME_PERIOD)]

        # Split array in individual data arrays
        times = [point[0].timestamp() for point in self.dataArray]
        KK4_temp_array = [point[1] for point in self.dataArray]
        KK4c_temp_array = [point[2] for point in self.dataArray]
        KK3b_temp_array = [point[3] for point in self.dataArray]

        # Update the GUI
        self.ax.clear()
        self.ax.plot(times, KK4_temp_array, 'b', marker='o')
        self.ax.plot(times, KK4c_temp_array, 'b', marker='x')
        self.ax.plot(times, KK3b_temp_array, 'r', marker='o')
        self.ax.set_title('Room temperatures the last 5 Minutes')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Temperature [C]')
        self.ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: datetime.fromtimestamp(x).strftime('%H:%M:%S')))
        self.fig.autofmt_xdate()

        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = VentekLogger(root)
    app.mainloop()