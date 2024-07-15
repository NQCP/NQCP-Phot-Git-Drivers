


from photonicdrivers.FiberPolarizationController.Thorlabs_MPC320 import *

def start_server():
    serial_number = "38449564"
    driver = Thorlabs_MPC320_Serial(serial_number)
    request_handler = Thorlabs_MPC320_Request_handler(driver=driver)
    local_ip_adress = socket.gethostbyname(socket.gethostname())
    server = Instrument_Server(request_handler, host_ip=local_ip_adress)
    server.start()

def start_client():
    local_ip_adress = socket.gethostbyname(socket.gethostname())
    thorlabs_MPC320_driver = Thorlabs_MPC320_Proxy(host_ip_address=local_ip_adress, host_port=8090)
    thorlabs_MPC320_driver.connect()
    thorlabs_MPC320_driver.disconnect()

def main():
    start_server()
    start_client()
    
if __name__ == '__main__':
    main()

