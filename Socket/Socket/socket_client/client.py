#!/usr/bin/env python
#encoding:utf-8

import  socket,json,sys,os,commands,time

class ftp_opt(object):
    def __init__(self,host,port):
        self.client = socket.socket()
        self.client.connect((host, port))
        self.inputsomething()

    def inputsomething(self):                       #检测输入的内容，是否为命令、还是文件上传下载操作
        while True:
            try:
                send_data = raw_input('-->').strip()
            except Exception,e:
                print('Program exit')
                sys.exit(0)
            if len(send_data) == 0 :
                continue
            elif send_data == 'quit' or send_data == 'exit':
                sys.exit(0)
            elif hasattr(self,send_data.split()[0]):
                func = getattr(self,send_data.split()[0])
                func(send_data,send_data.split()[1])
            elif send_data in ['rls','rll','rcd','rrm']:
                 self.exec_commands(send_data)
            else:
                self.local_commands(send_data)

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
        # print(cmds,filename)
        print('Send cmds:',cmds)
        self.client.send(cmds)              #将命令传送给服务器

        filename_dict = {}
        filename_dict['type'] = 'put'
        filename_dict['name'] = filename
        if os.path.isfile(filename):         # 检测本地文件是否存在
            # print(os.path.isfile(filename))
            filename_dict["len"] = os.path.getsize(filename)
            filename_dict["status"] = 0
            filename_dict['info'] = filename + ' file is exist.'
            # print(filename,filename_dict,filename_dict['len'])
            # print("filename is %s" % filename)

            print("send dict to Server.")
            self.client.send(json.dumps(filename_dict))    # 发送字典过去包含文件大小，文件名称，类型,状态
            time.sleep(0.5)
            print("waiting response dict")
            client_recv = self.client.recv(1024)           # 接收回传的信息
            print 'client_recv:',client_recv

            if client_recv== 'exist' :                # 1表示服务器己存在此文件
                while True:
                    chioces = raw_input('are you ovveride file %s (y|n):' % filename_dict['name'])
                    if chioces == 'y' or chioces == 'Y' or chioces == 'n' or chioces == 'N':
                        print('user chiose is %s' %chioces)
                        self.client.send(chioces)
                        break
                    else:
                        continue
                f = open(filename, 'r')  # 发送文件
                print('file exist start write..')
                i=0
                for line in f.read():
                    self.client.send(line)
                    i +=1
                    print('send line num is %s'% i)

                    # print("send done.")             # 传输完成
            else:       #服务器不存在此文件
                print('file not exist start write..')
                f = open(filename, 'r')  # 直接发送文件
                print('send file .....')
                i = 1
                for line in f.read():
                    self.client.send(line)
                    #time.sleep(0.3)
                    # i +=1
                    # print('send line num is %s'% i)
            f.close()
        else:
            # 检测本地文件不存在
            print("%s is not exist" % filename)

    def exec_commands(self,send_data):

        print('exec commands: %s'% send_data)
        send_data=send_data.split('r')[1:]
        send_data = ''.join(send_data)

        self.client.send(send_data)                                         #发送命令操作到服务器

        result_dict = json.loads(self.client.recv(1024))                    #接收命令的结果长度，类型，状态字典

        recv_result = self.client.send('client send data')                #发送接收命令执行的结果请求

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

    def local_commands(self,commands):
        result = os.popen(commands).read()
        if len(result) ==0:
            result = 'Nothing display'
        print result

if __name__ == '__main__':
    ftp_opt('192.168.101.98',3991)
