#!/usr/bin/env python
#encoding:utf-8

import SocketServer,json
import os,sys,commands

host,port='192.168.101.98', 31397

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

    def handle(self):
        print("New Connect,from:%s" % self.client_address[0])
        data = self.request.recv(1024)
        userdata = (json.loads(data))
        auth_result = self.auth(userdata)
        self.request.send(auth_result)

        while True:
            data = self.request.recv(1024)
            ftp_opt = ftp_function()
            if not data :
                print("Disconnect from %s" % self.client_address[0])
            else:
                print("from %s send %s" % (self.client_address[0], data))
                print 'data:',data ,'type',type(data)
                cmds = data.split()[0]
                if hasattr(self,cmds):
                    func = getattr(self,cmds)
                    func()
                else:
                    self.command(data)

            # self.request.send('hello')
            if data == 'exit':
                break

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

    def get(self):
        print("get")

    def put(self):
        print("put")

    def command(self, cmds):
        cmds = commands.getstatusoutput(cmds)
        print cmds[1]
        self.request.send(cmds[1])




if __name__ == '__main__':
    s = SocketServer.ThreadingTCPServer((host,port),MyHandler)
    s.serve_forever()


