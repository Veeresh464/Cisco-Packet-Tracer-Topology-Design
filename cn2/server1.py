import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port number

# Create a socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  # Bind to the address and port
server_socket.listen(5)  # Listen for connections (max 5 clients)

print(f"Server listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()  # Accept connection
    print(f"Connection established with {client_address}")

    message = client_socket.recv(1024).decode()  # Receive message from client
    print(f"Received: {message}")

    response = f"Hello Client, you sent: {message}"
    client_socket.send(response.encode())  # Send response

    client_socket.close()  # Close connection
