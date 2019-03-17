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
        print "#########ACCNO##############\n\n",self.accno
        print "#########NOTE YOUR ATMPIN:##############\n\n", self.atmpin
        ATM.filesave(self)
        print' \n\naccount added succcessfully'
    def checkbalance(self):
        print 'your balance INR:',self.bal
    def display(self,i):
        fi = open('bankdetails.txt', 'r', 1)
        liss=fi.readlines()
        print liss[i]
        # print 'name:', self.name, '\nphone no:', self.ph, '\naddress:', self.addr
    def deposit(self,i,money):
        self.bal += money
        fi = open('bankdetails.txt', 'r', 1)
        liss = fi.readlines()

        print'cash deposited'
    def withdraw(self,atm,withdraw):
        if self.atmpin == atm:
            if self.bal > 0:
                if self.bal >= withdraw:
                    self.bal -= withdraw
                    print 'INR', withdraw, "withdrawed"
                    print 'available balance=INR', self.bal
                else:
                    print"insufficient fund"
            else:
                print"insufficient fund"
        else:
            print "atm pin is wrong"

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
        accno=10001+count
        balance=0
        atmpin+=1
        obj.append(ATM(accno,name,ph,addr,balance,atmpin))
        obj[count].addacc()
        count+=1
    if choice==2:
        flag = 0
        acc=input("your acc no:")
        money=input("amount:")
        fi = open('bankdetails.txt', 'r', 1)
        countl = fi.readlines()
        # print countl
        lim = len(countl)
        for i in range(lim):
            sp = countl[i].split(',')
            # print sp
            if sp[0] == acc:
                obj[i] = ATM(1, 'a', 9, 'we', 0, 9)
                obj[i].deposit(i,money)
                break

        if flag==0:
            print"no account"
    if choice==3:
        acc = input("your acc no:")
        for i in range(count):
            if i + 10001 == acc:
                obj[i].checkbalance()
    if choice==4:
        flag=0
        acc = input("your acc no:")
        atm=input("enter your atmpin:")
        withdraw = input("amount:")
        for i in range(count):
            if i + 10001 == acc:
                flag=1
                obj[i].withdraw(atm,withdraw)
                break
        if flag==0:
            print"no account"
    if choice==5:
        acc=raw_input("your acc no:")
        fi = open('bankdetails.txt', 'r', 1)
        countl=fi.readlines()
        # print countl
        lim=len(countl)
        for i in range(lim):
            sp=countl[i].split(',')
            # print sp
            if sp[0]==acc:
                obj[i]=ATM(1, 'a', 9, 'we', 0, 9)
                obj[i].display(i)
                break
    if choice==6:
        fi.close()
        print " thanks"
        break
    fi.close()