print "options:\n1-registration\n2-Login\n"
f=open('login3.txt','a',1)
f=open('login3.txt','r',1)
dict={}
key=0
list1=[]
while 1:
    ch = input("enter your choice:")
    if ch==1:
        # temp={}
        f = open('login3.txt', 'a', 1)
        f2=open('login2.txt','a',1)
        username=raw_input("enter your username:")
        password=raw_input("enter your password:")
        username=username+','
        password=password+'\n'
        # temp.setdefault('user',username)
        # temp.setdefault('pass',password)
        # dict.setdefault(key,temp)
        # key+=1
        f.write(username)
        f.write(password)
        print "registration successfull##"
        f.close()
        # dict.setdefault(key,f.readlines(2))
        # key+=1
        # print dict
        # print f.read()
    elif ch==2:
        flag = 0
        user=raw_input("username:")
        passs=raw_input("password")
        passs = passs + '\n'
        f = open('login3.txt', 'r', 1)
        c=f.readline()
        while c:
            y=c.split(',')
            # if y[0]==user:
            #     flag=2
            if y[0]==user and y[1]==passs:
                flag=1
                break
            c = f.readline()
        if flag==1:
            print "options:\n1-view prof\n2-edit username\n3-edit password"
            logchoice=input("your choice:")
            if logchoice==1:
                print 'username=',user
                print 'password=',passs
            elif logchoice==2:
                list1=[]
                # print y
                # print z
                f2 =open('login2.txt','w',1)
                f2.write('')
                f=open('login3.txt','r',1)
                f2 = open('login2.txt', 'a', 1)
                list1=f.readlines()
                # print list1[0]
                # input()
                upd = raw_input("new username:")
                for i in range(len(list1)):
                    z = list1[i].split(',')
                    if z[0]==user and z[1]==passs:
                        z[0]=upd+','
                        yz=z[0]+z[1]
                        list1[i]=yz
                f2.writelines(list1)
                f2=open('login2.txt','r',1)
                f=open('login3.txt','w',1)
                f.write('')
                f=open('login3.txt','a',1)
                print f2.read()
                for i in list1:
                    f.write(i)
                # f=open('login.txt','w',1)
                # f.write(f2)
                print list1
                f.close()
                f2.close()
            elif logchoice==3:
                list=[]
                f2 = open('login2.txt', 'w', 1)
                f2.write('')
                f = open('login3.txt', 'r', 1)
                f2 = open('login2.txt', 'a', 1)
                list1 = f.readlines()
                for i in range(len(list1)):
                    if list1[i] == user:
                        pas = raw_input("new password:")
                        list1[i+1] = pas + '\n'
                        # f2.write(list1[i+1])
                    else:
                        f2.write(list1[i])
                f2 = open('login2.txt', 'r', 1)
                f = open('login3.txt', 'w', 1)
                f.write('')
                f = open('login3.txt', 'a', 1)
                # print f2.read()
                for i in list1:
                    f.write(i)
                print f
                # f=open('login.txt','w',1)
                # f.write(f2)
                # print list1
                f.close()
                f2.close()
            else:
                print "invalid option"
        elif flag==0:
            print "not registered"

        else:
            # print y
            # print z
            print "username or password are incorrect!!!"
        f.close()



    else:
        print"invalid"
    print"do you want to continue:(y/n)"
    y=raw_input("")
    if(y=='y'):
        continue
    else:
        break
