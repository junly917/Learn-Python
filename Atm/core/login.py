#!/usr/bin/env python
#coding:utf8
import sys,time,os

BASEDIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

print os.path.abspath(__file__)
print '11111111111'
user= BASEDIR+'\conf\user.txt'
def login():
    count=0
    sleep=2
    while True:
        username=raw_input("Please Input Username:").strip()
        passwd=raw_input("Please Input Password:").strip()
        f = open(user,'r')
        for line in f.readlines():
            if '#' in line:
                continue
            else:
                if 'auth' in line and (username in line.split(':')[1]) and (passwd in line.split(':')[2]):
                    pass
                else:
                    print("Err: invlid Username or Password")
                    count +=1
        if count == 3:
            print("输入密码错误次数过多")
            time.sleep(sleep)
            count =0
            sleep+=5
    f.close()
