from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QDoubleSpinBox
import sys

import pyvisa as visa
import numpy as np


import serial
from time import sleep

class MyWindow(QMainWindow):
    
    
    def __init__(self, port, baudrate):
        super(MyWindow, self).__init__()
        self.port = port
        self.baudrate = baudrate
        self.timeout = 10000
        self.stages = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        
        # print("Enabling the stages")
        enable_stages = 'MM1\r\n' # 'MM0\r\n' to disable both
        self.stages.write(enable_stages.encode())
        
        self.setGeometry(500, 200, 700, 130) # (position_x, position_y, width, height)
        self.setWindowTitle("FCL100 Stage Controller") 
        self.initUI()
    
    def connect(self):
        print("Enabling the stages")
        enable_stages = 'MM1\r\n' # 'MM0\r\n' to disable both
        self.stages.write(enable_stages.encode())
        
    def disconnect(self):
        disable_stages = 'MM0\r\n'
        print("Disabling the stages")
        self.stages.write(disable_stages.encode()) 
       # self.stages.close()

    def initUI(self):

        

        read_position_stage1 = '1TP\r\n'
        read_position_stage2 = '2TP\r\n'
        
        # Send command to read position of stage 1 (Y-axis)
        self.stages.write(read_position_stage1.encode())
        # Send command to read position of stage 2 (X-axis)
        self.stages.write(read_position_stage2.encode())
        
        response_stage1 = self.stages.readline().decode().strip()
        response_stage2 = self.stages.readline().decode().strip()

        position_stage1 = float(response_stage1.split('TP')[1] if 'TP' in response_stage1 else 'N/A')
        position_stage2 = float(response_stage2.split('TP')[1] if 'TP' in response_stage2 else 'N/A')
        
        margin = 10
        self.label = QLabel(self)
        self.label.setText(f"Application started! Position (x mm,y mm): {position_stage2:.2f}, {position_stage1:.2f}" )
        self.label.setStyleSheet('color: red')
        self.label.adjustSize()
        self.label.move(350+margin, 100+margin)  
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        self.step = QDoubleSpinBox(self)
        self.step.setRange(0.0,1000.0)
        self.step.setSingleStep(0.1)
        self.step.setDecimals(1)
        self.step.move(350+margin,75)
        self.steplabel = QLabel(self)
        self.steplabel.setText("Step size [µm]")
        self.steplabel.move(350+margin, 50)
        
        self.rotate = QDoubleSpinBox(self)
        self.rotate.setRange(0.0,360.0)
        self.rotate.setSingleStep(0.1)
        self.rotate.setDecimals(1)
        self.rotate.move(350+margin,25)
        self.rotatelabel = QLabel(self)
        self.rotatelabel.setText("Rotation angle [deg]")
        self.rotatelabel.move(350+margin, 0)

        column_2_x_position = 500
        self.move_to_x = QDoubleSpinBox(self)
        self.move_to_x.setRange(-50, 50)
        self.move_to_x.setSingleStep(0.01)
        self.move_to_x.setDecimals(3)
        self.move_to_x.move(column_2_x_position+margin,25)
        self.move_to_x_label = QLabel(self)
        self.move_to_x_label.setText("Go to x [mm]")
        self.move_to_x_label.move(column_2_x_position+margin, 0)
        
        self.move_to_y = QDoubleSpinBox(self)
        self.move_to_y.setRange(-50, 50)
        self.move_to_y.setSingleStep(0.001)
        self.move_to_y.setDecimals(3)
        self.move_to_y.move(column_2_x_position+margin,75)
        self.move_to_y_label = QLabel(self)
        self.move_to_y_label.setText("Go to y [mm]")
        self.move_to_y_label.move(column_2_x_position+margin, 50)

        self.move_up = QPushButton(self)
        self.move_up.setText("up")
        self.move_up.move(100+margin, margin)
        self.move_up.clicked.connect(self.clicked_up)

        self.move_down = QPushButton(self)
        self.move_down.setText("down")
        self.move_down.move(100+margin,90)
        self.move_down.clicked.connect(self.clicked_down)

        self.move_left = QPushButton(self)
        self.move_left.setText("left")
        self.move_left.move(0+margin,50)
        self.move_left.clicked.connect(self.clicked_left)

        self.move_right = QPushButton(self)
        self.move_right.setText("right")
        self.move_right.move(200+margin,50)
        self.move_right.clicked.connect(self.clicked_right)

        self.go_to = QPushButton(self)
        self.go_to.setText("Go")
        self.go_to.setFixedSize(50, 50)
        self.go_to.move(column_2_x_position+margin+120, 40)
        self.go_to.clicked.connect(self.clicked_go_to)

        self.connect_button = QPushButton(self)
        self.connect_button.setCheckable(True)
        self.connect_button.setText("Connection")
        self.connect_button.setFixedSize(65, 40)
        self.connect_button.move(0+margin+120, 45)
        self.connect_button.clicked.connect(self.changeColor)
        self.connect_button.setStyleSheet("background-color : green")
        self.connect_button.clicked.connect(self.clicked_connect_button)

        self.connect_button = QPushButton(self)
        self.connect_button.setCheckable(True)
        self.connect_button.setText("Connection")
        self.connect_button.setFixedSize(65, 40)
        self.connect_button.move(0+margin+120, 45)
        self.connect_button.clicked.connect(self.changeColor)
        self.connect_button.setStyleSheet("background-color : green")
        self.connect_button.clicked.connect(self.clicked_connect_button)

    def changeColor(self):
    
             # if button is checked
        if self.connect_button.isChecked():
 
            # setting background color to light-blue
            self.connect_button.setStyleSheet("background-color : red")
 
        # if it is unchecked
        else:
 
            # set background color back to light-grey
            self.connect_button.setStyleSheet("background-color : green")

    def get_position(self):
            read_position_stage1 = '1TP\r\n'
            read_position_stage2 = '2TP\r\n'
            
            # Send command to read position of stage 1 (Y-axis)
            self.stages.write(read_position_stage1.encode())
            # Send command to read position of stage 2 (X-axis)
            self.stages.write(read_position_stage2.encode())
            
            response_stage1 = self.stages.readline().decode().strip()
            response_stage2 = self.stages.readline().decode().strip()
    
            position_stage1 = float(response_stage1.split('TP')[1] if 'TP' in response_stage1 else 'N/A')
            position_stage2 = float(response_stage2.split('TP')[1] if 'TP' in response_stage2 else 'N/A')
            return position_stage2, position_stage1

    def clicked_connect_button(self):
        # if button is checked
        if self.connect_button.isChecked():

            # setting background color to light-blue
            self.disconnect()

        # if it is unchecked
        else:

            # set background color back to light-grey
            self.connect()
            
    def clicked_left(self):
        delta = self.step.value()
        theta = self.rotate.value()
        self.stages.write(f'2PR{-delta*1e-3*np.cos(theta*np.pi/180)}\r\n'.encode())
        self.stages.write(f'1PR{delta*1e-3*np.sin(theta*np.pi/180)}\r\n'.encode())
        x, y = self.get_position()
        self.label.setText(f"Moved left {delta:.1f}µm. Position (x mm,y mm): {x:.2f}, {y:.2f}")
        self.update()
        
    
    def clicked_right(self):
        delta = self.step.value()
        theta = self.rotate.value()
        self.stages.write(f'2PR{delta*1e-3*np.cos(theta*np.pi/180)}\r\n'.encode())
        self.stages.write(f'1PR{-delta*1e-3*np.sin(theta*np.pi/180)}\r\n'.encode())
        x, y = self.get_position()
        self.label.setText(f"Moved right {delta:.1f}mm. Position (x mm,y mm): {x:.2f}, {y:.2f}")
        self.update()
    
    def clicked_up(self):
        delta = self.step.value()
        theta = self.rotate.value()
        self.stages.write(f'2PR{-delta*1e-3*np.sin(theta*np.pi/180)}\r\n'.encode())
        self.stages.write(f'1PR{-delta*1e-3*np.cos(theta*np.pi/180)}\r\n'.encode())
        x, y = self.get_position()
        self.label.setText(f"Moved up {delta:.1f}µm. Position (x mm,y mm): {x:.2f}, {y:.2f}")
        self.update()
    
    def clicked_down(self):
        delta = self.step.value()
        theta = self.rotate.value()
        self.stages.write(f'2PR{delta*1e-3*np.sin(theta*np.pi/180)}\r\n'.encode())
        self.stages.write(f'1PR{delta*1e-3*np.cos(theta*np.pi/180)}\r\n'.encode())
        x, y = self.get_position()
        self.label.setText(f"Moved down {delta:.1f}µm. Position (x mm,y mm): {x:.2f}, {y:.2f}")
        self.update()

    def clicked_go_to(self):
        go_to_x = self.move_to_x.value()
        go_to_y = self.move_to_y.value()
        self.stages.write(f'2PA{go_to_x}\r\n'.encode())
        self.stages.write(f'1PA{go_to_y}\r\n'.encode())
        sleep(0.5)
        x, y = self.get_position()
        self.label.setText(f"Moved to (x mm,y mm): {x:.2f}, {y:.2f}")
        self.update()


    def update(self):
        self.label.adjustSize()

        
    

port = 'COM4'
baudrate = 115200


def window():
    app = QApplication(sys.argv)
    win = MyWindow(port, baudrate)
    win.show()
    sys.exit(app.exec_())

window()  # make sure to call the function

# #%% To disconnect
# stage = MyWindow(port,baudrate)
# stage.disconnect()
