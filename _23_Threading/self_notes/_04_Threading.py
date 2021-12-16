#Creating a thread without creating sub class to thread class
from threading import *
class MyThread:
    def __init__(self,str):
        self.str = str
    def display(self,x,y):
        print(self.str)
        print("The args are ",x,y)

obj = MyThread("Hello")

t1 = Thread(target = obj.display, args = (1,2))
t1.start()