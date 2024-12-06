import socket
import select
import random

HOST = 'localhost'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('서버 시이작~')

    readsocks = [s]
    answers = {}
    num_clients = 0

    while True:
        readables, writeables, exceptions = select.select(readsocks, [], [])

        for sock in readables:
            if sock == s:
                newsock, addr = s.accept()
                num_clients += 1
                print(f'클라이언트가 접속했습니다.:{addr}, 정답은 {num_clients} 입니다.')
                readsocks.append(newsock)
                answers[newsock] = num_clients
                for key in answers.keys():
                    answers[key] = num_clients

            else:
                conn = sock
                data = conn.recv(1024).decode('utf-8')
                print(f'데이터:{data}')

                try:
                    n = int(data)
                except ValueError:
                    conn.sendall(f'입력값이 올바르지 않습니다.:{data}'.encode('utf-8'))
                    continue

                answers = answers.get(conn)

                if n == 0:
                    conn.sendall(f"종료".encode('utf-8'))
                    conn.close()
                    num_clients -= 1
                    print(f'클라이언트가 게임을 종료했습니다.:{addr}, 정답은 {num_clients} 입니다.')

                    for key in answers.keys():
                        answers[key] = num_clients
                    readsocks.remove(conn)

                elif n > answers:
                    conn.sendall("너무 높습니다.".encode('utf-8'))
                elif n < answers:
                    conn.sendall("너무 낮습니다.".encode('utf-8'))
                else:
                    conn.sendall("정답입니다 !".encode('utf-8'))