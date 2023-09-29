import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind(("localhost", 12345))

print("Waiting for data...")

while True:
    # Receive data
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received: {data.decode()}")

