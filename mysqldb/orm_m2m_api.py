#!/usr/bin/env python
#encoding:utf-8

from sqlalchemy.orm import sessionmaker
import orm_m2m

Session = sessionmaker(bind=orm_m2m.engine)()


# A1 = orm_m2m.Address(name="hunan")
# A2 = orm_m2m.Address(name="guangdong")
# G1 = orm_m2m.Groups(name="Admin")
# G2 = orm_m2m.Groups(name="Guest")
#
# Session.add_all([A1,A2,G1,G2])
# Session.commit()
# U1 = orm_m2m.Userss(name="huang",group=1,address=2)
# Session.add(U1)
# Session.commit()

#
# a1 = orm_m2m.C_Address(name="hunan")
# a2 = orm_m2m.C_Address(name="hubei")
# c1 = orm_m2m.Customer(name="shopp",bi_address=1,si_address=1)
# Session.add_all([a1,a2,c1])
# Session.commit()

b1 = orm_m2m.Book(name="python",pub_data="2017-01-01")
b2 = orm_m2m.Book(name="Linux",pub_data="2016-01-01")
a1 = orm_m2m.Author(name="junly")
a2 = orm_m2m.Author(name="huang")

# b1.authors(a1)
# b2.authors(a1,a2)
a1.book_2_author(b1)
a2.book_2_author(b1,b2)
Session.add_all([b1,b2,a1,a2])
Session.commit()






