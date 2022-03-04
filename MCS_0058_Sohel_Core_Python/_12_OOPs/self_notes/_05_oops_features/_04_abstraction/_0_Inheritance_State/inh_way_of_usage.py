# Python program demonstrate
# abstract base class work
"""from abc import ABC, abstractmethod


class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()
"""
# A class with a  method
"""class Myclass:
    def calculate(self, x):
        print("Square values :", x * x)

# all objects share the same calculated() method
satish = Myclass()
satish.calculate(2)

venkat = Myclass()
venkat.calculate(3)

sam = Myclass()
sam.calculate(4)

# abstract class method



# Python program to define
# abstract class"""

"""from abc import ABC


class Polygon(ABC):

    # abstract method
    def sides(self):
        pass


class Triangle(Polygon):

    def sides(self):
        print("Triangle has 3 sides")


class Pentagon(Polygon):

    def sides(self):
        print("Pentagon has 5 sides")


class Hexagon(Polygon):

    def sides(self):
        print("Hexagon has 6 sides")


class square(Polygon):

    def sides(self):
        print("I have 4 sides")

    # Driver code


t = Triangle()
t.sides()

s = square()
s.sides()

p = Pentagon()
p.sides()

k = Hexagon()
k.sides()

print("------1.Normal Inheritance: - 1.1 - Reuse super class methods  AS IS-------")

class A:

    def m1(self):
        print("A  m1()")

    def m2(self):
        print("A  m2()")

class B(A):
    def m3(self):
        print("B  m3()")
b = B()
b.m1()
b.m2()
b.m3()

print("------1.Normal Inheritance: - 1.2 Override super class methods--------")
class A:
    def m1(self):
        print("A  m1()")   # method implementation/method body

    def m2(self):
        print("A  m2()")

class B(A):
    def m1(self):
        print("B  m1()")   # my own implementation

    def m2(self):   # my own implementation
        print("B  m2()")

    def m3(self):
        print("B m3()")

b = B()
b.m1()
b.m2()
b.m3()

print("------1.Normal Inheritance: - 1.3 Few Super classmeethods AS IS, few unique--------")
class A:
    def m1(self):    # Required AS IS in sub class
        print("A  m1()")

    def m2(self):    # Required in unique way in sub class
        print("A  m2()")

class B(A):
    def m3(self):
        print("B  m3()")

b1 = B()
b1.m1()
b1.m2()
b1.m3()


class Pendrive:
    def usb_mesaure(self):
        print("Pendrive  m1()")

class Kingston(Pendrive):
    def usb_mesaure(self):
        print("Pendrive  my own design")



k = Kingston()
k.usb_mesaure()

'''
  1. 2L of Can <== 2L water - YES
  2. 5L of Can <== 5L water - YES
  3. 5L of Can <== 2L water - YES  (Memory Loss)  90%
  4. 2L of Can <== 5L water - NO  (Data Loss) 
x = 10
int x = 10
'''
'''
class Animal:
    def m1()
    
class Tiger(Animal):
    def m2()

Tiger tiger = new Tiger()    # 1    tiger.m1()
                                    tiger.m2()
                                    
Animal animal = new Animal() # 2    animal.m1()
                                        
Animal animal = new Tiger()  # 3**    animal.m1()
                                      animal.m2()  ==> Will give error
                                      

Tiger tiger = new Animal()   # 4    Error Downcasting



x = 10
print(x)  - 10
x = 10.5  
print(x)  - 10.5

int x   = 10     # 1
float x = 10.5   # 2
float x = 10     # 3 Implicit casting   ==> float x = (float)10(internally converts)
int x = 10.5  XX # 4 Explict casting    ==> int x = (int)10.5 (externally you have to write)
"""

# abstract class method

"""from abc import ABC,abstractmethod
class Myclass(ABC):
    @abstractmethod
    def calculated(self,x):
        pass #empty boby,no code

    #subclass1
class Sub1(Myclass):
    def calculated(self,x):
        print("Square of the values :",x * x)

        # sub class2
import math
class Sub2(Myclass):
    def calculated(self,x):
        print("Square root :",math.sqrt(x))

#sub class3
class Sub3(Myclass):
    def calculated(self,x):
        print("Square cube :",x ** 3)

sai = Sub1()
sai.calculated(16)

sam = Sub2()
sam.calculated(6536567876)

venkat = Sub3()
venkat.calculated(18)"""

"""
from abc import*
class Student(ABC):
    def __init__(self,name):
        self.name = name

    def student1(self):
        
      print("Enter the student details",self.name)

    def satish(self):
        pass
    def venkat(self):
        pass
       """
# this is a sub class for abstract car class
from abc import ABC,abstractmethod
class Maruthi(ABC):
    def steering(self):
        print("maruthi uses manual steering")
        print("Drive the car")
    def braking(self):
        print("Maruthi uses the hydraulic brakes")
        print("Apply the breaks stop the car")
        m = Maruthi(1001)
        m.openTank()
        m.steering()
        m.braking()
