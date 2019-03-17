import threading
import time
import oopspgm.atmfilepgm
import os
sss=os.name
print sss
class MyReserve(threading.Thread):
    time=10
    seat=[]
    seatname=[]
    def __init__(self,name,ph,resereid):
        self.n=name
        self.ph=ph
        self.rid=resereid
        MyReserve.seat=avail
        MyReserve.seatname=seatname
        threading.Thread.__init__(self)
    def run(self):
        l.acquire()
        print self.n,'is in'
        flg=0
        cost=0
        while 1:
            print '1-book\n2-exit\n'
            str1=input("enter option")
            if str1 ==1:
                print'seats available',MyReserve.seat
                while 1:
                    seat=input("select seat no:")
                    if MyReserve.seat[seat-1]=='':
                        print'already booked'
                        continue
                    else:
                        MyReserve.seat[seat-1]=''
                        print MyReserve.seat
                        MyReserve.seatname[seat-1]=self.n
                        print 'seat no:',seat,'is selected'
                        y=raw_input('book another one(y/n):')
                        if y=='y':
                            continue
                        else:
                            num=input('press 1 for payment')
                            if num==1:
                                print'seat no:',
                                for i in range(len(MyReserve.seatname)):
                                    if MyReserve.seatname[i]==self.n:
                                        cost+=200
                                        print i+1,
                                print'is selected'
                                print'cost is INR:',cost
                                num=input('confirm your payment by press 1/for exit press any other key:')
                                if num==1:
                                    print 'please wait...'
                                    time.sleep(3)
                                    print'bank server is loading...'
                                    time.sleep(6)
                                    print 'server loaded successfully'
                                    time.sleep(2)
                                    num=input('proceed payment by pressing 1:')
                                    if num==1:
                                        flg=1
                                        # f=open('G:\\workspace\\pythonpgm\\oopspgm\\bankdetails.txt','r',1)
                                        # print f.read()
                                        flag = 0
                                        acc = raw_input("your acc no:")
                                        atm = raw_input("enter your atmpin:")
                                        withdra = cost
                                        f = open('bankdetails.txt', 'r', 1)
                                        ccc = f.readlines()
                                        # print ccc
                                        for i in range(len(ccc)):
                                            s = ccc[i].split(',')
                                            # print s[0]
                                            # print acc
                                            # print s[5]
                                            # print atm
                                            if sss =='posix':
                                                if s[0] == acc and s[5] == atm+'\r\n':
                                                    print 'hai ',s[1]
                                                    print 'your payment is processing...'
                                                    time.sleep(6)
                                                    flag = 1
                                                    oopspgm.atmfilepgm.thirdpartywithdraw(i,withdra)
                                                    break
                                            elif sss=='nt':
                                                if s[0] == acc and s[5] == atm+'\n':
                                                    print 'hai ',s[1]
                                                    print 'your payment is processing...'
                                                    time.sleep(6)
                                                    flag = 1
                                                    oopspgm.atmfilepgm.thirdpartywithdraw(i,withdra)
                                                    break

                                        if flag == 0:
                                            print"no account/passwrd or pin is wrong"
                                        # oopspgm.atmfilepgm.ATM.withdraw()

                        break
                if flg==1:
                    print'**THANKS', self.n, '****'
                    l.release()
                    break
            elif str1==2:
                print'**THANKS,',self.n,'****'
                l.release()
                break
            else:
                print"invalid choice"
                l.release()
                break
avail=[]
seatname=[]
for i in range(10):
    avail.append(i+1)
    seatname.append('')
l=threading.Lock()
print"****welcome to seat reservation portal***\n***cancelation not available temporarly******" \
     "\n-------total no:of seats:10"
obj1=MyReserve('ABC',98764,1)
obj2=MyReserve('XYZ',435345,2)
obj1.start()
obj2.start()
