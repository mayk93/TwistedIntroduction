#!/usr/local/bin/python3

import socket
from random import randint

print(0)
HOST = ''                 # Symbolic name meaning all available interfaces
print(1)
PORT = 50007              # Arbitrary non-privileged port
print(2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(3)
s.bind((HOST, PORT))
print(4)
s.listen(1)
print(5)
conn, addr = s.accept()
print(6)
print('Connected by: ' + str(addr))
while True:
    data = conn.recv(1024)
    if randint(0,1000) == 423:
        print(type(data))
    if not data:
        break
    conn.sendall("You sent: " + str(data))
conn.close()
