# 타임 서버
# 클라이언트가 접속하면 현재 시간을 전송하는 프로그램

from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s = bind(('', 9999))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('connection from ', addr)

    conn.send(time.ctime(time.time()).encode())
    conn.close()