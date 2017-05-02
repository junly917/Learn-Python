#!/usr/bin/env python
#encoding:utf-8
import os,sys,socket,commands,time,hashlib,json

BASEDIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
import local_exec
from run_display import run_display
print sys.path

#运行软件时输出的内容


if __name__ == '__main__':
    run_display().keyin()


