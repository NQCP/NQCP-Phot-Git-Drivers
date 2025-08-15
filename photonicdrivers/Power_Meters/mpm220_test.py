import socket

# ip = "192.168.1.161" # default device IP
ip = "10.209.69.171" # KU IT registered IP, MAC address 3C 6F 45 10 11 64
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, port))
    s.sendall(b"*IDN?\n")
    print(s.recv(1024).decode())