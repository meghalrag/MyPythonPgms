from tkinter import *
import tkMessageBox

def fun2():
    win = Tk()
    win.title('MY APPLICATION')
    win.geometry('{}x{}'.format(750, 500))

    lname = Label(win, text='name:').place(x=20, y=10)
    varn = StringVar()
    tname = Entry(win,state='disabled',textvariable=varn)
    tname.place(x=100, y=10)

    lage = Label(win, text='age:').place(x=20, y=50)
    vara = IntVar()
    tage = Entry(win, textvariable=vara).place(x=100, y=50)

    lphone = Label(win, text='phone:').place(x=20, y=90)
    varp = IntVar()
    tphone = Entry(win, textvariable=varp).place(x=100, y=90)

    lgen = Label(win, text='gender:').place(x=20, y=130)
    varradio = IntVar()
    lradio = Radiobutton(win, text='male', value=0, variable=varradio).place(x=70, y=130)
    lradio2 = Radiobutton(win, text='female', value=1, variable=varradio).place(x=130, y=130)

    lcheck = Label(win, text='choose your skills:').place(x=20, y=170)
    varcheck1 = IntVar()
    varcheck2 = IntVar()
    varcheck3 = IntVar()
    varcheck4 = IntVar()
    check1 = Checkbutton(win, text='python', variable=varcheck1, onvalue=1, offvalue=0).place(x=50, y=190)
    check2 = Checkbutton(win, text='java', variable=varcheck2, onvalue=1, offvalue=0).place(x=50, y=210)
    check3 = Checkbutton(win, text='android', variable=varcheck3, onvalue=1, offvalue=0).place(x=50, y=240)
    check4 = Checkbutton(win, text='asp.net', variable=varcheck4, onvalue=1, offvalue=0).place(x=50, y=270)

    listcheck = Label(win, text='choose your country:').place(x=20, y=300)
    lb = Listbox(win)
    lb.insert(1, 'india')
    lb.insert(2, 'usa')
    lb.insert(3, 'uk')
    lb.insert(4, 'nz')
    lb.insert(5, 'aus')
    lb.place(x=40, y=330)

    b = Button(win, text='submit', command=lambda: fun()).place(x=300, y=300)
    win.mainloop()

def fun():
    l=[]
    l2=''
    name=varn.get()
    age=vara.get()
    ph=varp.get()
    if varradio.get()==1:
        gender='female'
    elif varradio.get()==0:
        gender='male'
    if varcheck1.get()==1:
        l.append('python')
    if varcheck2.get()==1:
        l.append('java')
    if varcheck3.get()==1:
        l.append('android')
    if varcheck4.get()==1:
        l.append('asp.net')
    listt=lb.get(ACTIVE)
    tkMessageBox.showinfo('a','name:\n'+name+',age:'+str(age)+',phone:'+str(ph)+',gender:'+gender+',country:'+listt
                          +',skill:'+l[0]+'&'+l[1])
    # print name

win=Tk()
win.title('MY APPLICATION')
win.geometry('{}x{}'.format(750,500))

lname=Label(win,text='name:').place(x=20,y=10)
varn=StringVar()
varn.set('123')
tname=Entry(win,textvariable=varn,state='disabled').place(x=100,y=10)

lage=Label(win,text='age:').place(x=20,y=50)
vara=IntVar()
tage=Entry(win,textvariable=vara).place(x=100,y=50)

lphone=Label(win,text='phone:').place(x=20,y=90)
varp=IntVar()
tphone=Entry(win,textvariable=varp).place(x=100,y=90)

lgen=Label(win,text='gender:').place(x=20,y=130)
varradio=IntVar()
lradio=Radiobutton(win,text='male',value=0,variable=varradio).place(x=70,y=130)
lradio2=Radiobutton(win,text='female',value=1,variable=varradio).place(x=130,y=130)

lcheck=Label(win,text='choose your skills:').place(x=20,y=170)
varcheck1=IntVar()
varcheck2=IntVar()
varcheck3=IntVar()
varcheck4=IntVar()
check1=Checkbutton(win,text='python',variable=varcheck1,onvalue=1,offvalue=0).place(x=50,y=190)
check2=Checkbutton(win,text='java',variable=varcheck2,onvalue=1,offvalue=0).place(x=50,y=210)
check3=Checkbutton(win,text='android',variable=varcheck3,onvalue=1,offvalue=0).place(x=50,y=240)
check4=Checkbutton(win,text='asp.net',variable=varcheck4,onvalue=1,offvalue=0).place(x=50,y=270)

listcheck=Label(win,text='choose your country:').place(x=20,y=300)
lb=Listbox(win)
lb.insert(1,'india')
lb.insert(2,'usa')
lb.insert(3,'uk')
lb.insert(4,'nz')
lb.insert(5,'aus')
lb.place(x=40,y=330)

b=Button(win,text='submit',command=lambda :fun()).place(x=300,y=300)
win.mainloop()
