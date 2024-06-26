import sys, os
import numpy as np
from time import sleep

real_cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(real_cwd)
sys.path.append(os.path.join(real_cwd, "AttocubeAPI"))

from Powermeter import Powermeter
from MovingFunctions import connect_AttoStages, move_stage
# from photonicdrivers.Instruments.Implementations.Power_Meters.Thorlabs_PM100U.Thorlabs_PM100U import Thorlabs_PM100U

if  __name__ == "__main__":
    device = connect_AttoStages('192.168.1.1')

    device.connect()

    all_pos = device.control.getPositionsAndVoltages()

    powermeter = Powermeter('PM100D')


    num_steps = 10

    step_size = 500 #in nm


    print(all_pos)
    pos_x = all_pos[0]
    pos_y = all_pos[1]
    pos_z = all_pos[2]

    dist = step_size * num_steps

    start_x = pos_x - dist/2.
    end_x = pos_x + dist/2.  
    x_pos_list = np.linspace(start_x, end_x, num_steps)
    print(x_pos_list)


    start_y = pos_y - dist/2.
    end_y = pos_y + dist/2.   
    y_pos_list = np.linspace(start_y, end_y, num_steps)
    print(y_pos_list)


    all_powers = np.zeros((num_steps, num_steps))

    best_pow = 0
    best_x = pos_x
    best_y = pos_y

    for x_ix, x in enumerate(x_pos_list):
        for y_ix, y in enumerate(y_pos_list):
            print('Moving to (x,y):', x, y)
            asd = move_stage(device, x, y, pos_z, enable_Z_move = False)
            sleep(1)
            pow = powermeter.measure()
            print('  ', pow)
            all_powers[x_ix, y_ix] = pow

            if pow > best_pow:
                best_pow = pow
                best_x = x
                best_y = y


print(all_powers)

print(best_pow, best_x, best_y)
asd = move_stage(device, best_x, best_y, pos_z, enable_Z_move = False)



#     # powermeter.close()
