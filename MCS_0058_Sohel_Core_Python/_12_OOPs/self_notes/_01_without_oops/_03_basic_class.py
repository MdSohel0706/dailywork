# OOPs concepts
'''
Class Object
Encapsulation
Abstraction
Inheritance
Polymorphism
'''
'''
""" # STATE    - data structures  - fields
# BEHAVIOR - functions        - methods

variables value                 #   x = 10
parameters arguments functions  #  def func(params)  func(args)
fields, methods                 #  Inside class 
"""
#Example 1:
#Creating a class and object with class and instance attributes

"""class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
  
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
  
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
  """

Example 2: 
#Creating Class and objects with methods:
"""
class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
          
    def speak(self):
        print("My name is {}".format(self.name))
  
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
  
# Accessing class methods
Rodger.speak()
Tommy.speak()
"""

"""Inheritance
Inheritance is the capability of one class to derive or inherit the properties 
from another class. The class that derives properties is called the derived class or base class and the
class from which the properties are being derived is called the base class or parent class.

The benefits of  inheritance are: 

It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again.
 Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A,
 then all the subclasses of B would automatically inherit from class A."""

#Example: 
#Inheritance in Python
"""# Python code to demonstrate how parent constructors are called.
 
# parent class
class Person(object):
  
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
  
    def display(self):
        print(self.name)
        print(self.idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
      
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
  
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
  
  
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
  
# calling a function of the class Person using
# its instance
a.display()
a.details() 
"""

"""Polymorphism:

Polymorphism simply means having many forms. For example, we need to determine if the given species
of birds fly or not,
using polymorphism we can do this using a single function.
"""

"""
class Bird:
    
    def intro(self):
        print("There are many types of birds.")
  
    def flight(self):
        print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly.")
  
class ostrich(Bird):
  
    def flight(self):
        print("Ostriches cannot fly.")
  
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()"""

"""
#Encapsulation:

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification 
of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. 
Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc."""

""" 
# Python program to
# demonstrate private members
  
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
  
# Creating a derived class
class Derived(Base):
    def __init__(self):
  
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
  
  
# Driver code
obj1 = Base()
print(obj1.a)
  
# Uncommenting print(obj1.c) will
# raise an AttributeError
  
# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
"""

'''

# Retrieve employee information  with hike 10% in an organization
# emp_data = [{'eid':100,'ename':'Madhu N','sal':10000},.......]
# Without oops concepts
  # 1. Retrieve the emp data - RETRIEVAL/READ

print("-----Without oops concepts--------")
    # STATE
emp_id = 100
emp_name = 'Madhu Nettem'
e_sal = 10000
    # BEHAVIOR
def get_edata(eid, name, sal):
    sal = sal + sal*10/100
    print("Employee after Hike :",eid," - ",name," - ",sal)

get_edata(emp_id, emp_name, e_sal)

print("-----With oops concepts--------")
# class definition
class Employee:
    # STATE   # fields
    def __init__(self, eid, ename, sal):  # parameters
        self.eid = eid      # RHS --> Local variables
        self.ename = ename  # LHS --> Instance variables
        self.sal = sal      # self -> instance/object/ref variable

    # BEHAVIOR  # methods
    def get_emp_details(self):
        self.sal = self.sal + self.sal*10/100
        print("Employee information :", self.eid, " - ", self.ename, " - ", self.sal)


# object creation
madhu = Employee(100, 'Madhu Nettem', 10000)  # madhu - object*/reference/instance  RHS - Object creation
madhu.get_emp_details()

'''
        x = 10 
  varible = value     
parameter = argument    
object    = object creation
/instance/
ref. variable  

'''
kiran = Employee(101, 'Kiran Kumar', 15000)
kiran.get_emp_details()

prakash = Employee(102, 'Prakash Kumar', 20000)
prakash.get_emp_details()

# declaration     - int x
# initialization  - int x = 10

list1 = list([1,2,3])  # [1,2,3]
# list1 is an object of type list class(builtins.py)
# madhu is an object of type Employee class


print("-----------Student class-----------------")
class Student:
    # STATE
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks

    # BEHAVIOR
    def get_student_details(self):
        print("Student details : ", self.sid, self.name, self.marks)

s_id = int(input("Enter student id : "))
sname = input("Enter student name : ")
smarks = int(input("Enter student marks : "))

dilip = Student(s_id, sname, smarks)
dilip.get_student_details()

chandra = Student(55, 'Chandra Kala V', 90)
chandra.get_student_details()

print(dilip, id(dilip), type(dilip))
# 10 int 10.5 float "hello" string

# class   n no of objects

print(dilip)
print(chandra)