#!/usr/local/bin/python3

import socket
import datetime

HOST = '104.155.75.83'
PORT = 50008
BATCH_SIZE = 1024

def configure_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.setblocking(0)
    return sock

def get_text(sock):
    text = ""
    while True:
        # While receiving data, the client is blocked.
        try:
            data = sock.recv(BATCH_SIZE)
            if not data:
                sock.close()
                break
            print("Received at "+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))+":\n"+str(data.decode('utf-8')))
            text += data.decode('utf-8')
        except Exception as e:
            print(str(exception))
    return text

def main():
    start = datetime.datetime.now()
    sock = configure_socket()
    text = get_text(sock)
    end = datetime.datetime.now()
    print("Entire text received in: "+str(end-start))
    print("Entire Text:")
    print("\n--- * ---\n")
    print(text)
    print("\n--- * ---\n")

if __name__ == '__main__':
    main()
