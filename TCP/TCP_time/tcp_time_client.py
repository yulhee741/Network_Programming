# 타임 클라이언트
# 타임 서버에 접속하여 시간을 읽어 오는 클라이언트

from socket import *

port = 9999
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

print("Time : ", sock.recv(BUF_SIZE).decode())
sock.close()
