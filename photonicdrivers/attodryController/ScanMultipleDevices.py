import sys, os
import numpy as np
from time import sleep

real_cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(real_cwd)
sys.path.append(os.path.join(real_cwd, "AttocubeAPI"))

from MovingFunctions import connect_AttoStages, move_stage
from PowerOptimization import full_find_waveguide_coupling
from PathFinder import find_route


def dev_coords_to_ix_on_grid(coords, num_x_devs, num_y_devs):
    if coords[0]< 0 or coords[0]>=num_x_devs:
        raise ValueError('Invalid x coordinate')
    elif coords[1]< 0 or coords[1]>=num_y_devs:
        raise ValueError('Invalid y coordinate')
    else:
        return coords[1]*num_x_devs + coords[0]

def dev_ix_to_coords_on_grid(ix, num_x_devs, num_y_devs):
    if ix >= num_x_devs*num_y_devs:
        raise ValueError('Invalid index')
    else:
        return (int(ix / num_y_devs), ix % num_y_devs)


if  __name__ == "__main__":
    import matplotlib.pyplot as plt
    from time import time
    from Powermeter import Powermeter
    from MovingFunctions import connect_AttoStages, move_stage

    stages_device = connect_AttoStages('192.168.1.1')

    stages_device.connect()

    powermeter = Powermeter('PM100D')


    ############################ define devices lattice

    x_distance_um = 50   # in um
    y_distance_um = 120   # in um

    num_devices_x = 8
    num_devices_y = 4

    starting_device_coords = (4, 3)   



    # #### simple test with just 2 devices
    # num_devices_x = 2
    # num_devices_y = 2
    # starting_device_coords = (1, 1)   

    ############################ define coupling parameters

    max_dist_rough_nm = 20000
    step_size_rough_nm = 1500
    threshold_pow_rough_mw = 2.E-6

    max_dist_fine_nm = 5000
    step_size_fine_nm = 1000

    max_dist_fine_fine_nm = 3000
    acceptable_maxpow_ratio_final = 0.8


    ############################  Initialize devices grid and coupling route

    x_distance_nm = x_distance_um * 1000
    y_distance_nm = y_distance_um * 1000
    starting_device_ix = dev_coords_to_ix_on_grid(starting_device_coords, num_devices_x, num_devices_y)
    print(starting_device_ix)

    xy_positions = []
    for y_ix in range(num_devices_y):
        for x_ix in range(num_devices_x):       
            x_pos = x_distance_nm * x_ix
            y_pos = y_distance_nm * y_ix
            xy_positions.append([x_pos, y_pos])
    xy_positions = np.array(xy_positions)
    num_devices = len(xy_positions)

    xy_positions_ordered, indexes_points, total_dist = find_route(xy_positions, start_point_ix = starting_device_ix, dist_type = 'Euclidean')

    xy_change_each_step = np.diff(xy_positions_ordered, n=1, axis=0, prepend=np.array([xy_positions_ordered[0]]))
    print(xy_change_each_step)
    ############################  Start scan

    all_pos0 = stages_device.control.getPositionsAndVoltages()
    x0 = all_pos0[0]
    y0 = all_pos0[1]
    z0 = all_pos0[2]
    
    current_x = x0
    current_y = y0

    print('----  Starting scan of devices ----\n\n')
    start_time = time()

    found_devices_positions = []
    found_devices_powers = []


    for device_ix in range(num_devices):
        print('\nMoving to new device',device_ix, ': ', dev_ix_to_coords_on_grid(device_ix, num_devices_x, num_devices_y))
        xy_move =  xy_change_each_step[device_ix]
        print('    xy_move:', xy_move)
        new_x = current_x + xy_move[0]
        new_y = current_y + xy_move[1]
        
        print('New device position: ', new_x,',', new_y)

        move_stage(stages_device, new_x, new_y, z0, enable_Z_move = False, wait_while_moving=True)

        # sleep(2)

        ####### power optimization goes here
        final_x, final_y, final_z, final_pow, all_x, all_y, all_pow = full_find_waveguide_coupling(stages_device, powermeter, 
                                                                                                max_dist_rough_nm = max_dist_rough_nm, 
                                                                                                step_size_rough_nm = step_size_rough_nm, 
                                                                                                threshold_pow_rough_mw = threshold_pow_rough_mw, 
                                                                                                max_dist_fine_nm = max_dist_fine_nm, 
                                                                                                max_dist_fine_fine_nm = max_dist_fine_fine_nm, 
                                                                                                step_size_fine_nm = step_size_fine_nm)

        all_pos = stages_device.control.getPositionsAndVoltages()
        current_x = all_pos[0]
        current_y = all_pos[1]
        current_z = all_pos[1]

        found_devices_positions.append([current_x, current_y, current_z])


        # sleep(1)

        pow = powermeter.measure_average()
        found_devices_powers.append(pow)
        print('   measured power (mW):', pow)

        ####### characteristion functions go here

    found_devices_positions = np.array(found_devices_positions)
    found_devices_powers = np.array(found_devices_powers)
    ############################  Go back to original position


    sleep(2)

    print('\nMoving back to starting position')

    move_stage(stages_device, x0, y0, z0, enable_Z_move = True, wait_while_moving=True)

    sleep(2)

    ############################ 

    end_time = time()


    print('\nTime it took for the scan (s)', end_time-start_time)


    # print('\n\nFound_devices_powers:')
    # print(found_devices_powers)

    # print('\n\found_devices_positions:')
    # print(found_devices_positions)


    fig = plt.figure()
    plt.scatter(found_devices_positions[:,0], found_devices_positions[:,1], c = found_devices_powers, cmap = 'magma')
    plt.xlabel(r'$\Delta x$ (nm)')
    plt.ylabel(r'$\Delta y$ (nm)')
    plt.colorbar(label = 'Optical Power (mW)')
    plt.show()

    powermeter.close()