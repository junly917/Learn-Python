#!/usr/bin/env python
#encoding:utf-8
import os,sys,socket,commands,time,hashlib,json

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

import local_exec
from run_display import run_display
print sys.path

if __name__ == '__main__':
    run_display().keyin()


