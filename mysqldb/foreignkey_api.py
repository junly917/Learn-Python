#!/usr/bin/env python
#encoding:utf-8
from sqlalchemy.orm import sessionmaker
import orm_foreignkey

Session = sessionmaker(bind=orm_foreignkey.engine)()

#添加数据
user_add_obj = orm_foreignkey.User(name="huang",passwd="123")
user_add_obj1 = orm_foreignkey.User(name="junly",passwd="3456")

# 提交到数据库操作
Session.add_all([user_add_obj,user_add_obj1])
Session.add_all([user_add_obj])
Session.commit()

#绝对查询
user_obj = Session.query(orm_foreignkey.User).\
    filter(orm_foreignkey.User.id == 1).first()

# like查询
user_obj = Session.query(orm_foreignkey.User).\
    filter(orm_foreignkey.User.name.like("%un%")).first()
print(user_obj)

#in查询操作
user_obj = Session.query(orm_foreignkey.User)\
    .filter(orm_foreignkey.User.name.in_(['huang','junly'])).all()
print(user_obj)

#修改数据库操作并提交
user_obj.name = "huangamw"
Session.commit()

#删除操作
user_obj = Session.query(orm_foreignkey.User).filter(orm_foreignkey.User.id ==1).delete()
Session.commit()
print(user_obj)

# 外键插入操作
user_obj = Session.query(orm_foreignkey.User).first()
user_obj1 = Session.query(orm_foreignkey.User).all()[1]
user_obj1.address = [orm_foreignkey.Address(email="1212@qq.com")]
user_obj.address = [orm_foreignkey.Address(email="haha@qq.com")]
Session.commit()

# 使用外键查询操作通过用户查地址
user_obj = Session.query(orm_foreignkey.User).filter(orm_foreignkey.User.id==1).first()
print(user_obj.address)

# 使用外键查询操作通过地址查用户
user_obj = Session.query(orm_foreignkey.User).filter(orm_foreignkey.Address.email == "haha@qq.com").first()
print(user_obj)



















