import socket
import ssl
from base64 import b64encode

userEmail = "smtplab23@gmail.com"
userPassword = "lmvgusmmhxkmzoti"
userDestinationEmail = input("Enter Email Destination: ")
userSubject = input("Enter Subject: ")
userBody = input("Enter Message: ")
msg = '{}.\r\n I love computer networks!'.format(userBody)

# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = "smtp.gmail.com"
port = 587
#Fill in end

# Create socket called clientSocket and establish a TCP connection with
mailserver
#Fill in start
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, port))
#Fill in end


recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

clientSocket.send("STARTTLS\r\n".encode())
clientSocket.recv(1024)
sslClientSocket = ssl.wrap_socket(clientSocket)
# sslContext = ssl.create_default_context()
# sslClientSocket = sslContext.wrap_socket(clientSocket, server_hostname="smtp.gmail.com")

sslClientSocket.send("AUTH LOGIN\r\n".encode())
print(sslClientSocket.recv(1024))
sslClientSocket.send(b64encode(userEmail.encode()) + "\r\n".encode())
print(sslClientSocket.recv(1024))
sslClientSocket.send(b64encode(userPassword.encode()) + "\r\n".encode())
print(sslClientSocket.recv(1024))

# Send MAIL FROM command and print server response.
#Fill in start
sslClientSocket.send("MAIL FROM: {}\r\n".format(userEmail).encode())
recv2 = sslClientSocket.recv(1024).decode()
print(recv2)
#Fill in end

# Send RCPT TO command and print server response.
#Fill in start
sslClientSocket.send("RCPT TO: {}\r\n".format(userDestinationEmail).encode())
recv3 = sslClientSocket.recv(1024).decode()
print(recv3)
#Fill in end

# Send DATA command and print server response.
#Fill in start
sslClientSocket.send("DATA\r\n".encode())
recv4 = sslClientSocket.recv(1024).decode()
print(recv4)
#Fill in end

# Send message data.
#Fill in start
sslClientSocket.send("Subject: {}\r\n\r\n".format(userSubject).encode())
sslClientSocket.send(msg.encode())
#Fill in end

# Message ends with a single period.
#Fill in start
sslClientSocket.send("\r\n.\r\n".encode())
recv5 = sslClientSocket.recv(1024).decode()
print(recv5)
#Fill in end

# Send QUIT command and get server response.
#Fill in start
sslClientSocket.send("QUIT\r\n".encode())
recv6 = sslClientSocket.recv(1024).decode()
print(recv6)
#Fill in end

clientSocket.close()
