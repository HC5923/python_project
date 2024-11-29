import socket
import select

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()
print('서버가 실행되었습니다.')

readsocks = [server_socket]

while True:
    readables, writeables, exceptions = select.select(readsocks, [], [])
    for sock in readables:
        if sock == server_socket:
            client_socket, addr = server_socket.accept()

            print('접속한 클라이언트 주소입니다.')
            print('Connected by', addr)

            readsocks.append(client_socket)

        else:
            while True:
                data = sock.recv(1024)
                
                if not data:
                    print(sock.getpeername(), '접속 종료', data.decode())
                    
                    sock.close()
                    readsocks.remove(sock)
                    break

                print('Received from', sock.getpeername(), data.decode())
                sock.sendall(data)

server_socket.close()
