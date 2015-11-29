# Echo client program
import socket

print(0)
HOST = '130.211.73.8'    # The remote host
print(1)
PORT = 50007              # The same port as used by the server
print(2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(3)
s.connect((HOST, PORT))
print(4)
s.sendall(b'Hello, world')
print(5)
data = s.recv(1024)
print(6)
s.close()
print(7)
print('Received', repr(data))
