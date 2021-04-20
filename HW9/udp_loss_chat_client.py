from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True: 
    msg = input('-> ')
    # 재전송 횟수 
    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), ('localhost', port))
        sock.settimeout(2)  # 소켓의 timeout 설정. 해당 timeout 내 메시지
                            # 수신을 못하면 timeout 예외 발생
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue 
        else:
            break
    
    #if reTx > 3:
        #print('Timeout')
        #sock.sendto(b'Timeout', ('localhost', port))


    sock.settimeout(None)   # 소켓의 블로킹 모드 timeout 설정 
    while True:     # None인 경우, 무한정 블로킹됨
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            #print('Packet from {} lost!'.format(addr))
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break