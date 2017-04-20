#from function import name
#name().names
# import function
# print function.names

# import time
# print(time.localtime())

class stu(object):

    sex="M"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def tellme(self):
        sex=self.age
        return sex
    def __del__(self):
        print "%s stu is Dead.." % self.name
my = stu('huang','27')
me = stu('123','2b7')
print my.tellme()
print my.sex
my.sex="F"
print my.sex
my.name="junly"
print my.name



