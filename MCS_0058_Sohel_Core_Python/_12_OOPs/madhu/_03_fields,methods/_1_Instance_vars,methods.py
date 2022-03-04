'''
Instance variables
Instance methods
'''

"""Instance method in Python
A class is a user-defined blueprint or prototype from which objects are created.
Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of that type to be made. 
Each class instance can have attributes attached to it for maintaining its state. 
Class instances can also have methods (defined by its class) for modifying its state.

Instance Method
Instance attributes are those attributes that are not shared by objects. Every object
has its own copy of the instance attribute.
For example, consider a class shapes that have many objects like circle, square,
triangle, etc. having its own attributes and methods. An instance attribute refers to the
properties of that particular object like edge of the triangle being 3, while the edge of
the square can be 4.
An instance method can access and even modify the value of attributes of an instance.
It has one default parameter:-
self – It is a keyword which points to the current passed instance. But it need not be
passed every time while calling an instance method.

"""
"""class shape:
# Instance Method

     def finEdges(self):
      return self.edge
      
# Instance Method

     def modifyEdges(self, newedge):
      self.edge = newedge
# Driver Code
circle = shape(0, 'red')
square = shape(4, 'blue')
# Calling Instance Method
print("No. of edges for circle: "+ str(circle.finEdges()))
# Calling Instance Method
square.modifyEdges(6)
print("No. of edges for square: "+ str(square.finEdges()))"""


"""# Python program to demonstrate
# classes  
  
class Person:  
      
    # init method or constructor   
    def __init__(self, name):  
        self.name = name  
      
    # Sample Method   
    def say_hi(self):  
        print('Hello, my name is', self.name)  
      
p = Person('Nikhil')  
p.say_hi() 
"""
'''
def func1():
    print("Funciton1 body")

func1()

class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def __init__(self, eid, name, sal):
        print("Self address : ", self)
        self.eid = eid
        self.name = name
        self.sal = sal

    # instance methods
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)


venkat = Employee(100, 'satsh', 15000)
venkat.get_edata()  # Employee.get_edata(madhu)




li1 = [1, 2, 3]  # list1 is of type class list
li1.append(100)  # list.append(li1,100)
li1.pop()        # list.pop(li1)
'''


"""class Sample:
    bank_name = 'icici'

    def get_data(self):
        self.bank_name = 'axis'
        print(self.bank_name)

s = Sample()
print(dir(s))
s.get_data()
s.bank_name = 'axis'
print(dir(s))
s.get_data()"""
