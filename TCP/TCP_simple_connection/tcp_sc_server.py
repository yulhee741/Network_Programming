# 간단한 서버 생성 함수 : create_server()
#   -> 서버에서 TCP 소켓 생성, bind, listen을 한번에 수행해주는 함수
#   -> socket(), bind(), listen()이 합쳐진 것

from socket import *

port = 2500
BUF_SIZE = 1024

# backlog = 동시 접속 가능
sock = socket.create_server(('', port), family=AF_INET, backlog = 1)
conn, addr = sock.accept()
print('connected by ', addr)

while True:
    data = conn.recv(BUF_SIZE)
    if not data:
        break

    print("Recieved data : ", data.decode())
    conn.send(data)

conn.close()