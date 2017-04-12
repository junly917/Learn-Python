#!/usr/bin/env python
#coding:utf8
import sys,time,os

BASEDIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

user= BASEDIR+'\conf\user.txt'

def login():
    '''
    登录用户程序
    :return:
    '''
    count=0
    sleep=2
    while True:
        username=raw_input("Please Input Username:").strip()
        passwd=raw_input("Please Input Password:").strip()
        f = open(user,'r')
        if count == 3:
            print("输入密码错误次数过多")
            time.sleep(sleep)
            count =0
            sleep+=10
            continue
        if username == "" or username is None:
            count +=1
            print("账号或密码不能为空")
        else:
            for line in f.readlines():
                if '#' in line:
                    continue
                else:
                    print username,line.split(':')[2]
                    if 'auth' in line and (username in line.split(':')[1]) and (passwd in line.split(':')[2]):
                        #file format:
                        # auth:user:passwd:cost
                        print("Login Sucesses")
                        return 1
                    else:
                        print("Err: invlid Username or Password")
                        count +=1

            f.close()

def logout():
    pass
login()
