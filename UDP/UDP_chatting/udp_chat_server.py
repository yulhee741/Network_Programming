# 1:1 채팅을 할 수 있는 서버 프로그램
# 수신 메시지는 화면에 출력하고, 키보드 입력 메시지를 상대방으로 송신하는 서버 프로그램
# 지속적인 채팅이 가능하도록 무한루프로 실행

from socket import *

port = 3333
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUF_SIZE)
    print('<- ', data.decode())
    resp = input('-> ')
    sock.sendto(resp.encode(), addr)