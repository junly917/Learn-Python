#!/usr/bin/env python
#encoding:utf-8

import os,sys,socket

#运行软件时输出的内容
class run_display(object):
    info = '''
        --------Welcome to Transfer Machine --------
                    Auth:Junly
    '''
    print info
    while True:
            send_data = raw_input('==>: ').strip()
            if len(send_data) == 0 :
                continue
            elif send_data == 'quit' or send_data == 'exit':
                sys.exit(0)
            else:
                local_command()

#执行本地命令和login中转机
class local_command(object):
    '''执行本地命令以及login中转机'''
    def __init__(self,full_command):
        self.local_command =full_command
        command_name = full_command.split()[0]
        if hasattr(self,command_name):
            func = getattr(self,command_name)
            #login() #执行登录中转机
            func(full_command)                              #login() #执行登录中转机
        else:
            #执行本地的命令
            self.local_exec_command(self.local_command)    #执行本地的命令

    #执行本地命令
    def local_exec_command(self,full_command):
        """执行本地命令"""
        pass

    #登录到中转机操作
    def login(self,command):
        """登录到中转机操作"""
        local_login()

#登录远程服务器、上传、下载文件到远程服务器
class local_login(object):
    def __init__(self):
        pass

    #打印登录信息
    def login_display(self):
        pass

    #上传文件到远程服务器
    def upload(self):
        pass

    #下载文件
    def download(self):
        pass

    #登录远程服务器
    def login_server(self):
        pass

#登录远程中转机服务器
class login_server(object):
    '''
    登录远程服务器
    '''
    def __init__(self):
        pass

    #打印登录信息
    def display_server(self):
        pass

    #登录远程中转机服务器
    def login(self):
        pass

if __name__ == '__main__':
    run_display()

