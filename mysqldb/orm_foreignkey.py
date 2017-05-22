#!/usr/bin/env python
#encoding:utf-8

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey,Column,INTEGER,String
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:huangamw@192.168.101.98/tmdb?charset=utf8",
                       encoding="utf-8",
                       # echo=True,
                       )
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id =Column(INTEGER,primary_key=True)
    name = Column(String(32),nullable=True)
    passwd = Column(String(32),nullable=True)

    def __repr__(self):
        return "id: %s,name:%s,passwd:%s" %(self.id,self.name,self.passwd)

class Address(Base):
    __tablename__ = 'address'
    id =Column(INTEGER,primary_key=True)
    email = Column(String(32),nullable=True)
    userid = Column(INTEGER,ForeignKey("users.id"))
    user = relationship("User",backref="address")


    def __repr__(self):
        return "email_address: %s,userid: %s" % (self.email,self.userid)

Base.metadata.create_all(engine)








