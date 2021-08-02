# recv() 해결책 : 해당 데이터를 모두 수신할 때까지, 반복적으로 데이터 수신

from socket import *

sock = create_connection(('localhost', 9999))

# 수신할 데이터 크기
data_size = 20
rx_size = 0
total_data = []

while rx_size < data_size:
    # 최대 4바이트 수신하도록 설정
    data = sock.recv(4)
    if not data:
        break
    rx_size += len(data)
    total_data.append(data.decode())
    print(total_data)   # 확인용

# 리스트의 각 요소 사이사이를 공백으로 채워줌
msg = ''.join(total_data)
print(msg)

sock.close()