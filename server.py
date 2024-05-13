import socket


def encrypt(text, e, n):
    encrypted = [pow(ord(char), e, n) for char in text]
    return encrypted


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening...")

client_socket, address = server_socket.accept()

e = 65537
n = 9516311845790656153499716760847001433441357  # Простые числа p и q

while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break

    print("Received message:", data)

    encrypted_data = encrypt(data, e, n)
    client_socket.send(str(encrypted_data).encode())

client_socket.close()
server_socket.close()
