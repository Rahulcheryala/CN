import socket
import random

def client():
    # Define client name
    client_name = "Client"

    # Generate a random number
    client_number = random.randint(1, 100)

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's port
    server_address = ('localhost', 8888)
    client_socket.connect(server_address)

    try:
        # Send data
        message = f"{client_name},{client_number}"
        client_socket.sendall(message.encode())

        # Receive data from server
        data = client_socket.recv(1024)
        server_name, server_number = data.decode().split(',')

        # Print received data
        print(f"Server: {server_name.strip()}, Client: {client_name}")
        print(f"Server number: {server_number}")
        # print(f"Sum: {int(server_number) + client_number}")

    finally:
        # Clean up
        client_socket.close()

if __name__ == "__main__":
    client()
