#!/usr/bin/env python
#enconding:utf-8
import  json,urllib2
urls = 'http://192.168.101.147/zabbix/api_jsonrpc.php'
header = {"Content-Type":"application/json"}
data = json.dumps(
            {
            "jsonrpc":"2.0",
            "method":"host.get",
            "params":{
                "output":["hostid","name","status","templateid"],
                "filter":{"host":""},
            },
            "auth":"e143716f96e4ba0da503fcee921e3614",
            "id":1,
        }
)

request = urllib2.Request(urls,data)
for key in header:
    request.add_header(key,header[key])
    try:
        result = urllib2.urlopen(request)
        response = json.loads(result.read())
    except Exception,e:
        if hasattr(e,'reason'):
            print 'we failed to reach a server'
            print e.reason
        elif hasattr(e,"code"):
            print "The server could not fulfill the request"
        else:
            response = json.loads(result.read())
            result.close()
            print "Number Of Hosts: ", len(response['result'])
    i = 0
    for host in response['result']:
        #print host
        print "Host ID:",host['hostid'],", Host Name:",host['name'],\
            ", Host Status:",host['status'],host['templateid']
        i +=1
    print "Host Number is :",i