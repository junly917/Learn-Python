#!/usr/bin/env python
#encoding:utf-8

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey,Column,INTEGER,String
from sqlalchemy.orm import relationship,sessionmaker

engine = create_engine("mysql+pymysql://root:huangamw@192.168.101.98/tmdb?charset=utf8",
                       encoding="utf-8",
                       # echo=True,
                       )

Base = declarative_base()

class Teacher(Base):    #老师
    __tablename__ = 'teacher'
    id = Column(INTEGER,primary_key=True)
    name = Column(String(32))
    age = Column(INTEGER)
    def __repr__(self):
        return self.name

class term(Base):    #学期
    __tablename__ = 'term'
    id = Column(INTEGER,primary_key=True)
    term_num = Column(INTEGER)
    teacher = Column(INTEGER,ForeignKey("teacher.id"))
    # teacher = relationship("teacher")
    def __repr__(self):
        return self.term_num

class Classes(Base):    #班级
    __tablename__ = 'classes'
    id = Column(INTEGER,primary_key=True)
    class_name = Column(String(32))
    teacher = Column(INTEGER,ForeignKey("teacher.id"))
    # teacher = relationship("teacher")
    def __repr__(self):
        return self.class_name

class grade(Base):  #成绩表
    __tablename__ = 'grade'
    id = Column(INTEGER,primary_key=True)
    grade_num = Column(INTEGER)
    def __repr__(self):
        return self.grade_num

class student(Base):    #学生
    __tablename__ = 'student'
    id = Column(INTEGER,primary_key=True)
    name = Column(String(32))
    age = Column(INTEGER)
    stu_class = Column(INTEGER,ForeignKey("classes.id"))
    stu_term = Column(INTEGER,ForeignKey("term.id"))
    stu_grade = Column(INTEGER,ForeignKey("grade.id"))

Base.metadata.create_all(engine)	#创建表结构


'''
    #
    # Session = sessionmaker(bind=engine)()
    # inpt = ""
    # while True:
    #     inpt = raw_input("exit ?:").strip()
    #     if inpt=="n":
    #         teacher_name = raw_input("please input teacher name:").strip()
    #         teacher_age = raw_input("please input teacher age:").strip()
    #         t1 = Teacher(name=teacher_name,age=teacher_age)
    #         Session.add_all([t1])
    #         Session.commit()
    #
    #     elif inpt == 'q':
    #         break
    #     else:
    #         continue
    #
    # print "Staring Create Classes.."
    # t1_obj = Session.query(Teacher).all()
    # teacher_list = {}
    # classes_name_obj = raw_input("please input classes name:").strip()
    # print(t1_obj)
    # classes_teach_obj = raw_input("please input teacher num:").strip()
    # teach_id = Session.query(Teacher.id).filter(Teacher.name==classes_teach_obj).first()
    # add_teacher = Classes(class_name=classes_name_obj,teacher=teach_id[0] )
    # Session.add_all([add_teacher])
    # Session.commit()
    # print "Create Classes Finished."
'''

