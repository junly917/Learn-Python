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


class manager_host(object):
    '''
    主机管理操作
    '''
    def __init__(self):
        pass

    #添加主机
    def Add_host(self):
        pass

    #删除主机
    def Del_host(self):
        pass

    #监控主机
    def Monitor_host(self):
        pass



