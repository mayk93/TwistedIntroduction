#!/usr/local/bin/python3

import socket
import datetime

HOST = '104.155.75.83'
PORTS = [50007,50008,50009]
BATCH_SIZE = 1024

def configure_socket(current_socket):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORTS[current_socket]))
    sock.setblocking(0)
    return sock

def get_text():
    text = ""
    attempt = 0
    current_socket = 0
    while True:
        # While receiving data, the client is blocked.
        sock = configure_socket(current_socket)
        try:
            data = sock.recv(BATCH_SIZE)
            if not data:
                sock.close()
                break
            print("Received at "+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))+":\n"+str(data.decode('utf-8')))
            text += data.decode('utf-8')
        except Exception as e:
            attempt += 1
            current_socket = attempt%3
            print("Now trying to seceive on socket " + str(current_socket))
            if attempt >= 4:
                attempt = 0
    return text

def main():
    start = datetime.datetime.now()
    text = get_text()
    end = datetime.datetime.now()
    print("Entire text received in: "+str(end-start))
    print("Entire Text:")
    print("\n--- * ---\n")
    print(text)
    print("\n--- * ---\n")

if __name__ == '__main__':
    main()
