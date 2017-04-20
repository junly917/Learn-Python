#!/usr/bin/env python
#encoding:utf-8

import json,urllib2
from urllib2 import URLError

class Auth_Zabbix(object):
    def __init__(self):
        """
        定义api地址和http 头部
        :return:
        """
        self.url = 'http://192.168.101.147/zabbix/api_jsonrpc.php'
        self.header ={"Content-Type":"application/json"}

    def Login(self):
        """
        登录zabbix并获取Session Id
        :return:
        """
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

        return response['result']

#res = Auth().Login()
#获取session id
