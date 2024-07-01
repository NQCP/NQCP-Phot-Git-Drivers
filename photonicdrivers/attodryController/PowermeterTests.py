import sys, os

real_cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(real_cwd)
sys.path.append(os.path.join(real_cwd, "AttocubeAPI"))

from Powermeter import Powermeter
# from photonicdrivers.Instruments.Implementations.Power_Meters.Thorlabs_PM100U.Thorlabs_PM100U import Thorlabs_PM100U

if  __name__ == "__main__":
    from time import sleep

    powermeter = Powermeter('PM100D')

    sleep(0.1)


    pow = powermeter.measure()
    print(pow)

    powermeter.close()
