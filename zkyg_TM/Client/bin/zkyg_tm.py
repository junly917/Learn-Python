#!/usr/bin/env python
#encoding:utf-8
import os,sys,socket,commands,time,hashlib,json

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)

# from client_core.display_local import Display_func
# import zkyg_TM.Client.client_core.del____local_exec
from Client.client_core.display_local import  Display_func

if __name__ == '__main__':
    d = Display_func()
    d.User_Keyin


