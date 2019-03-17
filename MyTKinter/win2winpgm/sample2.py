from tkinter import *


def fun2(win2):
    win2.withdraw()
    win3 = Toplevel(win1)
    win3.geometry('{}x{}'.format(1000, 1000))
    Label(win3, text='window1').pack()
    Entry(win3, text="lll").pack()
    # Button(win2, text='next1', command=fun3(win)).pack()
    Button(win3, text='back', command=lambda: backfun(win2,win3)).pack()
    Button(win3, text='logout', command=lambda: win1.deiconify()).pack()
    win2.mainloop()


def backfun(win1,win2):
    win2.withdraw()
    win1.deiconify()

def fun1(win1):
    win1.withdraw()
    win2=Toplevel(win1)
    win2.geometry('{}x{}'.format(1000, 1000))
    Label(win2, text='window1').pack()
    Entry(win2, text="lll").pack()
    Button(win2, text='next1', command=lambda :fun2(win2)).pack()
    Button(win2,text='back',command=lambda :backfun(win1,win2)).pack()
    win2.mainloop()

win1=Tk()
win1.geometry('{}x{}'.format(1000, 1000))
Label(win1,text='window1').pack()
Entry(win1,text="lll").pack()
Button(win1,text='next1',command=lambda :fun1(win1)).pack()
win1.mainloop()