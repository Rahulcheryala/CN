import socket
import random

def client():
    client_name = "Client"
    client_number = random.randint(1, 100)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8008)
    client_socket.connect(server_address)
    try:
        message = f"{client_name},{client_number}"
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        server_name, server_number = data.decode().split(',')
        print(f"Server: {server_name.strip()}, Client: {client_name}")
        print(f"Server number: {server_number}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    client()