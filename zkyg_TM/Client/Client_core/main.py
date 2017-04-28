#!/usr/bin/env python
#encoding:utf-8


import os,sys,socket,commands,time,hashlib,json

BASEDIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
import local_exec
from login_localhost import login_localhost_class

print sys.path

#运行软件时输出的内容
class run_display(object):
    def __init__(self):
        self.info = '''
        --------Welcome to Transfer Machine --------
                    Auth:Junly
    '''
        self.func_desc = {
        'c or C':'login Tianjing or Dongguang Transfer Machine',
        ' cmds ':'Execute Local System Commands',
        'q or Q':'Exit Program.',
        'h or H':'List function',
        }
        self.env_desc= '==>:'
        print self.info
        print("func \t Description")
        print("------------------------")
        for k,v in self.func_desc.items():
            print k+':' +'\t'+v

    def local_exec(self,full_command):
        """执行本地命令"""
        result = os.popen(full_command).read()
        if len(result) ==0:
            result = 'Nothing display'
        print result

    def keyin(self):
        while True:
            full_command = str(raw_input( self.env_desc).strip())
            print(full_command)
            if len(full_command) == 0 :
                continue
            elif full_command == 'C' or full_command == 'c':
                login_localhost_class().display_login_info
            elif full_command == 'q' or full_command == 'Q':
                sys.exit(0)
            elif full_command == 'h' or full_command =='H':
                run_display().keyin()
            else:
                self.local_exec(full_command)

if __name__ == '__main__':
    run_display().keyin()


