class Person:
    def eat(self,breakfast=None,lunch=None,juice=None,supper=None):
        if breakfast is not None:
            print 'breakfast',breakfast
        if lunch!=None:
            print 'lunch',lunch
        if juice!=None:
            print 'juice',juice
p=Person()
p.eat('edly','meals')
p.eat(lunch='biriyani')
n=raw_input('')

p.eat(juice='mango')
