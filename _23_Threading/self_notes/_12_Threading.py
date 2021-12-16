from threading import *
from time import *

class Producer:
    def __init__(self):
        self.lst = []
        self.cv = Condition()

    def produce(self):
        self.cv.acquire()
        for i in range(1,11):
            self.lst.append(i)
            sleep(1)
            print("Item produced")
        self.cv.notify()
        self.cv.release()

class Consumer:
    def __init__(self,prod):
        self.prod = prod
    def consume(self):
        self.prod.cv.acquire()
        self.prod.cv.wait(timeout = 0)
        self.prod.cv.release()
        print(self.prod.lst)

p = Producer()
c = Consumer(p)

t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)

t1.start()
t2.start()