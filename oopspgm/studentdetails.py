# from compiler.ast import obj


class Student:
    def __init__(self,name,regno,dept,phno):
        self.name=name
        self.regno=regno
        self.dept=dept
        self.phno=phno
    def studdetails(self):
        print self.name
        print self.regno
        print self.dept
        print self.phno
obj=list()
no=input("number:")
for i in range(no):
    print 'stud',i+1,':'
    n=raw_input("enter stud name")
    r=raw_input("regno:")
    d=raw_input("department:")
    p=input("phone:")
    obj.append(Student(n,r,d,p))
for i in range(no):
    print obj[i].studdetails()
# obj2=Student(n,r,d,p)
# print obj2.studdetails()