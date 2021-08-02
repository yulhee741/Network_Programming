# recv() 해결책 : 해당 데이터를 모두 수신할 때까지, 반복적으로 데이터 수신

from socket import *

server = create_server(('', 9999))
conn, addr = accept()

conn.send(b'This is IoT world!!!')
conn.close()