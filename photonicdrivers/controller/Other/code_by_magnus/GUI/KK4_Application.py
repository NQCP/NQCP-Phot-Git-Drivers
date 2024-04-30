import queue
from tkinter import Tk

import json
from tkinter import *
import pyvisa as visa

from Instruments.Power_Meters.Thorlabs_PM100 import Thorlabs_PM100U

from PIL import ImageTk
from matplotlib import pyplot as plt
# these two imports are important
import threading

from thorlabs_tsi_sdk.tl_camera import TLCameraSDK

from Instruments.Camera.CameraAcquisitionThread import CameraAcquisitionThread, NoneThread
from Instruments.Camera.CameraWindow import CameraWindow
from Instruments.Camera.Thorlabs_Camera import Thorlabs_Camera
from Instruments.Camera.Thorlabs_Camera_Stub import Thorlabs_Camera_Stub
from Instruments.Camera.examples.windows_setup import configure_path
from Instruments.Settings.Console_Controller import Console_Controller
from Instruments.Settings.Settings_Controller import Settings_Controller


class Camera_Window:
    def __init__(self):
        self._image_width = 0
        self._image_height = 0
        self._frame_time = 50  # ms

        self.plot_flag = False
        self.camera = None

    def update(self):
        self.open_camera()
        self.plot_camera_image()

    def plot_camera_image(self):
        while self.plot_flag:
            Console_Controller.print_message("Plotting image...")

    def open_camera(self):
        if self.camera is None:
            self.resource_manager = TLCameraSDK()
            self.camera = Thorlabs_Camera_Stub(self.resource_manager, serial_number='12581')
            self.camera.connect()

            self.camera_settings_controller = Settings_Controller(self.camera)
            self.camera_settings_controller.load_settings('C:/Users/fkr476/OneDrive - University of '
                                                          'Copenhagen/PhD/Code/PicLab/Code/Settings/Thorlabs_Camera/',
                                                          'Thorlabs_Camera_Settings.txt')

    def setup_figure(self):
        self.plot_flag = True

    def close_window(self):
        self.plot_flag = False


class KK4_Application:

    def __init__(self):
        self.camera_acquisition_thread = NoneThread()
        Console_Controller.set_print_bool(True)

        self.camera = Thorlabs_Camera(TLCameraSDK(), serial_number='12581')
        self.camera_settings_controller = Settings_Controller(self.camera)

        self.picture_analyzer =


        self.camera_frame = None
        self.main_window = None
        self.menubar = None
        self.update_time = 100

        # initialise a window.
        self.configure_main_window()
        self.configure_menubar()

        self.camera_window = None

        self.figure_frame = Frame(self.main_window, bg="white")
        self.figure_frame.pack(side=RIGHT, expand=True, fill="both")
        self.camera_frame = Frame(self.figure_frame, bg="white")
        self.camera_frame.pack(side=TOP, expand=True, fill="both")

        self.camera_window = CameraWindow(parent=self.main_window)

        self.main_window.mainloop()

    def configure_menubar(self):
        self.menubar = Menu(self.main_window)
        self.file_menu = Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Save Settings", command=self.save_settings)
        self.file_menu.add_command(label="Save Figure", command=self.do_nothing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.close_application)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.camera_menu = Menu(self.menubar, tearoff=0)
        self.power_meter_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Cameras", menu=self.camera_menu)
        self.camera_menu.add_command(label="Toggle Acquisition", command=self.toggle_camera_acquisition)
        self.camera_menu.add_command(label="Start Acquisition", command=self.start_camera_acquisition)
        self.camera_menu.add_command(label="End Acquisition", command=self.stop_camera_acquisition)
        self.camera_menu.add_command(label="Toggle Connection", command=self.toggle_camera_connection)
        self.camera_menu.add_command(label="Connect", command=self.connect_camera)
        self.camera_menu.add_command(label="Disconnect", command=self.disconnect_camera)
        self.camera_menu.add_command(label="Load Settings", command=self.load_settings)
        self.camera_menu.add_command(label="Save Settings", command=self.save_settings)

        self.menubar.add_cascade(label="Power Meter", menu=self.power_meter_menu)
        self.power_meter_menu.add_command(label="Toggle Acquisition", command=self.do_nothing)
        self.power_meter_menu.add_command(label="Start Acquisition", command=self.do_nothing)
        self.power_meter_menu.add_command(label="End Acquisition", command=self.do_nothing)
        self.power_meter_menu.add_command(label="Toggle Connection", command=self.do_nothing)
        self.power_meter_menu.add_command(label="Connect", command=self.connect_power_meter)
        self.power_meter_menu.add_command(label="Disconnect", command=self.disconnect_power_meter)
        self.power_meter_menu.add_command(label="Load Settings", command=self.do_nothing)
        self.power_meter_menu.add_command(label="Save Settings", command=self.do_nothing)
        self.main_window.config(menu=self.menubar)

    def configure_main_window(self):
        self.main_window = Tk()
        self.main_window.wm_title("PIC LAB")
        self.main_window.config(background='white')
        self.main_window.geometry("1000x700")
        # self.main_window.attributes("-fullscreen", True)
        self.main_window.protocol("WM_DELETE_WINDOW", self.close_application)

    def do_nothing(self):
        pass

    def close_application(self):
        Console_Controller.print_message("Closing Application")
        self.camera_acquisition_thread.stop()
        self.main_window.quit()

    def update(self):
        self.main_window.update()
        self.main_window.after(self.update_time, self.update)

    def toggle_camera_acquisition(self):
        try:
            if not self.camera_acquisition_thread.get_is_alive():
                self.start_camera_acquisition()
            else:
                self.stop_camera_acquisition()
        except Exception as error:
            Console_Controller.print_message(error)


    def start_camera_acquisition(self):
        try:
            if not self.camera.is_connected:
                raise Exception("Cameras not connected")

            if self.camera_acquisition_thread.get_is_alive():
                raise Exception("Cameras acquisition is already running")

            self.camera_acquisition_thread = CameraAcquisitionThread(self.camera)

            self.camera_window.set_acquisition_thread(self.camera_acquisition_thread)
            self.picture_analyzer.set_acquistion_thread(self.camera_acquisition_thread)

            self.camera_window.start()
            self.camera_acquisition_thread.start()
        except Exception as error:
            Console_Controller.print_message(error)

    def stop_camera_acquisition(self):
        try:
            if not self.camera_acquisition_thread.get_is_alive():
                raise ConnectionError("Cameras acquisition not started")
            self.camera_acquisition_thread.stop()
        except Exception as error:
            Console_Controller.print_message(error)

    def toggle_camera_connection(self):
        try:
            if not self.camera.is_connected:
                self.connect_camera()
            else:
                self.disconnect_camera()
        except Exception as error:
            Console_Controller.print_message(error)

    def connect_camera(self):
        self.camera.connect()

    def disconnect_camera(self):
        self.camera.disconnect()

    def load_settings(self):
        self.camera_settings_controller.load_settings(
            'C:/Users/fkr476/OneDrive - University of Copenhagen/PhD/Code/PicLab/Code/Settings/Thorlabs_Camera/',
            'Thorlabs_Camera_Settings.txt')

    def save_settings(self):
        self.camera_settings_controller.save_settings(
            'C:/Users/fkr476/OneDrive - University of Copenhagen/PhD/Code/PicLab/Code/Settings/Thorlabs_Camera/',
            'Thorlabs_Camera_Settings.txt')

    def connect_power_meter(self):
        self.power_meter.connect()

    def disconnect_power_meter(self):
        self.power_meter.disconnect()