#!/usr/bin/env python
#coding:utf-8
#
# names="huang"
# def name():
#     print("name")
#import shutil
#help(shutil.make_archive)
#shutil.make_archive(base_name='abc',format='zip',base_dir='d:\\python\\Learn')


import configparser
config = configparser.ConfigParser()
config['sec_a']={'a_key1' : 20,'a_key2': 10}
#conf = config.
with open('abc.txt','w',encoding='utf-8') as  f :
    f.write(config)

