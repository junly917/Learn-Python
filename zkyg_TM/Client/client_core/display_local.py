#!/usr/bin/env python
#encoding:utf-8
import os,sys,commands
import time
import hashlib,getpass
import auth_login
import sys,os
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)

# import local_exec
from login_local import login_localhost_class
# print sys.path

class Display_func(object):
    def __init__(self):
        self.info = '''
        --------Welcome to Transfer Machine --------
                    Auth:Junly
    '''
        self.func_desc = {
        'c    ': 'Connect IDC Romter Transfer Machine',
        '"cmd"':'Execute Local System Commands',
        'q    ':'Exit Program.',
        'h    ':'List function',
        }
        self.env_desc= '==>:'
        print self.info
        print("func \t Description")
        print("------------------------")
        for k,v in self.func_desc.items():
            print k+':' +'\t'+v

    def Local_Exec(self,full_command):
        """执行本地命令"""
        result = os.popen(full_command).read()
        if len(result) ==0:
            result = 'Nothing display'
        print result

    @property
    def User_Keyin(self):
        while True:
            full_command = str(raw_input( self.env_desc).strip())
            print(full_command)
            if len(full_command) == 0 :
                continue
            elif full_command == 'c' or full_command == 'connect':

                login_localhost_class().display_login_info
            elif full_command == 'q' or full_command == 'exit':
                sys.exit(0)
            elif full_command == 'h' or full_command =='H':
                Display_func()
            else:
                self.Local_Exec(full_command)
# Display().User_Keyin()