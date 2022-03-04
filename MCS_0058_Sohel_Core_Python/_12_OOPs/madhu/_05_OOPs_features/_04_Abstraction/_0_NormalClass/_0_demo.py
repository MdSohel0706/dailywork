

'''


Solution : Use Inheritance 
           Implement classes as Super class - Sub class mechansim
'''

class Animal:
     def __init__(self):   #Common state
          print("In Animal object")

     # Generic behavior
     def eating(self):   # Common behavior for all sub classes
          print("Animal Eating")

class Cat(Animal):  # Cat is-a Animal

     def __init__(self):
          print("In CAT object")
     # Specific behavior
     def sleeping(self):
          print("Cat is sleeping")

animal = Animal()
animal.eating()

#animal.sleeping()
print("-----------------")

cat = Cat()
cat.sleeping()
cat.eating()
'''
Here Cat is sub class and Animal is super class. 
Cat as a sub class wil inherit all the features of Animal
Inheritance should be applicable when IS-A *** relationship is satisfied

'''


#Method overriding ==> Dynamic polymorphism

