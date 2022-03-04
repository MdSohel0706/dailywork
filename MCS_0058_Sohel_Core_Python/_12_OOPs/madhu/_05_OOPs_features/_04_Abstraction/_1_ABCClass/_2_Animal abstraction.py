
from abc import ABC, abstractmethod

'''
Here all sub classes of Animal,inherits eating() and running() AS IS, 
but sleeping() method is required for all sub classes, at the same time need to be implemeneted uniquely.

'''
class Animal(ABC):   # Abstract class

    def eating(self):   # concrete method/normal method
        print("Animal eating")

    def running(self):  # concrete method
        print("Animal running")

    @abstractmethod    # abstract method
    def sleeping(self):
        pass

class Cat(Animal):

    def sleeping(self):
        print("Cat sleeping")

cat = Cat()
cat.eating()
cat.running()
cat.sleeping()


