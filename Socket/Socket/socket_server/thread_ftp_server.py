#!/usr/bin/env python
#encoding:utf-8

import SocketServer,json
import os,sys,commands

host,port='localhost', 31397

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

    def command(self, cmds):
        '''
            recv cmds commands
        '''
        result = {}
        cmds = os.popen(cmds).read()        #exec cmds and get exec result
        result["type"]='cmd'
        result["len"]=len(cmds)
        result["status"] = 'ok'

        self.request.send(json.dumps(result))        #send result length
        self.request.recv(1024)             #recive continue
        self.request.send(cmds)             #send exe commands result


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
                if data == '':
                    #raise err print disconnect
                    raise "error"
                else:
                    ftp_opt = ftp_function()
                    print("from %s send %s" % (self.client_address[0], data))
                    cmds = data.split()[0]
                    if hasattr(self,cmds):
                        func = getattr(self,cmds)
                        func(data)
                    else:
                        self.command(data)

                    # self.request.send('hello')
                    if data == 'exit':
                        break
            except Exception as e :
                print("Disconnect from %s" % self.client_address[0])
                break




if __name__ == '__main__':
    s = SocketServer.ThreadingTCPServer((host,port),MyHandler)
    s.serve_forever()


