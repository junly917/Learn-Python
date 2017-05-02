#!/usr/bin/env python
#encoding:utf-8
import os,sys,commands
import time
import hashlib
import auth_login
import getpass
import sys,os

import run_display

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SSH_Client = PATH+"extend_ssh\Xshell.exe"
sys.path.append(PATH)
sys.path.append(SSH_Client)

class login_localhost_class(object):
    #设置相应的环境变量
    def __init__(self):
        self.info = '''
            --------Welcome to Office Transfer Machine --------
                        Auth:Junly
        '''
        self.host_dict={
            'host1':{'postion':'Office','ip':'192.168.2.2','port':'22'},
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
        #
        # print("func \t Description")
        # print("---------info---------------")
        # print(self.host_dict)
        # for k,v in self.func_desc.items():
        #     print k+':' +'\t'+v
        loginstatus = self.login()
        if loginstatus == 'quit' :
            self.conn_server

    #列出主机清单
    @property
    def showhostlist(self):
        print("Postion \t Host ip")
        # print("-----------aaa-------------")
        i= 1
        Host_New_Dict= hostlist={}
        for k,v in self.host_dict.items():
            hostlist[i] = v['ip']+',' +v['port']
            print('%5d:\t\t%5s  (%s:%s)' %(i,k,v['ip'],v['port']))
            Host_New_Dict[i] = str(k) + ','+str(v['ip']) + ',' + str(v['port'])
            i+=1

        return Host_New_Dict

    #输入账号密码并认证
    def login(self):
        count = 1
        while True:
            user = raw_input('Login:').strip()
            passwd = getpass.getpass('password:')
            # print(passwd)
            if len(user) ==0 or len(passwd) == 0:
                continue
            if count > 6:
                time.sleep(5)
            count +=1
            status = auth_login.auth(user,passwd,'dict')       #使用字典进行认证
            if status == 'login':
                print('auth Sucesses.')
                self.conn_server()

    #连接中转机服务器
    @property
    def conn_server(self):
        #列出主机清单
        Host_Dict  = self.showhostlist

        #['124.200.40.0 2002', '10.0.78.1 22', '192.168.1.1 22']
        #连接主机
        while True:

            chiose_host = raw_input( self.env_desc).strip()
            if chiose_host == 'quit' or chiose_host == 'exit':
                run_display.run_display().keyin()
                # sys.exit(0)
            elif chiose_host == 'l' or chiose_host == 'L':
                self.showhostlist
            else:
                try:
                    chiose_host = int(chiose_host)
                except Exception,e:
                    print("Please input digest,reinput")
                    continue
                try:
                    real_hostname = Host_Dict[chiose_host].split(',')[0]
                    real_ip = Host_Dict[chiose_host].split(',')[1]
                    real_port = Host_Dict[chiose_host].split(',')[2]
                    os.system('start xshell.exe %s:%s -newtab %s' %(real_ip,real_port,real_hostname))
                except  KeyError:
                    print("you input is nothing host ")


    #添加主机
    def Add_host(self):
        pass

    #删除主机
    def Del_host(self):
        pass

    #监控主机
    def Monitor_host(self):
        pass

    #上传文件到中转机服务器
    def upload(self):
        pass

    #下载文件到中转机服务器
    def download(self):
        pass


# s = login_localhost_class()
# s.conn_server
