print "options:\n1-ADD\n2-REMOVE\n3-UPDATE\n4-DISPLAY"
dnry={}
count=1
while(1):
    choice = input("enter your choice(1/2/3/4):")
    if choice==1:
        n=input("number:")
        for i in range(n):
            temp1={}
            temp2={}
            key=count
            count+=1
            name=raw_input("enter the name:")
            age=input("age")
            phone=input("enter phone number")
            print"enter marks"
            eng=input("english:")
            maths=input("maths:")
            temp2.setdefault("english",eng)
            temp2.setdefault("maths",maths)
            temp1.setdefault("name",name)
            temp1.setdefault("age",age)
            temp1.setdefault("phone",phone)
            temp1.setdefault("mark",temp2)
            dnry.setdefault(key,temp1)
        print "added successfully"
    elif choice==2:
        r=input("rollno:")
        del dnry[r]
        print "student data removed"
    elif choice==3:
        ro=input("student rollno:")
        upd=raw_input("update what?(name,age,phone,mark:(eng,maths):")
        newdata=raw_input("updated data:")
        if upd=='eng':
            dnry[ro]['mark']['english']
        if upd=='maths':
            dnry[ro]['mark']['maths']
        else:
            dnry[ro][upd]=newdata

    elif choice==4:
        print "rollno\t   name   \t   age\t   phone        \tmark:english\t    mark:maths\n",
        for i in range(1, count, 1):
            print i,"\t      ",dnry[i]["name"], "   \t", " ", dnry[i]["age"], "\t  ", dnry[i]["phone"], "\t         ", \
            dnry[i]["mark"]["english"], "\t  \t       ", dnry[i]["mark"]["maths"]
            # print "aju   \t",23,"\t  ",9877777777,"\t         ",67,"\t  \t       ",89
        # print dnry
    else:
        print "invalid"
    y=raw_input("do you want to continue(y/n):")
    if y=='y':
        continue
    else:
        print"****THANKS*******"
        break