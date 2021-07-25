# 예외처리
# 상대방과의 연결이 끊어졌을 때 send()/recv()를 호출하면 에러 발생
# 정상적인 프로그램 실행을 위해 예외 처리 필요

# 서버가 비정상적으로 종료되는 경우,
# 클라이언트의 send() 함수에서 connectionreseterror 발생 후 프로그램 종료
# 클라이언트가 비정상적으로 종료되는 경우,
# 서버의 recv() 함수에서 connectionreseterror 발생 후 프로그램 종료

from socket import * 

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM) 
sock.bind(('', port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept() 
print('connected by', remotehost, remoteport)

while True:
    try:
        data = conn.recv(BUFSIZE) 
    except:     # 수신할 때 예외 발생
        break 
    else:   # 예외 없는 경우
        if not data:    # 데이터가 없는 경우
            break
        print("Received message: ", data.decode())
    
    try:
        conn.send(data)
    except:     # 송신할 때 예외 발생
        break

conn.close()