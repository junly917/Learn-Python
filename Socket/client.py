#!/usr/bin/env python
#encoding:utf-8

import socket
ip_port=('127.0.0.1',9990)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
while True:
    print('Server Starting...')
    conn,addr = sk.accept()
    client_data = conn.recv(2048)
    print("Client Send Message: %s" %client_data)
    conn.sendall("Don't Send")
    conn.close()

