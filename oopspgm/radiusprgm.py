class Radius:
    def radius(self,l=0,b=0,r=0):
        if r!=0:
            circle=3.14*r*r
            print 'radius of circle=',circle
        if l!=0 and b!=0:
            print 'radius of rectangle=',l*b
        if l!=0:
            print 'radius of square=',l*l
l=input("length:")
b=input("breadth:")
r=input("radius:")
ob=Radius()
ob.radius(l=l)
ob.radius(l=l,b=b)
ob.radius(r=r)
# ob.radius(l=l,b=b,r=r)
