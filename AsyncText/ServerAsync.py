#!/usr/local/bin/python3

import socket
import time

HOST = ''
PORTS = [50007,50008,50009]
FILES = ["text1.txt","text2.txt","text3.txt"]
SERVING_SIZES = [50,25,75]
DELAYS = [5,3,7]

def get_files(files_to_get):
    return [open(file_to_get, mode='r', encoding='utf-8') for file_to_get in files_to_get]

def configure_sockets():
    sockets_and_numbers = [(socket.socket(socket.AF_INET, socket.SOCK_STREAM),number) for number in range(3)]
    for sock,number in sockets_and_numbers:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORTS[number]))
        sock.listen(5)
    return sockets_and_numbers

def send_text(sock, file_to_serve, SERVING_SIZE, delay):
    print("Sending.")
    while True:
        batch = file_to_serve.read(SERVING_SIZE)
        if not batch:
            sock.close()
            file_to_serve.close()
            return
        print("Sending "+str(len(batch))+" to client.")
        try:
            # Sending a batch takes time. This time is spent waiting for the batch to be sent.
            sock.sendall(batch.encode('utf-8'))
        except Exception as e:
            print(str(e))
            sock.close()
            file_to_serve.close()
            return
        time.sleep(delay)

def serve(listen_sockets, files_to_serve, serving_sizes, delays):
    print("Serving.")
    while True:
        for sock,number in listen_sockets:
            sockt, addr = sock.accept()
            print("Sending text to: "+str(addr))
            send_text(sockt, files_to_serve[number], serving_sizes[number], delays[number])

def main():
    print("Preparing.")
    sockets_and_numbers = configure_sockets()
    files_to_serve = get_files(FILES)
    print("Now serving the following sockets:")
    for sock,number in sockets_and_numbers:
        print(str(number)+" - "+str(sock.getsockname()[0]) + ":" + str(sock.getsockname()[1]))
    serve(sockets_and_numbers,files_to_serve,SERVING_SIZES,DELAYS)

if __name__ == "__main__":
    main()
