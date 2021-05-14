# 에코 클라이언트
# 서버에 연결하여 메시지를 전송하고, 수신 메시지를 출력

from socket import *

port = int(input("Port Num : "))
address =('localhost', port)
BUF_SIZE = 1024

s = sock(AF_INET, SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Message to send : ")
    s.send(msg.encode())
    data = s.recv(BUF_SIZE)
    print("Received message: %s", %data.decode())

s.close()