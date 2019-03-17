class F:
    def add(self):
        print"i am father"
class C(F):
    def add(self):
        print "i am child"
a=C()
a.add()
# print type(C)
print super(C,a).add()