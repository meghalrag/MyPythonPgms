list=[]
flag=0
A=raw_input("1st person name:")
B=raw_input("2nd persons name:")
for i in range(3):
    r=[]
    for j in range(3):
        x=str(i)+str(j)
        r.append(x)
    list.append(r)
for i in range(3):
    print list[i]," "
A=A.upper()
B=B.upper()
print "--------Game starts with-------------",A,"vs",B

for i in range(5):
        if flag==0:
            print A,"'s turn:(X)"
            p=input("enter i:")
            q=input("enter j:")
            if p>2 or p<0 or q>2 or q<0:
                print "position unavailable,try another one"
                continue
            if list[p][q]=='X' or list[p][q]=='O':
                print "already entered in that position,try another one:"
                continue
            else:

                list[p][q]='X'
                if p==0 and q==0:

                    if list[p][q]=='X' and list[p+1][q]=='X' and list[p+2][q]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p][q+1]=='X' and list[p][q+2]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p+1][q+1]=='X' and list[p+2][q+2]=='X':
                        print "*****",A," wins","*********"
                        break
                if p==0 and q==1:
                    if list[p][q]=='X' and list[p][q-1]=='X' and list[p][q+1]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p+1][q]=='X' and list[p+2][q]=='X':
                        print "*****",A," wins","*********"
                        break

                if p==0 and q==2:
                    if list[p][q]=='X' and list[p][q-1]=='X' and list[p][q-2]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p+1][q]=='X' and list[p+2][q]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p+1][q-1]=='X' and list[p+2][q]=='X':
                        print "*****",A," wins","*********"
                        break
                if p==1 and q==0:

                    if list[p][q]=='X' and list[p][q+1]=='X' and list[p][q+2]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p-1][q]=='X' and list[p+1][q]=='X':
                        print "*****",A," wins","*********"
                        break
                if p==1 and q==1:
                    if list[p][q]=='X' and list[p][q-1]=='X' and list[p][q+1]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p-1][q+1]=='X' and list[p+1][q]=='X':
                        print "A wins"
                        break
                    elif list[p][q]=='X' and list[p+1][q+1]=='X' and list[p-1][q-1]=='X':
                        print "*****",A," wins","*********"
                        break
                if p==1 and q==2:
                    if list[p][q]=='X' and list[p][q-1]=='X' and list[p][q-2]=='X':
                        print "*****", A, " wins", "*********"
                        break
                    elif list[p][q]=='X' and list[p-1][q]=='X' and list[p+1][q]=='X':
                        print "*****",A," wins","*********"
                        break
                if p==2 and q==0:
                    if list[p][q]=='X' and list[p-1][q]=='X' and list[p-2][q]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p-1][q+1]=='X' and list[p-2][q+2]=='X':
                        print "*****", A, " wins", "*********"
                        break
                    elif list[p][q]=='X' and list[p][q+1]=='X' and list[p][q+2]=='X':
                        print "*****", A, " wins", "*********"
                        break
                if p==2 and q==1:
                    if list[p][q]=='X' and list[p-1][q]=='X' and list[p-2][q]=='X':
                        print "*****", A, " wins", "*********"
                        break
                    elif list[p][q]=='X' and list[p][q-1]=='X' and list[p][q+1]=='X':
                        print "*****",A," wins","*********"
                        break
                if p==2 and q==2:
                    if list[p][q]=='X' and list[p-1][q-1]=='X' and list[p-2][q-2]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p-1][q]=='X' and list[p-2][q]=='X':
                        print "*****",A," wins","*********"
                        break
                    elif list[p][q]=='X' and list[p-1][q]=='X' and list[p-2][q]=='X':
                        print "*****",A," wins","*********"
                        break
                for k in range(len(list)):
                    for m in range(len(list)):
                        print list[k][m], " ",
                    print
                    print
                if i==4:
                    break
        print B,"'s turn:(O)"
        y = input("enter i:")
        z = input("enter j:")
        if y> 2 or y < 0 or z>2 or z<0:
            print "position unavailable,try another one"
            flag=1
            continue
        if list[y][z]=='O' or list[y][z]=='X':
            print "already entered in that position,try another one"
            flag=1
            continue
        else:
            flag=0
            list[y][z] = 'O'
            if y==0 and z==0:

                if list[y][z]=='O' and list[y+1][z]=='O' and list[y+2][z]=='O':
                    print "******",B," wins**********"
                    break
                elif list[y][z]=='O' and list[y][z+1]=='O' and list[p][z+2]=='O':
                    print "******",B," wins**********"
                    break
                elif list[y][z]=='O' and list[y+1][z+1]=='O' and list[y+2][z+2]=='O':
                    print "******",B," wins**********"
                    break
            if y==0 and z=='X':
                if list[y][z]=='O' and list[y][z-1]=='O' and list[y][z+1]=='O':
                    print "******",B," wins**********"
                    break
                elif list[y][z]=='O' and list[y+1][z]=='O' and list[y+2][z]=='O':
                    print "******",B," wins**********"
                    break

            if y==0 and z==2:
                if list[y][z]=='O' and list[y][z-1]=='O' and list[y][z-2]=='O':
                    print "******",B," wins**********"
                    break
                elif list[y][z]=='O' and list[y+1][z]=='O' and list[y+2][z]=='O':
                    print "B wins"
                    break
                elif list[y][z]=='O' and list[y+1][z-1]=='O' and list[y+2][z]=='O':
                    print "******", B, " wins**********"
                    break
            if y==1 and z==0:

                if list[y][z]=='O' and list[y][z+1]=='O' and list[y][z+2]=='O':
                    print "******", B, " wins**********"
                    break
                elif list[y][z]=='O' and list[y-1][z]=='O' and list[y+1][z]=='0':
                    print "******", B, " wins**********"
                    break
            if y==1 and z==1:
                if list[y][z]=='O' and list[y][z-1]=='O' and list[y][z+1]=='O':
                    print "******", B, " wins**********"
                    break
                elif list[y][z]=='O' and list[y-1][z+1]=='O' and list[y+1][z]=='O':
                    print "******", B, " wins**********"
                    break
                elif list[y][z]=='O' and list[y+1][z+1]=='O' and list[y-1][z-1]=='O':
                    print "******", B, " wins**********"
                    break
            if y==1 and z==2:
                if list[y][z]=='O' and list[y][z-1]=='O' and list[y][z-2]=='O':
                    print "******", B, " wins**********"
                    break
                elif list[y][z]=='O' and list[y-1][z]=='O' and list[y+1][z]=='O':
                    print "B wins"
                    break
            if y==2 and z==0:
                if list[y][z]=='O' and list[y-1][z]=='O' and list[y-2][z]=='O':
                    print "******", B, " wins**********"
                    break
                elif list[y][z]=='O' and list[y-1][z+1]=='O' and list[y-2][z+2]=='O':
                    print "******", B, " wins**********"
                    break
                elif list[y][z]=='O' and list[y][z+1]=='O' and list[y][z+2]=='O':
                    print "******", B, " wins**********"
                    break
            if y==2 and z==1:
                if list[y][z]=='O' and list[y-1][z]=='O' and list[y-2][z]=='O':
                    print "******",B," wins**********"
                    break
                elif list[y][z]=='O' and list[y][z-1]=='O' and list[y][z+1]=='O':
                    print "******",B," wins**********"
                    break
            if y==2 and z==2:
                if list[y][z]=='O' and list[y-1][z-1]=='O' and list[y-2][z-2]=='O':
                    print "******", B, " wins**********"
                    break
                elif list[y][z]=='O' and list[y-1][z]=='O' and list[y-2][z]=='O':
                    print "******",B," wins**********"
                    break
                elif list[y][z]=='O' and list[y-1][z]=='O' and list[y-2][z]=='O':
                    print "******",B," wins**********"
                    break
            for k in range(len(list)):
                for m in range(len(list)):
                    print list[k][m], " ",
                print
                print

if(i==4):
    print "try next game"
else:
    print
    for i in range(len(list)):
        for j in range(len(list)):
            print list[i][j]," ",
        print
        print






