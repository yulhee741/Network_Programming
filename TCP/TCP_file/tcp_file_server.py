# 파일 서버

# 예외처리
# filename에 해당되는 파일이 존재하지 않는 경우: 연결 종료
# 메시지가 수신되지 않거나, 다른 메시지가 오는 경우 
#   예) 파일 전송 완료 후 ‘Bye’ 메시지가 오지 않는 경우
#       → 일정 시간 기다린 후, 연결 종료

from socket import *
import os   # 파일크기 체크에 유용

BUF_SIZE = 1024 
LENGTH = 20
sock = socket(AF_INET, SOCK_STREAM) 
sock.bind(('', 7777)) 
sock.listen(10)

# 클라이언트 접속 대기
print('File server is running...')

while True:
    conn, addr = sock.accept()
    # 클라이언트로부터 ‘Hello’ 메시지 수신  
    msg = conn.recv(BUF_SIZE) 
    if not msg:
        conn.close()
        continue    # 다시 위로 가서 소켓을 새로 생성
    elif msg != b'Hello':
        print('client:', addr, msg.decode()) 
        conn.close()    # 클라이언트의 연결'만' 끊음, 종료해서는 안 됨
        continue
    else:
        # hello를 잘 수신한 경우, hello 출력
        print('client:', addr, msg.decode())
        # 클라이언트로 ‘Filename’ 메시지 전송 
        conn.send(b'Filename')

        # 클라이언트로부터 filename 수신
        msg = conn.recv(BUF_SIZE) 
        if not msg:
            conn.close()
            continue
        filename = msg.decode() 
        print('client:', addr, filename)

    try:
        # 파일 크기 
        filesize = os.path.getsize(filename)
    except: 
        # 파일이 없는 경우
        conn.send(b'Nofile') 
        conn.close() 
        continue
    else:
        # 클라이언트로 해당 파일의 크기를 전송 
        # htonl = 2바이트 양의 정수를 호스트 바이트 순서에서 네트워크 바이트 순서로 변환
        fs_net = htonl(filesize) 
        conn.send(str(fs_net).zfill(LENGTH).encode())
    
    # 해당 filename의 파일 열기, 읽기 전용
    # 클라이언트로 해당 파일 내용을 전송
    f = open(filename, 'rb') 
    data = f.read() 
    conn.sendall(data)


    # 클라이언트로부터 ‘Bye’ 메시지 수신
    msg = conn.recv(BUF_SIZE)
    if not msg:
        pass
    else:
        print('client:', addr, msg.decode())
    
    # 연결 종료
    f.close()
    conn.close()