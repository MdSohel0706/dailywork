"""

#Method overriding:

What ever members available in the parent class are bydefault available to the child class through
inheritance. If the child class not satisfied with parent class implementation then child class is
allowed to redefine that method in the child class based on its requirement. This concept is called
overriding.
Overriding concept applicable for both methods and constructors.

"""

#Program for Method overriding:

class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('satish')
class C(P):
    def marry(self):
         print('venkat')
c=C()
c.property()
c.marry()

#From Overriding method of child class,we can call parent class method also by using super() method.

class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('satish')
class C(P):
    def marry(self):
        super().marry()
        print('venkat')
c=C()
c.property()
c.marry()

#Program for Constructor overriding:

class P:
    def _init_(self):
        print('Parent Constructor')
class C(P):
    def _init_(self):
        print('Child Constructor')
c=C()

#Program to call Parent class constructor by using super():

class Person:
     def _init_(self,name,age):
            self.name=name
            self.age=age
class Employee(Person):
     def _init_(self,name,age,eno,esal):
            super()._init_(name,age)
            self.eno=eno
            self.esal=esal
     def display(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee Salary:',self.esal)
e1=Employee('venkat',48,872425,26000)
e1.display()
e2=Employee('satish',39,872426,36000)
e2.display()


'''
                           Animal
                  Cat    Dog   Tiger    Lion

Own Specific method
Inherited method
Overriden method

'''


class Animal:
    def __init__(self):
        print("In Animal object")

    # Generic behavior
    def eating(self):
        print("Animal Eating")


class Cat(Animal):

    def __init__(self):
        print("In CAT object")

    # Specific behavior
    def sleeping(self):
        print("Cat is sleeping")

    # method overriding
    def eating(self):
        print("Cat is Eating")

cat = Cat()
cat.sleeping()
cat.eating()


# SCENARIOS
print("--------------------------")
class Dog(Animal):
    def __init__(self):
        print("In DOG object")

    # Specific behavior
    def barking(self):
        print("DOG is barking")

dog = Dog()
dog.barking()
dog.eating()

print("----------------------")
class Lion(Animal):
    def __init__(self):
        print("In LION object")

lion = Lion()
lion.eating()