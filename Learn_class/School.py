#!/usr/bin/env python
#encoding:utf-8
'''
class SchoolMember(object):
    Members=0
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def enroll(self):
        SchoolMember.Members += 1
        print("Welcome to School : %s " %SchoolMember)

class TecherMember(object,SchoolMember):
    def __init__(self,name,age,salary,course):
        self.salary= salary
        self.course = course
    def tellme(self):
        print("%s welcome to Teacher" % self.name)
    def teacher(self):
        print ("%s teacher course %s " %(self.name,self.course))

class StudentMember(object,SchoolMember):
    def __init__(self,name,age,stu_id,classes):
        super
        self.stu_id = stu_id
        self.classes = classes

    def learing(self,):
        pass
t1 = TecherMember('junly','23',2300,'it')
t1.tellme()
'''

'''
class alls(object):
    def all_tack(self,obj):
        obj.tell()

class cat(object):
    def tell(self):
        print("cat meow..")
class dog(object):
    def tell(self):
        print("dog woow..")
a=cat()
d=dog()
x
alls().all_tack(a)
alls().all_tack(d)
'''


#批量创建
class all_create(object):
    def all_create(self,obj):
        obj.create()
#学校
class schoole(object):
    # sch_num = []
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
    def create (self,name,addr):
        # self.sch_num.append(self.name,self.addr)
        print("Create Schoole %s address is %s." % (self.name,self.addr))
#课程
class course(schoole):
    def __init__(self,obj,course,course_id):
        super(course,self).__init__()
        self.course = course
        self.course_id = course_id

    def create(self):
        print("Schoole %s Create %s ,id is %s" % (self.name,self.course,self.course_id))
#讲师
class teacher(object):
    pass

#学员
class student(object):
    pass
#班级
class room(object):
    pass
# sch1 = schoole("BJ-School","Beijing")
sch2 = schoole("SH-School","Shanghai")
course1 =course(sch2,"Python","Num1's")
# all_create().all_create(sch1)
# all_create().all_create(sch2)
all_create().all_create(course1)







