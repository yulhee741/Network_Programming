# 예외처리
# 상대방과의 연결이 끊어졌을 때 send()/recv()를 호출하면 에러 발생
# 정상적인 프로그램 실행을 위해 예외 처리 필요

# 서버가 비정상적으로 종료되는 경우,
# 클라이언트의 send() 함수에서 connectionreseterror 발생 후 프로그램 종료
# 클라이언트가 비정상적으로 종료되는 경우,
# 서버의 recv() 함수에서 connectionreseterror 발생 후 프로그램 종료

import socket

port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(address)

while True:
    msg = input("Message to send: ")
    try:
        bytesSent = s.send(msg.encode())
    except:     # 송신할 때 예외 발생
        print('connection closed')
        break 
    else:
        # 전송 내용 출력
        print("{} bytes send".format(bytesSent))

    try:
        data = s.recv(BUFSIZE)
    except:     # 수신할 때 예외 발생
        print('connection closed') 
        break
    else:
        if not data:    # 데이터 없는 경우
            break
        print("Received message: %s" %data.decode()) 
s.close()