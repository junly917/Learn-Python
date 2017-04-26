#!/usr/bin/env python
#encoding:utf-8


import  socket,json,sys,hashlib,time

host,port = 'localhost',31397

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
                result = self.client.recv(1024)
                print(result)
                lens = json.loads(result)   #recv commands result length
                # print(type(lens),':',lens)
                if lens['len'] > 1024:
                    self.client.send('continue')    #发送继续状态
                    part_len = 0
                    tatol_data = ""
                    while part_len < int(lens):
                        data = self.client.recv(1024)
                        part_len +=len(data)
                        tatol_data += data

                elif lens['len'] > 0 and lens['len'] < 1024 :
                    self.client.send('continue')  # 发送继续状态
                    tatol_data = self.client.recv(1024)

                else:
                    tatol_data = lens['status']
                print(tatol_data)

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




