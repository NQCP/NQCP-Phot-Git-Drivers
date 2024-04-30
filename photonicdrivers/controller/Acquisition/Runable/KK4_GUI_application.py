import json
from tkinter import *

from matplotlib import pyplot as plt
# these two imports are important
import threading

from photonicdrivers.controller.GUI.Sweep_Wavelength_Menu_Window import Sweep_Wavelength_Menu_Window
from photonicdrivers.controller.GUI.Sweep_Wavelength_Plot_Window import Sweep_Wavelength_Plot_Window


class GUI_Controller:

    def __init__(self):

        self.is_voltage_sweep_on = None
        self.is_wavelength_sweep_on = None
        self.voltage_sweep_save_path = None
        self.wavelength_sweep_save_path = None
        self.sweep_wavelength_mode = "Loss"
        self.save_bool = True
        self.piezo_optimization_thread = None
        self.main_loop_bool = True
        self.sweep_wavelength_thread = None
        self.acquisition_thread = None

        self.is_optimize_piezo_on = False
        self.is_instruments_on = False
        self.is_acquisition_on = False

        self.sweep_pause_time = 1

        self.sweep_wavelength_menu_window = Sweep_Wavelength_Menu_Window(self.instrument_controller, self)
        self.sweep_wavelength_plot_window = Sweep_Wavelength_Plot_Window(self.instrument_controller, self)

        settings = 'C:/Users/shd-PhotonicLab/Documents/Python Scripts/Qversion_exp/Settings/optimize_piezo_settings'

        # initialise a window.
        self.main_window = Tk()
        self.main_window.wm_title("PIC LAB")
        self.main_window.config(background='white')
        self.main_window.geometry("1000x700")
        # self.main_window.attributes("-fullscreen", True)
        self.main_window.protocol("WM_DELETE_WINDOW", self.close_application)

        self.menubar = Menu(self.main_window)

        self.file_menu = Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Save", command=self.do_nothing)
        self.file_menu.add_command(label="Save Figure", command=self.do_nothing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.close_application)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.instrument_menu = Menu(self.menubar, tearoff=0)
        self.instrument_menu.add_command(label="Connect/Disconnect", command=self.toggle_instruments)
        self.menubar.add_cascade(label="Code", menu=self.instrument_menu)

        self.control_frame = Frame(self.main_window, bg="white")
        self.control_frame.pack(side=LEFT, expand=True, fill="y")

        self.sweep_frame = Frame(self.main_window, bg="white")
        self.sweep_frame.pack(side=RIGHT, expand=True, fill="y")

        self.sweep_wavelength_frame = self.sweep_wavelength_menu_window.open(self.sweep_frame)
        self.sweep_wavelength_frame.pack(side=TOP, fill="both")

        self.sweep_wavelength_plot_frame = Frame(self.figure_frame, bg="white")
        self.sweep_wavelength_plot_frame.pack(side=TOP, expand=True, fill="both")

        self.main_window.config(menu=self.menubar)

        self.open_instruments()
        self.main_iteration()
        self.main_window.mainloop()

    def get_sweep_wavelength_mode(self):
        return self.sweep_wavelength_mode

    def get_save_bool(self):
        return self.save_bool

    def close_application(self):
        self.close_instruments()
        print("Closing Application")
        self.main_window.quit()

    def do_nothing(self):
        pass

    def toggle_instruments(self):
        if self.is_instruments_on:
            self.close_instruments()
        else:
            self.open_instruments()

    def close_instruments(self):
        if self.is_instruments_on:
            self.is_instruments_on = False
            self.instrument_controller.close_instruments()

    def open_instruments(self):
        if not self.is_instruments_on:
            self.is_instruments_on = True
            self.instrument_controller.open_instruments()

    def main_iteration(self):
        self.main_window.update
        self.sweep_wavelength_menu_window.update_window()
        self.main_window.after(100, self.main_iteration)

    def toggle_save_bool(self):
        self.save_bool = not self.save_bool

    def run_sweep_wavelength(self):
        if not self.is_wavelength_sweep_on:
            self.is_wavelength_sweep_on = True
            self.open_instruments()
            self.sweep_wavelength_plot_window.setup_figure(self.sweep_wavelength_plot_frame)
            self.sweep_wavelength_thread = threading.Thread(target=self.sweep_wavelength_plot_window.update)
            self.sweep_wavelength_thread.start()


GUI_Controller()
