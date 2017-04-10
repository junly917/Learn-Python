#!/usr/bin/env python
#coding:utf-8
#
import os,sys
BASEDIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from core import login

print os.path.abspath(__file__)
print("""
    Welcome to My Shop, Please Login
""")

login.login()
