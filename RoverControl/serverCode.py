import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(("localhost", 12345))

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")
client_socket, client_address = server_socket.accept()
print("Connected to", client_address)

# Send data (similar to the client code)
client_socket.send(b"bro how are you")
client_socket.send(b"Im good broski")

# Close the sockets
client_socket.close()
server_socket.close()
