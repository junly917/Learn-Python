#!/usr/bin/env python
#encoding:utf-8
import  sys,os,commands,time
import auth_login
class local_command(object):
    '''执行本地命令以及login中转机'''
    def __init__(self,full_command):
        self.local_command =full_command
        command_name = full_command.split()[0]
        if hasattr(self,command_name):
            func = getattr(self,command_name)
            #login() #执行登录中转机
            func(full_command)                              #执行登录中转机
        else:
            #执行本地的命令
            self.local_exec_command(self.local_command)    #执行本地的命令

    #执行本地命令
    def local_exec_command(self,full_command):
        """执行本地命令"""
        result = os.popen(full_command).read()
        if len(result) ==0:
            result = 'Nothing display'
            print result

    #登录到中转机操作
    def login(self,cmd):
        """登录到中转机操作"""
        commands.getstatusoutput('clear')
        auth_login().login_server()