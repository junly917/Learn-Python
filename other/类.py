#!/usr/bin/env python
#encoding:utf-8

class bar(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print self.name,self.age

bar("huang",23)