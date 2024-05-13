import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

base = 5
private_key = 15
public_key = (base ** private_key) % 23

server_public_key = int(client_socket.recv(1024).decode())

client_socket.send(str(public_key).encode())

shared_secret = (server_public_key ** private_key) % 23

print("Shared secret:", shared_secret)

client_socket.close()
