#!/usr/bin/env python
#encoding:utf-8
import os,sys
import ConfigParser
import os,sys,string

class Manager_User(object):
    '''
    中转机用户管理操作
    '''
    def __init__(self,name):
        self.name = name

    #添加用户
    def Add_User(self):
        pass

    #删除用户
    def Del_User(self):
        pass

    #获取用户
    def Get_Userlist(self):
        pass

cf = ConfigParser.ConfigParser()
dbconf = 'conf/dbconf'
cf.read('dbconf')



