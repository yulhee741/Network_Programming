from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
dic = {}
while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    msg = data.decode()

    r_list = msg.split()
    mboxID, message = r_list[1], r_list[2:]

    if r_list[0] == 'send':
        if mboxID in dic:
            dic[mboxID].append(message)
        else:
            dic[mboxID] = [message]
        sock.sendto(b'OK', addr)

    if r_list[0] == 'receive':
        if not mboxID in dic or len(dic[mboxID]) < 1:
            sock.sendto(b'No messages', addr)
        else:
            sv_msg = "".join(dic[mboxID][0])
            del dic[mboxID][0]
            sock.sendto(sv_msg.encode(), addr)
            
            
    print(dic)

    