#!/usr/bin/env python
#encoding:utf-8

import socket

def handle_request(client):
    buf=client.recv(2048)
    client.sen("hello World")
def main():
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(('127.0.0.1',9990))
    sk.listen(10)
    while True:
        conn,addr = sk.accept()
        handle_request(conn)
        conn.close()


if __name__ == '__main__':
    main()







