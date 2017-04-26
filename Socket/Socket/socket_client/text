#!/usr/bin/env python
#encoding:utf-8

'''
import SocketServer
class MyServer(SocketServer.BaseServer):
    def handle(self):
        conn = self.request
        conn.sendall("mulit process ")
        Flag = True
        while True:
            data = conn.recv(1024)
            if data == 'exit' or data == 'Exit':
                Flag  = False

            elif data == 0:
                conn.sendall("you input is 0")
            else:
                conn.sendall('Please reinput:')

if __name__ == "__main__":
    server = SocketServer.ThreadingTCPServer(('localhost',9990),MyServer)
    server.serve_forever()


'''

#!/usr/bin/env python
#encoding:utf-8
'''
import SocketServer
class MyServer(SocketServer.BaseServer):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data: break
            self.reqest.sendall(data.upper())
if __name__ == "__main__":
    ip,port = 'localhost',9999
    server = SocketServer.ThreadingTCPServer((ip,port),MyServer)
    server.serve_forever()
'''

import socket,os,commands,time


ip = 'localhost'
port = 1993
server = socket.socket()
server.bind((ip,port))
server.listen(4)
while True:
    print("Wait Connection.")
    conn,addr = server.accept()
    print("New Connection:",addr)
    while True:
        recv_data = conn.recv(1024)
        if not recv_data:
            print("Disconnet to Server")
            break
        print("Exec command: %s" % recv_data)
        cmd_result = commands.getoutput(recv_data)
        if len(cmd_result) == 0:
            cmd_result = 'command exec result is None.'
        print(str(len(cmd_result)))
        conn.send(str(len(cmd_result)))
        print(conn.recv(1024))
        conn.send(cmd_result)


server.close()




