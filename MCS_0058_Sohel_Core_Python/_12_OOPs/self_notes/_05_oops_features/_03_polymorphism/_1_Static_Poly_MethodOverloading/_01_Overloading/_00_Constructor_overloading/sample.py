class Employee:

    def __init__(self, eid, name='Madhu N', sal=1000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)

# Constructor Overloading

madhu = Employee(100)
madhu = Employee(101, 'Madhu Nettem')
kiran = Employee(102, 'Kiran Kumar', 20000)

class Employee:

    def _init_(self, eid, name='suma p', sal=1000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)

# Constructor Overloading

suma = Employee(100)
suma= Employee(101, 'satish')
priya = Employee(102, 'venkat', 20000)

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