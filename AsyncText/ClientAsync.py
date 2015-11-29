#!/usr/local/bin/python3

import socket
import datetime

HOST = '104.155.75.83'
PORTS = [50007,50008,50009]
BATCH_SIZE = 1024

def configure_sockets():
    socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for port in PORTS]
    for sock,port in zip(socks,PORTS):
        sock.connect((HOST, port))
        sock.setblocking(0)
    return socks

def get_text(socks):
    text = ""
    attempt = 0
    current_socket = 0
    while True:
        # While receiving data, the client is blocked.
        #try:
        data = socks[current_socket].recv(BATCH_SIZE)
        if not data:
            sock.close()
            break
        print("Received at "+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))+":\n"+str(data.decode('utf-8')))
        text += data.decode('utf-8')
        #except Exception as e:
        attempt += 1
        current_socket = attempt%3
        if attempt >= 4:
            attempt = 0
    return text

def main():
    start = datetime.datetime.now()
    socks = configure_sockets()
    text = get_text(socks)
    end = datetime.datetime.now()
    print("Entire text received in: "+str(end-start))
    print("Entire Text:")
    print("\n--- * ---\n")
    print(text)
    print("\n--- * ---\n")

if __name__ == '__main__':
    main()
