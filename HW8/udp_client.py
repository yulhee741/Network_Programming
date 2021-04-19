from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    input_msg = input('Enter the message("send mboxId message" or "recei mboxId"): ')
    sock.sendto(input_msg.encode(), ('localhost', port))

    if input_msg == 'quit':
        break

    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())

