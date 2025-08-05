### Load libraries
import sys
import time

from photonicdrivers.Spectrographs.Andor_Kymera import Andor_Kymera
from photonicdrivers.Spectrographs.Andor_Newton import Andor_Newton
from controllers.Spectrograph_Calibration.spectrograph_calibration import Spectograph_Calibration


import numpy as np
import matplotlib.pyplot as plt

### Initialize Camera and Spectrograph ###

spc=Andor_Kymera()
cam=Andor_Newton()

#spectograph
spc.connect()

#connect
cam.connect()

# ### SET READOUT MODE ###
cam.set_read_mode(0)    
cam.set_image(1,1,1,cam.num_pixel_x,1,cam.num_pixel_y)


## Set CameraTemperature ###
cam.cooler_on()
cam.set_temperature(-60)

#we wait for the camera to cool down
temperature = cam.get_temperature()
while temperature >= -55:
    time.sleep(10)
    temperature = cam.get_temperature()
    print("T=", temperature)

## Set the spectrograph for a region we have a calibration for
spc.set_grating(1)
spc.set_center_wavelength(1330)


# ### SET ACQUISITION MODE ###
cam.set_camera_acquisition(1)

cam.set_exposure_time_s(1)



num_cams=cam.get_available_cameras()
print('Num cameras:', num_cams)  

serial = cam.get_serial_number()
print("Camera serial ", serial)


# print("Get Grating Info", spc.GetGratingInfo(device=0, Grating=1, maxBlazeStrLen= 12000))
# print("Spectrograph Center Wavelength", spc.GetWavelength(device=0))
# print("Camera Capabilities: ", cam.GetCapabilities())
# print("Available Cameras: ", cam.GetAvailableCameras())
# print("Current Camera: ", cam.GetCurrentCamera())
# print(spc.GetWavelengthLimits(device=0, Grating=1))


# ### GET IMAGE ###
image = cam.get_image()
counts = cam.get_trace()


#Defining manual calibration dicts assuming linearity. Just forrr a rough conversion to wvl
CalibDict1330 = Spectograph_Calibration([0,0,512], [1206.49,1206.49,1453.62], 1, 1330, 1)
CalibDict1220 = Spectograph_Calibration([0,0,512], [1096.17,1096.17,1343.96], 1, 1220, 1)


#we intepolate based on our calibration class
CalibDict1330.fit(1)
wvl_list=CalibDict1330.interpolate_from_fit(cam.num_pixel_x)

plt.figure()
plt.plot(wvl_list,counts)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Counts")
plt.show()

cam.disconnect()
