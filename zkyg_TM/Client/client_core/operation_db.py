#!/usr/bin/env python
#encoding:utf-8
import os,sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,INTEGER,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from zkyg_TM.Client.client_core import db_arch

Session = sessionmaker(bind=db_arch.engine)()

class db_select(object):
    def __init__(self,tables,sql):
        self.sqls = sql
        self.tables = tables

    def table_select(self):
        # Session.query(db_arch.Users).filter(sql).all()
        obj_data = {}
        hasattr(db_arch,self.tables)
        db_objs =getattr(db_arch,self.tables)
        data =  Session.query(db_objs).filter(self.sqls).all()
        obj_data['info'] =data
        obj_data['num']=len(data)
        print obj_data

class db_insert(object):
    def User_tb(self):
        pass

    def Group_tb(self):
        pass

    def IDC_tb(self):
        pass

class db_delete(object):
    def User_tb(self):
        pass

    def Group_tb(self):
        pass

    def IDC_tb(self):
        pass

class db_update(object):
    def User_tb(self):
        pass

    def Group_tb(self):
        pass

    def IDC_tb(self):
        pass


ops = db_select('Users','user_id>0')
ops.table_select()




