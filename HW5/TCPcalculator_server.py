from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    result = 0
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            rsp = data.decode()
            r_list = rsp.split(' ')
            num1 = int(r_list[0])
            num2 = int(r_list[2])
            if r_list[1] == '+':
                result = num1 + num2
            elif r_list[1] == '-':
                result = num1 - num2
            elif r_list[1] == '*':
                result = num1 * num2
            elif r_list[1] == '/':
                result = round(float(num1) / float(num2), 1)
            result = str(result)
        except:
            client.send(b'Try again')
        else:
            client.send(result.encode())


    client.close()
