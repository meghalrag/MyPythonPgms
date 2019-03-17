#method overriding
class Father:

    def drive(self):
        print 'cycle'
class Child(Father):
    def drive(self):
        Father.drive(self)
        print"car"
c=Child()
c.drive()
#pgm-2
# class Father:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
# class Child(Father):
#     def newfunc(self,name,age,education):
#         Father.__init__(self, name, age)
#         self.edu=education
#         self.name=name
#         self.age=age
#         print 'name',self.name
#         print 'age',self.age
#         print 'educ',self.edu
# c=Child('n',20)
# c.newfunc('n',20,'asd')