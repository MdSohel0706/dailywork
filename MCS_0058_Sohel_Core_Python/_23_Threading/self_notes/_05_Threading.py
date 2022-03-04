from threading import *
from time import *

class MyThread:
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("Boil milk and tea powder for 5 minutes...", end=" ")
        sleep(5)
        print("Done")

    def task2(self):
        print("Add sugar and tea for 3 minutes...", end = " ")
        sleep(3)
        print("Done")

    def task3(self):
        print("Filter it and serve...", end = " ")
        print("Done")

obj = MyThread()

t = Thread(target=obj.prepareTea())
t.start()
