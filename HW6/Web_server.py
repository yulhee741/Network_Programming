from socket import *

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('', 80))
s.listen(10) 

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    filename = req[0].split()[1][1:]

    if filename == '':
        filename = 'index.html'

    try:
        filename = req[0].split()[1][1:]

        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
            data = f.read()
            c.send(b'HTTP/1.1 200 OK\r\n')
            c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
            c.send(b'\r\n')
            c.send(data.encode('euc-kr', 'ignore'))
        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
            data = f.read()
            c.send(b'HTTP/1.1 200 OK\r\n')
            c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
            c.send(b'\r\n')
            c.send(data)
        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
            data = f.read()
            c.send(b'HTTP/1.1 200 OK\r\n')
            c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
            c.send(b'\r\n')
            c.send(data)
        else:
            raise Exception # 예외 발생

    except Exception as e:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')

    c.close()