#!/usr/bin/env python
#encoding:utf-8
import ConfigParser
import os,sys,commands
from zkyg_TM.Client.client_core.auth_passwd import *
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,INTEGER,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table

cf = ConfigParser.ConfigParser()
Basedir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file=Basedir+"\conf\dbconf"
cf.read(file)
db_name = cf.get('mysqldb','db_name')
db_host = cf.get('mysqldb','db_host')
db_port = cf.get('mysqldb','db_port')
db_user = cf.get('mysqldb','db_user')
db_passwd = cf.get('mysqldb','db_passwd')

engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" %
                       (db_user,db_passwd,db_host,db_port,db_name),
                       encoding="utf-8",
                       echo=True,
                       )
Base = declarative_base()
Session = sessionmaker(bind=engine)()  #会话绑定

#定义Group表的结构
class Groups(Base):
    __tablename__='tm_group'
    group_id = Column(INTEGER,primary_key=True)
    group_name = Column(String(64))

    def __repr__(self):
        return "id:%s,name:%s" %(self.group_id,self.group_name)

#定义Users表的结构
class Users(Base):
    __tablename__ = 'tm_user'
    user_id = Column(INTEGER,primary_key=True)
    user_name=Column(String(64))
    user_passwd = Column(String(32))
    user_descr = Column(String(256))
    user_email = Column(String(25))
    user_group = Column(INTEGER,ForeignKey(Groups.group_id))

    def __repr__(self):
        return "id:%s,name:%s,passwd:%s,descr:%s,email:%s,group:%s" %\
               (self.user_id,self.user_name,self.user_passwd,self.user_descr,self.user_email,self.user_group)

#定义IDC表的结构
class IDCs(Base):
    __tablename__ = 'idc_center'
    id = Column(INTEGER,primary_key=True)
    name=Column(String(64))
    address = Column(String(24))
    ipaddr = Column(String(18))
    port = Column(INTEGER)
    manager = Column(INTEGER,ForeignKey(Users.user_id))

    def __repr__(self):
        return "id:%s,name:%s,address:%s,ipaddr:%s,manager:%s" % \
               (self.id,self.name,self.address,self.ipaddr,self.manager)


def init_dropdb():
    Base.metadata.drop_all(engine)

def init_createdb():
    Base.metadata.create_all(engine)

#填充Userg表
def Users_Full():
    #输入管理员的账号密码及邮件地址
    user_data = {}
    User_input = raw_input('请输入管理员的密码:').strip()     #输入二次密码并进行验证
    # User_input2 = raw_input('请确认管理员的密码:').strip()
    User_input_email  = raw_input('请输入管理员的邮件地址:').strip()
    passwd =  md5sums(User_input)
    group_admin  = Session.query(Groups).filter(Groups.group_name=='Admin').first().group_id
    user1_obj = Users(user_name='admin',user_passwd=passwd,
                              user_descr="Admin Account",user_email=User_input_email,
                              user_group=group_admin
                              )
    Session.add(user1_obj)
    Session.commit()

#填充Group
def Groups_Full():
    group1_obj = Groups(group_name='Admin')
    group2_obj = Groups(group_name='User')
    group3_obj = Groups(group_name='Guest')
    Session.add(group1_obj)
    Session.add(group2_obj)
    Session.add(group3_obj)
    Session.commit()

#填充IDC
def IDCs_Full():
    #填充IDC相关信息
    name = raw_input('请输入IDC名称：').strip()
    address = raw_input('请输入IDC位置：').strip()
    ipaddr = raw_input('请输入IDC中转机的可访问地址：').strip()
    user = raw_input('请输入IDC中转机的管理员（1，2）：').strip()
    port = raw_input('请输入IDC中转机的端口：').strip()
    user_obj = Session.query(Users.user_name).all()
    idc_obj = IDCs(name=name,address=address,ipaddr=ipaddr,port=port,manager=user)
    Session.add(idc_obj)
    Session.commit()

# init_dropdb()
# init_createdb()
# Groups_Full()
# Users_Full()
#
# IDCs_Full()
