import socket
import os

def handle_request(request):
    filename = request.split()[1][1:]
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            content = file.read()
        response = "HTTP/1.1 200 OK\r\n\r\n" + content
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n404 Not Found"
    return response
def start_server():
    server_address = ('', 8008)
    server_port = 8008
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print(f"Server is listening on port {server_port}...")

    while True:
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")
            data = connection.recv(1024)
            request = data.decode()
            response = handle_request(request)
            connection.sendall(response.encode())
        finally:
            connection.close()

if __name__ == "__main__":
    start_server()
