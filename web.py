import socket

# Определение рабочей директории сервера
root_dir = "веб-сайт"

# Создание сокета сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 80))
server_socket.listen()

def handle_request(client_socket):
    # Получение запроса клиента
    request = client_socket.recv(1024).decode()

    # Разбор запроса на метод, путь и версию HTTP
    method, path, version = request.split(" ")

    # Определение пути к запрашиваемому ресурсу
    if path == "/":
        path = "/index.html"
    resource_path = root_dir + path

    # Определение типа содержимого запрашиваемого ресурса
    content_type = "text/html" if path.endswith(".html") else "text/plain"

    try:
        # Открытие и чтение запрашиваемого ресурса
        with open(resource_path, "rb") as f:
            content = f.read()

        # Формирование ответа сервера
        response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n{content}"

    except FileNotFoundError:
        # Ответ в случае отсутствия запрашиваемого ресурса
        response = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: 14\r\n\r\n404 Not Found"

    # Отправка ответа клиенту
    client_socket.sendall(response.encode())

    # Закрытие сокета клиента
    client_socket.close()

# Цикл обработки входящих соединений
while True:
    # Принятие входящего соединения
    client_socket, client_address = server_socket.accept()

    # Обработка запроса клиента
    handle_request(client_socket)