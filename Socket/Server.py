#!/usr/bin/env python
#encoding:utf-8
'''
import socket,os,commands

server = socket.socket()
server.bind(('localhost',2222))
server.listen(4)
print("Waiting New Connection...")
while True:
    conn,addr = server.accept()
    print("New Connection addr is" , addr)
    data = conn.recv(1024)
    print("Client Send Command is ", data)
    if len(data) == 0 :
        print("Disconnect to Server..")
    else:
        result = os.popen(data).read()
        print("result is :",result)
    conn.send(str(len(result)))
    conn.recv(1024)
    conn.send(result)
server.close()
'''

class my(object):
    def __init__(self):
        pass
    def login(self):
        pass
name = 'logins abc'
print(name.split()[0])
print(hasattr(my(),name.split()[0]))

name = ('a','b')
print(name[1])
