import socket

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()
print('서버가 실행되었습니다.')

client_socket, addr = server_socket.accept()

print('접속한 클라이언트의 주소입니다.')
print('Connected by', addr)

while True:
    data = client_socket.recv(1024)

    if not data:
        break

    print('Received from', addr, data.decode())

    client_socket.sendall(data)

client_socket.close()
server_socket.close()