#Creating a thread without using a class
from threading import *

def display(s):
    print(s)

for i in range(5):
    t = Thread(target= display, args=("Hello",))
    t.start()