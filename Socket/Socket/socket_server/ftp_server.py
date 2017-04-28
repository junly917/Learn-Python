#!/usr/bin/env python
#encoding:utf-8

import socket,os,commands


ip,port = 'localhost',1996

server = socket.socket()
server.bind((ip,port))
server.listen(3)
print("Connection waiting..")
while True:
    conn,port = server.accept()
    print("New Connection Addr is ",port)
    while True:

        file_name = conn.recv(1024)
        if not file_name :
            print("Disconnect from client")
            break
        if os.path.isfile(file_name):
            conn.send("file_exist")
            opt = conn.recv(1024)
            if opt == 'N':
                file_name=file_name + '_new'
        else:
            conn.send(str(len(file_name)))

        file_size = conn.recv(1024)
        conn.send(str(len(file_size)))
        recv_size = 0
        print('file size is:',len(file_size))
        with open(file_name,"wb") as f:
            while recv_size < int(file_size):
                file_data = conn.recv(1024)
                recv_size +=len(file_data)
                f.write(file_data)
                print('recv_size is:', recv_size, '/' ,file_size)
            else:
                print("file transfer done. file size is:",file_size,"recv file size si:",recv_size)
                f.close()




