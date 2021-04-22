from socket import *

sock = create_connection(('localhost', 9999))

data_size = 20
rx_size = 0
total_data = []

while rx_size < data_size:
    data = sock.recv(4)
    if not data:
        break
    rx_size += len(data)
    total_data.append(data.decode())
    print(total_data)   

msg = ''.join(total_data)
print(msg)

sock.close()