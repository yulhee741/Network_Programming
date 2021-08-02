# 간단한 서버 접속 함수 : create_connection()
#   -> 클라이언트에서 TCP소켓 생성과 연결 요청을 한번에 수행해줌
#   -> socket()과 connect가 합쳐진 것

from socket import *

BUF_SIZE = 1024

# 기본적으로 TCP 소켓을 만들어 줌
s = socket.create_connection(('localhost', 2500))

while True:
    msg = inpurt("Message to send : ")
    s.send(msg.encode())
    data = s.recv(BUF_SIZE)
    if not data:
        break
    print("Received message : %s" %data.decode())