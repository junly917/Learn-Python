#!/usr/bin/env python
#coding:gb2312

import random,os,sys,commands


print sys.getdefaultencoding()
class Yum_config(object):
    pass

#Search Yum Repo List
    def List_Yum_Repo(self):
        pass
#Create Yum Repo
def Create_Yum_Repo():
    ''' Creaet Yum Repo '''
    while True:
        File_name = raw_input("Please Input Yum Repo File Name: ").strip()
        if File_name != "" :
            break
    while True:
        File_Baseurl = raw_input("Please Input Yum Repo BaseURL: ").strip()
        if "http:/" == File_Baseurl[:6] or "file:/" == File_Baseurl[:6]  or "ftp://" == File_Baseurl[:6] :
            break
        else:
            print "Input Baseurl is invailed,please reinput"
            continue
    Isenable = raw_input("Are You enable %s,(default enabled): " % File_name).strip()
    if Isenable == "" or int(Isenable) == 1 :
        Isenable = 1

    Cost_Num = raw_input("Please Input Cost for %s Number(default Radom(100-130): " % File_name).strip()
    if Cost_Num == "":
        Cost_Num = random.randint(100,130)

    Gpgcheck = raw_input("Please Input gpgcheck Status(default is 0): ").strip()
    if Gpgcheck == "":
        Gpgcheck = 0


    print '''
        [%s]
        name=%s
        baseurl=%s
        enabled=%d
        gpgcheck=%d
        cost=%d
    ''' %(File_name,File_name,File_Baseurl,Isenable,Gpgcheck,Cost_Num)


    Template_file = "./Template/yum.repo-template"
    Destnation_file = "./Destnation/"
    with open(Template_file,'r') as f , \
          open (Destnation_file+File_name+".repo",'w') as d:
        for line in f :
            if "[]" in line :
                line = "[" + File_name + ']'
            if "name" in line:
                line = "name=" + File_name
            if "baseurl" in line:
                line = "baseurl=" + File_Baseurl
            if "enable" in line :
                line = "enabled=" + str(Isenable)
            if "cost=" in line :
                line = "cost=" + str(Cost_Num)
            if "gpgcheck=" in line:
                line = "gpgcheck=" + str(Gpgcheck)
            d.write(line+'\n')

#Delete Yum Repo
def Delete_Yum_Repo():
    pass

#Disabled Yum Repo
def Disabled_Yum_Repo():
    pass
    #Get_Yum_Status

#Modify Yum Repo

#Get Yum Status
def Get_Yum_Status():
    dest="dir Destnation/*.repo"
    file_list=commands.getstatusoutput(dest)[1]
    file_list=file_list.split('\n')
    enable_repo=[]
    for files in file_list:
        status = 0
        print "=============="
        with open(files,'r') as f:
            for line in f:
                if "enabled=1" in line:
                    status = 1
                    break

        print files
        enable_repo.append(os.path.basename(files))
    print enable_repo

#Create_Yum_Repo()
Get_Yum_Status()