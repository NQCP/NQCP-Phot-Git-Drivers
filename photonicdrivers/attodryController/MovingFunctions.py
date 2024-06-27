import sys, os

real_cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(real_cwd, "AttocubeAPI"))

import AttocubeAPI.AMC as AMC


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



def move_stage(device, xpos, ypos, zpos, piezo_controllers_params = piezo_controllers_params, enable_Z_move = False):
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

    return ref1, ref2, ref3, refpos1, refpos2, refpos3, pos1, pos2, pos3



######################################################


if  __name__ == "__main__":
    from time import sleep

    device = connect_AttoStages('192.168.1.1')

    device.connect()

    all_pos = device.control.getPositionsAndVoltages()
    print(all_pos)
    pos_x = all_pos[0]
    pos_y = all_pos[1]
    pos_z = all_pos[2]

    # sleep(1)

    # to move down
    # new_pos_x = pos_x + 46000
    # new_pos_y = pos_y - 3000
    # new_pos_z = pos_z

    # #  to move up
    new_pos_x = pos_x - 46000
    new_pos_y = pos_y + 3000
    new_pos_z = pos_z

    print('Preparing to move stage')

    print(new_pos_x, new_pos_y, new_pos_z)

    # asd = move_stage(device, new_pos_x, new_pos_y, new_pos_z, enable_Z_move = False)

    asd = move_stage(device, 2950614.778, 3433899.781, 3179695.125, enable_Z_move = False)
    # asd = move_stage(device, 3009894.661, 3440630.683, 3179695.125, enable_Z_move = False)


    # print(asd)
    7
    print('Moving stage')


    device.close()