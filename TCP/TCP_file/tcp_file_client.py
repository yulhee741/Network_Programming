# 파일 클라이언트

# 예외처리; 메시지가 수신되지 않거나, 다른 메시지가 오는 경우
#   예) 서버 접속 후 ‘Hello’ 메시지를 보낸 후, ‘Filename’ 메시지가 오지 않는 경우
#   → 일정 시간 기다린 후, 연결 종료
#   예) 서버 접속 후 ‘Hello’ 메시지를 보낸 후, ‘Bye’ 메시지가 오는 경우
#   → 연결 종료 (또는, 해당 메시지를 버리고, ‘Filename’ 메시지를 계속 기다리기) 

from socket import * 
import sys

BUF_SIZE = 1024
LENGTH = 20

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))

# 서버 접속 후 ‘Hello’ 메시지 전송
s.send(b'Hello') 

# 서버로부터 ‘Filename’ 메시지 수신
msg = s.recv(BUF_SIZE) 

if not msg:
    s.close()   # 소켓 연결 끊기
    sys.exit()  # 코드 종료
elif msg != b'Filename':    # 받은 메세지가 파일이름이 아닌 경우
    print('server:', msg.decode()) 
    s.close()
    sys.exit() 
else:
    print('server:', msg.decode())  # 정상적으로 받으면 출력

# 메시지 수신 후, 사용자로부터 filename 입력 받기
filename = input('Enter a filename: ') 

# 입력 받은 filename을 서버로 전송
s.send(filename.encode()) 

# 서버로부터 수신할 파일의 크기 수신
msg = s.recv(BUF_SIZE) 

if not msg:
    s.close()
    sys.exit()
elif msg == b'Nofile':  # 파일이 없는 경우
    print('server:', msg.decode()) 
    s.close()
    sys.exit()

# partial read
else:
    rx_size = len(msg)
    data = msg
    while rx_size < LENGTH:
        msg = s.recv(BUF_SIZE) 
        if not msg:
            s.close()
            sys.exit()
        data = data + msg
        rx_size += len(msg)    
    if rx_size < LENGTH:    # 예외처리 
        s.close()
        sys.exit()
    filesize = ntohl(int(data))
    print('server:', filesize)

rx_size = 0
# 서버로부터 수신할 파일 열기, 쓰기 전용
f = open(filename, 'wb') 

# 서버로부터 수신한 파일 내용을 수신하여 파일에 저장 
while rx_size < filesize:
    data = s.recv(BUF_SIZE)
    if not data:
        break
    f.write(data)
    rx_size += len(data)
# 예외처리
if rx_size < filesize: 
    s.close()
    sys.exit()    

print('Download complete') 

# 서버로 ‘Bye’ 메시지 전송
# 연결 종료
s.send(b'Bye') 
f.close()
s.close()