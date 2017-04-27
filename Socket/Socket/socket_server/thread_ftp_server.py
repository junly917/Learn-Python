#!/usr/bin/env python
#encoding:utf-8

import SocketServer,json
import os,sys,commands

host,port='localhost', 31394

class ftp_function(object):
    '''
    
    '''
    def __init__(self):
        pass

    def auth(self,data):
        user = data.get('user')
        passwd = data['passwd']
        if passwd == 'cb8757a672fed7bfedf6a4eba5a9134c':
            print("reciv user %s login " % user)

        if user == 'admin':
            if passwd == 'cb8757a672fed7bfedf6a4eba5a9134c':
                auth_result = 'login'
                print("%s login scuesses" % user)
            else:
                print("user or passwd is Wrong...")
        else:
            auth_result = 'failed'
        return auth_result



class MyHandler(SocketServer.BaseRequestHandler):

    def auth(self,data):
        user = data.get('user')
        passwd = data['passwd']
        if passwd == 'cb8757a672fed7bfedf6a4eba5a9134c':
            print("reciv user %s login " % user)

        if user == 'admin':
            if passwd == 'cb8757a672fed7bfedf6a4eba5a9134c':
                auth_result = 'login'
                print("%s login scuesses" % user)
            else:
                print("user or passwd is Wrong...")
        else:
            auth_result = 'failed'
        return auth_result

    def get(self,data):         #send get filename
        result = {}
        filename = data.split()[1]
        if os.path.isfile(filename):
            filesize = os.stat(filename).st_size
            result["type"] = 'put'
            result["len"] = "%d" % filesize
            result["status"] = 'get file %s' % filename
            print  result,filesize

            self.request.send(json.dumps(result))       #发送一个文件长度、type的字典
            self.request.recv(1024)
            f = open(filename,'r')
            for line in f:
                self.request.send(f)
            print("file send done.")
        else:
            result["type"] = 'put'
            result["len"] = -1
            result["status"] = 'file %s is not exist' % filename
            print result
            self.request.send(json.dumps(result))

    def put(self,data):
        print("put",data)

    def command(self, data):
        '''
            recv cmds commands
        '''
        result = {}
        # cmds = os.popen(cmds).read()        #exec cmds and get exec result
        cmds = commands.getstatusoutput(data)
        print('commands is :%s' % data)
        result["type"]='cmd'
        result["len"]=len(cmds[1])
        result["status"] = cmds[0]

        if cmds[1] == '':                                   #如果命令执行完，但是没有返回结果
            result['info'] ='commands exe finash,but return Null'
            result["len"] = 0
            print result
            self.request.send(json.dumps(result))
        else:
            print 'send:',result
            self.request.send(json.dumps(result))             #send exe commands resultxfjs

        #接收客户端的请求结果
        print('recv:.....')
        self.request.recv(1024)             #recive continue

        # 返回结果给客户端
        result["info"] = cmds[1]
        print 'cmds[1]:',result["info"]

        self.request.send(result["info"])
        print('result[info]:',resutl['info'])
    def handle(self):
        print("New Connect,from:%s" % self.client_address[0])
        '''
        data = self.request.recv(1024)
        userdata = (json.loads(data))
        auth_result = self.auth(userdata)
        self.request.send(auth_result)
        '''
        while True:
            try:

                data = self.request.recv(1024)
                print("接收发过来的命令：%s" % data)
                if data == '':
                    #raise err print disconnect
                    raise "error"
                else:
                    ftp_opt = ftp_function()
                    print("from %s send %s" % (self.client_address[0], data))
                    cmds = data.split()[0]
		    print("cmds is :",cmds)
                    if hasattr(self,cmds):
                        func = getattr(self,cmds)
			print('func name is :',func)
                        func(data)
                    else:
                        self.command(data)
            except Exception as e :
                print("Disconnect from %s" % self.client_address[0])
                break


if __name__ == '__main__':
    s = SocketServer.ThreadingTCPServer((host,port),MyHandler)
    s.serve_forever()


