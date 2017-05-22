#!/usr/bin/env python
#encoding:utf-8
import os,sys,commands
import time
import hashlib
import zkyg_TM.Client.client_core.auth_login
import getpass
import sys,os

import zkyg_TM.Client.client_core.display_local

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
SSH_Client = PATH+"extend_ssh\Xshell.exe"
sys.path.append(SSH_Client)


class Manager_Host(object):
    '''
    中转主机管理操作
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

    #获取主机清单
    def Get_hostlist(self):
        pass

