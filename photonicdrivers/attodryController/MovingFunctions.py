import sys, os

real_cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(real_cwd, "AttocubeAPI"))

import AttocubeAPI.AMC as AMC
from time import sleep
import numpy as np


######################################################


piezo_controllers_params ={
    ### All values are expressed in nm
    'xmin' : None,
    'xmax' : None,
    'ymin' : None,
    'ymax' : None,
    'zmin' : 0.,
    'zmax' : 3350000.,
}

######################################################


def connect_AttoStages(ipaddress):
    return AMC.Device(ipaddress)



def move_stage(device, xpos, ypos, zpos, piezo_controllers_params = piezo_controllers_params, enable_Z_move = False, wait_while_moving = True, delta_t_wait = 0.1):
    if (piezo_controllers_params['xmin'] is not None and xpos < piezo_controllers_params['xmin']) or (piezo_controllers_params['xmax'] is not None and xpos > piezo_controllers_params['xmax']):
        raise ValueError('Inserted x position must be within the range ['+str(piezo_controllers_params['xmin'])+','+str(piezo_controllers_params['xmax'])+'] in nm')
    elif (piezo_controllers_params['ymin'] is not None and ypos < piezo_controllers_params['ymin']) or (piezo_controllers_params['ymax'] is not None and ypos > piezo_controllers_params['ymax']):
        raise ValueError('Inserted y position must be within the range ['+str(piezo_controllers_params['ymin'])+','+str(piezo_controllers_params['ymax'])+'] in nm')
    else:
        if enable_Z_move:
            if (piezo_controllers_params['zmin'] is not None and zpos < piezo_controllers_params['zmin']) or (piezo_controllers_params['zmax'] is not None and zpos > piezo_controllers_params['zmax']):
                raise ValueError('Inserted z position must be within the range ['+str(piezo_controllers_params['zmin'])+','+str(piezo_controllers_params['zmax'])+'] in nm')
            else:
                ref1, ref2, ref3, refpos1, refpos2, refpos3, pos1, pos2, pos3 = \
                        device.control.MultiAxisPositioning(1,
                                                            1, 
                                                            1, 
                                                            xpos, 
                                                            ypos, 
                                                            zpos)
        else: 
            ref1, ref2, ref3, refpos1, refpos2, refpos3, pos1, pos2, pos3 = \
            device.control.MultiAxisPositioning(1,
                                                1, 
                                                0, 
                                                xpos, 
                                                ypos, 
                                                zpos)
            
    if wait_while_moving:
        any_moving = True
        while any_moving:
            sleep(delta_t_wait)
            status = device.control.getStatusMovingAllAxes()
            any_moving = np.any(status)

    return ref1, ref2, ref3, refpos1, refpos2, refpos3, pos1, pos2, pos3



######################################################


if  __name__ == "__main__":
    from time import sleep
    import numpy as np

    device = connect_AttoStages('192.168.1.1')

    device.connect()




    all_pos = device.control.getPositionsAndVoltages()
    print(all_pos)
    pos_x = all_pos[0]
    pos_y = all_pos[1]
    pos_z = all_pos[2]

    # # #  to move up
    # new_pos_x = pos_x - 10000
    # new_pos_y = pos_y + 10000
    # new_pos_z = pos_z

    # print('Preparing to move stage')

    # print(new_pos_x, new_pos_y, new_pos_z)

    # asd = move_stage(device, new_pos_x, new_pos_y, new_pos_z, enable_Z_move = False)

    asd = move_stage(device, 2945004.854, 3434544.614, 3171067.087, enable_Z_move = False) #### good coupling for pCW structure
    # asd = move_stage(device, 3009894.661, 3440630.683, 3179695.125, enable_Z_move = False)



    ###################################################
    # new_pos_x = pos_x 
    # new_pos_y = pos_y 
    # new_pos_z = pos_z - 10000

    # asd = move_stage(device, pos_x, pos_y, new_pos_z, enable_Z_move = True) #### good coupling for pCW structure

    ###################################################
    # # print(asd)
    # print('Moving stage')

    # asd = move_stage(device, new_pos_x, new_pos_y, pos_z, enable_Z_move = False)

    # delta_t = 0.1
    # num_steps = 100

    # time = 0
    # for _ in range(num_steps):
    #     sleep(delta_t)
    #     time+=delta_t
    #     status = device.control.getStatusMovingAllAxes()
    #     print(status, np.any(status), '    t ', time)



    # print('Moving stage back')
    # print('Done')


    # asd = move_stage(device, pos_x, pos_y, pos_z, enable_Z_move = False)


    # time = 0
    # for _ in range(num_steps):
    #     sleep(delta_t)
    #     time+=delta_t
    #     status = device.control.getStatusMovingAllAxes()
    #     print(status, np.any(status), '    t ', time) 


    # device.close()