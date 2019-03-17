from tkinter import *
import AtmWithTKinter
import tkMessageBox
class logandreg:
    def iconifyfun(self,win1,win2):
        win2.withdraw()
        win1.deiconify()
    def backbutton(self,win1,win2):
        ab = Button(win2, width=8, height=1, text='back', foreground='white', activebackground="red",
                    background="gray", command=lambda:self.iconifyfun(win1,win2))
        ab.place(x=0,y=0)
    def login(self,win):
        win.withdraw()
        win1 = Toplevel(win)
        win1.title('welcome to XYZ BANK')
        win1.geometry('{}x{}'.format(1000, 1000))
        Label(win1,text='username').place(x=100,y=250)
        a = StringVar()
        ab = Entry(win1,bg='yellow',borderwidth=5,highlightbackground='green',width=50,textvariable=a)
        ab.focus()
        ab.place(x=300, y=250)
        Label(win1, text='password').place(x=100, y=400)
        b = StringVar()
        cd = Entry(win1,bg='yellow',borderwidth=5,highlightbackground='green',width=50,textvariable=b,show='*')
        cd.place(x=300, y=400)
        ab = Button(win1, width=10, height=2, text='login', foreground='white', activebackground="red",
                    background="gray", command=lambda:ob.tkfunFopt(win,win1,a,cd))
        ab.place(x=300, y=500)
        self.backbutton(win,win1)
        win.mainloop()

