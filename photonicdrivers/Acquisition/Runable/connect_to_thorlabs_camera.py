import tkinter as tk

from photonicdrivers.Controller.Instruments.Implementations.Cameras.CameraAcquisitionThread import \
    CameraAcquisitionThread
from photonicdrivers.Controller.Instruments.Implementations.Cameras.CameraWindow import CameraWindow
from photonicdrivers.Controller.Instruments.Implementations.Cameras.Thorlabs_Camera import Thorlabs_Camera
from photonicdrivers.Controller.Instruments.Implementations.Cameras.examples.windows_setup import configure_path
from photonicdrivers.Controller.Instruments.Settings.Console_Controller import Console_Controller
from photonicdrivers.Controller.Instruments.Settings.Settings_Controller import Settings_Controller
from thorlabs_tsi_sdk.tl_camera import TLCameraSDK

configure_path()

resource_manager = TLCameraSDK()
camera = Thorlabs_Camera(resource_manager, serial_number='26925')
camera.connect()


root = tk.Tk()

camera_settings_controller = Settings_Controller(camera)
camera_settings_controller.load_settings('C:/Users/fkr476/OneDrive - University of '
                                         'Copenhagen/PhD/Code/PicLab/Code/Settings/Thorlabs_Camera/',
                                         'Thorlabs_Camera_Settings.txt')
camera.print_settings()
camera.set_exposure_time_us(40000)
camera.set_gain(50)
camera.print_settings()
camera_settings_controller.save_settings('C:/Users/fkr476/OneDrive - University of '
                                         'Copenhagen/PhD/Code/PicLab/Code/Settings/Thorlabs_Camera/',
                                         'Thorlabs_Camera_Settings.txt')

camera_widget = CameraWindow(parent=root)
camera_acquisition_thread = CameraAcquisitionThread(camera)
camera_widget.set_acquisition_thread(camera_acquisition_thread)

camera_widget.start()
Console_Controller.print_message("Starting image acquisition thread...")
camera_acquisition_thread.start()

Console_Controller.print_message("App starting")

root.mainloop()

Console_Controller.print_message("Waiting for image acquisition thread to finish...")

camera_acquisition_thread.stop()
camera_acquisition_thread.join()

Console_Controller.print_message("Closing resources...")
