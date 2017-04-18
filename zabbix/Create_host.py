#!/usr/bin/env python
#encoding:utf-8

import json,urllib2
from urllib2 import URLError
url = 'http://192.168.101.147/zabbix/api_jsonrpc.php'
header ={"Content-Type":"application/json"}
def login():
    login_data = json.dumps({
        "jsonrpc":"2.0","method":"user.login",
        "params":{"user":"Admin","password":"zabbix"},"id":0,
    })
    request = urllib2.Request(url,login_data)
    for key in header:
        request.add_header(key,header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print "Auth Failed,Please Check Your name and password",e.code
        else:
            response = json.loads(result.read())
            result.close()
            return response['result']
authid = login()
data = json.dumps({
    "jsonrpc":"2.0",
    "method":"host.create",
    "params":{
        "host":"Linux Server123",
        "interfaces":[{
            "type":1,
            "main":1,
            "useip":1,
            "ip":"192.168.101.2",
            "dns":"",
            "port":"10050",
            }],
        "groups":[{
            "groupid":"50",
        }],
        "templates":[{
            "templateid":"10001",
        }],
        "inventory_mode":0,
        # "inventory":{},
    },
    "auth":authid,
    "id":1,
})
print authid
request  = urllib2.Request(url,data)
for key in header:
    request.add_header(key,header[key])
    # print header[key],request
    result = urllib2.urlopen(request)
    response = json.loads(result.read())
    result.close()




