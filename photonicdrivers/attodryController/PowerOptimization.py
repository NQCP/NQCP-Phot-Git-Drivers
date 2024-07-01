import sys, os
import numpy as np
from time import sleep

real_cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(real_cwd)
sys.path.append(os.path.join(real_cwd, "AttocubeAPI"))
from MovingFunctions import connect_AttoStages, move_stage


from RouteFunctions import spiral_path
# from photonicdrivers.Instruments.Implementations.Power_Meters.Thorlabs_PM100U.Thorlabs_PM100U import Thorlabs_PM100U



####################################


def find_coupling_spiral(stages_device, powermeter, max_dist_nm = 10000, step_size_nm = 500, stop_at_pow_threshold = False, power_threshold_mw = 5.E-6 ):

    all_pos = stages_device.control.getPositionsAndVoltages()



    # print(all_pos)
    x0 = all_pos[0]
    y0 = all_pos[1]
    z0 = all_pos[2]

    xy_pos_list = spiral_path(x0, y0, step_size_nm, max_dist_nm)
    xy_pos_given = []
    num_steps = len(xy_pos_list)

    all_powers = []

    best_pow = 0
    best_x = x0
    best_y = y0

    xy_pos_list_real = []

    found_threshold = False

    for step_ix, xy in enumerate(xy_pos_list):
        x = xy[0]
        y = xy[1]
        xy_pos_given.append([x, y])
        # print('Moving to (x,y):', x, y)
        move_stage(stages_device, x, y, z0, enable_Z_move = False, wait_while_moving=True)
        sleep(0.1)
        all_pos = stages_device.control.getPositionsAndVoltages()
        real_x = all_pos[0]
        real_y = all_pos[1]
        xy_pos_list_real.append([real_x, real_y])
        pow = powermeter.measure_average()
        # print('  ', pow)
        all_powers.append(pow)

        if pow > best_pow:
            best_pow = pow
            best_x = real_x
            best_y = real_y

        if stop_at_pow_threshold and (best_pow > power_threshold_mw):
            # print('Found power above threshold: rough coupling achieved')
            found_threshold = True
            break


    # print(all_powers)

    # print(best_pow, best_x, best_y)
    if not found_threshold:
        move_stage(stages_device, best_x, best_y, z0, enable_Z_move = False, wait_while_moving=True)
        sleep(1)

    pow = powermeter.measure_average()
    # print(pow, best_pow)

    # powermeter.close()

    return best_x, best_y, z0, best_pow, pow, np.array(xy_pos_given), np.array(xy_pos_list_real), np.array(all_powers), x0, y0


def fine_opt_function(stages_device, powermeter, fine_step_nm = 200, max_num_steps = 100):


    all_pos = stages_device.control.getPositionsAndVoltages()

    x0 = all_pos[0]
    y0 = all_pos[1]
    z0 = all_pos[2]

    best_x = x0
    best_y = y0

    x_dir = np.random.choice([1, -1]) 
    y_dir = np.random.choice([1, -1]) 

    x_just_changed = False
    y_just_changed = False
    x_converged = False
    y_converged = False
    converged = False

    step_ix = 0    

    sleep(0.1)

    pow = powermeter.measure_average()
    best_pow = pow

    xy_list = [[x0, y0]]
    all_powers = [pow]

    x = x0
    y = y0

    while not converged and step_ix < max_num_steps:
        axis_to_move = np.random.choice([0, 1])
        if axis_to_move==0:   # will move along x
            x = best_x + x_dir * fine_step_nm
            y = best_y
        else:                 # will move along y
            x = best_x 
            y = best_y + y_dir * fine_step_nm
        print('Moving to (x,y):', x, y)
        move_stage(stages_device, x, y, z0, enable_Z_move = False, wait_while_moving=True)
        sleep(0.1)
        all_pos = stages_device.control.getPositionsAndVoltages()
        real_x = all_pos[0]
        real_y = all_pos[1]
        pow = powermeter.measure_average()
        print('  ', pow)
        xy_list.append([real_x, real_y])
        all_powers.append(pow)

        if pow > best_pow:
            best_pow = pow
            # best_x = real_x
            # best_y = real_y
            best_x = x
            best_y = y
            x_just_changed = False
            x_converged = False
            y_just_changed = False
            y_converged = False
        else: 
            if axis_to_move==0:
                x_dir = -1 * x_dir
                if x_just_changed:
                    x_converged = True
                else:
                    x_just_changed = True
            else:
                y_dir = -1 * y_dir
                if y_just_changed:
                    y_converged = True
                else:
                    y_just_changed = True

        if x_converged and y_converged:
            converged = True
        step_ix += 1

    move_stage(stages_device, best_x, best_y, z0, enable_Z_move = False)
    sleep(1)
    pow = powermeter.measure_average()
    print(pow, best_pow)

    # powermeter.close()

    return best_x, best_y, z0, best_pow, pow, np.array(xy_list), np.array(all_powers), x0, y0

