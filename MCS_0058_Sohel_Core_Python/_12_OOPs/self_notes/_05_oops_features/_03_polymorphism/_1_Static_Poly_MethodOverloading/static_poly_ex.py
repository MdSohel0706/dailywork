'''
python interpreted programming language

 .java   ---compilation ---> .class   --runtime->


Polymorphism : Ability to exists in multiple forms
2 types : Static polymorphism - compile time - Ex => Method Overloading
          Dynamic polymorphism - run time    - Ex => Method Overriding
'''
# Static polymorphism

'''
Method overloading in other languages:
---------------------------------------
class Employee:
    def getdata(eid):
        pass
    def getdata(eid,name):
        pass
    def getdata(eid,name,sal):
        pass

satish= Employee()
satish.getdata(10)  17th line
satish.getdata(10,'satish')  19th line
satish.getdata(10,'satish',1000) 21st line

in Python:
----------
def getdata(eid = 0, name = None, sal = 0):  # Method Overloading
    pass

getdata(10)
getdata(10,'satish')
getdata(10,'satish',1000)   
getdata(name='satish', sal=1000) 
getdata(name='satish')
getdata(sal=1000) 


'''
x = 10
print(x)
x = 20
print(x)


def getdata(eid):
    print("Data is : ", eid)


getdata(10)


def getdata(eid, name):
    print("Data is : ", eid, name)


getdata(10)  # ERROR
getdata(10, 'satish')  # WORKS


def getdata(eid, name, sal):
    print("Data is : ", eid, name, sal)


getdata(10)  # ERROR
getdata(10, 'satish')  # ERROR
getdata(10, 'satish', 1000)


# Solution is use one single method with default arguments for parameters


def getdata(id=None, name=None, sal=None):  # Ex for static poly...
    print("Data : ", id, name, sal)


getdata()  # getdata(id=None,name=None,sal=None)
getdata(10)  # getdata(id=10,name=None,sal=None)
getdata(10, 'satish')  # getdata(id=10,name='satish',sal=None)
getdata(10, 'satish', 1000)  # getdata(id=10,name='satish',sal=1000)

'''
This method will exhibit Static polymorphism'''

# *args  **kwargs : Will see in decorator concept

# in static constructor overloading
class Employee:

    def _init_(self, eid, name='suma p', sal=1000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)

# Constructor Overloading

suma = Employee(100)
suma= Employee(101, 'suma priya puchalapalli')
priya = Employee(102, 'priya puchalapalli', 20000)

"""

Constructor overloading is not possible in Python.
If we define multiple constructors then the last constructor will be considered.

"""

class Test:
    def _init_(self):
         print('No-Arg Constructor')

    def _init_(self,a):
        print('One-Arg constructor')

    def _init_(self,a,b):
        print('Two-Arg constructor')
#t1=Test()
#t1=Test(10)
t1=Test(10,20)

#Constructor with Default Arguments:

class Test:
    def _init_(self,a=None,b=None,c=None):
        print('Constructor with 0|1|2|3 number of arguments')

t1=Test()
t2=Test(10)
t3=Test(10,20)
t4=Test(10,20,30)

#Constructor with Variable Number of Arguments:
class Test:
    def _init_(self,*a):
        print('Constructor with variable number of arguments')
t1=Test()
t2=Test(10)
t3=Test(10,20)
t4=Test(10,20,30)
t5=Test(10,20,30,40,50,60)

#with default arguments
class MyClass:
    def _init_(self, edate=None, fdate=""):
        if edate:
            print("Constructors", edate)
        else:
            print("Default Constructor")


obj1 = MyClass("01-Dec-2021")

obj2 = MyClass()

class Student:
    # one argument constructor
    def _init_(self, name):
        print("One arguments constructor")
        self.name = name

    # two argument constructor
    def _init_(self, name, age):
        print("Two arguments constructor")
        self.name = name
        self.age = age

# creating first object
emma = Student('Emma')

# creating Second object
kelly = Student('Kelly', 13)
"""
2.Method Overloading:

If 2 methods having same name but different type of arguments then those methods are said to
be overloaded methods.

Eg: m1(int a)
m1(double d)
But in Python Method overloading is not possible.
If we are trying to declare multiple methods with same name and different number of arguments
then Python will always consider only last method.

"""

#example:

class Test:
    def m1(self):
       print('no-arg method')
    def m1(self,a):
        print('one-arg method')
    def m1(self,a,b):
        print('two-arg method')
t=Test()
#t.m1()
#t.m1(10)
t.m1(10,20)


class Person:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
# Create instance
obj = Person()
# Call the method
obj.Hello()
# Call the method with a parameter
obj.Hello('Edureka')


# Program to illustrate method overloading
class edpresso:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')


# Create an instance
obj = edpresso()

# Call the method
obj.Hello()

# Call the method with a parameter
obj.Hello('Kadambini')


class FeedbackForm:

    def _init_(self):
        pass

    def feedback(self, rating=10,
                 comments=None):  # method overloading (function overloading)
        print("Feedback is :", rating, ", ", comments)


