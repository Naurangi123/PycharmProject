import socket

host='127.0.0.1'
port =5000

s=socket.socket()
s.connect((host,port))

str=input('Enter Data')

while str!='exit':
    s.send(str.encode())

    data=s.recv(1024)
    data=data.decode()
    print('From server:'+data)

    str=input('Enter data:')

s.close()