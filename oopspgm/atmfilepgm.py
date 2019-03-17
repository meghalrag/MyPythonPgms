class ATM:
    def __init__(self,accno,name,ph,address,balance,atmpin):
        self.accno=accno
        self.name=name
        self.ph=ph
        self.addr=address
        self.bal=balance
        self.atmpin=atmpin
    def filesave(self):
        fi = open('bankdetails.txt', 'a', 1)
        accnew=str(self.accno)+','
        namenew=self.name+','
        phnew=str(self.ph)+','
        addrnew=self.addr+','
        balnew=str(self.bal)+','
        atmpinnew=str(self.atmpin)+'\n'
        fi.write(accnew)
        fi.write(namenew)
        fi.write(phnew)
        fi.write(addrnew)
        fi.write(balnew)
        fi.write(atmpinnew)
    def addacc(self):
        print 'name:',self.name,'\nphone no:',self.ph,'\naddress:',self.addr
        print "#########ACCNO##############\n",self.accno
        print "#########NOTE YOUR ATMPIN:##############\n", self.atmpin
        ATM.filesave(self)
        print' account added succcessfully'
    def checkbalance(self,i):
        f=open('bankdetails.txt','r',1)
        ccc=f.readlines()
        chb=ccc[i].split(',')
        print 'availabel balance:INR',chb[4]
    def display(self,i):
        fi = open('bankdetails.txt', 'r', 1)
        liss=fi.readlines()
        sq=liss[i].split(',')
        print 'ACC NO:',sq[0]
        print 'NAME  :',sq[1]
        print 'PHONE NO:',sq[2]
        print 'ADDRESS :',sq[3]
        print 'ACC BALANCE:',sq[4]

        # print 'name:', self.name, '\nphone no:', self.ph, '\naddress:', self.addr
    def deposit(self,i,money):
        fi = open('bankdetails.txt', 'r', 1)
        liss = fi.readlines()
        # print liss
        s=liss[i].split(',')
        x=int(s[4])
        self.bal=x+money
        s[4]=str(self.bal)
        # print s
        newstr=''
        for im in range(len(s)):
            newstr+=s[im]
            if im==len(s)-1:
                break
            newstr+=','
        liss[i]=newstr
        # print liss
        # print liss[i]
        fi.close()
        fil=open('bankdetails.txt','w',1)
        for j in liss:
            fil.write(j)
        print'amount creditted successfully'
    def withdraw(self,i,withdr):
        f=open('bankdetails.txt','r',1)
        cccc=f.readlines()
        ss=cccc[i].split(',')
        availbal=int(ss[4])
        newbal=availbal-withdr
        if newbal>=0:
            ss[4]=str(newbal)
            newstr=''
            for jm in range(len(ss)):
                newstr+=ss[jm]
                if jm==len(ss)-1:
                    break
                newstr+=','
            cccc[i]=newstr
            f = open('bankdetails.txt', 'w', 1)
            for j in cccc:
                f.write(j)
            print 'amount debitted succesfully'
        else:
            print 'insufficient balance'

        # if self.atmpin == atm:
        #     if self.bal > 0:
        #         if self.bal >= withdraw:
        #             self.bal -= withdraw
        #             print 'INR', withdraw, "withdrawed"
        #             print 'available balance=INR', self.bal
        #         else:
        #             print"insufficient fund"
        #     else:
        #         print"insufficient fund"
        # else:
        #     print "atm pin is wrong"
def thirdpartywithdraw(i,withdr):
    # print i
    f = open('bankdetails.txt', 'r', 1)
    cccc = f.readlines()
    # print cccc
    # num=input()
    s = cccc[i].split(',')
    availbal = int(s[4])
    newbal = availbal - withdr
    if newbal >= 0:
        s[4] = str(newbal)
        newstr = ''
        for jm in range(len(s)):
            newstr += s[jm]
            if jm == len(s) - 1:
                break
            newstr += ','
        cccc[i] = newstr
        f = open('bankdetails.txt', 'w', 1)
        for j in cccc:
            f.write(j)
        print 'payment is successfull'
    else:
        print 'insufficient balance'
def fun():

    obj=list()
    fi = open('bankdetails.txt', 'a', 1)
    fi = open('bankdetails.txt', 'r', 1)
    countl=fi.readlines()
    cou=len(countl)
    for i in range(cou):
       obj.append('')
    # print countl
    accno=''
    count=len(countl)
    # print count
    balance=0
    atmpin=1000
    while 1:
        print '\noptions\n1-addacc\n2-deposite\n3-checkbalance\n4-withdraw\n5-display\n6-exit'
        choice=input('your choice:')
        if choice==1:
            name=raw_input("your name:")
            ph=input("phone:")
            addr=raw_input("address:")
            atmpin=input('choose your atm pin:')
            accno=10001+count
            balance=0
            obj.append(ATM(accno,name,ph,addr,balance,atmpin))
            obj[count].addacc()
            count+=1
        elif choice==2:
            flagdep=0
            acc=raw_input("your acc no:")
            fi = open('bankdetails.txt', 'r', 1)
            countl = fi.readlines()
            # print countl
            lim = len(countl)
            for i in range(lim):
                sp = countl[i].split(',')
                # print sp
                if sp[0] == acc:
                    flagdep=1
                    print 'hai',sp[1]
                    money = input("enter amount:")
                    obj[i] = ATM(1, 'a', 9, 'we', 0, 9)
                    obj[i].deposit(i,money)
                    break
            if flagdep==0:
                print'no accno found'
        elif choice==3:
            flag=0
            fi=open('bankdetails.txt','r',1)
            acc = raw_input("your acc no:")
            atmp=raw_input('your atm pin:')
            countl = fi.readlines()
            # print countl
            lim = len(countl)
            for i in range(lim):
                sp = countl[i].split(',')
                # print sp
                if sp[0] == acc and sp[5]==atmp+'\n':
                    print 'hai',sp[1]
                    flag=1
                    obj[i] = ATM(1, 'a', 9, 'we', 0, 9)
                    obj[i].checkbalance(i)
                    break
            if flag==0:
                print 'no account found/accno,atmpin is incorrect'
        elif choice==4:
            flag=0
            acc = raw_input("your acc no:")
            atm=raw_input("enter your atmpin:")
            f=open('bankdetails.txt','r',1)
            ccc=f.readlines()
            for i in range(len(ccc)):
                s=ccc[i].split(',')
                if s[0]==acc and s[5]==atm+'\n':
                    flag=1
                    print 'hai',s[1]
                    print 'available balance:',s[4]
                    withdra = input("\nenter amount:")
                    obj[i] = ATM(1, 'a', 9, 'we', 0, 9)
                    obj[i].withdraw(i,withdra)
                    break
            if flag==0:
                print"no account/passwrd or pin is wrong"
        elif choice==5:
            flagdis=0
            acc=raw_input("your acc no:")
            fi = open('bankdetails.txt', 'r', 1)
            countl=fi.readlines()
            # print countl
            lim=len(countl)
            for i in range(lim):
                sp=countl[i].split(',')
                # print sp
                if sp[0]==acc:
                    flagdis=1
                    obj[i]=ATM(1, 'a', 9, 'we', 0, 9)
                    obj[i].display(i)
                    break
            if flagdis==0:
                print'accountno not found'

        elif choice==6:
            fi.close()
            print " thanks"
            break
        else:
            print'invalid choice'
        fi.close()
# fun()