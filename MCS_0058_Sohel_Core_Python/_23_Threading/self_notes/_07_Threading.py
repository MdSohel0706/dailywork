from threading import *
from time import *

class Railway:
    def __init__(self,available):
        self.available = available

    def reserve(self,wanted):
        print("Available no of berths = ",self.available)

        if(self.available>=wanted):
            name = current_thread().getName()
            print(wanted," berths allotted for ",name)
            sleep(1.5)
            self.available -= wanted
        else:
            print("Sorry, no berths to allot")

obj = Railway(1)

t1 = Thread(target= obj.reserve, args=(1,))
t2 = Thread(target= obj.reserve, args=(1,))

t1.setName("Person 1")
t2.setName("Person 2")

t1.start()
t2.start()