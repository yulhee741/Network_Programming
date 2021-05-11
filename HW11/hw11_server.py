# TCP를 이용한 단체 채팅 프로그램 만들기(select)
# 서버
#   -> 채팅 서버를 select() 함수를 이용하여 작성하여야 함
#   -> 새로운 클라이언트가 접속할 때마다, 소켓 리스트에 추가

import socket
import select
import time

socks = []

s_sock = socket.socket()
s_sock.bind(('', 5555))
s_sock.listen(5)

# 소켓 리스트에 서버 소켓을 추가
socks.append(s_sock)
print('Server Started')

while True:
    # 읽기 이벤트(연결요청 및 데이터수신) 대기
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    # 수신(읽기 가능한) 소켓 리스트 검사
    for s in r_sock:
        # 새로운 클라이언트의 연결 요청 이벤트 발생
        if s == s_sock:
            conn, addr = s_sock.accept()
            socks.append(conn)
            print(f'Client ({addr} connected.')
        # 기존 클라이언트의 데이터 수신 이벤트 발생
        else:
            data = s.recv(1024)
            if 'quit' in data.decode():
                print(addr, 'exited')
                s.close()
                socks.remove(s)
                continue

            print(time.asctime() + str(s.getsockname()) + ':' + data.decode())
            for client in socks:
                if client != s and client != s_sock:
                    client.send(data)