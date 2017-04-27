import os,commands,sys
size = os.path.getsize('server.py')
print size
f = open('server.py','r')
fseek = f.seek(0,os.SEEK_END)
print fseek.tell()