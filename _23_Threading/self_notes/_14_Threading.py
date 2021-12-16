from threading import *
from time import *

def display():
    for i in range(1,6):
        print("Normal thread ", end = " ")
        print(i)
        sleep(1)

def display_time():
    while True:
        print("Daemon thread : ", end = " ")
        print(ctime())
        sleep(2)

t = Thread(target = display)
t.start()

d = Thread(target = display_time)
d.daemon = True

d.start()