#!/usr/bin/env python
#coding:utf-8
import os,sys
BASEDIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
user= BASEDIR+'\conf\user.txt'
def showaccount():
    '''
    显示所有用户清单，返回所有用户清单。

    '''
    accountdict= {}
    try:
        f = open(user, 'r')
        i=1
        for line in f.readlines():
            if '#' in line or line == "\n" :
                continue
            else:
                accountdict[i]=line.split(':')[1].strip()
                i+=1
    except :
        print( '密码文件不存在')
    f.close()
    return accountdict

def addacount():
    sumaccount=[]
    user = showaccount().values()
    print user
    while True:
        username = raw_input("Please input Username(Exit:Q,List:L):").strip()
        if username in user:
            print("用户名己存在，请重新输入。")
        elif username == 'q' or username == 'Q':
            break
        elif username == 'L' or username == 'l':
            user = showaccount().values()
            print user
        else:
            passwd = raw_input("Please input Password:").strip()
            with open(user,'a+') as f:
                #f1.write(f.read())
                f.write('username:'+username+':'+passwd+':'+str(0)+'\n')
                print("用户" +username+"添加成功")

#accounts = showaccount()
#print "User list is :"
#for i in accounts.itervalues():
#    print i

#addacount()