def optimize_z_coupling(stages_device, powermeter, max_dist_nm = 5000, step_size_nm = 1000, stop_at_pow_threshold = False, power_threshold_mw = 5.E-6 ):

    print('Starting Z coupling optimization')

    all_pos = stages_device.control.getPositionsAndVoltages()

    # print(all_pos)
    x0 = all_pos[0]
    y0 = all_pos[1]
    z0 = all_pos[2]

    z_pos_list = np.arange(z0 - max_dist_nm, z0 +max_dist_nm, step_size_nm)
    z_pos_given = []
    num_steps = len(z_pos_list)

    all_powers = []

    best_pow = 0
    best_z = z0

    z_pos_list_real = []

    found_threshold = False

    for step_ix, z in enumerate(z_pos_list):
        z_pos_given.append(z)
        print('Moving to z:', z)
        move_stage(stages_device, x0, y0, z, enable_Z_move = True, wait_while_moving=True)
        sleep(0.1)
        all_pos = stages_device.control.getPositionsAndVoltages()
        real_x = all_pos[0]
        real_y = all_pos[1]
        real_z = all_pos[1]
        z_pos_list_real.append(real_z)
        pow = powermeter.measure_average()
        print('  ', pow)
        all_powers.append(pow)

        if pow > best_pow:
            best_pow = pow
            best_z = real_z

        if stop_at_pow_threshold and (best_pow > power_threshold_mw):
            # print('Found power above threshold: rough coupling achieved')
            found_threshold = True
            break


    # print(all_powers)

    # print(best_pow, best_x, best_y)
    if not found_threshold:
        move_stage(stages_device, x0, y0, z0, enable_Z_move = True, wait_while_moving=True)
        sleep(1)


    print(all_powers)

    print(best_pow, best_z)

    pow = powermeter.measure_average()
    print(pow, best_pow)

    # powermeter.close()

    return x0, y0, best_z, best_pow, pow, np.array(z_pos_given), np.array(z_pos_list_real), np.array(all_powers)


