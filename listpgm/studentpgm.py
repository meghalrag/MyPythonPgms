print "options:","\n","1:ADD STUDENT\n2:DISPLAY ALL DETAILS\n3:REMOVE\n4:Update"
list1=list()
limit=0
remove=False
checkname=False
while(1):
    choice=input("enter your choice?(1,2,3,4):")
    if choice==1:
        list=[]
        limit=limit+1
        name = raw_input("enter student name:")
        age = input("enter the age:")
        dept = raw_input("enter the department:")
        list.append(name)
        list.append(age)
        list.append(dept)
        list1.append(list)
        print"Details added successfully"
    elif choice==2:
        for i in range(len(list1)):
            print list1[i],""
    elif choice==3:
        removename=raw_input("enter the student name you want to remove:")
        for i in range(len(list1)):
            remove=removename in list1[i]
            if remove==True:
                del list1[i]
                break
        if remove==True:
            print"remove successfully"
            print list1
        else:
            print"no data is present in the record to remove"
    elif choice==4:
        namestud=raw_input("name of the student update:")
        optupdate=input("choose update option:name/age/department(1/2/3):")
        if optupdate==2:
            updatevalue=input("enter the updated value:")
        elif optupdate==1 or optupdate==3:
            updatevalue=raw_input("enter the updated value:")
        else:
            print "invalid entered"
        for i in range(len(list1)):
            checknamae=namestud in list1[i]
            if checknamae==True:
                list1[i][optupdate-1]=updatevalue
        if checknamae==True:
            print "updated successfully"
        else:
            print "error occured /name doesnt exist"
    else:
        print "invalid choice"
    y=raw_input("do you want to continue(y/n):")
    if y=='y':
        continue
    else:
        break


