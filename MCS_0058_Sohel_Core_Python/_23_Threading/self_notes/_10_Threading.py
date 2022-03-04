from threading import *

l1 = Lock()
l2 = Lock()

def bookticket():
    l1.acquire()
    print("Book ticket locked train")
    l2.acquire()
    print("Book ticket locked compartment")
    l2.release()
    print("Book ticket unlocked compartment")
    l1.release()
    print("Book ticket unlocked train")

def cancelticket():
    l1.acquire()
    print("Cancel ticket locked compartment")
    l2.acquire()
    print("Cancel ticket locked train")
    l2.release()
    print("Cancel ticket unlocked train")
    l1.release()
    print("Cancel ticket unlocked compartment")
    
t1 = Thread(target=bookticket)
t2 = Thread(target=cancelticket)

t1.start()
t2.start()