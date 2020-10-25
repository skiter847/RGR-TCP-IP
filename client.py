import socket

# адрес сервера
CONNECT_HOST = 'localhost'

# порт сервера
CONNECT_PORT = 5555

# создание КЛИЕНТСОГО сокета, первый параметр указывает какоя версия IP будет использована если AF_INET значит IPV4...
# если AF_INET6 значит IPV6, вторым параметром мы указывает какой протокол передачи данных мы будет использывать...
# если SOCK_STREAM значит протокол TCP, если  SOCK_DGRAM протокол UDP, все данные взяты и документации python https://docs.python.org/3/library/socket.html#socket-objects
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# устанавливаем соедение с сервером
client_socket.connect((CONNECT_HOST, CONNECT_PORT))

# отправляем серверу новое сообщение
client_socket.send(bytes('привет сервер, я клиент, я к тебе подключился :)', encoding='utf-8'))

while True:

    # Т.к. мы не можем точно знать, что и в каких объемах сервер нам пошлет, то мы будем получать данные от него небольшими порциями.
    # Чтобы получить данные нужно воспользоваться методом recv, который в качестве аргумента принимает количество байт для чтения.
    # Мы будем читать порциями по 1024 байт (или 1 кб)
    data = client_socket.recv(1024)
    if data:
        # выведем в консоль сообщение которое пришло нам от сервера
        print(data.decode('utf-8'))
