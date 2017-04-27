#!/usr/bin/env python
#encoding:utf-8


import  socket,json,sys,hashlib,time

host,port = 'localhost',31394

class ftp_opt(object):
    '''
    auth login status
    '''
    def __init__(self):

        self.client = socket.socket()
        self.client.connect((host, port))

        #
        # self.login(self.user,md5passwd)


    def login(self,user,passwd):
        '''
        transfer user,passwd to server ,auth user,passwd
        '''
        md5passwd = self.md5sums(passwd)
        authdata={}
        authdata['user'] = user
        authdata['passwd'] = md5passwd
        print("before send user:%s ,passwd: %s" % (user,md5passwd))
        data = json.dumps(authdata)
        print(data)
        self.client.send(data)
        auth_result = self.client.recv(1024)
        if auth_result == 'login':
            return auth_result
        else:
            return False

    def md5sums(self,passwd):
        '''
        passwd jiami 
        '''

        m = hashlib.md5()
        m.update(passwd)
        return m.hexdigest()

    def opt_ftp(self):
        print("""
                --------------Welcome to Junly Ftp Server ---------------
                """)
        while True:
            userdata = raw_input("-->:").strip()
            if len(userdata) == 0 :
                continue
            elif userdata == 'quit' or userdata == 'exit':
                #exit login
                self.client.close()
                main().login
            else:

                self.client.send(userdata)      #send commands
                # print("第一次发送的命令是:",userdata)


                result = self.client.recv(1024)
                # print("num1 recv dict is :", result, "type is:", type(result))

                recv_data = json.loads(result)   #recv commands result length
                # print('data:',recv_data)
                total_lens = recv_data['len']
                print 'lens is %s' %total_lens
                if total_lens > 1024:

                    # print("第二次要求发送结果过来")
                    self.client.send('continue')    #发送继续操作状态
                    print('continue')

                    part_len = 0
                    tatol_data = ""
                    recv =1
                    while part_len < int(total_lens):
                        new_recv_data = self.client.recv(1024)
                        print("new_recv_data:" , new_recv_data)

                        part_len += len(new_recv_data)
                        print("len(data) is %s" % len(new_recv_data))
                        recv +=1
                        tatol_data += new_recv_data
                        if recv == 20:
                            break

                else:
                    # print("要求接收小于1024的内容")
                    self.client.send('continue')  # 发送继续状态

                    # print("开始接收小于1024的内容")
                    tatol_data = self.client.recv(1024)


                print (tatol_data)


class main(object):
    def __init__(self):
        pass

    @property
    def login(self):
        print("""
        --------------Welcome to Junly Ftp Server ,Please Login---------------
        """)
        login_count = 0     #login counts
        while True:

            # login count le 5
            if login_count > 5:
                time.sleep(3)

            user = raw_input("login:").strip()
            passwd = raw_input("passwd:").strip()
            #input is Null
            print(user,passwd)
            if len(user)==0 or len(passwd) == 0:
                continue
            else:

                # auth user and passwd
                result = ftp_opt()
                login_result = result.login(user,passwd)

                # login sucesses
                if login_result == 'login':
                    result.opt_ftp()

                # login failed
                else:
                    print("login failed,Please retry.")
                    login_count +=1
                    continue

if __name__ == "__main__":
    # start = main()
    # start.login
    s = ftp_opt()
    s.opt_ftp()




