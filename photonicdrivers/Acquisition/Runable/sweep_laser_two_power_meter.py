## Python sample script to communicate with RLS Picus laser
import datetime
import tkinter as tk

import h5py
import numpy as np
import pyvisa
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from photonicdrivers.Instruments.Implementations.Lasers.Toptica_CTL950.Toptica_CTL950 import Toptica_CTL950
from photonicdrivers.Instruments.Implementations.Power_Meters.Thorlabs_PM100.Thorlabs_PM100U import Thorlabs_PM100U


def add_dict_to_h5(dict, group):
    for key, element in dict.items():
        group.attrs[key] = element


instrument_list = []

resource_manager = pyvisa.ResourceManager()
print(resource_manager.list_resources())

power_meter_input = Thorlabs_PM100U(resource_manager, 'USB0::0x1313::0x8078::P0041989::0::INSTR',
                                    "C:\Repositories\PhotonicDrivers\photonicdrivers\Instruments\Settings\Thorlabs_PM100U\Thorlabs_PM100U_Settings_1.txt")
power_meter_output = Thorlabs_PM100U(resource_manager, 'USB0::0x1313::0x8078::P0045344::0::INSTR',
                                    "C:\Repositories\PhotonicDrivers\photonicdrivers\Instruments/Settings/Thorlabs_PM100U/Thorlabs_PM100U_Settings_1.txt")
power_meter_input.connect()
power_meter_input.set_detector_wavelength(930)
power_meter_output.connect()
power_meter_output.set_detector_wavelength(930)
instrument_list.append(power_meter_input)
instrument_list.append(power_meter_output)

wavelength_list_loop = np.arange(910, 980 + 0.1, 0.1)

toptica_laser = Toptica_CTL950(IP_address='10.209.67.103',
                               settings_path="C:/Users/NQCPQP/PycharmProjects/LabController/Code/Settings"
                                             "/Toptica_CTL950/Toptica_CTL950_Settings.txt")
toptica_laser.connect()
toptica_laser.enable_emission()

toptica_laser.set_power_stabilization(True)
toptica_laser.set_wavelength(910)
toptica_laser.set_power(10)
toptica_laser.print_emission_status()

instrument_list.append(toptica_laser)

transmission_power_list = []
input_power_list = []
wavelength_list = []

beginning_time = datetime.datetime.now()

# Create a Tkinter window
root = tk.Tk()
root.title("Matplotlib Plot in Tkinter")

# Create an empty plot
fig, ax = plt.subplots()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Matplotlib Plot in Tkinter')

# Set up the axes limits
ax.set_xlim(910, 980)
#ax.set_ylim(0, 20)


# Initialize an empty line object
line_input, = plt.plot([], [], 'bo-')
line_output, = plt.plot([], [], 'bo-')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

for wavelength in wavelength_list_loop:
    toptica_laser.set_wavelength(wavelength)
    plt.pause(0.1)
    transmission_power_list.append(power_meter_output.get_detector_power())
    input_power_list.append(power_meter_input.get_detector_power())
    wavelength_list.append(wavelength)

    line_input.set_xdata(wavelength_list)
    line_input.set_ydata(input_power_list)

    line_output.set_xdata(wavelength_list)
    line_output.set_ydata(transmission_power_list)

    # Update y-axis limits to match the min and max of y-data
    ax.set_ylim(0, np.max(transmission_power_list))
    canvas.draw()
    print(wavelength)

toptica_laser.set_wavelength(930)

root.mainloop()

subject_id = "MWresonator_030112023"
measurement_type = "transmission"
setup_id = "room_temp_KK4_v1.00.00"
device_id = "calibration"
#filename = beginning_time.strftime("%Y-%m-%d_%H-%M-%S") + "_setup_id_" + setup_id + "_subject_id_" + subject_id + "_device_id_" + device_id
filename = beginning_time.strftime("%Y-%m-%d_%H-%M-%S") + "_subject_id_" + subject_id + "_device_id_" + device_id + "_setup_id_" + setup_id + "_measurement_type_" + measurement_type

with h5py.File("N:/SCI-NBI-NQCP/Phot/rawData/A000000A00_MWresonators_NQCP_03112023/Transmission/27_05_2024/calibration/" + filename + ".hdf5", 'w') as f:
    # Create a group and add metadata
    meta_data_group = f.create_group('meta_data')
    meta_data_group.attrs['author'] = "Magnus_Linnet_Madsen"
    meta_data_group.attrs['time_stamp'] = beginning_time.strftime("%Y-%m-%d_%H-%M-%S")
    meta_data_group.attrs['measurement_type'] = measurement_type
    meta_data_group.attrs['subject_id'] = subject_id
    meta_data_group.attrs['device_id'] = device_id
    meta_data_group.attrs['setup_id'] = setup_id

    # Create a dataset and add metadata
    data_group = f.create_group('data')

    data_input_power = data_group.create_dataset('input_power', data=input_power_list)
    data_input_power.attrs['units'] = "W"

    data_transmission_power = data_group.create_dataset('transmission_power', data=transmission_power_list)
    data_transmission_power.attrs['units'] = "W"

    data_wavelength = data_group.create_dataset('wavelength', data=wavelength_list)
    data_wavelength.attrs['units'] = "nm"

    instruments_group = f.create_group('instruments')

    for instrument in instrument_list:
        instrument_group = instruments_group.create_group(instrument.get_id())
        instrument_settings = instrument.get_settings()
        for key in instrument_settings:
            print(key + ":" + str(instrument_settings[key]))
            instrument_group.create_dataset(key, data=instrument_settings[key])

for instrument in instrument_list:
    instrument.save_settings()
    instrument.disconnect()
