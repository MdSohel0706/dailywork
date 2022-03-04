'''
Created on Dec 5, 2019

@author: madhu
'''
from abc import ABC, abstractmethod


class Animal(ABC): 
    
    @abstractmethod
    def move(self): 
        pass
    
    def details(self):
        print("Concrete methods")
    
class Human(Animal): 
    pass

class Dog(Animal): 
    def move(self): 
        print("I am Dog and I can bark")   

class Lion(Animal): 
    def move(self): 
        print("I can roar") 

class Snake(Animal): 
    def move(self): 
        print("I can crawl") 
  

  
  
# c=Animal() # TypeError: Can't instantiate abstract class Animal with abstract methods move
hu_obj = Human()
hu_obj.move()

dog_obj = Dog()
dog_obj.move()