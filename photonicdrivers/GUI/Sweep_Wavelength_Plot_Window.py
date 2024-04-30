import matplotlib as mpl
import numpy as np

mpl.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import h5py
import datetime


# Simon Test

class Sweep_Wavelength_Plot_Window:
    def __init__(self, instrument_controller, gui_controller):
        self.waveform_generator = None
        self.delta_variable = None
        self.max_variable = None
        self.min_variable = None
        self.delta_wavelength = None
        self.gui_controller = gui_controller
        self.graph = None
        self.ax = None
        self.power_dBm_plot_list = None
        self.power_W_plot_list = None
        self.power_dBm_array = None
        self.variable_array = None
        self.variable_array_plot = None
        self.points_plot = None
        self.power_W_array = None
        self.folder = None

        self.instrument_controller = instrument_controller
        self.gui_controller = gui_controller
        self.target_detector = None
        self.laser = None
        self.target_detector_index = 0
        self.detector_list = None
        self.power_stability_bool = True
        self.power_stability_W_ref = None
        self.fig = None
        self.num_stability_runs = 0
        self.target_detector_follow_wavelength = None
        self.mode = None

    def setup_figure(self, frame):
        self.mode = self.gui_controller.get_sweep_wavelength_mode()
        self.folder = self.gui_controller.get_sweep_wavelength_mode()
        self.target_detector = self.instrument_controller.get_target_detector()
        self.target_detector_index = self.instrument_controller.get_target_detector()
        self.detector_list = self.instrument_controller.get_detector_list()
        self.laser = self.instrument_controller.get_target_laser()
        if self.mode == "Voltage":
            self.waveform_generator = self.instrument_controller.get_waveform_generator_list()[0]
        if self.mode == "Power":
            self.min_variable = self.instrument_controller.get_min_power()
            self.max_variable = self.instrument_controller.get_max_power()
            self.delta_variable = self.instrument_controller.get_sweep_power()
        elif self.mode == "Voltage":
            self.min_variable = self.instrument_controller.get_min_voltage()
            self.max_variable = self.instrument_controller.get_max_voltage()
            self.delta_variable = self.instrument_controller.get_sweep_voltage()
        else:
            self.min_variable = self.instrument_controller.get_min_wavelength()
            self.max_variable = self.instrument_controller.get_max_wavelength()
            self.delta_variable = self.instrument_controller.get_sweep_wavelength()

        self.variable_array = np.arange(self.min_variable, self.max_variable + self.delta_variable,
                                        self.delta_variable, dtype=float)
        rows, cols = (len(self.detector_list), len(self.variable_array))
        self.power_W_array, self.power_dBm_array = np.empty([rows, cols]), np.empty([rows, cols])
        self.variable_array_plot, self.power_W_plot_list, self.power_dBm_plot_list = [], [], []

        if self.fig is None:
            SMALL_SIZE, MEDIUM_SIZE, BIGGER_SIZE = 22, 24, 26
            mpl.rcParams['font.sans-serif'] = "Arial"
            plt.rc('font', size=MEDIUM_SIZE)
            plt.rc('axes', titlesize=MEDIUM_SIZE, labelsize=MEDIUM_SIZE)
            plt.rc('xtick', labelsize=SMALL_SIZE)
            plt.rc('ytick', labelsize=SMALL_SIZE)
            plt.rc('legend', fontsize=SMALL_SIZE)
            plt.rc('figure', titlesize=BIGGER_SIZE)

            SMALL_SIZE, MEDIUM_SIZE, BIGGER_SIZE = 22, 24, 26
            mpl.rcParams['font.sans-serif'] = "Arial"
            plt.rc('font', size=MEDIUM_SIZE)
            plt.rc('axes', titlesize=MEDIUM_SIZE, labelsize=MEDIUM_SIZE)
            plt.rc('xtick', labelsize=SMALL_SIZE)
            plt.rc('ytick', labelsize=SMALL_SIZE)
            plt.rc('legend', fontsize=SMALL_SIZE)
            plt.rc('figure', titlesize=BIGGER_SIZE)
            mpl.use("TkAgg")  # set the backend

            self.fig = Figure()
            self.graph = FigureCanvasTkAgg(self.fig, master=frame)
            self.graph.get_tk_widget().pack(side="right", fill='both', expand=True)

            self.ax = self.fig.add_subplot(111)
            if self.mode == "Power":
                self.ax.set(xlabel='Power (mW)', ylabel='Power (dBm)')
            elif self.mode == "Voltage":
                self.ax.set(xlabel='Voltage (V)', ylabel='Power (dBm)')
            else:
                self.ax.set(xlabel='Wavelength (nm)', ylabel='Power (dBm)')
            self.ax.grid()
            self.ax.set_xlim([self.min_variable, self.max_variable])
            self.points_plot, = self.ax.plot(self.variable_array_plot, self.power_dBm_plot_list)

    def update(self):
        self.ax.set_xlim([self.min_variable, self.max_variable])
        self.variable_array = np.arange(self.min_variable, self.max_variable + self.delta_variable, self.delta_variable,
                                        dtype=float)
        for variable_index in range(len(self.variable_array)):
            variable = round(self.variable_array[variable_index], 2)

            self.change_laser(self.mode, variable)
            self.change_detector(variable)
            self.change_pause(variable_index)
            self.detector_acquisition(variable, variable_index)
            self.points_plot.set_data(self.variable_array_plot, self.power_dBm_plot_list)
            self.ax.set_ylim([min(self.power_dBm_plot_list) - 1, max(self.power_dBm_plot_list) + 1])
            self.graph.draw()

        self.save_data()
        self.gui_controller.is_wavelength_sweep_on = False

    def detector_acquisition(self, variable, variable_index):
        for detector_index in range(0, len(self.detector_list)):
            detector = self.detector_list[detector_index]
            power_W = detector.get_detector_power_get()
            power_dBm = power_W_to_dBm(power_W)

            self.power_W_array[detector_index][variable_index] = power_W
            self.power_dBm_array[detector_index][variable_index] = power_dBm

            if detector_index == self.instrument_controller.get_target_detector_index():
                self.power_W_plot_list.append(power_W)
                self.power_dBm_plot_list.append(power_dBm)
                self.variable_array_plot.append(variable)

    def change_pause(self, variable_index):
        if variable_index == 0:
            plt.pause(3)
        else:
            plt.pause(self.gui_controller.get_sweep_pause_time())

    def change_detector(self, variable):
        if self.mode == "Loss":
            self.target_detector.set_detector_wavelength_set(variable)  # Loss
        elif self.mode == "SFG":
            self.target_detector.set_detector_wavelength_set(980)
            # self.target_detector.set_detector_wavelength_set(1 / (1 / 2325.8 + 1 / variable))
        elif self.mode == "Follow":
            self.target_detector.set_detector_wavelength_set(self.target_detector_follow_wavelength)
        elif self.mode == "DFG":
            wavelength = 1 / (
                    1 / self.instrument_controller.get_toptica_laser().get_wavelength_set() - 1 / self.instrument_controller.get_exfo_laser().get_wavelength_set())
            self.target_detector.set_detector_wavelength_set(wavelength)
        else:
            pass

    def change_laser(self, mode, variable):
        if mode == "Power":
            self.laser.set_power(variable)
        elif mode == "Voltage":
            self.waveform_generator.set_voltage(variable)
        else:
            self.laser.set_wavelength(variable)

    def save_data(self):
        beginning_time = datetime.datetime.now()
        laser_info = ""
        for laser in self.instrument_controller.get_laser_list():
            laser_info += str(laser.get_name()) + "_" + str(np.round(laser.get_power_set(), 1)) + "_" + str(
                np.round((laser.get_wavelength_set()), 1)) + "_"

        filename = beginning_time.strftime("%Y-%m-%d_%H-%M-%S") + "_" + \
                   self.gui_controller.get_wavelength_sweep_save_path() + "_" + \
                   self.gui_controller.get_sweep_wavelength_mode() + "_" + \
                   str(self.laser.get_name()) + "_" + \
                   str(self.min_variable) + "_" + \
                   str(self.max_variable) + "_" + \
                   str(self.delta_variable) + "_" + \
                   laser_info

        if self.gui_controller.save_bool:
            header = \
                "#\n# Date: %s\n#\n" % beginning_time.strftime("%Y-%m-%d_%H-%M-%S") + \
                "# Laser: %s\n" % self.laser.get_name() + \
                "# Power: %s\n" % self.laser.get_power()

            self.fig.savefig("Figures/" + filename + ".pdf", bbox_inches='tight')
            hf = h5py.File('Data/' + self.folder + '/' + filename + '.h5', 'w')
            hf.create_dataset('Header', data=header)
            if self.mode == "Power":
                hf.create_dataset('Power_mW', data=self.variable_array)
            elif self.mode == "Voltage":
                hf.create_dataset('Voltage_V', data=self.variable_array)
            else:
                hf.create_dataset('Wavelength_nm', data=self.variable_array)
            for detector_index in range(0, len(self.detector_list)):
                hf.create_dataset(self.detector_list[detector_index].get_name() + "_power_W",
                                  data=self.power_W_array[detector_index])

            hf.close()

    def follow_phase_matching(self):
        for wavelength in np.arange(1590, 1630, 1):
            exfo_laser = self.instrument_controller.get_exfo_laser()
            exfo_laser.set_wavelength(wavelength)
            self.update()

            rows, cols = (len(self.detector_list), len(self.variable_array))
            self.power_W_array, self.power_dBm_array = np.empty([rows, cols]), np.empty([rows, cols])
            self.variable_array_plot, self.power_W_plot_list, self.power_dBm_plot_list = [], [], []

    def sweep_power(self):
        target_laser = self.instrument_controller.get_toptica_laser()
        for power in range(target_laser.get_min_power(), target_laser.get_max_power() + 1, 1):
            target_laser.set_power(power)
            self.update()
            rows, cols = (len(self.detector_list), len(self.variable_array))
            self.power_W_array, self.power_dBm_array = np.empty([rows, cols]), np.empty([rows, cols])
            self.variable_array_plot, self.power_W_plot_list, self.power_dBm_plot_list = [], [], []

    def close(self):
        if self.fig is not None:
            plt.close(self.fig)
            self.fig = None
