import socket

ip = "192.168.1.161"
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, port))
    s.sendall(b"*IDN?\n")
    print(s.recv(1024).decode())