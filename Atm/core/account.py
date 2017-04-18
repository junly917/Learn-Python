#!/usr/bin/env python
#coding:utf-8
import os,sys,time
BASEDIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
userfile= BASEDIR+'\conf\user.txt'
tmpfile= BASEDIR+'\conf\user-tmp.txt'

def showaccount():
    '''
    显示所有用户清单，返回所有用户清单。
    '''
    accountdict= {}
    try:
        f = open(userfile, 'r')
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

def manageaccount():
    '''账号管理'''
    while True:
        print("""您可以进行以下操作：
            a: 修改用户属性
              """)
        optuser = raw_input("请选择您的操作：").strip()
        if optuser not in ['a']:
            print("您输入的有问题，请重新输入")
        if optuser == 'a':
            modfiyaccount()

def modfiyaccount():
    user = showaccount().values()
    print  '当前可用户列表：',user
    name = raw_input("输入用户名: ").strip()
    f = open(userfile ,'r')
    newf= open(tmpfile,'w')
    listline=[]
    md_status='old'
    for line in f.readlines():
        if name == line.split(':')[1]:
            pwd= str(raw_input("输入%s的密码: "% name).strip())
            #listline.append(line.split(':')[2]=name)
            listline = line.split(':')
            listline[2]=pwd
            newline = (':').join(listline)
            newf.write(newline)
            md_status = 'new'
            continue
        else:
            newf.write(line)
            continue

    f.close()
    newf.close()
    if md_status == 'new':
        print("密码修改成功")
    else:
        print("没有找到账号")

def delaccount():
    pass

def addacount():
    sumaccount=[]
    user = showaccount().values()
    print '当前用户：',user

    while True:
        username = raw_input("请输入要增加的用户名(退出:Q,列出所有用户:L):").strip()
        if username in user:
            print("用户名己存在，请重新输入。")
            continue
        elif username == 'q' or username == 'Q':
            break
        elif username == 'L' or username == 'l':
            user = showaccount().values()
            print  '当前用户：',user
            time.sleep(2)
        else:
            passwd = raw_input("请输入%s密码:" % username).strip()
            print userfile
            with open(userfile,'a+') as f:
                #f1.write(f.read())
                f.write('auth:'+username+':'+passwd+':'+str(0)+'\n')
                print("用户" +username+"添加成功")

#accounts = showaccount()
#print "User list is :"
#for i in accounts.itervalues():
#    print i

#addacount()
#manageaccount()
#modfiyaccount()
