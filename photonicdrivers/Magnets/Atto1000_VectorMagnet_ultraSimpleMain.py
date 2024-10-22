from photonicdrivers.Magnets.APS100_PS_Driver import APS100_PS_Driver
from instruments.Abstract.Connectable import Connectable

import numpy as np

class Atto1000_VectorMagnet(Connectable):
    def __init__(self, B_max:float=2, Bx_max:float=2, By_max:float=2, Bz_max:float=5) -> None:
        '''
        Initialises a class for the Attocube vector magnet

        Parameters:
        B fields are in unit of T
        
        '''
        
        # The X and Z magnet share the same power supply (PS). The PS operates in dual mode

        self.power_supply_x = APS100_PS_Driver() # COM4
        self.power_supply_y = APS100_PS_Driver() # COM6
        self.power_supply_z = self.power_supply_x

        self.channel_x = 1
        self.channel_y = None
        self.channel_z = 2

        self.B_max = B_max
        self.Bx_max = Bx_max
        self.By_max = By_max
        self.Bz_max = Bz_max

        self.x_A_per_T = 1
        self.y_A_per_T = 1
        self.z_A_per_T = 1

        print("Setting the mode to 1D. This will allow you to operate the Z magnet only.")
        self.mode = "1D"

    def connect(self) -> None:
        self.power_supply_x.connect()
        self.power_supply_y.connect()
        self.power_supply_z.connect()

    def disconnect(self) -> None:
        self.power_supply_x.disconnect()
        self.power_supply_y.disconnect()
        self.power_supply_z.disconnect()

    def is_connected(self) -> bool:
        x = self.power_supply_x.is_connected()
        y = self.power_supply_y.is_connected()
        z = self.power_supply_z.is_connected()

        return x and y and z

    def set_mode(self, mode_str:str) -> None:
        Bx, By, Bz, B_tot = self.get_B()

        if mode_str == "1D":
            if self.power_supply_x.is_enabled or self.power_supply_y.is_enabled:
                print("Cannot change to 1D mode before the X and Y power supplies are disabled.")
            else:
                self.mode = mode_str

        elif mode_str == "vector":
            if B_tot > self.B_max:
                print("Cannot change to vector mode as the total field is larger than the limit of [T]:" + str(self.B_max))
            else:
                self.mode = mode_str
        
        else:
            print("Mode is " + mode_str + " but must be either 1D or vector")

    def enable_power_supply_outputs(self) -> None:
        if self.mode == "1D":
            self.power_supply_z.enable_output()
            print("Enabling the Z power supply output. Power supply is operating in '1D' mode.")
        elif self.mode == "vector":
            self.power_supply_x.enable_output()
            self.power_supply_y.enable_output()
            self.power_supply_z.enable_output()
            print("Enabling the X, Y, and Z power supply output. Power supply is operating in 'vector' mode.")
        else:
            print("Power supply mode is not set.")

    def disable_power_supply_outputs(self) -> None:
        self.power_supply_x.disable_output()
        self.power_supply_y.disable_output()
        self.power_supply_z.disable_output()

    def are_outputs_enabled(self) -> bool | bool | bool:
        x = self.power_supply_x.is_enabled()
        y = self.power_supply_y.is_enabled()
        z = self.power_supply_z.is_enabled()
        return x, y, z

    def set_B(self, Bx:float, By:float, Bz:float) -> None:
        self.set_Bx(Bx)
        self.set_By(By)
        self.set_Bz(Bz)

    def set_Bx(self, new_Bx:float) -> None:
        if self.mode != "1D":
            print("To operate the X magnet, you must set the mode to 'vector'.")
            return

        Bx, By, Bz = self.get_B()

        if self.is_B_within_thresholds(new_Bx, By, Bz):
            current = self.x_A_per_T * new_Bx
            self.power_supply_x.set_current(current, self.channel_x)

    def set_By(self, new_By:float) -> None:
        if self.mode != "1D":
            print("To operate the X magnet, you must set the mode to 'vector'.")
            return
        
        Bx, By, Bz = self.get_B()

        if self.is_B_within_thresholds(Bx, new_By, Bz):
            current = self.y_A_per_T * new_By
            self.power_supply_y.set_current(current)

    def set_Bz(self, new_Bz:float) -> None:
        Bx, By, Bz = self.get_B()

        if self.is_B_within_thresholds(Bx, By, new_Bz):
            current = self.z_A_per_T * new_Bz
            self.power_supply_z.set_current(current, self.channel_z)

    def get_B(self) -> float | float | float | float:
        I_x = self.power_supply_x.get_current(self.channel_x)
        I_y = self.power_supply_y.get_current()
        I_z = self.power_supply_z.get_current(self.channel_z)

        Bx = I_x / self.x_A_per_T
        By = I_y / self.y_A_per_T
        Bz = I_z / self.z_A_per_T

        Btot = self.__calc_Btot_from_Bxyz(Bx,By,Bz)

        return Bx, By, Bz, Btot
    
    def is_B_within_thresholds(self, new_Bx:float, new_By:float, new_Bz:float) -> bool:
        new_Btot = self.__calc_Btot_from_Bxyz(new_Bx, new_By, new_Bz)

        if self.mode == "vector":
            try:
                if new_Btot > self.B_max:
                    raise ValueError(str(new_Btot) + " T exceeds the threshold of " + str(self.B_max) + " T.")
                if new_Bx > self.Bx_max:
                    raise ValueError(str(new_Bx) + " T exceeds the threshold of " + str(self.Bx_max) + " T.")
                if new_By > self.By_max:
                    raise ValueError(str(new_By) + " T exceeds the threshold of " + str(self.By_max) + " T.")
                if new_Bz > self.Bz_max:
                    raise ValueError(str(new_Bz) + " T exceeds the threshold of " + str(self.Bz_max) + " T.")

                return True
            
            except ValueError as error:
                print(error)
                return False
            
        elif self.mode == "1D":
            try:
                if new_Bz > self.Bz_max:
                    raise ValueError(str(new_Bz) + " T exceeds the threshold of " + str(self.Bz_max) + " T.")
                return True
            
            except ValueError as error:
                print(error)
                return False
            
        else:
            print("Mode is not defined. Cannot evaluate field thresholds. Returning False")
            return False

    ################################ PRIVATE METTHODS ################################

    def __calc_Btot_from_Bxyz(self, Bx, By, Bz) -> float:
        return np.sqrt(np.pow(Bx,2) + np.pow(By,2) + np.pow(Bz,2))