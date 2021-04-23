# 전송 손실을 가정한 UDP 서버 프로그램
# 30%의 데이터 손실이 발생한 것으로 가정
# 수신 데이터 중에서 70%에 대해서만 응답을 전송

from socket import *
import random   # 확률을 사용하므로

port = 5555
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
print('Listening....')

while True:
    data, addr = sock.recvfrom(BUFSIZE)

    # 일부러 70% 만 ack 전송
    if random.randint(1,10) <= 3:
        # 30% 내의 확률로 데이터 손실이 발생할 경우
        print('Packet from {} lost!'.format(addr))
        continue
    print('Packet is {} from {}'.format(data.decode(), addr))

    sock.sendto('ack'.encode(), addr)