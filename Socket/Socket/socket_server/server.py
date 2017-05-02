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

    def __writefile(self,filename,filename_dict):
        '''
        写入文件当中
        :param filename: 
        :param filename_dict: 
        :return: 
        '''
        filename = filename_dict["name"]
        file_count = 0
        num = 1
        file_content = ''
        f =open(filename, 'wb')
        if filename_dict['len'] > 1024:  # 文件很大
            print('gt 1024 write')
            print 'file count is :', type(file_count), 'filename_dict len is:', type(filename_dict['len'])
            while file_count < filename_dict['len']:
                file_data = self.request.recv(1024)
                file_count += len(file_data)
                if file_data == 'finished':
                    print('write data is finished')
                    break
                print('file conut is :%s' % file_count,filename_dict['len'])
                file_content +=file_data
                print(file_count < filename_dict['len'])
            f.write(file_content)
        else:
            print('lt 1024 write')
            file_data = self.request.recv(1024)  # 文件较小
            f.write(file_data)  # 文件写入
        f.close()

    def put(self):
        # print ('put file is ')

        print('recv to dicts')
        recv_data =self.request.recv(1024)            #接收字典内容
        filename_dict = json.loads(recv_data)

        print("filename dict is:%s" % filename_dict)
        filename=filename_dict["name"]
        file_count =0
        num = 1
        file_content = ''

        if os.path.isfile(filename):        #检测文件是否存在，提示是否覆盖
            print('check file is exist.')
            filename_dict["status"] = 'exist'     #文件己存在，需要客户端处理
            print("send filename_dict['status']")
            self.request.send(filename_dict["status"])    #发送字典回复
            overrid = self.request.recv(1024)
            if overrid == 'y' or overrid == 'Y':    #覆盖操作
                self.__writefile(filename,filename_dict)
                # print('override write')
                # with open(filename, 'wb') as fwrite:
                #     if filename_dict['len'] > 1024:  # 文件很大
                #         print('gt 1024 write')
                #         print 'file count is :' ,type(file_count),'filename_dict len is:',type(filename_dict['len'])
                #         while file_count < filename_dict['len']:
                #             file_data = self.request.recv(1024)
                #             file_count += len(file_data)
                #             file_content +=file_data
                #         fwrite(file_content)
                #         print('write data is finished')
                #     else:
                #         print('lt 1024 write')
                #         file_data = self.request.recv(1024)  # 文件较小
                #         fwrite.write(file_data)  # 文件写入
            else:           #不覆盖操作
                print('Not override write')
                while True:
                    if os.path.isfile(filename=filename + '.' + num):
                        num += 1
                        continue
                    else:
                        self.__writefile(filename,filename_dict)
                        # with open(filename, 'wb') as fwrite:
                        #     if filename_dict['len'] > 1024:  # 文件很大
                        #         print('gt 1024 write')
                        #         print 'file count is :', type(file_count), 'filename_dict len is:', type(
                        #             filename_dict['len'])
                        #         while file_count < filename_dict['len']:
                        #             file_data = self.request.recv(1024)
                        #             file_count += len(file_data)
                        #             file_content+=file_data
                        #             print("continue while recv")
                        #         print('write data is finished')
                        #         fwrite(file_content)  # 文件写入
                        #
                        #     else:
                        #         print('lt 1024 write')
                        #         file_data = self.request.recv(1024)  # 文件较小
                        #         fwrite.write(file_data)  # 文件写入

        else:
            print('check file is not exist.')
            filename_dict["status"]="not_exist"
            self.request.send(filename_dict["status"])
            print("write file")
            self.__writefile(filename, filename_dict)
            # filename = open(filename, 'wb')
            # if int(filename_dict['len']) > 1024:  # 文件很大
            #     while file_count < int(filename_dict['len']):
            #         file_data = self.request.recv(1024)
            #         file_count += len(file_data)
            #         filename.write(file_data)  # 文件写入
            #         print('file count is %s' % file_count)
            # else:
            #     file_data = self.request.recv(1024)  # 文件较小
            #     filename.write(file_data)  # 文件写入
            # filename.close()

    def handle(self):
        while True:
            result_dict = {}
            try:
                print("等待客户端传送数据.")
                recv_cmd = self.request.recv(1024)          #接收客户端传过来的命令
                print("recv cmd is:" , recv_cmd)
                self.request.send('recvd')
                cmds = recv_cmd.split()[0]
                print('cmds is:',cmds)

                if hasattr(self,cmds):                #如果是get put 操作则执行get和put 函数
                    print('hassattr :%s' %cmds)
                    cmds_patter = recv_cmd.split()[1]
                    func = getattr(self,cmds)
                    func()
                else:
                    cmd_result = commands.getstatusoutput(recv_cmd)
                    print('cmd_result:%s' % cmd_result[1])

                    result_dict["type"] = 'cmd'             #生成字典{类型，状态，长度}
                    result_dict["status"] = cmd_result[0]
                    result_dict["len"]=len(cmd_result[1])
                    # print('result_dict:' ,result_dict)
                    print('send dict.')
                    self.request.send(json.dumps(result_dict))  #发送字典

                    print('recv dict response')
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
    host, port = '0.0.0.0', 3991
    start = SocketServer.ThreadingTCPServer((host,port),MyFtpServer)
    start.serve_forever()



