#!/usr/bin/env python
#encoding:utf-8
import os,sys,socket,commands,time,hashlib,json

#密码验证
def auth(user,passwd,authtype):
    '''
    transfer user,passwd to server ,auth user,passwd
    '''

    #md5passwd = md5sums(passwd) #对密码进行加密操作
    authdata={}                 #账号密码字典
    authdata['user'] = user
    authdata['passwd'] = passwd
    if authtype == 'mysql':
        pass
    elif authtype == 'dict':
        dbdict = {'user':'admin','passwd':'huangamw'}
        if authdata['user'] == dbdict['user'] and authdata['passwd'] == dbdict['passwd']:
            return  'login'       #密码己匹配
        else:
            return 'Failed'

#密码加密操作
def md5sums(passwd):
    '''
    passwd 加密操作
    '''
    m = hashlib.md5()
    m.update(passwd)
    return m.hexdigest()