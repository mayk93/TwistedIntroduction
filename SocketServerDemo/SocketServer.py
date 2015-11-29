#!/usr/local/bin/python3

import socket
from random import randint

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by: ' + str(addr))
while True:
    data = conn.recv(1024)
    if randint(0,1000) == 423:
        print(type(data))
    if not data:
        break
    conn.sendall("You sent: " + str(data))
conn.close()
