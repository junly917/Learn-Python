#!/usr/bin/env python
#encoding:utf-8

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,INTEGER,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table
engine = create_engine("mysql+pymysql://root:huangamw@192.168.101.98/tmdb",encoding="utf-8",echo=True)
Base = declarative_base()


'''
class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "id=%d,name = %s ,password = %s" % (self.id,self.name,self.password)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)()
#单表Add
db_obj = User(name='huang',password='huang1')
db_obj = User(name='aaa',password='abcd123')
Session.add(db_obj)
Session.commit()


#单表Select
print("#获取一条数据")
db_data = Session.query(User).filter_by(name='huang').first()
print(db_data.name,db_data.password)                #获取一条数据

print("#获取所有的数据，以列表形式进行展示")
db_data = Session.query(User.id,User.name,User.password).all()
print(db_data)                #获取所有的数据，以列表形式进行展示

print("#获取所有id大于1的所有记录")
db_data = Session.query(User).filter(User.id > 1).all()
print(db_data)

print("获取精确的值")
db_data = Session.query(User).filter(User.name=='huang').filter(User.password=="huang1").all()
print(db_data[0])
print(len(db_data))


#Foreignkey
class Address(Base):
    __tablename__ = 'Address'
    id = Column(INTEGER,primary_key=True)
    user_id = Column(INTEGER,ForeignKey(User.id))
    user = relationship(User,backref = 'Address')
    address = Column(String(512))
    mail_address = Column(String(64),nullable=False)

    def __repr__(self):
        return "id:%s,user_id:%s,user:%s,address:%s,mail_address:%s" % (
            self.id,
            self.user_id,
            self.user,
            self.address,
            self.mail_address,
        )

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)()

#多表Add

User_id = Session.query(User).filter(User.name =='huang').first().id #获取name为huang的id值
print(User_id)      #打印获取到的id

data_obj = Address(address='beijing',mail_address='1212@qq.com',user_id =User_id )  #插入到地址表里面
Session.add(data_obj)
Session.commit()        #提交到数据库


#多表Select
db_obj = Session.query(Address).first()       #获取第一条数据
print(db_obj)

db_obj = Session.query(Address).filter(Address.address =='hunan').all()   #获取address 是hunan的数据
print(db_obj)

db_obj = Session.query(Address).all()       #获取所有数据
print(len(db_obj))  #查看数据有多少条

'''

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)()
'''
# book_2_author=Table('book_2_auth',Base.metadata,
#                     Column('book_id',INTEGER,ForeignKey('book.id')),
#                     Column('auth_id',INTEGER,ForeignKey('auth.id')),
#                     )
#
# class Auth(Base):
#     __tablename__ = 'auth'
#     id = Column(INTEGER,primary_key=True)
#     name = Column(String(30))
#     authors = relationship('Auth',secondary = 'book_to_auth',backref = 'Book')
#     def __repr__(self):
#         return 'name:%' %(self.name)
#
# class Book(Base):
#     __tablename__ = 'book'
#     id = Column(INTEGER,primary_key=True)
#     name = Column(String(24))
#
#     def __repr__(self):
#         return "name:%s"%(self.name)
#
# # Base.metadata.create_all(engine)
# # Session = sessionmaker(bind=engine)()
#
# b1=Book(name="python")
# b2=Book(name='java')
#
# a1=Auth(name='junly')
# a2=Auth(name='huang')
#
# a1.authors=[b1,b2]
# a2.authors=[b1,b2]
#
# # Session.add_all([a1,b1,a2,b2])
# # Session.commit()
#
# Session.add(b1)
# Session.commit()
'''

'''
class group(Base):
    __tablename__='group'
    group_id = Column(INTEGER,primary_key=True)
    group_name = Column(String(64))

    def __repr__(self):
        return "id:%s,name:%s" %(self.group_id,self.group_name)

class user(Base):
    __tablename__ = 'user'
    user_id = Column(INTEGER,primary_key=True)
    user_name=Column(String(64))
    user_passwd = Column(String(256))
    user_descr = Column(String(256))
    user_email = Column(String(25))
    user_group=Column(INTEGER,ForeignKey(group.group_id))

    def __repr__(self):
        return "id:%s,name:%s,passwd:%s,descr:%s,email:%s,group:%s" %\
               (self.user_id,self.user_name,self.user_passwd,self.user_descr,self.user_email,self.user_group)

class idc(Base):
    __tablename__ = 'idc_center'
    id = Column(INTEGER,primary_key=True)
    name=Column(String(64))
    address = Column(String(24))
    ipaddr = Column(String(18))
    manager = Column(INTEGER,ForeignKey(user.user_id))

    def __repr__(self):
        return "id:%s,name:%s,address:%s,ipaddr:%s,manager:%s" % \
               (self.id,self.name,self.address,self.ipaddr,self.manager)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)()


#
# data_obj = group(name='Admin')
# data_obj2 = group(name='User')
# Session.add(data_obj)
# Session.add(data_obj2)
# Session.commit()
#


'''

class Group222(Base):
    __tablename__ = 'group222'
    id= Column(INTEGER,primary_key=True)
    name = Column(String(24))

class User11(Base):
    __tablename__ = 'Users'
    id= Column(INTEGER,primary_key=True)
    name = Column(String(24))
    group= Column(INTEGER,ForeignKey(Group222.id))

class Group111(Base):
    __tablename__ = 'group111'
    id= Column(INTEGER,primary_key=True)
    name = Column(String(24))
    uuid= Column(INTEGER,ForeignKey(User11.id))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)()