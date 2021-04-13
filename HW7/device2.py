from socket import *
import sys
import random

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE)
    if not msg:
        sock.close()
        continue
    elif msg == b'quit':
        print('client: ', addr, msg.decode())
        conn.close()
        sys.exit()
    elif msg == b'Request':
        print('client: ', addr, msg.decode())

        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)

        data = f'{heartbeat} {steps} {cal}'
        conn.send(data.encode())