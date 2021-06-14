# 1:1 채팅을 할 수 있는 클라이언트 프로그램
# 키보드 입력 메시지를 상대방으로 송신하고 수신 메시지는 화면에 출력하는 클라이언트 프로그램
# 지속적인 채팅이 가능하도록 무한루프로 실행

from socket import *

port = 3333
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
# TCP와는 다르게 UDP 프로토콜은 connect()와 같은 연결이 없음

while True:
    msg = input('-> ')
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUF_SIZE)
    print('<- ', data.decode())