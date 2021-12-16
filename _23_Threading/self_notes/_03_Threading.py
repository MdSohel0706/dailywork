#Creating a thread by creating a sub class to the Thread class
from threading import *
class MyThread(Thread):
    def __init__(self,stri):
        Thread.__init__(self)
        self.s = stri
    def run(self):
        print(self.s)

t1 = MyThread("Hello")
t1.start()
t1.join()