import socket
import random

def server():
    server_name = "Server"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8008)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print(f"{server_name} is waiting for a connection...")

    while True:
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")
            data = connection.recv(1024)
            client_name, client_number = data.decode().split(',')
            server_number = random.randint(1, 100)
            print(f"Client: {client_name.strip()}, Server: {server_name}")
            print(f"Client number: {client_number}, Server number: {server_number}")
            print(f"Sum: {int(client_number) + server_number}")
            message = f"{server_name},{server_number}"
            connection.sendall(message.encode())
        finally:
            connection.close()
            
if __name__ == "__main__":
    server()
