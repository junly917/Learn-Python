#!/usr/bin/env python
#encoding:utf-8

import os,sys,commands
class Packages(object):
    def __init__(self,packagename):
        self.packname = packagename

class Rpm(Packages):
    '''
    安装软件包
    '''
    def __init__(self,packagename):
        super(Rpm,self).__init__(packagename)
        print self.packname
    def Install_soft(self):
        result = {}
        installer = commands.getstatusoutput('yum install -y %s' % (self.packname))
        if installer[0] == 0 :
            if commands.getstatusoutput('rpm -qa|grep %s' % (self.packname))[0] == 0 :
                result["id"] = 0
                result["Content"] = "Install Sucesses."
                return result
            else:
                result["id"] = 1
                result["Content"] = "Install Sucesses.but check Package is Error,Please Check it."
                return result
        else:
            result["id"] = 2
            result["Content"] = "Install Failed,Please recheck."
            return result

class Tar(Packages):
    pass

class Zip(Packages):
    pass

if __name__ == "__main__":
    packagename = raw_input("Please Input Package name: ").strip()
    yum_packaget = commands.getstatusoutput('yum list all |grep ^%s.x86_64' %packagename )
    if yum_packaget[0] != 0:
        packagename = yum_packaget[1].split()[0]
        install_result = Rpm(packagename)
        print("sldkjllllllllllll")
        print install_result.Install_soft()
    #print packagename


