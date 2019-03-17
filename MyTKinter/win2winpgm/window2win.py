from tkinter import *
import tkinter
# class windowsss:
def fun(win,var):
    print var
def win1():
    win = Tk()
    win.title('MY APPLICATION')
    win.geometry('{}x{}'.format(750, 500))
    var=StringVar()
    e=Entry(win,textvariable=var)
    e.pack()
    bbb = Button(win, command=lambda :fun(win,e.get())).pack()
    win.mainloop()
# def win2():
win2=Tk()
win2.title('MY APPLICATION')
win2.geometry('{}x{}'.format(750, 500))
b=Button(win2,command=lambda :win1()).pack()
win2.mainloop()
# win2()
# ob=windowsss()
# ob.win2()