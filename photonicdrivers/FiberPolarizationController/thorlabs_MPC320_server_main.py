


from photonicdrivers.FiberPolarizationController.Thorlabs_MPC320_driver import *
from threading import Thread, Event
import time
import socket
import sys

def setup_server():
    serial_number = "38449564"
    driver = Thorlabs_MPC320_Serial(serial_number)
    request_handler = Thorlabs_MPC320_Request_handler(driver=driver)
    local_ip_adress = socket.gethostbyname(socket.gethostname())
    server = Instrument_Server(request_handler, host_ip=local_ip_adress, host_port=8089)
    return server    

def run_client():
    local_ip_adress = socket.gethostbyname(socket.gethostname())
    host_port = 8089
    thorlabs_MPC320_driver = Thorlabs_MPC320_Proxy(host_ip_address=local_ip_adress, host_port=host_port)
    thorlabs_MPC320_driver.connect()
    thorlabs_MPC320_driver.set_position_2(160)
    thorlabs_MPC320_driver.set_position_0(160)
    thorlabs_MPC320_driver.set_position_1(45)
    thorlabs_MPC320_driver.disconnect()
    print("Press 'q' to quit: ")
    

def monitor_user_input(stop_event):
    while not stop_event.is_set():
        user_input = input("Enter 'q' to quit: ")
        if user_input.lower() == 'q':
            stop_event.set()

def main():
    stop_event = Event()
    
    server = setup_server()
    server_thread = Thread(target=server.start)
    server_thread.start()
    
    time.sleep(5)
    
    client_thread = Thread(target=run_client)
    client_thread.start()
    
    input_thread = Thread(target=monitor_user_input, args=(stop_event,))
    input_thread.start()

    try:
        while not stop_event.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
    
    server.stop()
    server_thread.join()
    sys.exit("User requested exit")

def main_2():

    server = setup_server()
    server_thread = Thread(target=server.start)
    server_thread.start()
    server.stop()
    

if __name__ == '__main__':
    main_2()
