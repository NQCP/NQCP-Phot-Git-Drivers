import os
import subprocess

FNULL = open(os.devnull, 'w') #use this if you want to suppress output to stdout from the subprocess
args = ("C:/Users/NQCPQP/Repositories/opencv/build/x64/vc15/bin/opencv_annotation.exe "
        "--annotations=N:/SCI-NBI-NQCP/Phot/rawData/microwave_resonator"
        "/MWresonators_NQCP_ResOnly_NoCapacitor_18032024_A001004A02/Photos/TrainingData/Resonator/26042024/positive"
        ".txt --images=N:/SCI-NBI-NQCP/Phot/rawData/microwave_resonator"
        "/MWresonators_NQCP_ResOnly_NoCapacitor_18032024_A001004A02/Photos/TrainingData/Resonator/26042024/positive/")
subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

# You click once to set the upper left corner, then again to set the lower right corner.
# Press 'c' to confirm.
# Or 'd' to undo the previous confirmation.
# When done, click 'n' to move to the next image.
# Press 'esc' to exit.
# Will exit automatically when you've annotated all of the images
