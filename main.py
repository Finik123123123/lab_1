import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening...")

client_socket, address = server_socket.accept()

prime_number = 23
base = 5
private_key = 6
public_key = (base ** private_key) % prime_number

client_socket.send(str(public_key).encode())

client_public_key = int(client_socket.recv(1024).decode())

shared_secret = (client_public_key ** private_key) % prime_number

print("Shared secret:", shared_secret)

client_socket.close()
server_socket.close()
