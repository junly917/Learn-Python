#!/usr/bin/env python
#encoding:utf-8
from zkyg_TM.Client.client_core import operation_db
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)

host_dict = operation_db.db_select('Users','name="admin"').table_select()
print host_dict
#连接中转机服务器
class Connect_tm(object):
    #设置相应的环境变量
    def __init__(self):

        self.host_dict={
            'host1':{'postion':'Office','ip':'192.168.2.2','port':'22'},
            'host2':{'postion':'DG-IDC','ip':'10.0.78.1','port':'22'},
            'host3':{'postion':'TJ-IDC','ip':'124.200.40.0','port':'2002'},
        }
        self.func_desc = {
            'C or c':'Connection IDC Transfer Machine ',
            'E or e':'Exit Program.return Transfer Machine',

        }
        self.env_desc='Connection host:'

    #列出主机清单
    @property
    def showhostlist(self):
        print("Postion \t Host ip")
        i= 1
        Host_New_Dict= hostlist={}
        for k,v in self.host_dict.items():
            hostlist[i] = v['ip']+',' +v['port']
            print('%5d:\t\t%5s  (%s:%s)' %(i,k,v['ip'],v['port']))
            Host_New_Dict[i] = str(k) + ','+str(v['ip']) + ',' + str(v['port'])
            i+=1
        return Host_New_Dict

    @property
    def conn_server(self):
        #列出主机清单
        Host_Dict  = self.showhostlist

        #['124.200.40.0 2002', '10.0.78.1 22', '192.168.1.1 22']
        #连接主机
        while True:

            chiose_host = raw_input( self.env_desc).strip()
            if len(chiose_host) == 0:
                continue
            elif chiose_host == 'quit' or chiose_host == 'exit':
                sys.exit(0)
            elif chiose_host == 'l' or chiose_host == 'L':
                self.showhostlist
            else:
                try:
                    chiose_host = int(chiose_host)
                except Exception,e:
                    print("Please input digest,reinput")
                    continue
                try:
                    real_hostname = Host_Dict[chiose_host].split(',')[0]
                    real_ip = Host_Dict[chiose_host].split(',')[1]
                    real_port = Host_Dict[chiose_host].split(',')[2]
                    os.system('start xshell.exe %s:%s -newtab %s' %(real_ip,real_port,real_hostname))
                except  KeyError:
                    print("you input is nothing host ")


class testpass(object):
    pass




