
import os
import subprocess

FNULL = open(os.devnull, 'w')  # use this if you want to suppress output to stdout from the subprocess
path_data = ("N:/SCI-NBI-NQCP/Phot/rawData/microwave_resonator"
             "/MWresonators_NQCP_ResOnly_NoCapacitor_18032024_A001004A02/Photos/TrainingData/Resonator/26042024/")
path_executable = "C:/Users/NQCPQP/Repositories/opencv/build/x64/vc15/bin/opencv_createsamples.exe"
args = (path_executable +
        " -info" + path_data + "positive.txt"
        " -w 24"
        " -h 24"
        " -num 1000"
        " -vec " + path_data + "positive.vec")
subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False
)