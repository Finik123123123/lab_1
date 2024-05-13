import socket

# Создание сокета клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
client_socket.connect(("localhost", 80))

# Создание запроса к серверу
request = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"

# Отправка запроса серверу
client_socket.sendall(request.encode())

# Получение и вывод ответа сервера
response = client_socket.recv(1024)
print(response.decode())

# Закрытие сокета клиента
client_socket.close()