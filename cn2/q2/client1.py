import socket

def get_forwarding_interface(ip_address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5000))  # Connect to the server

    client_socket.send(ip_address.encode())  # Send IP address to server
    response = client_socket.recv(1024).decode()  # Receive response

    print(f"Datagram for {ip_address} should be forwarded via: {response}")

    client_socket.close()

if __name__ == "__main__":
    ip_to_lookup = input("Enter IP address to forward: ")
    get_forwarding_interface(ip_to_lookup)
