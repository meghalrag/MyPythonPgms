from tkinter import *
from tkinter import filedialog
a = Tk()
a.geometry('{}x{}'.format(500,500))   #setsize of window
a.title("GUI")
# label = Label(a, text = "welcome").place(x=100,y=10)
# label = Label(a, text = "hai").place(x=200,y=30)
# label = Message(a, text = "welcome").pack()
# h=Message(a,bd=10,text='hai',)
# h.grid(row=0,column=1)
#
# v=StringVar()    #variable to display in label
# v.set('name')
# b=Label(a,width=10,height=3,bg='red',textvariable=v).pack(side="bottom",fill="x")



######grid arrangement

v=StringVar()    #variable to display in label
v.set('name:')
b=Label(a,textvariable=v)
b.grid(row=0)
tv=IntVar()
tv.set('123')
b=Entry(a,textvariable=tv,state='disabled').grid(row=0,column=1)

v=StringVar()    #variable to display in label
v.set('age:')
b=Label(a,textvariable=v).grid(row=1)
tv=IntVar()
b=Entry(a,textvariable=tv)
b.focus()
b.grid(row=1,column=1)

bb=Button(a,text='browse',command=lambda :filedialog.askopenfilename())
bb.grid(row=2)
######################

# tv=IntVar()
# # b=Entry(a,width=20,bg='white',textvariable=tv)
# # b.grid(row=0,column=1)
a.mainloop()