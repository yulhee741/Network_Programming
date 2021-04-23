# 명령행 인자 에코 클라이언트 프로그램

from socket import *
import argparse # 모듈 추가 필요

s = socket(AF_INET, SOCK_STREAM)
parser = argparse.ArgumentParser() # 파서 객체 생성

# 인자 추가하기
parser.add_argument('-s', default='localhost') 
parser.add_argument('-p', type=int, default=2500) 

# 인자 파싱하기
args = parser.parse_args()

s.connect((args.s, args.p))
print('connected to ', args.s, args.p)

while True:
    msg = input("Message to send: ")
    if msg == 'q':
        break
    s.send(msg.encode()) 
    data = s.recv(1024) 
    if not data:
        break
    print('Received message: ', data.decode()) 

s.close()