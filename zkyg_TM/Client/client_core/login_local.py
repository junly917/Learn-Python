#!/usr/bin/env python
#encoding:utf-8
import os,sys,commands
import time
import hashlib
import getpass
from zkyg_TM.Client.client_core.auth_passwd import auth,md5sums

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)
SSH_Client = BASEDIR+"extend_ssh\Xshell.exe"
sys.path.append(SSH_Client)

from zkyg_TM.Client.client_core.local_tm_manager import Connect_tm
# import zkyg_TM.Client.client_core.display_local.Display_func


class login_localhost(object):
    def __init__(self):
        self.info = '''
            --------Welcome to Office Transfer Machine --------
                        Auth:Junly
        '''
    #打印登录信息
    @property
    def display_login_info(self):
        '''打印显示信息'''
        print self.info
        loginstatus = self.login()
        if loginstatus == 'quit' :
            self.conn_server
    #输入账号密码并认证
    def login(self):
        count = 1
        while True:
            user = raw_input('Login:').strip()
            # passwd = getpass.getpass('password:')
            passwd = raw_input('password:').strip()
            if count > 6:
                time.sleep(5)
            count +=1
            if len(user) ==0 or len(passwd) == 0:
                continue
            status = auth(user,passwd,'dict')       #使用字典进行认证
            if status == 'login':
                print('auth Sucesses.')
                Connect_tm().conn_server
