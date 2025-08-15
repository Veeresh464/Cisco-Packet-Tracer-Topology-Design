import socket
import sys

nodes = ['A', 'B', 'C', 'D']
INF = sys.maxsize  

graph = [
    [0,   1,   4, INF],  # A -> (B:1, C:4, D:∞)
    [1,   0,   2,   5],  # B -> (A:1, C:2, D:5)
    [4,   2,   0,   1],  # C -> (A:4, B:2, D:1)
    [INF, 5,   1,   0]   # D -> (B:5, C:1, A:∞)
]

def dijkstra(matrix, start, end):
    """Find the shortest path using Dijkstrs Algorithm (Adjacency Matrix)."""
    n = len(matrix)
    start_index = nodes.index(start)
    end_index = nodes.index(end)

    dist = [INF] * n
    dist[start_index] = 0
    visited = [False] * n
    parent = [-1] * n  

    for _ in range(n):
        min_dist = INF
        min_index = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i

        visited[min_index] = True

        for j in range(n):
            if matrix[min_index][j] != INF and not visited[j]:
                new_dist = dist[min_index] + matrix[min_index][j]
                if new_dist < dist[j]:
                    dist[j] = new_dist
                    parent[j] = min_index

    path = []
    current = end_index
    while current != -1:
        path.insert(0, nodes[current])
        current = parent[current]

    return dist[end_index], path if dist[end_index] != INF else []

HOST = '10.1.6.168'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is running on {HOST}:{PORT}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr}")

    data = client_socket.recv(1024).decode().strip()
    source, destination = data.split()

    cost, path = dijkstra(graph, source, destination)

    response = f"{cost} {'->'.join(path)}"
    client_socket.send(response.encode())

    client_socket.close()
