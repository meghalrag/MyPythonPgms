#procedural oriented thread concept.there may be a chance to access fun() of two threads at the same time
import thread
import time
def fun(name,ti):
    while 1:
        print name,
        time.sleep(ti)
thread.start_new_thread(fun,('a',5))
thread.start_new_thread(fun,('b',3))
thread.start_new_thread(fun,('c',1))
while 1:
    pass
#thread with oops concept
# import threading
# # import thread
# import time
# class Mythread(threading.Thread):
#     def __init__(self,name,tim):
#         self.n=name
#         self.t=tim
#         threading.Thread.__init__(self)
#     def run(self):
#         l.acquire()
#         print self.n,
#         time.sleep(self.t)
#         for i in range(10):
#             print i,
#         l.release()
#
# l=threading.Lock()
# t1=Mythread('A',3)
# t2=Mythread('B',2)
# t1.start()
# t2.start()
# while 1:
#     pass