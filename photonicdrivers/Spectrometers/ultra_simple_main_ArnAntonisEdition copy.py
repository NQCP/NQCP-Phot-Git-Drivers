### Load libraries
import sys
import time

sys.path.append(r"C:\\Program Files\\Andor SDK\\Python\\pyAndorSDK2")
sys.path.append(r"C:\\Program Files\\Andor SDK\\Python\\pyAndorSpectrograph")

from pyAndorSDK2 import atmcd, atmcd_codes, atmcd_errors
from pyAndorSpectrograph.spectrograph import ATSpectrograph
from controllers.Spectrograph_Calibration.spectrograph_calibration import Spectograph_Calibration

codes = atmcd_codes

### Initialize Camera and Spectrograph ###

#spectograph
spc = ATSpectrograph(userPath="C:\\Program Files\\Andor SDK\\Python\\pyAndorSpectrograph\\pyAndorSpectrograph\\libs\\Windows\\64")

shm = spc.Initialize("")
print(shm)
if shm == 20202:
    print('Spectrograph Initialization Successful')
elif spc.GetNumberGratings(device=0)[1]!=0:
    print('Spectrograph Already Initialized')
else:
    print('ERROR WHEN INITIALIZING SPECTROGRAPH')

#Our connection issues stem from these lines of code. When we instantiate a new atmcd-object we lose the connection with the camera
# this is what forces us to connect and disconnect. The spectograph seems more stable to re-instantiation, but it has been observed to hang in the same way some times.
cam = atmcd(userPath="C:\\Program Files\\Andor SDK\\Python\\pyAndorSDK2\\pyAndorSDK2\\libs\\Windows\\64")

ret = cam.Initialize("")
# Check whether we have connection, using serial number to verify that we can get non-zero results.
if ret == 20002:
    print('Camera Initialization Successful')
elif ret == 20992 and cam.GetCameraSerialNumber()[0]==20002:
    print('Camera Already Initialized')
else:
    print('ERROR WHEN INITIALIZING CAMERA')


# #Set our camera to the 0th
# cam_ix = 0
# ret, handle = cam.GetCameraHandle(cam_ix)
# print(cam.handle_return(ret))
# ret = cam.SetCurrentCamera(handle)
# print(cam.handle_return(ret))
#works

# ### SET READOUT MODE ###
ret = cam.SetReadMode(4)
print(cam.handle_return(ret))

_,num_pixel_x,num_pixel_y=cam.GetDetector()        

print('get detector:',cam.GetDetector())
ret = cam.SetImage(1,1,1,num_pixel_x,1,num_pixel_y)
print(cam.handle_return(ret))


## Set CameraTemperature ###
set_temp=-2


ret = cam.CoolerON()
ret = cam.SetTemperature(set_temp)
ret, temperature = cam.GetTemperature()

#we wait for the camera to cool down
while temperature >= set_temp + 5:
    time.sleep(2)
    ret, temperature = cam.GetTemperature()
    print("T=", temperature)

#If camera is already cool, the script gets stuck in a loop in the 'while' above, so, maybe skip it    


## Set Spectrograph correctly
set_wvl=1350
set_grating=1

spc.SetGrating(device=0, grating=set_grating)
spc.SetWavelength(device=0, wavelength=set_wvl)

#seems to be giving gating limits and not limits of current position
spc.GetWavelengthLimits(device=0, Grating=set_grating)


# ### SET ACQUISITION MODE ###
ret = cam.SetAcquisitionMode(codes.Acquisition_Mode.SINGLE_SCAN)
print(ret)
exposure_time = 1
ret = cam.SetExposureTime(exposure_time)
print(ret)
ret = cam.PrepareAcquisition()
print(ret)
ret = cam.StartAcquisition()
print(ret)
ret = cam.WaitForAcquisition()
print(ret)


message, num_cams = cam.GetAvailableCameras()
print('Num cameras:', num_cams, ',   message:', message)  

# cameraHandle
serial = cam.GetCameraSerialNumber()
print("Camera serial ", serial)

# ret = spc.GetNumberDevices()
# print("Num devices ", ret)


# ret = spc.GetNumberGratings(device=0)
# print("Num gratings ", ret)

# #getTemp
# ret, temperature = cam.GetTemperature()
# print("T=", temperature)




#does not seem to work, probably because the spectrograph doesn't know about the camera
# print("Get Number Pixel", spc.GetNumberPixels(device=0))
# print(spc.GetCalibration(device=0, NumberPixels=0))
# print(spc.GetPixelCalibrationCoefficients(device=0))


print("Get Grating Info", spc.GetGratingInfo(device=0, Grating=1, maxBlazeStrLen= 12000))
print("Spectrograph Center Wavelength", spc.GetWavelength(device=0))
print("Camera Capabilities: ", cam.GetCapabilities())
print("Available Cameras: ", cam.GetAvailableCameras())
print("Current Camera: ", cam.GetCurrentCamera())
print(spc.GetWavelengthLimits(device=0, Grating=1))




# ### GET IMAGE ###
(ret, arr, validfirst, validlast) = cam.GetImages16(1,1, size=num_pixel_x*num_pixel_y)

print('Well done!')

import numpy as np
import matplotlib.pyplot as plt

#defining manual calibration dicts assuming linearity, Marcus-style
CalibDict1330 = Spectograph_Calibration([0,0,num_pixel_x], [1206.49,1206.49,1453.62], 1, 1330, 1)
CalibDict1220 = Spectograph_Calibration([0,0,num_pixel_x], [1096.17,1096.17,1343.96], 1, 1220, 1)

# # Generate a sample 1D array with length 200*1600 (for demonstration purposes)
length = 1 * 512
array_1d = arr  # A 1D array from 0 to 255


# # Reshape the 1D array to a 2D array with shape (200, 1600)
image = np.flip(np.flip(np.reshape(array_1d, (num_pixel_y, num_pixel_x)), axis=1),axis=0)
collapse = np.sum(image, axis=0)

# # Plot the 2D array as an image
# plt.imshow(image, cmap='gray', aspect='auto')
# plt.colorbar()  # Add a colorbar to show the mapping of values to colors
# plt.title("2D Image Representation of 1D Array")






#we intepolate based on our calibration class
CalibDict1330.fit(1)
wvl_list=CalibDict1330.interpolate_from_fit(num_pixel_x)

plt.figure()
plt.plot(wvl_list,collapse)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Counts")
plt.show()

spec=np.array([wvl_list,collapse])

cam.AbortAcquisition()
cam.SetAdvancedTriggerModeState(0)

cam.CoolerOFF()
ret, temperature = cam.GetTemperature()
while temperature < -20:
    time.sleep(10)
    ret, temperature = cam.GetTemperature()
    print("T=", temperature)

cam.ShutDown()

spc.Close()