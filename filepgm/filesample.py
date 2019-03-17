import os
# file=open('sample.txt','w',1)
# f=open('sample2.txt','a',1)
# f.write('a\nb\nc\nd\ne',)
co=[]
i=' '
f=open("sample2.txt","a+",1)
i=raw_input("input:")
i=i+'\n'
f.write(i)
f.seek(0)
# print f.tell()
# print f.readline()
# print f.tell()
# f.seek(-6,2)
# print f.tell()
# print f.read()
# print f.readlines()
# f=open('sample2.txt','r',1)
# print f.readlines()
print f.readline()
print f.read()
# print c
# print co
# print f.readline()
# f.seek(1)
# print f.readline()
# c = f.readline()
# # print c
# c=f.readline()
# l=[]
# while c:
#     print c
#     l=c.split(',')
#     print l[0]
#     c=f.readline()
# # f=open('sample2.txt','r',1)
# # file.write("hello how are you?")
# # file.close()
# f.close()
# print f.seek(1)