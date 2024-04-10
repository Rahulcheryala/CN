from pydoc import cli
import socket
from urllib import response
import json

client_info = {}


def send_message(client_socket, message):
    client_socket.send(message.encode())


def receive_message(client_socket):
    return client_socket.recv(1024).decode()


def start_client():
    # Define server IP and port
    server_ip = "127.0.0.1"
    server_port = 8888

    # Create a TCP socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print("Connected to server.")

    try:
        #! Send name to server
        response_name = receive_message(client_socket)
        name = input(response_name)

        #! Send public key to server
        response_public_key = receive_message(client_socket)
        public_key = input(response_public_key)

        #! Create a dictionary to hold client data
        client_info = {"name": name, "public_key": public_key}

        #! Send client data to the server in JSON format
        client_socket.send(json.dumps(client_info).encode("utf-8"))

        #! Receive updated dictionary from server
        updated_dict = client_socket.recv(1024).decode("utf-8")

        #! Parse the received JSON data
        updated_client_dict = json.loads(updated_dict)

        #! Print the updated dictionary
        print("Updated client dictionary received from server:")
        print(updated_client_dict)

        # Perform further communication with the server (secure chat, video streaming, etc.)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    start_client()
