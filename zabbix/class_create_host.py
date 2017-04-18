#!/usr/bin/env python
#encoding:utf-8
import json,urllib2
from urllib2 import URLError

class class_create_host(object):
    def __init__(self):
        self.url = 'http://192.168.101.147/zabbix/api_jsonrpc.php'
        self.header ={"Content-Type":"application/json"}
        self.AuthID = self.login()

    def login(self):
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
        print response['result']
        return response['result']

    def create_host(self):
        hostip="192.168.101.213"
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
                            "groups": [{"groupid":"1"}],
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
test = class_create_host()
print test.create_host()
