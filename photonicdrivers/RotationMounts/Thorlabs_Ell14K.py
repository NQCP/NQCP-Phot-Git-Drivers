
import time


def from_twos_complement(n, bits=32):
    if n < (1 << (bits-1)): return n
    return n - (1 << bits)

def to_twos_complement(n, bits=32):
    return (1 << bits) + n if n < 0 else n

# Encoder counts per revolution (from manual)
COUNTS_PER_REVOLUTION = 143360

# List of status responses
RESPONSES = [
    'ok',
    'communication timeout',
    'mechanical timeout',
    'command error',
    'value out of range',
    'module isolated',
    'module out of isolation',
    'initialization error',
    'thermal error',
    'busy',
    'sensor error',
    'motor error',
    'out of range',
    'overcurrent',
]


class Thorlabs_ELL14K:
    def __init__(
            self,
            serial_connection, 
            address: str, # Device address on controller bus.
            offset: int, # Software angle offset, in encoder counts.
        ):
        self._conn = serial_connection
        self.address = address
        self.offset = offset
        self.current_angle = 0

    def send(self, command, data=b''):
        """Send the given command type, with the given data payload."""
        packet = (
            str(self.address).encode('utf-8')
            + command.encode('utf-8')
            + data.hex().upper().encode('utf-8')
            + b'\n'
        )
        self._conn.write(packet)

    def query(self, command, data=b''):
        """
        Send the given command type, with the given data payload.
        Return the response type and decoded data payload from the Elliptec controller.
        """
        self.send(command, data=data)

        response = b''
        while True:
            response += self._conn.read(8192)
            if response.endswith(b'\r\n'): break
            time.sleep(0.2)

        header, data = response[:3], response[3:-2]
        assert chr(header[0]) == str(self.address)
        return header[1:].decode(), int(data.decode(), 16)

    def home(self):
        """
        Return the stage to the home position.
        (May correspond to 0 degrees in software.)
        """
        self.query('ho')

    def tare(self):
        """Mark the current position as 0° in software."""
        self.offset = 0

    def get_angle(self):
        """Return the current angle (CCW)."""
        return self.current_angle % 360
    
    def set_angle(self):
        pass
    



if __name__ == "__main__":
    from serial import Serial
    port = "COM8"
    connection = Serial(port=port, baudrate=9600, stopbits=1, parity='N', timeout=0.05)
    rotation_mount_quarter = Thorlabs_ELL14K(serial_connection=connection, offset=0, address="A")
    rotation_mount_half = Thorlabs_ELL14K(serial_connection=connection, offset=0, address="B")
    rotation_mount_quarter.home()
    
    connection.close_connection()


