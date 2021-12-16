from threading import *

l1 = Lock()
l2 = Lock()

def bookticket():
    print("Locking train")
    l1.acquire()
    print("Locking compartment")
    l2.acquire()
    print("Unlocking compartment")
    l2.release()
    print("Unlocking train")
    l1.release()

def cancelticket():
    print("Locking compartment")
    l2.acquire()
    print("Locking train")
    l1.acquire()
    print("Unlocking train")
    l1.release()
    print("Locking compartment")
    l2.release()

t1 = Thread(target=bookticket)
t2 = Thread(target=cancelticket)

t1.start()
t2.start()

