class Sample:
    def __init__(self,n,a):
        name=n
        address=a
    def sprint(self):
        return self.name
# s=Sample('abs','xyz')
# s.sprint()
sw=[]
for i in range(3):
    abs=raw_input("")
    xyz=raw_input("")
    sw.append(Sample(abs,xyz))
for i in range(3):
    print sw[i].sprint()