# 명령행 인자 에코 서버 프로그램
# 서버의 포트번호를 명령행 인자로 받음
# ex) python3 cmd_server.py 5555

from socket import *
import sys
port = 2500 # default
BUFSIZE = 1024

# cmd_server.py = sys.argv[0]
# 5555 = sys.argv[1]
if len(sys.argv) > 1:
    port = int(sys.argv[1])

sock = socket(AF_INET, SOCK_STREAM) 
sock.bind(('', port)) 
sock.listen(1)
conn, addr = sock.accept() 
print('connected by', addr)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    print("Received message: ", data.decode()) 
    conn.send(data)

conn.close()