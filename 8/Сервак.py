import socket
from _thread import start_new_thread

clients = []

def client(conn, addr):
    conn.send("Асалам алейкум".encode())
    while True:
        message = conn.recv(1024).decode()
        if message:
            print(f"<{addr}> {message}")
            broadcast(message, conn)
        else:
            break
    conn.close()
    clients.remove(conn)

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            client.send(message.encode())

def start_server():
    server = socket.socket()
    server.bind(('localhost', 2281))
    server.listen(5)
    print("Вроде что то работает...")

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        print(f"Опа кто то тут {addr}")
        start_new_thread(client, (conn, addr))

start_server()