# Method overloading
feed = FeedbackForm()

feed.feedback()  # Default args
feed.feedback(4)  # Default args
feed.feedback(9, 'Good')  # Positional args
feed.feedback(comments='Very Bad')  # keyword args
feed.feedback(comments='Very Bad', rating=1)  # keyword args

"""
In java/.net
def feedback(self):
    pass

def feedback(self, rating):
    pass

def feedback(self, rating, comments):
    pass

def feedback(self,comments):
    pass

"""
# Function overloading
def sum(a=10, b=20, c=30):
    print("Sum is ", a + b + c)


# Overloading - Depends on how many arguments we are passing
sum()
sum(15)
sum(15, 25)
sum(15, 25, 35)
sum(b=200, a=100)
sum(b=200, c=300)
sum(a=100, c=300)
sum(b=200, a=100, c=300)


def add(x, y):
    pass


def sum(a, b):
    res = add(a, b)


'''
# In JAVA

def product(a, b):
    res = a * b
    print(res)
def product(a, b, c):
    res = a * b * c
    print(res)
product(10,20)  # 7th line
product(10,20,30) # 10th line
'''

# First product method.
# Takes two argument and print their
# product
"""def product(a):
    pass

def product(a, b):
    res = a * b
    print(res)

product(10)  # ERROR

# We can call only in one way,by passing both arguments
product(3, 4) # Positional args
product(a = 3, b = 4) # Keyword args
product(b = 4, a = 3) # Keyword args

print("Function product : ",product)
# Second product method
# Takes three argument and print their
# product

def product(a, b, c = 1):
    p = a * b * c
    print(p)

print("Function product : ",product)
# Uncommenting the below line shows an error
product(4, 5)
# This line will call the second product method
product(3, 4)
product(4, 5, 5)


def sum(a, b, c = 0):
    return a + b + c

print("Sum :",sum(10, 20))


#examples:
class product():
    def product(self,x,y,z):
          a=x*y*z
          print(a)
product(3,5,6)

from itertools import product

if _name_ == "_main_":
    arr1 = [1, 2, 3]
    arr2 = [5, 6, 7]
print( list(product(arr1, arr2)) )
"""


'''
python interpreted programming language

 .java   ---compilation ---> .class   --runtime->


Polymorphism : Ability to exists in multiple forms
2 types : Static polymorphism - compile time - Ex => Method Overloading
          Dynamic polymorphism - run time    - Ex => Method Overriding
'''
# Static polymorphism

'''
Method overloading in other languages:
---------------------------------------
class Employee:
    def getdata(eid):
        pass
    def getdata(eid,name):
        pass
    def getdata(eid,name,sal):
        pass
   
satish = Employee()
madhu.getdata(10)  17th line
madhu.getdata(10,'satish')  19th line
madhu.getdata(10,'satish',1000) 21st line

in Python:
----------
def getdata(eid = 0, name = None, sal = 0):  # Method Overloading
    pass

getdata(10)
getdata(10,'Madhu')
getdata(10,'Madhu',1000)   
getdata(name='Madhu', sal=1000) 
getdata(name='Madhu')
getdata(sal=1000) 
 
'''
x = 10
print(x)
x = 20
print(x)

def getdata(eid):
    print("Data is : ", eid)
getdata(10)

def getdata(eid, name):
    print("Data is : ", eid, name)

getdata(10) # ERROR
getdata(10,'Madhu') # WORKS

def getdata(eid, name, sal):
    print("Data is : ", eid, name, sal)

getdata(10) # ERROR
getdata(10, 'Madhu') # ERROR
getdata(10, 'Madhu', 1000)

# Solution is use one single method with default arguments for parameters


def getdata(id=None, name=None, sal=None):  # Ex for static poly...
    print("Data : ", id, name, sal)


getdata()                   # getdata(id=None,name=None,sal=None)
getdata(10)                 # getdata(id=10,name=None,sal=None)
getdata(10, 'Madhu')        # getdata(id=10,name='Madhu',sal=None)
getdata(10, 'Madhu', 1000)  # getdata(id=10,name='Madhu',sal=1000)

'''
This method will exhibit Static polymorphism'''

# *args  **kwargs : Will see in decorator concept

'''
Created on 13-Jun-2021
@author: madhu
'''
'''Below fucntion can be called in 2 ways
 1. By passing one argument only
 1. By passing two argument only
'''
def get_power(voltage, state='MY_STATE'):
    print("Voltage, State : ",voltage,state)

get_power(10)        # Default
get_power(10, "AP")  # Positional
get_power(state='Karnataka', voltage=10)  # keyword
get_power(voltage=10, state='Telangana')  # keyword

print("----------------------------")

def get_power(voltage, state='state', action='action', type='type'):
    print("VOLTAGE = ", voltage)
    print("STATE   = ", state)
    print("ACTION  = ", action)
    print("TYPE    = ", type)
    print("---------------End of method--------------")

