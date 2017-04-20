#!/usr/bin/env python
#encoding:utf-8

import json,urllib2
from urllib2 import URLError
from Login_zabbix import Auth_Zabbix

Session_id =  Auth_Zabbix().Login()


class Get_Graphs(object):
    def __init__(self):
        self.url = 'http://192.168.101.147/zabbix/api_jsonrpc.php'
        self.header ={"Content-Type":"application/json"}

    def Get_Graphs(self):
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "graph.get",
            "params": {
                #"output":"name,graphid",     #输出哪些字段
                "output":"extend",          #输出哪些字段
                "hostids":10115,             #主机ID1
                "sortfield":"name",         #哪个字段排序
                "filter":{                   #过滤哪些字段
                    "name":"CPU load",
                }
            },
            "auth": Session_id,
            "id": 1
        })
        req = urllib2.Request(self.url,data)
        for key in self.header:
            req.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(req)
        except URLError,e:
            print "Get host Graphs is Errors.."
        else:
            response = json.loads(result.read())
            result.close()
        return response

print Get_Graphs().Get_Graphs()




