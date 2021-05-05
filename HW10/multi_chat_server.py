import socket
import time
import threading

port = 2500
BUFFSIZE = 1024

clients = []

def chat(conn, addr):
    while True:
        data = conn.recv(BUFFSIZE)

        if 'quit' in data.decode():
            if conn in clients:
                print(addr, 'exited')
                clients.remove(conn)
        else:
            print(time.asctime() + str(addr) + ":" + data.decode())

            for client in clients:
                if client != conn:
                    client.send(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(5) # TCP용

print("Server started")


while True:
    conn, addr = s.accept() # TCP용

    print("connected by ", addr) # TCP용

    if conn not in clients:
        print("new client", addr)
        clients.append(conn)
    
    # 연결이 될 때마다 thread 생성
    th = threading.Thread(target=chat, args=(conn, addr, ))
    th.start()

s.close()