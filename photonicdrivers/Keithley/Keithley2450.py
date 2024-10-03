import socket

class Keithley2450:

    def __init__(self, ip_address="10.209.67.218", port=5025):
        """
        Initialize the Keithley 2450 SourceMeter driver.

        :param ip_address: IP address of the Keithley 2450.
        :param port: Port number for SCPI communication (default is 5025).
        """
        self.ip_address = ip_address
        self.port = port
        self.socket = None

    def connect(self):
        """
        Establish a connection to the Keithley 2450.
        """
        if self.socket:
            print("Already connected.")
            return
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(10)  # Set a timeout for connection attempts

        try:
            self.socket.connect((self.ip_address, self.port))
            print(f"Connected to {self.ip_address}:{self.port}")
        except socket.timeout:
            print("Connection timed out.")
            self.socket = None
        except socket.error as e:
            print(f"Socket error: {e}")
            self.socket = None

    def disconnect(self):
        """
        Close the connection to the Keithley 2450.
        """
        if self.socket:
            self.socket.close()
            self.socket = None
            print("Connection closed.")

    def send_command(self, command):
        """
        Send an SCPI command to the Keithley 2450 and receive the response.

        :param command: SCPI command to send.
        :return: Response from the Keithley 2450.
        """
        if not self.socket:
            raise RuntimeError("Not connected to the device.")
        
        try:
            self.socket.sendall(command.encode('ascii') + b'\n')
            response = self.socket.recv(4096)  # Adjust buffer size if needed
            return response.decode('ascii').strip()
        except socket.error as e:
            print(f"Socket error: {e}")
            return None

    def query(self, command):
        """
        Send a command and return the response.

        :param command: SCPI command to send.
        :return: Response from the Keithley 2450.
        """
        return self.send_command(command)

    def identify(self):
        """
        Query the Keithley 2450 for its identification information.

        :return: Identification string.
        """
        return self.query("*IDN?")

# Example usage:
if __name__ == "__main__":
    # Replace with the actual IP address of your Keithley 2450
    device = Keithley2450()

    try:
        device.connect()
        print("Identification:", device.identify())
    finally:
        device.disconnect()