from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('calculation to send : ')
    if msg == 'q':
        break
    
    s.send(msg.encode())
    data = s.recv(1024)

    print('Received message: ', data.decode())
s.close()