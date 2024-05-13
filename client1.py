import socket

def decrypt(encrypted, d, n):
    decrypted = [chr(pow(char, d, n)) for char in encrypted]
    return ''.join(decrypted)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

d = 3  # Закрытый ключ
n = 5  # Простые числа p и q

while True:
    message = input("Enter a message to send: ")
    client_socket.send(message.encode())

    encrypted_response = eval(client_socket.recv(1024).decode())
    crypted = decrypt(encrypted_response, d, n)
    print("Crypted message:", crypted)

client_socket.close()