from pydoc import cli
import socket
import threading
import json

server_dict = {}


def handle_client(client_socket, addr, client_dict):
    try:

        #! Receive client's name
        client_socket.send("Enter your name: ".encode())

        #! Receive client's public key
        client_socket.send("Enter your public key: ".encode())

        #! Receive
        client_info = client_socket.recv(1024).decode("utf-8")

        #! Parse the received JSON data
        client_data = json.loads(client_info)

        #! Extract client name and public key from received data
        client_name = client_data["name"]
        client_public_key = client_data["public_key"]

        #! Store the client's name and public key in the dictionary
        server_dict[client_name] = client_public_key
        print(server_dict)

        #! Send updated dictionary to the client
        client_socket.send(json.dumps(server_dict).encode("utf-8"))

        #! Notify existing clients about the new connection
        for client in server_dict:
            if client != client_name:
                client_socket.send(
                    f"{client_name} has joined the chat.".encode())

        # Handle client communication (secure chat, video streaming, etc.)

    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        client_socket.close()


def start_server():
    # Define server IP and port
    server_ip = "127.0.0.1"
    server_port = 8888

    # Create a TCP socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server is listening on {server_ip}:{server_port}")

    # Dictionary to store client information (name -> public key)
    client_dict = {}

    while True:
        # Accept incoming client connection
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")

        # Handle the client connection in a separate thread
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, addr, client_dict))
        client_thread.start()


if __name__ == "__main__":
    start_server()
