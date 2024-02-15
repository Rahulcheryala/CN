import socket
import os

# Function to handle HTTP requests
def handle_request(request):
    # Extract the filename from the HTTP request
    filename = request.split()[1][1:]

    # Check if the file exists
    if os.path.isfile(filename):
        # Open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Create HTTP response message with status 200 OK
        response = "HTTP/1.1 200 OK\r\n\r\n" + content
    else:
        # File not found, create HTTP response message with status 404 Not Found
        response = "HTTP/1.1 404 Not Found\r\n\r\n404 Not Found"

    return response

# Function to start the server
def start_server():
    # Define server address and port
    server_address = ('', 8008)  # Use an empty string to bind to all available interfaces
    server_port = 8008

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"Server is listening on port {server_port}...")

    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()

        try:
            print(f"Connection from {client_address}")

            # Receive the data from the client
            data = connection.recv(1024)
            request = data.decode()

            # Handle the HTTP request and generate the HTTP response
            response = handle_request(request)

            # Send the HTTP response back to the client
            connection.sendall(response.encode())
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    start_server()
