#!/usr/bin/env python
#encoding:utf-8
#Author:Junly

from Learn_class import classes
from sqlalchemy.orm import Session,sessionmaker
Session = sessionmaker(bind=classes.engine)()

class Orm_teach(object):
    def __init__(self,obj):
        self.obj = obj

    def Add_teach(self):
        teacher_name = raw_input("please input teacher name:").strip()
        teacher_age = raw_input("please input teacher age:").strip()
        t1 = self.obj(name=teacher_name,age=teacher_age)
        Session.add_all([t1])
        Session.commit()

    def Del_teach(self,**args):
        print(args)     #{'id': 1}
        keys = args.keys()[0]
        values = args.get(keys)
        print keys,'==',values
        teach_obj = Session.query(classes.Teacher).filter(classes.Teacher.keys==values).first()
        print(Session.query(classes.Teacher).filter(classes.Teacher.id==2).all())
        print(teach_obj)
        Session.commit()

    def Update_teach(self):
        pass

    def Select_teach(self):
        pass

    def Select_all_teach(self):
        t1_obj = Session.query(classes.Teacher).all()
        if len(t1_obj):
           print("当前所有的老师清单:%s " % t1_obj)
        else:
            print("没有老师存在，请添加吧；")


if __name__ == '__main__':
    menu = ('''
        1.教师管理
        2.课程管理
        3.教学学期管理
        4.班级管理
        5.学生管理
        6.学生成绩管理
    ''')
    teach_manage  = """
        1.添加老师
        2.删除老师
        3.修改老师属性
        4.列出所有教师
    """
    while True:
        print menu
        chioce = raw_input("please chioce opertion.").strip()
        if len(chioce) == 0 :
            continue
        if chioce == '1' or chioce ==1: #老师管理
            opt_teach = Orm_teach(classes.Teacher)
            print teach_manage
            while True:
                chioce_teach = raw_input("please chioce teach opertion.").strip()
                if   chioce_teach == '1':
                    opt_teach.Add_teach()
                elif chioce_teach == '2':
                    opt_teach.Del_teach(id=2)
                elif chioce_teach == '3':
                    opt_teach.Update_teach()
                elif chioce_teach ==  '4':
                    opt_teach.Select_all_teach()
                elif chioce_teach == 'q':
                    break
                else:
                    continue
        elif chioce == '2':
            opt_other = 'opt student'
        elif chioce == 'q':
            break
        else:
            continue


