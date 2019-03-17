class Father:
    id=0                                 #static variable#shares common memory for all obj
    def __init__(self,name):
        print ""
        self.n=name                     #instance variable
    def show(self):
        z='hello'                       #local variable
a=Father("father of a")
print a.n
print a.id
b=Father("father of b")
print b.id
print b.n
Father.id=100
print b.id
print a.id
Father.id=200
print a.id
print a.id
Father.id=300
