# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:53:31 2024

@author: Magnus Madsen
"""

import serial
import time


class Newport_FCL100():
    
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.timeout = 10000
        self.stages = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        
    def connect(self):
        print("Enabling the stages")
        enable_stages = 'MM1\r\n' # 'MM0\r\n' to disable both
        self.stages.write(enable_stages.encode())

        
    def home(self):
        homing ='OR\r\n'
        print("Homing")
        self.stages.write(homing.encode())
        
        self.WaitStatus('1TS000032', 10000)
   
    def set_position(self, x, y):
        move_stage1 = f'1PA{y}\r\n'
        move_stage2 = f'2PA{x}\r\n'
        
        print("Moving to absolute position")
        
        # Send command to move stage 1 (Y-axis)
        self.stages.write(move_stage1.encode())
        # Send command to move stage 2 (X-axis)
        self.stages.write(move_stage2.encode())

        self.WaitStatus('1TS000033', 10)
            
    def set_relative_position(self, x, y):
            relative_move_stage1 = f'1PR{y}\r\n'
            relative_move_stage2 = f'2PR{x}\r\n'
            
            print("Moving to relative position")
            
            # Send command to move stage 1 (Y-axis)
            self.stages.write(relative_move_stage1.encode())  
            # Send command to move stage 2 (X-axis)
            self.stages.write(relative_move_stage2.encode())
            
            print(relative_move_stage1)
            print(relative_move_stage2)
            
            
            self.WaitStatus('1TS000033', 10000)
    
    def get_position(self):
            read_position_stage1 = '1TP\r\n'
            read_position_stage2 = '2TP\r\n'
            
            # Send command to read position of stage 1 (Y-axis)
            self.stages.write(read_position_stage1.encode())
            # Send command to read position of stage 2 (X-axis)
            self.stages.write(read_position_stage2.encode())
            
            response_stage1 = self.stages.readline().decode().strip()
            response_stage2 = self.stages.readline().decode().strip()
    
            position_stage1 = response_stage1.split('TP')[1] if 'TP' in response_stage1 else 'N/A'
            position_stage2 = response_stage2.split('TP')[1] if 'TP' in response_stage2 else 'N/A'
            
            print(f'(x,y) = ({position_stage2},{position_stage1}) ')
            return float(position_stage2), float(position_stage1)
        
    def disconnect(self):
        disable_stages = 'MM0\r\n'
        print("Disabling the stages")
        self.stages.write(disable_stages.encode()) 
        self.stages.close()
        
    def get_status(self):
        cmd = '1TS\r\n'
        self.stages.write(cmd.encode())
        return self.stages.readline().decode().rstrip()   


    def WaitStatus(self, val, timeout):       
        print("WaitStatus : " + val)
        for x in range(timeout):
                time.sleep(0.001)
                cmd = '1TS\r\n'
                self.stages.write(cmd.encode())
                status = self.stages.readline().decode().rstrip()   
                if val in status:
                        print("Status = " + status)
    
                        return 1
    
    
        print("WaitStatus timeout, Status = " + status)
        return -1;

            
#%%
port = 'COM4'
baudrate = 115200
newport_FCL100 = Newport_FCL100(port, baudrate)
newport_FCL100.connect()
#%%%
# newport_FCL100.set_relative_position(0.2,0)
# newport_FCL100.set_relative_position(1.5,0) # to take it to the top left corner
newport_FCL100.get_position()

from time import sleep

# N=0
# while N<5:
#     print(N)
#     newport_FCL100.set_relative_position(0.05, 0)
#     sleep(1)
#     N = N+1
    



#%%
#newport_FCL100.set_position(1.996796,11.093515)# to center at objective
#sleep(0.1)
newport_FCL100.get_position()

#%%
# newport_FCL100.set_position(-50,-50) # to take it to the top left corner
# newport_FCL100.get_position()

#%%

newport_FCL100.disconnect()
