#!/usr/bin/env python
#encoding:utf-8

import sqlalchemy
from sqlalchemy import create_engine,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey,Column,INTEGER,String
from sqlalchemy.orm import relationship,sessionmaker

engine = create_engine("mysql+pymysql://root:huangamw@192.168.101.98/tmdb?charset=utf8",
                       encoding="utf-8",
                       # echo=True,
                       )
Base = declarative_base()

book2author = Table("book2author",Base.metadata,
    Column("Author_id",INTEGER,ForeignKey('author.id')),
    Column("Book_id",INTEGER,ForeignKey('book.id')),
)
class Author(Base):
    __tablename__ = 'author'
    id=Column(INTEGER,primary_key=True)
    name=Column(String(32))
    def __repr__(self):
        return "%s" %(self.name)

class Book(Base):
    __tablename__ = 'book'
    id=Column(INTEGER,primary_key=True)
    name=Column(String(32))
    authors = relationship('Author',secondary=book2author,backref='books')
    def __repr__(self):
        # return "%s Author is %s" %(self.name,self.authors)
        return self.name

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)()

a1 = Author(name="junly")
# a2 = Author(name="huang")
# a3 = Author(name="jack")
#
# b1 = Book(name="Linux")
b2 = Book(name="Python")
# b3 = Book(name="Java")
#
# b1.authors=[a1,a2,a3]       #添加作者和书对应关系
# b2.authors=[a1,a2]
# b3.authors=[a1,]
b2.authors.append(a1)
# Session.add_all([a1,a2,a3,b1,b2,b3])
# Session.add_all([a1,b3,])
b2 = Book(name="Python")
a1 = Author(name="junly")
b2.authors.append(a1)
Session.add_all([a1,b2])
Session.commit()





