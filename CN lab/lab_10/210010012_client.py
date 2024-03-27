import socket
import time

# Server address and port
server_address = ('localhost', 12000)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set timeout value to 1 second
client_socket.settimeout(1)

# Number of pings to send
num_pings = 10

for i in range(1, num_pings + 1):
    # Construct the message to send
    message = f"Ping {i}"

    # Record the time before sending the ping
    start_time = time.time()

    try:
        # Send the ping message to the server
        client_socket.sendto(message.encode(), server_address)

        # Receive the response from the server
        response, server = client_socket.recvfrom(1024)

        # Calculate round trip time (RTT)
        end_time = time.time()
        rtt = end_time - start_time

        # Print the response message from server and RTT
        print(f"Reply from {server}: {
            response.decode()}, RTT = {rtt:.6f} seconds")

    except socket.timeout:
        # Handle timeout
        print(f"Request timed out")

# Close the socket
client_socket.close()
