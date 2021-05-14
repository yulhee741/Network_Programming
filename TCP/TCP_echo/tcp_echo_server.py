# 에코 서버
# 클라이언트로부터 수신한 데이터를 출력하고 상대방에게 다시 전송

from socket import *

port = 2500
BUF_SIZE = 1024

sock = socket(AF_INET,SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
    data = conn.recv(BUF_SIZE)
    print("Received data : ", data.decode())
    conn.send(data)

conn.close()
sock.close()