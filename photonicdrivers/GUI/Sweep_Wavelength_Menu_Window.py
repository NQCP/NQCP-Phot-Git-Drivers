import tkinter as tk
from tkinter import ttk

from photonicdrivers.GUI.functions import get_float_from_string


class Sweep_Wavelength_Menu_Window:

    def __init__(self, instrument_controller, gui_controller):

        self.update_bool = None
        self.label = None
        self.instrument_controller = instrument_controller
        self.gui_controller = gui_controller
        self.button_1 = None
        self.button_2 = None
        self.button_3 = None
        self.button_4 = None
        self.button_5 = None
        self.entry_1 = None
        self.entry_2 = None
        self.entry_3 = None
        self.entry_4 = None
        self.frame = None

    def open(self, parent_frame):
        if self.frame is None:
            self.update_bool = True
            self.frame = tk.Frame(parent_frame, bg="white")

            msg = self.get_message()
            self.label = ttk.Label(self.frame, text=msg, font="Arial", background="white")
            self.label.pack(side="top", fill="x", pady=10)

            self.button_1 = ttk.Button(self.frame)
            self.button_1["text"] = "Run Sweep"
            self.button_1["command"] = lambda: self.run_sweep_button()
            self.button_1.pack(fill='both', expand=True)

            self.entry_2 = ttk.Entry(self.frame)
            self.button_4 = ttk.Button(self.frame)
            self.button_4["text"] = "Set Min Variable"
            self.button_4["command"] = lambda: self.set_min_variable_button()
            self.button_4.pack(fill='both', expand=True)
            self.entry_2.insert(0, "Set Min Variable...")
            self.entry_2.bind("<FocusIn>", lambda event: self.entry_2.delete(0, "end"))
            self.entry_2.pack(fill='both', expand=True)

            self.entry_3 = ttk.Entry(self.frame)
            self.button_5 = ttk.Button(self.frame)
            self.button_5["text"] = "Set Max Variable"
            self.button_5["command"] = lambda: self.set_max_variable_button()
            self.button_5.pack(fill='both', expand=True)
            self.entry_3.insert(0, "Set Max Variable...")
            self.entry_3.bind("<FocusIn>", lambda event: self.entry_3.delete(0, "end"))
            self.entry_3.pack(fill='both', expand=True)





    def get_message(self):
        if self.instrument_controller.instrument_connected_bool:
            if  self.gui_controller.get_sweep_wavelength_mode() == "Power":
                return "Sweep Power Mode: " + str(self.gui_controller.get_sweep_wavelength_mode()) + "\n" + \
                    "Save Bool: " + str(self.gui_controller.get_save_bool()) + "\n" + \
                    "Min Power: " + str(self.instrument_controller.get_min_power()) + " mW \n" + \
                    "Max Power: " + str(self.instrument_controller.get_max_power()) + " mW \n" + \
                    "Sweep Power: " + str(self.instrument_controller.get_sweep_power()) + " mW"
            elif self.gui_controller.get_sweep_wavelength_mode() == "Voltage":
                return "Sweep Voltage Mode: " + str(self.gui_controller.get_sweep_wavelength_mode()) + "\n" + \
                    "Save Bool: " + str(self.gui_controller.get_save_bool()) + "\n" + \
                    "Min voltage: " + str(self.instrument_controller.get_min_voltage()) + " V \n" + \
                    "Max voltage: " + str(self.instrument_controller.get_max_voltage()) + " V \n" + \
                    "Sweep voltage: " + str(self.instrument_controller.get_sweep_voltage()) + " V "
            else:
                return "Sweep Power Mode: " + str(self.gui_controller.get_sweep_wavelength_mode()) + "\n" + \
                    "Save Bool: " + str(self.gui_controller.get_save_bool()) + "\n" + \
                    "Min wavelength: " + str(self.instrument_controller.get_min_wavelength()) + " nm \n" + \
                    "Max wavelength: " + str(self.instrument_controller.get_max_wavelength()) + " nm \n" + \
                    "Sweep wavelength: " + str(self.instrument_controller.get_sweep_wavelength()) + " nm "
        else:
            return ""

    def run_sweep_button(self):
        self.gui_controller.run_sweep_wavelength()
        self.update_window()

    def set_sweep_pause_time_button(self):
        sweep_pause_time = get_float_from_string(self.entry_5.get(), self.gui_controller.get_sweep_pause_time())
        self.gui_controller.set_sweep_pause_time(sweep_pause_time)
        self.update_window()

    def set_sweep_variable_button(self):
        sweep_variable = get_float_from_string(self.entry_1.get(), self.instrument_controller.get_sweep_wavelength())
        if self.gui_controller.get_sweep_wavelength_mode() == "Power":
            self.instrument_controller.set_sweep_power(sweep_variable)
        elif self.gui_controller.get_sweep_wavelength_mode() == "Voltage":
            self.instrument_controller.set_sweep_voltage(sweep_variable)
        else:
            self.instrument_controller.set_sweep_wavelength(sweep_variable)
        self.update_window()

    def set_min_variable_button(self):
        min_variable = get_float_from_string(self.entry_2.get(), self.instrument_controller.get_min_wavelength())
        if self.gui_controller.get_sweep_wavelength_mode() == "Power":
            self.instrument_controller.set_min_power(min_variable)
        elif self.gui_controller.get_sweep_wavelength_mode() == "Voltage":
            self.instrument_controller.set_min_voltage(min_variable)
        else:
            self.instrument_controller.set_min_wavelength(min_variable)
        self.update_window()

    def set_max_variable_button(self):
        max_variable = get_float_from_string(self.entry_3.get(), self.instrument_controller.get_max_wavelength())
        if self.gui_controller.get_sweep_wavelength_mode() == "Power":
            self.instrument_controller.set_max_power(max_variable)
        elif self.gui_controller.get_sweep_wavelength_mode() == "Voltage":
            self.instrument_controller.set_max_voltage(max_variable)
        else:
            self.instrument_controller.set_max_wavelength(max_variable)
        self.update_window()

    def toggle_save_bool_button(self):
        self.gui_controller.toggle_save_bool()
        self.update_window()

    def get_toggle_save_button_label(self):
        return self.gui_controller.save_bool

    def update_window(self):
        if self.update_bool:
            self.label.config(text=self.get_message())

    def close(self):
        self.update_bool = False
        if self.frame is not None:
            self.frame.destroy()

    def set_save_path_button(self):
        save_path = self.entry_4.get()
        self.gui_controller.set_wavelength_sweep_save_path(save_path)

    def next_mode_button(self):
        self.gui_controller.next_sweep_wavelength_mode()