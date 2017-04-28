#!/usr/bin/env python
#encoding:utf-8


import  socket,os

server,port="localhost",1996


client = socket.socket()
client.connect((server,port))


while True:
    data = raw_input(">>:").strip()
    if len(data) == 0 :
        continue
    else:
        filename = data.split()[1]
        client.send(filename)        #send filename
        recv_data = client.recv(1024)
        if recv_data == "file_exist":       # filename is exist
            file_exist = raw_input("file is exist ,please chioces (Y|N)").strip()
            client.send(file_exist)
        file_size = os.stat(filename).st_size     #send filesize
        client.send(str(file_size))
        client.recv(1024)
        name = open(filename)
        for line in name.read():
            client.send(line)

        name.close()