'''
Error function calls:
----------------------
get_power(10,action='HELLO',100)    # Positional argument after keyword argument
get_power()                         # required argument missing
get_power(voltage=5.0, 'dead')      # non-keyword argument after a keyword argument
get_power(110, voltage=220)         # duplicate value for the same argument
get_power(110, actor='NTR')         # unknown keyword argument
'''

print("--------# 1 positional argument----------")
get_power(1000)
get_power(1000, 'X')
get_power(1000, 'X', 'Y')
get_power(1000, 'X', 'Y', 'Z')
get_power('a million', 'brief of life', 'jump')
print("------------------# 2 keyword argument------------------------")
get_power(action="myaction", type="mytype", voltage=1000)  # 2 keyword argument
print("------------------------------------------")
get_power(voltage=1000000, action='VOOOOOM')               # 2 keyword arguments
print("------------------------------------------")
get_power(action='VOOOOOM', voltage=1000000)               # 2 keyword arguments
print("------------------------------------------")
print("------------------------------------------")
get_power(1000, action='Hello World')           # 1 positional, 1 keyword
print("------------------------------------------")

#default arguments
def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")

def pow(x, y, mod=None):
    r = x ** y
    if mod is not None:
        r %= mod
    return r

pow(2, 10)  # valid
pow(2, 10, 17)  # valid
pow(2, 10, mod=17)  # valid
pow(x=2, y=10)  # invalid, will raise a TypeError
pow(2, y=10)  # invalid, will raise a TypeError

#Calculate power of a number using a while loop
base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))

# Python code to demonstrate pow()
# version 1

print("The value of 3**4 is : ", end="")

# Returns 81
print(pow(3, 4))


# Python code to demonstrate pow()
# version 2

print("The value of (3**4) % 10 is : ", end="")

# Returns 81%10
# Returns 1
print(pow(3, 4, 10))


# Python code to discuss negative
# and non-negative cases

# positive x, positive y (x**y)
print("Positive x and positive y : ", end="")
print(pow(4, 3))

print("Negative x and positive y : ", end="")
# negative x, positive y (-x**y)
print(pow(-4, 3))

print("Positive x and negative y : ", end="")
# positive x, negative y (x**-y)
print(pow(4, -3))

print("Negative x and negative y : ", end="")
# negative x, negative y (-x**-y)
print(pow(-4, -3))


base = int(input("Enter base:"))
power = int(input("Enter power:"))
n = 1
for i in range(1,power+1):
    n=base*n
print ("The value of",base,"**",power," is",n)


x = 7
y = 2
z = 5

print(pow(x, y, z))

# positive x, positive y (x**y)
print(pow(2, 2))

# negative x, positive y
print(pow(-2, 2))

# positive x, negative y (x**-y)
print(pow(2, -2))

# negative x, negative y
print(pow(-2, -2))

# Python code to demonstrate naive method
# to compute power
n = 1
for i in range(1, 5):
    n = 3 * n

print("The value of 3**4 is : ", end="")
print(n)

# Python code to demonstrate pow()
# version 1

print("The value of 3**4 is : ", end="")

# Returns 81
print(pow(3, 4))

# Python code to demonstrate pow()
# version 2

print("The value of (3**4) % 10 is : ", end="")

# Returns 81%10
# Returns 1
print(pow(3, 4, 10))

#arags and kwargs
"""

#How we can handle overloaded method requirements in Python:

Most of the times, if method with variable number of arguments required then we can handle
with default arguments or with variable number of argument methods.
"""
#Program with Default Arguments:

class Test:
    def sum(self,a=None,b=None,c=None):
             if a!=None and b!= None and c!= None:
                        print('The Sum of 3 Numbers:',a+b+c)
             elif a!=None and b!= None:
                        print('The Sum of 2 Numbers:',a+b)
             else:
                        print('Please provide 2 or 3 arguments')

t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)

#Program with Variable Number of Arguments::

class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
            print('The Sum:',total)
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
t.sum()


# First product method.
# Takes two argument and print their
# product
def product(a, b):
    p = a * b
    print(p)


# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print(p)


# Uncommenting the below line shows an error
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)


# Function to take multiple arguments
def add(datatype, *args):
    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:
        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')


# class
class Compute:
# area method
    def area(self, x = None, y = None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0
# object
obj = Compute()
# zero argument
print("Area Value:", obj.area())
# one argument
print("Area Value:", obj.area(4))
# two argument
print("Area Value:", obj.area(3, 5))

def addition(a, b):
   return a + b
print(addition(3,4))

def addition(*args):
   result = 0
   for i in args:
      result += i
   return result
print(addition())
print(addition(1,4))
print(addition(1,7,3))

#keyword arguments
def addition(a, b, *args, option=True):
   result = 0
   if option:
      for i in args:
        result += i
      return a + b + result
   else:
      return result

print(addition(1, 4, 5, 6, 7))
print(addition(1, 4, 5, 6, 7, option=False))

#*args and kwargs

def arg_printer(a, b, *args, option=True, **kwargs):
   print(a, b)
   print(args)
   print(option)
   print(kwargs)
arg_printer(1, 4, 6, 5, param1=5, param2=6)