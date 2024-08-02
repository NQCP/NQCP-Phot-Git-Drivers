## Example received by email from Thomsen, Henrik Schildtmann <henrik.s.thomsen@ifm.com> 2/8 2024
## Peter Granum


import customtkinter as ctk
import requests
import time
import ping3
 
 
 
#api_url = http://192.168.82.202/iolinkmaster/port%5B1%5D/iolinkdevice/pdin/getdata
 
 
 
def check_connection(host):
    try:
        response = ping3.ping(host)
        if response is not None:
            response_ms = response * 1000  # Convert seconds to milliseconds
            print(f"Host {host} is reachable. Round-trip time: {response_ms:.2f} ms")
            make_api_call()
        else:
            print(f"Host {host} is not reachable.")
            check_connection(host)
    except OSError:
        print(f"Error: Unable to ping {host}.")
        check_connection(host)
 
 
def send_Fuse_update(number, state):
    adr = http://192.168.82.202
    # Define the JSON data
    json_data = {
        "code": "request",
        "cid": 1,
        "adr": "/iolinkmaster/port[1]/iolinkdevice/pdout/setdata",
        "data": {
            "newvalue": "000000F"
        }
    } 
 
    if number == 1:
        tempnumber = hex(fuse_2.get_status()*2 + fuse_3.get_status()*4 + fuse_4.get_status()*8 + state*1)[2:].upper() 
    elif number == 2:
        tempnumber = hex(fuse_1.get_status()*1 + fuse_3.get_status()*4 + fuse_4.get_status()*8 + state*2)[2:].upper() 
    elif number == 3:
        tempnumber = hex(fuse_1.get_status()*1 + fuse_2.get_status()*2 + fuse_4.get_status()*8 + state*4)[2:].upper() 
    elif number == 4:
        tempnumber = hex(fuse_1.get_status()*1 + fuse_2.get_status()*2 + fuse_3.get_status()*4 + state*8)[2:].upper() 
 
 
    json_data["data"]["newvalue"] = '0000000' + tempnumber
    
    print(tempnumber)
 
    # Sending the POST request with JSON data
    response = requests.post(adr, json=json_data)
    # Check the response status
    if response.status_code == 200:
        print("Request was successful!")
        print("Response:", response.json())
        
    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)
 
 
def switch_ch1_event():
    print("switch toggled, current value:", switch_ch1.get())
    print(send_Fuse_update(1,switch_ch1.get()))
def switch_ch2_event():
    print(send_Fuse_update(2,switch_ch2.get()))
def switch_ch3_event():
    print(send_Fuse_update(3,switch_ch3.get()))
def switch_ch4_event():     
    print(send_Fuse_update(4,switch_ch4.get()))
    None
 
# window
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")  
window = ctk.CTk()
window.title('Fuse Control')
window.geometry('300x200') 
window.columnconfigure(0, weight = 2)
window.columnconfigure(1, weight = 9)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)
window.rowconfigure(3, weight = 1)
 
switch_ch1 = ctk.CTkSwitch(window, text = 'Fuse 1', command = switch_ch1_event, progress_color ='orange')
switch_ch1.grid(row = 0, column = 1, sticky = 'w' )
switch_ch2 = ctk.CTkSwitch(window, text = 'Fuse 2', command = switch_ch2_event, progress_color ='orange')
switch_ch2.grid(row = 1, column = 1, sticky = 'w' )
switch_ch3 = ctk.CTkSwitch(window, text = 'Fuse 3', command = switch_ch3_event, progress_color ='orange')
switch_ch3.grid(row = 2, column = 1, sticky = 'w' )
switch_ch4 = ctk.CTkSwitch(window, text = 'Fuse 4', command = switch_ch4_event, progress_color ='orange')
switch_ch4.grid(row = 3, column = 1, sticky = 'w' )
 
 
 
class fuse_channel:
    def __init__(self, name):
        self.name = name
 
 
    def get_status(self):
        return self.status
    
    def get_status_str(self):
        return self.status_str
    
    def get_current(self):
        return self.current
    
    def get_name(self):
        return self.name
 
    def update_status(self, new_status):
        self.status = new_status
        if self.status == 1:
            self.status_str = 'On'
        else:
            self.status_str = 'OFF'   
 
    def update_current(self, new_cuurent):
        self.current = new_cuurent
 
def make_api_call():
    response = requests.get(http://192.168.82.202/iolinkmaster/port%5B1%5D/iolinkdevice/pdin/getdata)
      
    if response.status_code == 200:
        data = response.json()
        #print("Data:", data)
        value_data = data['data']['value']
        #print("Value:", value_data)
        fuse_1.update_current(int(str(value_data)[:2],16)* 0.125)
        #print('CH1 Current ' + str(currentChannel1))
        fuse_2.update_current(int(str(value_data)[2:4],16)*0.125)
        #print('CH2 Current ' + str(currentChannel2))
        fuse_3.update_current(int(str(value_data)[4:6],16)*0.125)
        #print('CH3 Current ' + str(currentChannel3))
        fuse_4.update_current(int(str(value_data)[6:8],16)*0.125)
        #print('CH4 Current ' + str(currentChannel4))
        on_off = int(str(value_data)[32:36],16)
        #print('Channels On/Off ' + str(on_off))
        fuse_1.update_status((on_off >> 0) & 1)
        fuse_2.update_status((on_off >> 1) & 1)
        fuse_3.update_status((on_off >> 2) & 1)
        fuse_4.update_status((on_off >> 3) & 1)
 
        # Update Switches
        switch_ch1.select() if fuse_1.get_status() else switch_ch1.deselect()
        switch_ch2.select() if fuse_2.get_status() else switch_ch2.deselect()
        switch_ch3.select() if fuse_3.get_status() else switch_ch3.deselect()
        switch_ch4.select() if fuse_4.get_status() else switch_ch4.deselect()
 
        # Update Text
        switch_ch1.configure(text = 'Fuse 1 - Current ' + str(fuse_1.get_current()) + ' A') if fuse_1.get_status() else switch_ch1.configure(text ='Fuse 1')
        switch_ch2.configure(text = 'Fuse 2 - Current ' + str(fuse_2.get_current()) + ' A') if fuse_2.get_status() else switch_ch2.configure(text ='Fuse 2')
        switch_ch3.configure(text = 'Fuse 3 - Current ' + str(fuse_3.get_current()) + ' A') if fuse_3.get_status() else switch_ch3.configure(text ='Fuse 3')
        switch_ch4.configure(text = 'Fuse 4 - Current ' + str(fuse_4.get_current()) + ' A') if fuse_4.get_status() else switch_ch4.configure(text ='Fuse 4')
        
 
        #print('data Received OK')
 
    else:
        print(f"Error: {response.status_code} - {response.text}")
 
    
    window.after(1000, make_api_call) 
 
 
 
 
 
# Create Fuses
fuse_1 = fuse_channel('Fuse 1')     
fuse_2 = fuse_channel('Fuse 2')   
fuse_3 = fuse_channel('Fuse 3')   
fuse_4 = fuse_channel('Fuse 4')      
check_connection('192.168.82.202')
 
 
 
#run
window.mainloop()
