#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

class Schoolmember(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def tellme(self):
        print("Hello,我的名字是：%s" % self.name)

class Teacher(Schoolmember):
    def __init__(self,name,age,salarys):
        super(Teacher,self).__init__(name,age)
        self.salarys = salarys
        Teachers=Schoolmember(name,age).tellme()

    def salary(self):
        print("老师：%s的工资是： %s" % (self.name,self.salarys))

class Student(Schoolmember):
    def __init__(self,name,age,grade,kec):
        super(Student,self).__init__(name,age)
        Students=Schoolmember(name,age).tellme()
        self.grade = grade
        self.kec = kec

    def lears(self):
        print("学生：%s 课程是： %s"%(self.name,self.kec))

if __name__ == "__main__":
    t1 = Teacher("junly","23","2000")
    t2 =Teacher("huang","30","3000")
    s1 = Student("h1","20","F","it")
    s2 = Student("h2","23","M","Python")
    s1.lears()
    s2.lears()

'''

'''
class jiao(object):
    def __init__(self,sex):
        self.sex = sex
        print("jiao sex is " % (self.sex))

class mao(jiao):
    def __init__(self,name):
        self.name = name
        print("this is mao name is: %s" %self.name)
    def jao(self):
        print("Miao...!")

class wa(jiao):
    def __init__(self,name):
        self.name = name
        print("this is gou name is: %s" %(self.name))
    def jao(self):
        print("Wa...!")

def fun(obj):
    obj.jao()

if __name__ == "__main__":
    dog1=wa("Mq")
    mao1=mao("Fq")
    fun(dog1)
    fun(mao1)
'''

'''
class fly(object):
    def __init__(self,name):
        self.name = name

    def checkfly(self,name):
        print("Check Fly Name is %s"%(self.name))
        return 1

    @property
    def status(self):
        check_result = self.checkfly(self.name)
        if check_result == 1:
            print("online")
        elif check_result == 2:
            print("offline")
        elif check_result ==0:
            print("goed")
        else:
            print("等会来查吧！")

    @status.setter
    def status(self,num):
        print num
        status_dic = {
            0:'cacelled',
            1:'arrived',
            2:'departured'
        }
        print("status is %s"%status_dic.get(num))

    @status.deleter
    def status(self):
        print("Delete status.")
if __name__ == "__main__":
    f1 = fly("3330")
    f1.status
    f1.status =2
    # f1.status(2)
'''

'''
class Foo:
    def __getitem__(self, item):
        print("keys",item)
names=Foo()
result = names['k1']

'''

'''
#定义类及类的方法、属性
class foo(object):
    def __init__(self):
        self.name = 'haha'
        print("haha")

    @property
    def func(self):
        print("func")
        return 'func'
#实例化
classis = 'foo'
execclass = eval(classis)()


#反射的调用方法
fun = getattr(execclass,'func')
execclass.func
'''

'''
class mydefins(Exception):
    def __init__(self,mesg):
        self.msg=mesg

    def __str__(self):
        return self.msg
try:
    mydefins("erros")
except Exception,e:
    print(e)

else:
    print("haha")
finally:
    print("hehe")
'''

'''
class foo(object):
    funcs = 'abc'
    def __init__(self):
        self.name = 'haha'
    def func(self):
        self.name= 'hehe'
s = foo()
print(hasattr(s,'name'))
print(hasattr(s,'func'))

print(getattr(s,'name'))
print(getattr(s,'func'))

print(setattr(s,'name','kkk'))
print(setattr(s,'func',lambda  num:num+1))
print(getattr(s,'name'))
print(getattr(s,'func'))

print(delattr(s,'name'))
print(delattr(s,'func'))
# print(getattr(s,'name'))
print(getattr(s,'func'))
'''















