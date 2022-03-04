# Python OOPs Concepts:

"""
In Python, object-oriented Programming (OOPs) is a programming
paradigm that uses objects and classes in programming. It aims to implement
real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.
The main concept of OOPs is to bind the data and the functions that work on that together
as a single unit so that no other partof the code can access this data.
  """

"""   Main Concepts of Object-Oriented Programming (OOPs):
Class
Objects
Polymorphism
Encapsulation
Inheritance
"""

"""Class :
 
A class is a collection of objects. 
A class contains the blueprints or the prototype from which the objects are being created. 
It is a logical entity that contains some attributes and methods. 
"""

"""Some points on Python class:  

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute
"""

"""Class Definition Syntax:

#class ClassName:
   # Statement-1
   .
   .
   .
   Statement-N"""


# Creating an empty Class in Python

# Python3 program to
# demonstrate defining
# a class

""" class Dog:
    pass
In the above example, we have created a class named dog using the class keyword."""

"""Objects
The object is an entity that has a state and behavior associated with it. 
It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. Integers, strings,
floating-point numbers, even arrays, and dictionaries, are all objects. More specifically, any 
single integer or any single string is an object. 
The number 12 is an object, the string “Hello, world” is an object, 
a list is an object that can hold other objects, and so on. 
You’ve been using objects all along and may not even realize it.
"""

"""An object consists of :
State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.
"""

"""To understand the state, behavior, and identity let us take the example of the class dog (explained above). 

The identity can be considered as the name of the dog.
State or Attributes can be considered as the breed, age, or color of the dog.
The behavior can be considered as to whether the dog is eating or sleeping.
"""

"""Creating an object:
obj = Dog()
"""

"""The self  
Class methods must have an extra first parameter in the method definition. 
We do not give a value for this parameter when we call the method, Python provides it
If we have a method that takes no arguments, then we still have to have one argument.
This is similar to this pointer in C++ and this reference in Java.
"""

"""The __init__ method 
The __init__ method is similar to constructors in C++ and Java. 
It is run as soon as an object of a class is instantiated. 
The method is useful to do any initialization you want to do with your object. 

Now let us define a class and create some objects using the self and __init__ method."""

""" REQUIREMENT : Sum of 2 given numbers

STATE :   -  Data Initialization  ==> Data types/data structures
n1 = 10  int(input("Enter number1"))
n2 = 20  int(input("Enter number2"))

 BEHAVIOR   - Implementation       ==>  Functions
def get_sum(num1, num2):
    result = num1 + num2
    return result

print("Sum of 2 numbers is : ", get_sum(n1, n2))

if elif else 
   for while 
   functions 
   class 
   try except finally 
   with




# class structure

class <class-name>:
        # 1. STATE
    n1 = 10
    n2 = 20
    
        # 2. BEHAVIOR
    def get_sum(num1, num2):
        result = num1 + num2
        return result


# REQ : Display each employee information   CRUD -> RETRIEVAL

CRUD 
Data type/structures
STATE
BEHAVIOR
# A1 :: Using Functions
    # 1. STATE
empid = int(input("Enter empid :"))
name = input("Enter name : ")
sal = int(input("Enter sal :"))

    # 2. BEHAVIOR
def get_einfo(eid, ename, esal):
    print("Employee details are ", eid, ename, esal)

get_einfo(empid,name,sal)

# Using OOPs  -- Class

# Step 1:
class Employee:
    # 1. STATE
    empid = 100 # int(input("Enter empid :"))
    name = 'satish' # input("Enter name : ")
    sal = 13000 # int(input("Enter sal :"))

    # 2. BEHAVIOR
    def get_einfo(eid, ename, esal):
        print("Employee details are ", eid, ename, esal)

# Step 2:
class Employee:

    # 1. STATE
    def __init__(self, empid, name, sal):
        self.empid = empid
        self.name = name
        self.sal = sal

    # 2. BEHAVIOR
    def get_einfo(self):
        print("Employee details are ", self.empid, self.name, self.sal)

# object creation
madhu = Employee(100, 'satish', 12000)    # x = 10
madhu.get_einfo()

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
satish.get_sinfo()"""

"""class Employee:
    #1.state
    def __init__(self,employeeid,employee_name,employee_email):
       self.employeeid = employeeid
       self.employee_name = employee_name
       self.employee_email = employee_email
   # 2 behaviour
    def get_venkat(self):
       print("Enter the employee details :",self.employeeid,self.employee_name,self.employee_email)


rinky = Employee(101,"venkat","venkat147@gmail.com")
rinky.get_venkat()\

class Pandu:

    # 1.state

    def __init__(self,mango,apple,cherry,smallapple,bigapple):
        self.mango = mango
        self.apple = apple
        self.cherry = cherry
        self.smallapple = smallapple
        self.bigapple = bigapple

      # 2.behaviour

    def get_satish(self):
        print("Enter the fruits Names :",self.mango,self.apple,self.cherry,self.smallapple,self.bigapple)

rinky = Pandu("mango3","apple12","cherry16","smallapple18","bigapple18")
rinky.get_satish()"""


"""class Bankemployee:

#state

  def __init__(self,bankemployeename,bankemployeeid,bankemployeeemail):
      self.bankemployeename = bankemployeename
      self.bankemployeeid = bankemployeeid
      self.bankemployeeemail = bankemployeeemail

              #behaviour

  def satish_get(self):
      print("Enter the bank employee Details:",self.bankemployeename,self.bankemployeeid,self.bankemployeeemail)


venkat = Bankemployee("venkat",101,"venkat143@gmail.com")
venkat.satish_get()

a,b,c,d,e = '12,34'
print(a,b,c,d,e)

list1 = ['a','b']
for i in list1:
    list1.append(i)

print(list1)"""



class Teacher:

   #state
    def __init__(self,name,id,subject,phno):
        self.name = name
        self.id = id
        self.subject = subject
        self.phno = phno

        #behaviour
    def satish_get(self):
        print("Enter the teacher Details:",self.name, self.id,self.subject,self.phno)

employee = Teacher("satish",101,"java","9556566563")
employee.satish_get()

































































































































































































































































































































