import socket
import random

def server():
    # Define server name
    server_name = "Server"

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 8888)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"{server_name} is waiting for a connection...")

    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()

        try:
            print(f"Connection from {client_address}")

            # Receive data from client
            data = connection.recv(1024)
            client_name, client_number = data.decode().split(',')

            # Generate a random number
            server_number = random.randint(1, 100)

            # Print information
            print(f"Client: {client_name.strip()}, Server: {server_name}")
            print(f"Client number: {client_number}, Server number: {server_number}")
            print(f"Sum: {int(client_number) + server_number}")

            # Send data back to client
            message = f"{server_name},{server_number}"
            connection.sendall(message.encode())

        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    server()
