import socket

# Server details
HOST = '127.0.0.1'  # Server IP (localhost)
PORT = 65432        # Port number

# Create a socket (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  # Connect to server

message = "Hello Server, this is the client!"
client_socket.send(message.encode())  # Send message to server

response = client_socket.recv(1024).decode()  # Receive response
print(f"Server Response: {response}")

client_socket.close()  # Close connection
