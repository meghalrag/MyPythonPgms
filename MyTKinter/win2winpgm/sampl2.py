from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.geometry('{}x{}'.format(750, 500))
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()
        self.var=StringVar()
        self.en=Entry(master,textvariable=self.var).pack()
        self.greet_button = Button(master, text="Greet", command=self.greet(self.en.get()))
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self,var):
        print("Greetings!")
        print var

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()