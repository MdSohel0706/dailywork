"""Inheritance
Inheritance is a powerful feature in object oriented programming.

It refers to defining a new class with little or no modification to an existing class.
The new class is called derived (or child) class and the one from which it inherits is called the base
(or parent) class.

Inheritance is a way of creating a new class for using details of an existing class without modifying it.
The newly formed class is a derived class (or child class). Similarly, the existing class is a base class
(or parent class).
 """

"""
Python Inheritance Syntax:
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
"""
"""
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
 
"""
"""
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
"""
"""
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
        """
"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("satish", "babu")
x.printnam
"""
"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("satish", "babu")
x.printname()
"""
"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("satish", "babu")
print(x.graduationyear)
"""

"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("satish", "babu", 2019)
x.welcome()
"""
"""
class Robot:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hi, I am " + self.name)
class PhysicianRobot(Robot):
    pass
x = Robot("satish")
y = PhysicianRobot("babu")
print(x, type(x))
print(y, type(y))
y.say_hi()
"""
"""
class Robot:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hi, I am " + self.name)
class PhysicianRobot(Robot):
    def say_hi(self):
        print("well come to satish") 
        print(self.name + " katta")
y = PhysicianRobot("babu")
y.say_hi()
"""
"""
class Employee:
    #1.state
    def __init__(self,employeeid,employee_name,employee_email):
       self.employeeid = employeeid
       self.employee_name = employee_name
       self.employee_email = employee_email
   # 2 behaviour
    def get_venkat(self):
       print("Enter the employee details :",self.employeeid,self.employee_name,self.employee_email)


rinky = Employee(101,"venkat","venkat147@gmail.com")
rinky.get_venkat()
"""
"""
class Student:

    # 1. STATE
    def __init__(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)

satish = Student(23, 'satish', 75)
satish.get_sinfo()
"""
"""
class Student:

    # 1. STATE
    def __init__(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)

satish = Student(23, 'satish', 98)
satish.get_sinfo()
"""

class Teacher:

   #state
   def __init__(self,name,id,email,ph_number):
       self.name = name
       self.id = id
       self.email = email
       self.ph_number = ph_number
class Student(Teacher):
    print()


