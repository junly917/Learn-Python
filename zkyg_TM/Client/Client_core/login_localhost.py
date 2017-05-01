#!/usr/bin/env python
#encoding:utf-8
import os,sys
import time
import hashlib
import auth_login

class login_localhost_class(object):
    #设置相应的环境变量
    def __init__(self):
        self.info = '''
            --------Welcome to Office Transfer Machine --------
                        Auth:Junly
        '''
        self.host_dict={
            'host1':{'postion':'Office','ip':'192.168.1.1','port':'22'},
            'host2':{'postion':'DG-IDC','ip':'10.0.78.1','port':'22'},
            'host3':{'postion':'TJ-IDC','ip':'124.200.40.0','port':'2002'},
        }
        self.func_desc = {
            'C or c':'Connection IDC Transfer Machine ',
            'E or e':'Exit Program.return Transfer Machine',

        }
        self.env_desc='Connection host:'

    #打印登录信息
    @property
    def display_login_info(self):
        '''打印显示信息'''
        print self.info
        self.login()
        print("func \t Description")
        print("---------info---------------")
        print(self.host_dict)
        for k,v in self.func_desc.items():
            print k+':' +'\t'+v


    #列出主机清单
    @property
    def showhostlist(self):
        print("Postion \t Host ip")
        # print("-----------aaa-------------")
        i= 1
        hostlist={}
        for k,v in self.host_dict.items():
            hostlist[i] = v['ip']+',' +v['port']
            print('%5d:\t\t%5s  (%s:%s)' %(i,k,v['ip'],v['port']))
            i+=1
        return hostlist

    #输入账号密码并认证
    def login(self):
        count = 1
        while True:
            user = raw_input('Login:').strip()
            passwd = raw_input('password:').strip()
            if len(user) ==0 or len(passwd) == 0:
                continue
            if count > 6:
                time.sleep(5)
            count +=1
            status = auth_login.auth(user,passwd,'dict')       #使用字典进行认证
            if status == 'login':
                print('认证成功.')
                self.conn_server()

    #连接中转机服务器
    @property
    def conn_server(self):
        #列出主机清单
        hostlist = self.showhostlist
        print hostlist
        #['124.200.40.0 2002', '10.0.78.1 22', '192.168.1.1 22']
        #连接主机
        while True:
            try:
                conn = int(raw_input( self.env_desc).strip())
            except Exception,e:
                print("Please input digest,reinput")
                continue
            if conn == 'quit':
                sys.exit(0)
            else:
                try:
                    print(hostlist[conn])
                    conn_host = hostlist[conn].split(',')[0]
                    conn_port = hostlist[conn].split(',')[1]
                    os.popen('ssh root@%s %s' %(conn_host,conn_port))
                except  KeyError:
                    print("you input is nothing host ")

                # os.popen('ssh %s %s' %() )
        #添加主机

        #删除主机

        #监控主机

    #上传文件到中转机服务器
    def upload(self):
        pass

    #下载文件到中转机服务器
    def download(self):
        pass


s = login_localhost_class()
s.conn_server