def full_find_waveguide_coupling(stages_device, powermeter, max_dist_rough_nm = 20000, step_size_rough_nm = 2000, threshold_pow_rough_mw = 2.E-6, max_dist_fine_nm = 5000, max_dist_fine_fine_nm = 3000, step_size_fine_nm = 1000, acceptable_maxpow_ratio_final = 0.9):
    best_x, best_y, pos_z, best_pow, pow, xy_pos_list, xy_pos_list_real, all_powers, x0, y0 = find_coupling_spiral(stages_device, powermeter, max_dist_nm = max_dist_rough_nm, step_size_nm = step_size_rough_nm, stop_at_pow_threshold = True, power_threshold_mw = threshold_pow_rough_mw)
    best_x_fine2, best_y_fine2, pos_z2, best_pow_fine2, pow_fine2, xy_list_fine2, xy_pos_list_real_fine2, all_powers_fine2, x0new2, y0new2 = find_coupling_spiral(stages_device, powermeter, max_dist_nm = max_dist_fine_nm, step_size_nm = step_size_fine_nm, stop_at_pow_threshold = False)
    
    threshold_pow_max = best_pow_fine2 * acceptable_maxpow_ratio_final
    
    best_x_fine3, best_y_fine3, pos_z3, best_pow_fine3, pow_fine3, xy_list_fine3, xy_pos_list_real_fine3, all_powers_fine3, x0new3, y0new3 = find_coupling_spiral(stages_device, powermeter, max_dist_nm = max_dist_fine_fine_nm, step_size_nm = step_size_fine_nm, stop_at_pow_threshold = True, power_threshold_mw = threshold_pow_max)

    all_x = np.concatenate([xy_pos_list_real[:,0], xy_pos_list_real_fine2[:,0], xy_pos_list_real_fine3[:,0]]) - x0
    all_y = np.concatenate([xy_pos_list_real[:,1], xy_pos_list_real_fine2[:,1], xy_pos_list_real_fine3[:,1]]) - y0
    all_pow = np.concatenate([all_powers, all_powers_fine2, all_powers_fine3])

    # x_afterz, y_afterz, best_z, best_pow_z, pow, z_list, z_list_real, all_powers_z = optimize_z_coupling(stages_device, powermeter, max_dist_nm = 5000, step_size_nm = 1000)

    # threshold_pow_max = best_z * acceptable_maxpow_ratio_final

    # x_afterz1, y_afterz1, best_z1, best_pow_z1, pow1, z_list1, z_list_real1, all_powers_z1 = optimize_z_coupling(stages_device, powermeter, max_dist_nm = 5000, step_size_nm = 1000, stop_at_pow_threshold = True, power_threshold_mw = threshold_pow_max)


    sleep(1)
    all_pos = stages_device.control.getPositionsAndVoltages()
    final_x = all_pos[0]
    final_y = all_pos[1]
    final_z = all_pos[2]
    final_pow = powermeter.measure_average()

    return final_x, final_y, final_z, final_pow, all_x, all_y, all_pow

#######################################




if  __name__ == "__main__":
    from Powermeter import Powermeter
    from MovingFunctions import connect_AttoStages, move_stage

    import matplotlib.pyplot as plt
    from time import time

    stages_device = connect_AttoStages('192.168.1.1')

    stages_device.connect()

    powermeter = Powermeter('PM100D')


    ############################ define coupling parameters

    max_dist_rough_nm = 20000
    step_size_rough_nm = 2000
    threshold_pow_rough_mw = 2.E-6

    max_dist_fine_nm = 5000
    step_size_fine_nm = 1000

    max_dist_fine_fine_nm = 3000
    acceptable_maxpow_ratio_final = 0.9



    ############################

    print('Starting power optimization')

    start_time = time()




    final_x, final_y, final_z, final_pow, all_x, all_y, all_pow = full_find_waveguide_coupling(stages_device, powermeter, 
                                                                                        max_dist_rough_nm = max_dist_rough_nm, 
                                                                                        step_size_rough_nm = step_size_rough_nm, 
                                                                                        threshold_pow_rough_mw = threshold_pow_rough_mw, 
                                                                                        max_dist_fine_nm = max_dist_fine_nm, 
                                                                                        max_dist_fine_fine_nm = max_dist_fine_fine_nm, 
                                                                                        step_size_fine_nm = step_size_fine_nm)

    # x0, y0, best_z, pow, z_pos_given, z_pos_list_real, all_powers, x0, y0 = optimize_z_coupling(stages_device, powermeter, max_dist_nm = 5000, step_size_nm = 1000)


    end_time = time()

    powermeter.close()

    
    print('Final x, y, z :', final_x, ',', final_y, ',', final_z)
    print('Optimized power:', final_pow)
    print('Time it took (s):', end_time - start_time)

    plt.scatter(all_x, all_y, c = all_pow, cmap = 'magma')
    plt.xlabel(r'$\Delta x$ (nm)')
    plt.ylabel(r'$\Delta y$ (nm)')
    plt.colorbar(label = 'Optical Power (mW)')
    plt.show()




    ##########
    