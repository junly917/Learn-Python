#!/usr/bin/env python
#encoding:utf-8
'''
import socket
ip = ('localhost',9990)
sk = socket.socket()
sk.connect(ip)
while True:
    data = sk.recv(1024)
    print('data:',data)
    intputdate = raw_input("input>> ")
    sk.sendall(intputdate)
    if intputdate == 'exit':
        break
sk.close()
'''


import socket

ip = 'localhost'
port = 1999

client = socket.socket()
client.connect((ip,port))
while True:
    data = raw_input(">>:").strip()
    if len(data) ==0 :
        continue
    else:
        client.send(data.encode("utf-8"))
    #recvie result lens
    lens = client.recv(1024)
    # print('result lens :',lens)
    client.send(str(len(lens)))

    #recvier result   2222   1024  +1024
    result_len = 0
    result = ''
    while result_len < int(lens):

        data = client.recv(1024)

        result_len += len(data)

        result += data
    else:
        print(result)
client.close()



