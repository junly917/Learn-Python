#!/usr/bin/env python
#encoding:utf-8

import SocketServer,sys,json,os,sys,commands



class MyFtpServer(SocketServer.BaseRequestHandler):

    def get(self,cmds_patter):
        print('Start get file..')

        filename = cmds_patter          #获取文件名称
        filename_dict = {}
        filename_dict['type'] = 'download_file'
        if os.path.isfile(filename):         # 检测文件是否存在
            # print(os.path.isfile(filename))
            filename_dict["len"] = os.path.getsize(filename)
            filename_dict["status"] = 0
            filename_dict['info'] = '%s file is exist.' % filename

            print("filename is %s" % filename)
            self.request.send(json.dumps(filename_dict))    # 发送文件大小，文件名称，类型,状态

            client_recv = self.request.recv(1024)           # 接收客户端回传的信息
            print('client send data is: %s ' % client_recv)

            f = open(filename,'r')          # 发送文件给客户端
            for line in f:
                print('send file .....')
                self.request.send(line)

            print("send done.")             # 传输完成
        else:
            # 发送文件不存在信息给客户端
            filename_dict["len"]=0
            filename_dict["status"]=-1
            filename_dict['info']='%s file is not exist.' % filename
            print("file %s is not exist" % filename)
            self.request.send(json.dumps(filename_dict))

    def put(self):
        print ('put file is ')
        filename={}
        filename_dict = self.request.recv(1024)
        filename = filename_dict['name']
        file_count =0
        num = 1
        print('check file is exist.')
        if os.path.isfile(filename):        #检测文件是否存在，提示是否覆盖
            filename_dict["status"] = 1     #文件己存在，需要客户端处理
            print("send filename_dict['status']")
            self.request.send(filename_dict["status"])
            overrid = self.request.recv(1024)
            if overrid == 'y' or overrid == 'Y':    #覆盖操作
                print('override write')
                filename = open(filename, 'wb')
                if int(filename_dict['len']) > 1024:  # 文件很大
                    while file_count < int(filename_dict['len']):
                        file_data = self.client.recv(1024)
                        file_count += len(file_data)
                        filename.write(file_data)  # 文件写入
                else:
                    file_data = self.client.recv(1024)  # 文件较小
                    filename.write(file_data)  # 文件写入
                filename.close()
            else:           #不覆盖操作
                print('Not override write')
                while True:
                    if os.path.isfile(filename=filename + '.' + num):
                        num += 1
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



    def handle(self):
        while True:
            result_dict = {}
            try:
                recv_cmd = self.request.recv(1024)          #接收客户端传过来的命令
                cmds = recv_cmd.split()[0]
                print (cmds,recv_cmd.split()[1])
                #
                # print ('recv_cmd:%s,cmds:%s,cmds_patter:%s' %(recv_cmd,cmds,cmds_patter))

                if hasattr(self,cmds):                #如果是get put 操作则执行get和put 函数
                    cmds_patter = recv_cmd.split()[1]
                    func = getattr(self,cmds)
                    func()
                else:
                    cmd_result = commands.getstatusoutput(recv_cmd)
                    print('cmd_result:%s' % cmd_result[1])

                    result_dict["type"] = 'cmd'             #生成字典{类型，状态，长度}
                    result_dict["status"] = cmd_result[0]
                    result_dict["len"]=len(cmd_result[1])
                    print(result_dict)

                    self.request.send(json.dumps(result_dict))  #发送字典

                    recv_result = self.request.recv(1024)       #接受客户端发过来的请求结果
                    print('recv_result: %s' % recv_result)

                    if len(cmd_result[1]) == 0 :                #判断结果为是为空，如果为空则发送相应内容，不为空发送内容
                        result_dict['info'] = 'command exec sucesses,but not data.'
                        print('command exec sucesses.')
                        self.request.send(result_dict['info'])
                    else:
                        print('------------')
                        self.request.send(cmd_result[1])
                        print(cmd_result[1])
            except Exception as e:
                print("client %s disconnect." % self.client_address[0])
                break

if __name__ == '__main__':
    host, port = 'localhost', 1996
    start = SocketServer.ThreadingTCPServer((host,port),MyFtpServer)
    start.serve_forever()



