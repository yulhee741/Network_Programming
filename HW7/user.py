from socket import *
import time
BUF_SIZE = 1024
LENGTH = 20


while True:
    user_input = input()

    # 디바이스 1 소켓
    device1_socket = socket(AF_INET, SOCK_STREAM)
    device1_socket.connect(('localhost', 7777))

    # 디바이스 2 소켓
    device2_socket = socket(AF_INET, SOCK_STREAM)
    device2_socket.connect(('localhost', 8888))

    if user_input == '1':
        device1_socket.send(b'Request')
        msg = device1_socket.recv(BUF_SIZE)

        temp, humid, illum = msg.decode().split(' ')
        now = time.strftime('%c', time.localtime(time.time()))
        string = now + f': Device1: Temp={temp}, Humid={humid}, Illum={illum}\n'
#        print(string)
        f = open('data.txt', 'a')
        f.write(string)
        f.close()

    elif user_input == '2':
        device2_socket.send(b'Request')
        msg = device2_socket.recv(BUF_SIZE)

        heartbeat, steps, cal = msg.decode().split(' ')
        now = time.strftime('%c', time.localtime(time.time()))
        string = now + f': Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}\n'
#        print(string)
        f = open('data.txt', 'a')
        f.write(string)
        f.close()

    elif user_input == 'quit':
        device1_socket.send(b'quit')
        device2_socket.send(b'quit')
        break