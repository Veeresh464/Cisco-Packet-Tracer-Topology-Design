import socket

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

source = input("Enter source node: ").strip()
destination = input("Enter destination node: ").strip()

client_socket.send(f"{source} {destination}".encode())

response = client_socket.recv(1024).decode()

print("Shortest Path:", response)

client_socket.close()
