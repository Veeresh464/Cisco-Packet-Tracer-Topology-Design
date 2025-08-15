import socket

forwarding_table = {
    "192.168.1.0/24": "eth0",
    "192.168.2.0/24": "eth1",
    "10.0.0.0/8": "eth2",
    "172.16.0.0/12": "eth3"
}

def longest_prefix_match(ip_address):
    best_match = None
    longest_prefix = -1

    for prefix, interface in forwarding_table.items():
        network, prefix_length = prefix.split('/')
        prefix_length = int(prefix_length)

        ip_binary = ''.join(f'{int(octet):08b}' for octet in ip_address.split('.'))
        network_binary = ''.join(f'{int(octet):08b}' for octet in network.split('.'))

        if ip_binary[:prefix_length] == network_binary[:prefix_length]:
            if prefix_length > longest_prefix:
                longest_prefix = prefix_length
                best_match = interface

    return best_match if best_match else "No route found"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))  # Bind to localhost on port 5000
server_socket.listen(5)

print("Server is running... Waiting for connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    ip_address = client_socket.recv(1024).decode()
    print(f"Received IP: {ip_address}")

    interface = longest_prefix_match(ip_address)

    client_socket.send(interface.encode())
    
    client_socket.close()
