from photonicdrivers.Piezo_AttocubeAMC.Piezo_AttocubeAMC_Driver import Piezo_AttocubeAMC_Driver

# has to run on the attocube PC
ip = "192.168.1.1"

# (2046444.326, 2170676.425, 3159894.639)

piezo = Piezo_AttocubeAMC_Driver(ip,z_max_nm=3_500_000)
piezo.connect()
# x,y,z = piezo.get_position()
# piezo.set_position(x_nm=x + 10*1000, move_x=True)

piezo.set_position_relative(x_nm=-2*1000, move_x=True)

# piezo.set_position_relative(y_nm=2*1000, move_y=True)

# piezo.set_position_relative(z_nm=-5*1000, move_z=True)

# print(piezo.is_axis_moving())

print(piezo.get_position())
# print(piezo.get_device_type())
piezo.disconnect()

