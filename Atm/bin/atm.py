#!/usr/bin/env python
#coding:utf-8
#
import os,sys
BASEDIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from core import login,account,cashin, shopping
from conf import *
import sys,os,time

print("""
    Welcome to My Shop, Please Login
""")

login_status = login.login()
if login_status ==1 :
    while True:
        print("""
            1. 修改额度
            2. 购买物品
            3. 提现
            4. 转账
            5. 查看消费记录
            6. 还款
            7. 查看购买物品
            8. 账号操作
            9. 登出操作
        """)
        opstat = raw_input("请选择操作的内容:").strip()
        try:
            opstat = int(opstat)
            if opstat == 1:
                pass
            if opstat == 2:
                pass
            if opstat == 3:
                pass
            if opstat == 4:
                pass
            if opstat == 5:
                pass
            if opstat == 6:
                pass
            if opstat == 7:
                pass
            if opstat == 8:
                account.addacount()
            if opstat == 9:
                login.logout()
        except:
            print("输入有问题，生重新选择。")
            time.sleep(1)
            continue



