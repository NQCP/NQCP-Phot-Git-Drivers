from photonicdrivers.AttocubeAPI import AMC
from photonicdrivers.Abstract.Connectable import Connectable


class Piezo_AttocubeAMC_Driver(Connectable):

    def __init__(self,_ip_string: str) -> None:
        self.ip_address = _ip_string

        self.amc = AMC.Device(self.ip_address)

    def connect(self) -> None:
        self.amc.connect()

    def disconnect(self) -> None:
        self.amc.close()

    def is_connected(self) -> bool:
        return True

    def get_position(self) -> float | float | float:
        x, y, z, v1, v2, v3 = self.amc.control.getPositionsAndVoltages()
        return x, y, z
    
    def set_position(self, x_nm:int=0, y_nm:int=0, z_nm:int=0, move_x:bool=False, move_y:bool=False, move_z:bool=False) -> None:
        self.amc.control.MultiAxisPositioning(int(move_x), int(move_y), int(move_z), x_nm, y_nm, z_nm)

    def set_position_relative(self, x_nm:int=0, y_nm:int=0, z_nm:int=0, move_x:bool=False, move_y:bool=False, move_z:bool=False) -> None:
        '''
        Moves the piezo with an amount specified by x_nm, y_nm,z_nm relative to the current position
        '''
        x0, y0, z0 = self.get_position()
        x = x0 + x_nm
        y = y0 + y_nm
        z = z0 + z_nm
        self.amc.control.MultiAxisPositioning(int(move_x), int(move_y), int(move_z), x, y, z)

    def is_axis_moving(self) -> bool | bool | bool:
        x_moving, y_moving, z_moving = self.amc.control.getStatusMovingAllAxes()
        return bool(x_moving), bool(y_moving), bool(z_moving)
