import socket
import threading

def messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if message:
            print(message)

def start_client_1():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 2281))
    threading.Thread(target=messages, args=(client,)).start()

    while True:
        message = input("1 человек: ")  #
        client.send(message.encode())

start_client_1()