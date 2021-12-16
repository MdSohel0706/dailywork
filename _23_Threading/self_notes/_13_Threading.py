from threading import *
from time import *
from queue import *

class Producer:
    def __init__(self):
        self.q = Queue()

    def produce(self):
        for i in range(1,11):
            print("Producing item ",i)
            self.q.put(i)
            sleep(1)

class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        for i in range(1,11):
            print("Receiving item ",self.prod.q.get(i))

p = Producer()
c = Consumer(p)

t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)

t1.start()
t2.start()