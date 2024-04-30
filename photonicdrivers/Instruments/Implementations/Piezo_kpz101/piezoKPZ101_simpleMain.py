import time
import tkinter as tk
from queue import Queue
from threading import Thread, Event

from piezoKPZ101 import PiezoKPZ101


# piezo = PiezoKPZ101("29252886")
# # print(piezo.enable)
# print(piezo.getMaxVoltage())
# print('done')


class App:
    def __init__(self, master, _piezoID):
        self.master = master
        self.queue = Queue()
        self.stop_event = Event()  # Event to signal the main loop to stop
        self.piezoID = _piezoID

        self.create_widgets()

        # Queue some initial functions
        self.piezo = PiezoKPZ101(self.piezoID)

        # Start a separate thread to run the main loop to prevent the GUI from freezing
        self.thread = Thread(target=self.main_loop)
        self.thread.start()

    def create_widgets(self):
        self.setVoltage_frame = tk.LabelFrame(self.master, text="Set Voltage", padx=10, pady=10)
        self.setVoltage_frame.pack()

        self.voltageSetPoint = tk.Entry(self.setVoltage_frame)
        self.voltageSetPoint.pack()

        self.button_setVoltage = tk.Button(self.setVoltage_frame, text="Set Voltage", command=self.enqueue_setVoltage)
        self.button_setVoltage.pack()

        self.readVoltage_frame = tk.LabelFrame(self.master, text="Voltage [V]", padx=10, pady=10)
        self.readVoltage_frame.pack()

        self.voltage_value_label = tk.Label(self.readVoltage_frame, text="NaN", font=("Helvetica", 16))
        self.voltage_value_label.pack()

        self.button_enable = tk.Button(self.master, text="Enable", command=self.enqueue_enable)
        self.button_enable.pack()

        self.button_disable = tk.Button(self.master, text="Disable", command=self.enqueue_disable)
        self.button_disable.pack()

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack()


    def enqueue_setVoltage(self):
        self.queue.put("setVoltage")

    def enqueue_enable(self):
        self.queue.put("enable")

    def enqueue_disable(self):
        self.queue.put("disable")

    def stop(self):
        self.stop_event.set()  # Set the stop event to signal the main loop to stop
        self.master.after(500, self.master.destroy)  # Schedule window destruction in the main thread after 10 ms
        # it is better to use the "after" function than the time.sleep function, as the latter will hold up the loop

    def main_loop(self):
        while not self.stop_event.is_set():
            try:
                task = self.queue.get_nowait()
            except:
                # Queue is empty, wait for a short time
                time.sleep(0.1)

                # Collect status information
                outputVoltage = self.piezo.getOutputVoltage()
                self.voltage_value_label.config(text=str(outputVoltage))

                # Log data to remote
                ### insert code here
                
                continue

            # Switch case based on the task
            if task == "setVoltage":
                value = self.voltageSetPoint.get()
                self.setVoltage(value)
            elif task == "enable":
                self.piezo.enable()
            elif task == "disable":
                self.piezo.disable()
    
    def setVoltage(self, voltage):
        print(voltage)
        self.piezo.setOutputVoltage(voltage)


if __name__ == "__main__":
    root = tk.Tk()
    piezoID = "29252886"
    app = App(root,piezoID)
    root.mainloop()