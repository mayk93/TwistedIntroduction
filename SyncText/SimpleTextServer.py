#!/usr/local/bin/python3

import socket
import time

HOST = 'localhost'
PORT = 50007
FILE = "text.txt"
SERVING_SIZE = 50
DELAY = 5

def get_file(file_to_get):
    return open(file_to_get, mode='r', encoding='utf-8')

'''
def configure_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5)
    return sock
'''

def send_text(sock, file_to_serve, SERVING_SIZE, delay):
    print("Sending.")
    while True:
        batch = file_to_serve.read(SERVING_SIZE)
        if not batch:
            sock.close()
            file_to_serve.close()
            return
        print("Sending "+len(batch)+" to client.")
        try:
            # Sending a batch takes time. This time is spent waiting for the batch to be sent.
            sock.sendall(batch)
        except Exceptions as e:
            print(str(e))
            sock.close()
            file_to_serve.close()
            return
        time.sleep(delay)

def serve(listen_socket, file_to_serve, SERVING_SIZE, delay):
    print("Serving.")
    while True:
        sock, addr = listen_socket.accept()
        print("Sending text to: "+str(addr))
        send_text(sock, file_to_serve, SERVING_SIZE, delay)

def main():
    print("Preparing.")
    file_to_serve = get_file(FILE)
    '''
    sock = configure_socket()
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print("Now serving at " + str(sock.getsockname()[0]) + ":" + str(sock.getsockname()[1]))
    serve(sock,file_to_serve,SERVING_SIZE,DELAY)

if __name__ == "__main__":
    main()
