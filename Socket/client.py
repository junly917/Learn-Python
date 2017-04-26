#!/usr/bin/env python
#encoding:utf-8

import  socket
client = socket.socket()
client.connect(('localhost',2222))
while True:
    data = raw_input("-->>: ").strip()
    if len(data) == 0 :
        continue
    else:
        client.send(data)       #发送命令
        result_lens = client.recv(1024) #接收结果的长度
        client.send(result_lens)    #发送收到结果的长度
        res_len = 0                 #接收执行的结果
        result=''
        while res_len < int(result_lens):
            tmp_result = client.recv(1024)
            res_len += len(tmp_result)
            result += tmp_result
        print(result.encode().decode("utf-8"))





