#!/usr/bin/env python
#encoding:utf-8
import json,urllib2
from urllib2 import URLError

class Class_Create_Host(object):
    def __init__(self):
        self.url = 'http://192.168.101.147/zabbix/api_jsonrpc.php'
        self.header ={"Content-Type":"application/json"}
        self.AuthID = self.Login()

    def Login(self):
        data = json.dumps({
            "jsonrpc":"2.0","method":"user.login",
            "params":{"user":"Admin","password":"zabbix"},"id":0,
        })
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e :
            print "URL is Error.."
        else:
            response = json.loads(result.read())
            result.close()
        #print response['result']
        return response['result']

    def Create_Host(self):
        hostip=raw_input("Please Input host ip: ")
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                            "host": hostip,
                            "interfaces": [
                                {
                                    "type": 1,
                                    "main": 1,
                                    "useip": 1,
                                    "ip": hostip,
                                    "dns": "",
                                    "port": "10050"
                                }
                            ],
                            "groups": [{"groupid":"2"}],
                            "templates":[{"templateid":"10001"}]
                    },
            "auth": self.AuthID,
            "id": 1
        })
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e :
            print "Create host is Error.."
            return  0
        else:
            response = json.loads(result.read())
            result.close()
        return response

    def Get_Host_Data(self):
        data = json.dumps({
            "jsonrpc":"2.0",
            "method":"host.get",
            "params":{
                #"output":["hostid","name","status","available"],
                "output":["name","available","host"],
                "filter":{
                    # "host":[]
                }
            },
            "auth":self.AuthID,
            "id":1,
        })
        request = urllib2.Request(self.url,data)
        i=1
        for key in self.header:
            request.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(request)
            i+=1
        except URLError as e :
            print "Get Host Data is Error,Please Check it!",e.code
        else:
            response = json.loads(result.read())
            result.close()
        # print response
        totale = online = offline = 0
        for i in response["result"]:
            totale +=1
            if i['available'] == '2':
                offline +=1
            else:
                online +=1
        response["host_totale"]=totale
        response["host_online"]=online
        response["host_offline"]=offline
        return response

    def Delete_Host(self):
        pass
# 
# test = Class_Create_Host()
# print test.Create_Host()
# print test.Get_Host_Data()
# res = test.Get_Host_Data()
# print res
# dict1 = res['result']
# print dict1
