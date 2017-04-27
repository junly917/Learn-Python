#!/usr/bin/env python
#encoding:utf-8

import  socket,json,sys,os,commands

class ftp_opt(object):
    def __init__(self,host,port):
        self.client = socket.socket()
        self.client.connect((host, port))
        self.inputsomething()

    def inputsomething(self):                       #检测输入的内容，是否为命令、还是文件上传下载操作
        while True:
            send_data = raw_input('-->').strip()
            if len(send_data) == 0 :
                continue
            elif send_data == 'quit' or send_data == 'exit':
                sys.exit(0)
            elif hasattr(self,send_data.split()[0]):
                func = getattr(self,send_data.split()[0])
                func(send_data,send_data.split()[1])
            else:
                self.exec_commands(send_data)

    def get(self,send_data,filename):
        self.client.send(send_data)
        print('self get filename..')
        filename_dict = self.client.recv(1024)  #接收文件属性的字典
        print('filename_dict:',filename_dict)
        self.client.send('reved_file')
        print('send reved_file:%s' % filename)
        print(os.path.isfile(filename))
        if os.path.isfile(filename):    #检测文件是否存在，提示是否覆盖

            file_count = 0
            file_data = ''
            num = 1
            while True:
                chiose = raw_input('%s file is exist,are you override.').strip()
                if chiose == 'y' or chiose == 'Y':  #覆盖文件操作
                    self.client.send(chiose)
                    print('override write')
                    filename = open(filename, 'wb')
                    print("filename_dict['len']:",type(filename_dict['len']))
                    if int(filename_dict['len']) > 1024: #文件很大
                        while file_count < int(filename_dict['len']):
                            file_data= self.client.recv(1024)
                            file_count += len(file_data)
                            filename.write(file_data)   #文件写入
                    else:
                        file_data = self.client.recv(1024) #文件较小
                        filename.write(file_data)       #文件写入
                    filename.close()
                elif chiose == 'n' or chiose == 'N': #不覆盖文件操作
                    print('Not override write')
                    while True:
                        if os.path.isfile(filename=filename+'.'+num):
                            num+=1
                            continue
                        else:
                            filename = open(filename, 'wb')
                            if filename_dict['len'] > 1024:  # 文件很大
                                while file_count < int(filename_dict['len']):
                                    file_data = self.client.recv(1024)
                                    file_count += len(file_data)
                                    filename.write(file_data)  # 文件写入
                            else:
                                file_data = self.client.recv(1024)  # 文件较小
                                filename.write(file_data)  # 文件写入
                            filename.close()
                else:
                    print('什么都没有干！')
                    continue

    def put(self,cmds,filename):
        print(cmds,filename)
        self.client.send(cmds)              #将命令传送给服务器
        print('self put file')
        filename_dict = {}
        filename_dict['type'] = 'put_file'
        filename_dict['name'] = filename
        if os.path.isfile(filename):         # 检测本地文件是否存在
            # print(os.path.isfile(filename))
            filename_dict["len"] = os.path.getsize(filename)
            filename_dict["status"] = 0
            filename_dict['info'] = filename ,' file is exist.'

            # print("filename is %s" % filename)

            self.client.send(json.dumps(filename_dict))    # 发送字典过去包含文件大小，文件名称，类型,状态

            client_recv = self.client.recv(1024)           # 接收回传的信息
            print('client send data is: %s ' % client_recv)
            if client_recv == 1 or client_recv == '1':
                while True:
                    chioces = raw_input('are you ovveride file %s' % filename_dict['name'])
                    if chioces == 'y' or chioces == 'Y' or chioces == 'n' or chioces == 'N':
                        self.client.send(chioces)
                    else:
                        continue
            f = open(filename,'r')          # 发送文件
            for line in f:
                print('send file .....')
                self.client.send(json.dumps(line))

            print("send done.")             # 传输完成
        else:
            print("file %s is not exist" % filename)

    def exec_commands(self,send_data):

        self.client.send(send_data)                                      #发送命令操作到服务器

        result_dict = json.loads(self.client.recv(1024))                 #接收命令的结果长度，类型，状态字典

        recv_result = self.client.send('client send data')                    #发送接收命令执行的结果请求

        if int(result_dict["len"]) > 1024:
            count = 0
            part_result = 0
            while part_result < int(result_dict["len"]):
                a_part = self.client.recv(1024)
                count += len(a_part)
                part_result += a_part
            print('recv is Finished.')
        else:
            recv_result = self.client.recv(1024)
            print(recv_result)


if __name__ == '__main__':
    ftp_opt('localhost',1996)
