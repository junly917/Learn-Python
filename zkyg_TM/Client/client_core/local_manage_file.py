#!/usr/bin/env python
#encoding:utf-8
import paramiko
import sys,os,commands
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from  login_local import login_localhost_class

#上传下载文件操作
class manager_file(object):
    '''
    上传下载文件操作
    '''
    def __init__(self,hostname,port,username,passwd,remote_files,local_files,auth_type):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.passwd = passwd
        self.remote_files = remote_files
        self.local_files =local_files
        self.auth_type = auth_type

    #上传文件到中转机服务器
    def upload(self):
        sftp = paramiko.Transport((self.hostname,self.port))
        sftp.connect(self.username,self.passwd)
        sftp_file = paramiko.SFTPClient.from_transport(sftp)
        sftp_file.put(self.local_files,self.remote_files)
        sftp_file.close()

    #从中转机服务器下载文件到本地
    def download(self):
        sftp = paramiko.Transport((self.hostname,self.port))
        sftp.connect(self.username,self.passwd)
        sftp_file = paramiko.SFTPClient.from_transport(sftp)
        sftp_file.put(self.remote_files,self.local_files)
        sftp_file.close()

#检查文件是否存在
def check_file(self,obj):
    file_status={}
    file_status['status'] = 0
    for file in xrange(len(obj)):
        if os.path.exists(file):
            continue
        else:
            file_status['status'] = 1
            file_status['name'] = file
            print('file is no exsit')
            return file_status

    return file_status

# 1.输入本地文件名称
local_filename_list = raw_input('please input filename[s]:').strip().split()

#2.检查文件是否存在
filestatus = check_file(local_filename_list)
if filestatus['status'] == 0 :
    #文件都存在
    #3.选择远程主机
    login_localhost_class().showhostlist
    #4.验证主机信息

    #5.输入远程文件名称及位置
    remote_filename_list = raw_input('please input filename[s]:').strip().split()

    #6.检查远程文件是否存在

    #7.发送文件操作
else:
    print('%s文件不存在'% filestatus['name'])