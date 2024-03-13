import qdac2
import common.connection as conn
# from serial import Serial

device = conn.find_qdac2_on_usb()
qdac = qdac2.QDAC2(device)
print(qdac.status())