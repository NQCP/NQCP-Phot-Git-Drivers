from photonicdrivers.Attocube_ASC500.FilesFromAttocubeGit.lib import ASC500
from photonicdrivers.Attocube_ASC500.FilesFromAttocubeGit.lib.asc500_scanner import ASC500Scanner

import os
import time

# has to run on the attocube PC

binPath = "C:\\gitRepositories\\NQCP-Phot-Git-Drivers\\photonicdrivers\\Attocube_ASC500\\FilesFromAttocubeGit\\Installer\\ASC500CL-V2.7.13\\"
dllPath = "C:\\gitRepositories\\NQCP-Phot-Git-Drivers\\photonicdrivers\\Attocube_ASC500\\FilesFromAttocubeGit\\64bit_lib\\ASC500CL-LIB-WIN64-V2.7.13\\daisybase\\lib\\"
dll_loc = dllPath + 'daisybase.dll'

# print(os.path.isfile(dll_loc))

# asc500 = ASC500(binPath, dllPath)
asc500 = ASC500(binPath, dllPath)

print("Starting Server: ")
asc500.base.startServer()

print("Send Profile: ")
asc500.base.sendProfile(binPath + 'afm.ngp')


###############################################################

# # print("Set Data Enable: ")
# # asc500.data.setDataEnable(1)

# # print("Getting Scanner State: ")
# # print(asc500.scanner.getScannerState())

# # print("Getting Scanner absolute coor system: ")
# # print(asc500.scanner.getScannerAbsolutCoordSystem())


# # print("Getting Scanner Position: ")
# # print(asc500.scanner.getPositionsXYZRel())

# # time.sleep(3)

# # print("start scanner: ")
# # # print(asc500.scanner.startScanner())
# # asc500.scanner.startScanner()

# # print("Setting Scanner Position: ")
# # new_position_m = [-10.0e-6, 0.0] # array is in pm, which is then convereted to m
# # asc500.scanner.setPositionsXYRel(new_position_m)
# # time.sleep(0.5)

# # print("stop scanner: ")
# # print(asc500.scanner.stopScanner())

# print("Getting Scanner State: ")
# print(asc500.scanner.getScannerState())

# print("Getting Scanner Position: ")
# print(asc500.scanner.getPositionsXYZRel())

# # print("Disabling outputs") # SHOULD PERHAPS ALSO BE ENABLED??
# # print(asc500.base.setOutputs(0))

# # print("closing scanner: ")
# # asc500.scanner.closeScanner()

# print("Stopping Server: ")
# asc500.base.stopServer()



###############################################################



# Activates the outputs of the ASC500. This is mandatory if you want to use the analog outputs of the ASC500 (DAC1-6 and SCAN)
asc500.base.setOutputsWaiting(1)
# As this might take a little, we wait until the outputs are on:
while not asc500.base.getOutputStatus():
    print('Waiting for outputs to switch on')
    print(asc500.base.getOutputStatus())
    time.sleep(1)

# Set the scanner moving speed. Not mandatory.
asc500.scanner.setPositioningSpeed(1e-6)

#Print the new position:
print(asc500.scanner.getPositionsXYZRel())

# Set the scanner position (in m).
asc500.scanner.setPositionsXYRel([6e-6, 5e-6])

# Wait a short time for communication to take place
time.sleep(0.5)

# Wait while scanner is moving.
print('Scanner State: {}'.format(asc500.scanner.getScannerStateMoving()))
# while asc500.scanner.getScannerStateMoving():
count =1
while count < 10:
    print("Scanner is still moving")
    print('Scanner State: {}'.format(asc500.scanner.getScannerStateMoving()))
    time.sleep(0.5)
    count += 1

#Print the new position:
print(asc500.scanner.getPositionsXYZRel())


#%% Close ASC500
#-----------------------------------------------------------------------
# Switching off the outputs will lead to the scanners falling back to [0, 0]
asc500.base.setOutputsWaiting(0)
while asc500.base.getOutputStatus():
    print('Waiting for outputs to switch off')
    time.sleep(1)

# stops the server (not mandatory)
asc500.base.stopServer()


print("done")



