import pymysql
import tkinterAtm
import tkMessageBox
from tkinter import *
db=pymysql.connect('localhost','root','root')
cur=db.cursor()
cur.execute('use bankforiegndb')
class ATM:
    def addacc(self,addr,phno,atmno,bal,accno):
        accno = int(accno) + 1
        cur.execute('select MAX(id) from register')
        rs=cur.fetchone()
        id=rs[0]
        cur.execute('select accno from login where fkid=%s',id)
        rs=cur.fetchone()
        if rs==None:
            cur.execute('update register set address=%s,phno=%s,atmno=%s where id=%s', (addr, phno, atmno,id))
            db.commit()
            self.login(accno,id,bal)
        else:
            tkMessageBox.showinfo('error','you have already an account')
    def login(self,accno,id1,bal):
        cur.execute('select MAX(id) from login')
        rs = cur.fetchone()
        id = rs[0]
        print id
        cur.execute('update login set accno=%s,fkid=%s where id=%s', (accno,id1,id))
        db.commit()
        self.balance(bal,id)
    def balance(self,bal,id2):
        print id2
        # raw_input()
        cur.execute('insert into balance(balance,fkid) values(%s,%s)', (bal,id2))
        db.commit()
        tkMessageBox.showinfo('success','account added successfully')
    def deposit(self,acc,amt):
        cur.execute('select * from login join balance on login.id=balance.fkid and login.accno=%s',acc)
        rs=cur.fetchone()
        print rs
        if rs==None:
            print 'account not found'
        else:
            # amt=input('enter the amount:')
            total=rs[6]+int(amt)
            print total
            print rs[5]
            cur.execute('update balance set balance=%s where id=%s',(total,rs[5]))
            db.commit()
            tkMessageBox.showinfo('deposit','INR'+amt+'credited\nnew balance INR'+str(total))
    def checkbalance(self,win2,win3,accno,passw):
        cur.execute('select * from login '
                        'join balance on login.id=balance.fkid '
                        'join register on login.fkid=register.id ')
        rs = cur.fetchall()
        # print rs
        # if rs==():
        #     print'account not found'
        for i in rs:
            if str(i[1])==accno or i[2]==accno:
                # print rs
                # atm = raw_input('enter password:')
                atm=passw
                if i[3] == atm:
                    print 'balance is:INR', i[6]
                    tkMessageBox.showinfo('msg','balance is INR'+str(i[6]))
                    win3.withdraw()
                    win2.deiconify()
                    break
    def withdraw(self,win1,win2,accno,passs,atm,amt):
        cur.execute('select * from login join balance on login.id=balance.fkid '
                    'join register on login.fkid=register.id '
                    'and login.accno=%s', accno)
        rs = cur.fetchone()
        if rs==None:
            print'acc not found'
        else:
            print rs
            # passs=raw_input('enter password:')
            if rs[3]==passs:
                # atm=input('enter atmno:')
                atm=int(atm)
                if rs[12]==atm:
                    print 'hello',rs[2]
                    # amt = input('enter the amount to withdraw:')
                    total = rs[6] -int(amt)
                    if total<0:
                        print'insufficient balance'
                    else:
                        print total
                        print rs[5]
                        cur.execute('update balance set balance=%s where id=%s', (total, rs[5]))
                        db.commit()
                        print 'withdraw successfully'
                        tkMessageBox.showinfo('success','amount withdrawed')
                        win2.withdraw()
                        win1.deiconify()
    def display(self,win1,win2,accno,passwd):
        cur.execute('select * from login')
        rs=cur.fetchall()
        usern=accno
        try:
            accno=int(accno)
        except ValueError,arg:
            print''
        for i in rs:
            if i[1]==accno and i[3]==passwd or i[2]==usern and i[3]==passwd:
                cur.execute('select * from register where id=%s',(i[4]))
                rs=cur.fetchone()
                cur.execute('select * from balance where fkid=%s',(i[0]))
                rc=cur.fetchone()
                print"\033[1;31;48m",
                print 'name:',rs[1]
                print 'username:',i[2]
                print 'password:',i[3]
                print 'address:',rs[2]
                print 'phone no:',int(rs[3])
                rs3=int(rs[3])
                print 'account num:',i[1]
                print 'atmno:',rs[4]
                print 'balance:',rc[1]
                print"\033[1;34;48m"
                tkMessageBox.showinfo('display','name:'+str(rs[1])+'\nusername:'+i[2]+'\npassword'+i[3]+'\naddress:'+
                                      rs[2]+'\nphone no'+str(rs3)+'\naccno:'+str(i[1])+'\natmno:'+str(rs[4])+
                                                                                    '\nbalance'+str(rc[1]))
                break
        win2.withdraw()
        win1.deiconify()
    def reg(self,user,pas,win,win1):
        cur.execute('select username,password from login where username=%s and password=%s',(user,pas))
        rs=cur.fetchone()
        if rs==None:
            tkMessageBox.showinfo('error','unknown account!!!!')
        else:
            ob=tkinterAtm.Mytk()
            ob.tkfunFoption(user,win,win1)
    def regfun(self,win,winr,name,usern,pass1,pass2,):
        print name,usern,pass1,pass2
        cur.execute('select username from login where username=%s',(usern))
        rs=cur.fetchone()
        if rs==None:
            if pass1==pass2:
                cur.execute('insert into login(username,password) values(%s,%s)',(usern,pass1))
                cur.execute('insert into register(name) values(%s)',(name))
                db.commit()
                tkMessageBox.showinfo('success','insert successfully\n login to continue')
                winr.withdraw()
                win.deiconify()
            else:
                tkMessageBox.showerror('error','password not match')
        else:
            tkMessageBox.showwarning('error','username already exists\nselect another one')
ob=ATM()
cur.execute('select max(accno) from login')
rs=cur.fetchone()
if rs[0]==None:
    accno=1000
else:
    accno=rs[0]
print accno
ob=tkinterAtm.Mytk()
ob.tkfunlogger()
# ob.tkinsertfun()
# while 1:
#     print'option\n1-addacc\n2-deposit\n3-checkbalance\n4-withdraw\n5-display\n6-exit'
#     choice=input('enter your choice:')
#     if choice==1:
#         accno=int(accno)+1
#         # name=raw_input('enter your name:')
#         # addr=raw_input('enter address:')
#         # phno=input('enter phone no:')
#         # username=raw_input('enter username')
#         # password=raw_input('enter a password')
#         # minbalance=input('set a min balance:')
#         # atmno=input('choose atm no:')
#         obtk=tkinterAtm.Mytk()
#         obtk.tkinfun()
#         # ob.addacc(name,addr,phno,atmno,username,password,minbalance,accno)
#     elif choice==2:
#         acc=input('enter the account number:')
#         ob.deposit(acc)
#     elif choice==3:
#         acc =raw_input('enter the accno: or username::')
#         ob.checkbalance(acc)
#     elif choice==4:
#         acc=input('enter the accno:')
#         ob.withdraw(acc)
#     elif choice==5:
#         accno=raw_input('enter accno: or username:')
#         password=raw_input('enter your password:')
#         ob.display(accno,password)
#     elif choice==6:
#         break

