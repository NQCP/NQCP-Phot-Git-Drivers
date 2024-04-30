
import threading
from tkinter import *

from photonicdrivers.Instruments.Settings.Console_Controller import Console_Controller


class KK4_Application:

    def __init__(self):
        self.camera_application_window = None
        Console_Controller.set_print_bool(True)

        self.main_window = None
        self.menubar = None
        self.update_time = 100

        # initialise a window.
        self.configure_main_window()
        self.configure_menubar()

        self.main_window.mainloop()

    def configure_menubar(self):
        self.menubar = Menu(self.main_window)
        self.file_menu = Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Save Settings", command=self.do_nothing)
        self.file_menu.add_command(label="Save Figure", command=self.do_nothing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.close_application)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.application_menu = Menu(self.menubar, tearoff=0)
        self.application_menu.add_command(label="Open Cameras Application", command=self.open_camera_application)
        self.menubar.add_cascade(label="Applications", menu=self.application_menu)
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
        self.main_window.quit()

    def update(self):
        self.main_window.update()
        self.main_window.after(self.update_time, self.update)

    def open_camera_application(self):
            self.camera_application_window_thread = threading.Thread(target=Camera_Application)
            self.camera_application_window_thread.daemon = True
            self.camera_application_window_thread.start()