class Mytk:
    def fun(self,win,win1,vara,varp,varbal,varatm):
        # name=''
        addr=vara
        phno=varp
        minbalance=varbal
        atmno=varatm
        objatm = AtmWithTKinter.ATM()
        objatm.addacc(addr,phno,atmno,minbalance,AtmWithTKinter.accno)
        win1.withdraw()
        win.deiconify()
        # tkMessageBox.showinfo('a','name:'+name)
        # print name
    def tkfunlogger(self):
        win=Tk()
        win.title('welcome to XYZ BANK')
        win.geometry('{}x{}'.format(1000,1000))
        ab = Button(win, width=50, height=4, text='register', foreground='black',font=("Arial Bold", 10), activebackground="red",
                    background="yellow", command=lambda: self.regfun(win))
        ab.place(x=300, y=200)
        cd = Button(win, width=50, height=4, text='login', activebackground="red",font=("Arial Bold", 10), background="yellow",
                    command=lambda: ob2.login(win))
        cd.place(x=300, y=400)
        win.mainloop()
    def depofun(self,winhome,winprev):
        winprev.withdraw()
        win4=Toplevel(bg='yellow')
        win4.title('deposit')
        win4.geometry('{}x{}'.format(500,400))
        Label(win4,text='accno:').place(x=10,y=50)
        v1=IntVar()
        t1=Entry(win4,textvariable=v1)
        t1.place(x=80,y=50)

        Label(win4, text='amount:').place(x=10, y=90)
        v2= IntVar()
        t2 = Entry(win4, textvariable=v2)
        t2.place(x=80, y=90)

        bb=Button(win4,text='submit',bg='gray',command=lambda :self.fundepo(win4,t1.get(),t2.get()))
        bb.place(x=50,y=130)
        ob2.backbutton(winprev,win4)
        win4.mainloop()
    def tkfunFoption(self,user,winhome,winofprev):
        winofprev.withdraw()
        win2 = Toplevel()
        msg='welcome '+user
        win2.title(msg)
        win2.geometry('{}x{}'.format(750, 500))
        ab = Button(win2,width=50,height=2, text='addacc',foreground='white',activebackground="red",background="green",
                    command=lambda:self.tkinsertfun(winhome,win2))
        ab.place(x=200,y=20)
        cd= Button(win2, width=50, height=2, text='deposit', activebackground="red", background="yellow",
                   command=lambda: self.depofun(winhome,win2))
        cd.place(x=200, y=100)
        ef = Button(win2, width=50, height=2, text='checkbalance', activebackground="red", background="green",
                   command=lambda: self.checkbalancefun(winhome,win2))
        ef.place(x=200, y=180)
        fg = Button(win2, width=50, height=2, text='withdraw', activebackground="red", background="yellow",
                   command=lambda: self.withdrawfun(winhome,win2))
        fg.place(x=200, y=260)
        gh = Button(win2, width=50, height=2, text='display', activebackground="red", background="green",
                   command=lambda: self.displayfun(winhome,win2))
        gh.place(x=200, y=340)
        ij = Button(win2, width=50, height=2, text='quit', activebackground="red", background="yellow",
                   command=lambda: win2.destroy())
        ij.place(x=200, y=420)
        ob2.backbutton(winofprev,win2)
        win2.mainloop()
    def tkinsertfun(self,win1,win2):
        win2.withdraw()
        win3=Toplevel(win1)
        win3.title('Welcome to XYZ Bank')
        win3.geometry('{}x{}'.format(750,500))

        lage=Label(win3, text='address').place(x=20,y=50)
        vara=StringVar()
        taddr=Entry(win3, textvariable=vara)
        taddr.place(x=100,y=50)

        lphone=Label(win3, text='phone:').place(x=20,y=90)
        varp=IntVar()
        tphone=Entry(win3, textvariable=varp)
        tphone.place(x=100,y=90)

        lbal = Label(win3, text='minbalance')
        lbal.place(x=20, y=210)
        varbal = IntVar()
        tbal = Entry(win3, textvariable=varbal)
        tbal.place(x=100, y=210)

        ltm = Label(win3, text='atmno:').place(x=20, y=250)
        varatm = IntVar()
        tatm = Entry(win3, textvariable=varatm)
        tatm.place(x=100, y=250)

        bbb=Button(win3,text='submit',command=lambda :self.fun(win2,win3,taddr.get(),tphone.get()
                                                               ,tbal.get(),tatm.get()))
        bbb.place(x=300,y=300)
        ob2.backbutton(win2,win3)
        win2.mainloop()

    def regfun(self,win):
        win.withdraw()
        winr=Toplevel(win)
        winr.geometry('{}x{}'.format(500,500))

        lname = Label(winr, text='name:').place(x=20, y=50)
        vara = StringVar()
        tname = Entry(winr, textvariable=vara)
        tname.place(x=150, y=50)

        luser = Label(winr, text='username:').place(x=20, y=100)
        varuser = StringVar()
        tuser = Entry(winr, textvariable=varuser)
        tuser.place(x=150, y=100)

        lpass = Label(winr, text='new password').place(x=20, y=150)
        varpass1 = StringVar()
        tpass = Entry(winr, textvariable=varpass1, show='*')
        tpass.place(x=150, y=150)

        lpass = Label(winr, text='confirm password').place(x=20, y=210)
        varpass = StringVar()
        tcpass = Entry(winr, textvariable=varpass, show='*')
        tcpass.place(x=150, y=210)
        objatm = AtmWithTKinter.ATM()
        bbb = Button(winr, text='submit', command=lambda: objatm.regfun(win,winr,tname.get(),tuser.get(),tpass.get(),tcpass.get()))
        bbb.place(x=200,y=270)
        ob2.backbutton(win,winr)
        # win.deiconify()
        winr.mainloop()
    def tkfunFopt(self, win, win1, param, param1):
        print param.get()
        print param1.get()
        objatm = AtmWithTKinter.ATM()
        objatm.reg(param.get(),param1.get(),win,win1)
        # self.tkfunFoption(win,win1)

    def fundepo(self, win4, acc,amt):
        objatm = AtmWithTKinter.ATM()
        objatm.deposit(acc,amt)
        win4.withdraw()

    def checkbalancefun(self, winhome, win2):
        win2.withdraw()
        win3=Toplevel(winhome)
        win3.geometry('{}x{}'.format(500,500))
        Label(win3,text='enter accno or username:').place(x=30,y=50)
        v1=StringVar()
        e1=Entry(win3,textvariable=v1)
        e1.place(x=150, y=50)

        Label(win3,text='enter password:').place(x=30,y=100)
        v2=StringVar()
        e2=Entry(win3,textvariable=v2,show='*')
        e2.place(x=150,y=100)

        objatm = AtmWithTKinter.ATM()
        bb=Button(win3,text='submit',command=lambda :objatm.checkbalance(win2,win3,e1.get(),e2.get()))
        bb.place(x=50,y=150)
        ob2.backbutton(win2,win3)
        win3.mainloop()

    def displayfun(self, winhome, win2):
        win2.withdraw()
        win5 = Toplevel(winhome)
        win5.geometry('{}x{}'.format(500, 500))
        Label(win5, text='enter accno or username:').place(x=30, y=50)
        v1 = StringVar()
        e1 = Entry(win5, textvariable=v1)
        e1.place(x=200, y=50)

        Label(win5, text='enter password:').place(x=30, y=100)
        v2 = StringVar()
        e2 = Entry(win5, textvariable=v2, show='*')
        e2.place(x=200, y=100)

        objatm = AtmWithTKinter.ATM()
        bb = Button(win5, text='submit', command=lambda: objatm.display(win2, win5, e1.get(), e2.get()))
        bb.place(x=100, y=150)

        ob2.backbutton(win2, win5)
        win5.mainloop()

    def withdrawfun(self, winhome, win2):
        win2.withdraw()
        win6 = Toplevel(winhome)
        win6.geometry('{}x{}'.format(500, 500))

        Label(win6, text='enter accno:').place(x=30, y=50)
        v1 = StringVar()
        e1 = Entry(win6, textvariable=v1)
        e1.place(x=200, y=50)

        Label(win6, text='enter password:').place(x=30, y=100)
        v2 = StringVar()
        e2 = Entry(win6, textvariable=v2, show='*')
        e2.place(x=200, y=100)

        Label(win6, text='enter atmno:').place(x=30, y=150)
        v3 = StringVar()
        e3 = Entry(win6, textvariable=v3, show='*')
        e3.place(x=200, y=150)

        Label(win6, text='enter amount:').place(x=30, y=200)
        v4 = StringVar()
        e4 = Entry(win6, textvariable=v4)
        e4.place(x=200, y=200)


        objatm = AtmWithTKinter.ATM()
        bb = Button(win6, text='submit', command=lambda: objatm.withdraw(win2, win6, e1.get(), e2.get(),e3.get(),e4.get()))
        bb.place(x=100,y=250)

        ob2.backbutton(win2, win6)
        win6.mainloop()

ob2=logandreg()
ob=Mytk()
# ob.tkfunFoption()
# ob.tkinfun()