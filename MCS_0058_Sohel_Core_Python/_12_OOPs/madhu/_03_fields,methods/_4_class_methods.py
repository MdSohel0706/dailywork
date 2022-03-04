"""classmethod() in Python:
The classmethod() is an inbuilt function in Python, which returns a class method for a given function.

Syntax: classmethod(function)"""


"""Parameter :This function accepts the function name as a parameter.
Return Type:This function returns the converted class method.
Syntax: 

@classmethod
   def fun(cls, arg1, arg2, ...):
   
   
   Where, 

fun: the function that needs to be converted into a class method
returns: a class method for function.
classmethod() methods are bound to a class rather than an object.
 Class methods can be called by both class and object.
 These methods can be called with a class or with an object. 
"""


"""Class method vs Static Method:

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take 
some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator 
to create a static method in python.

"""

"""
Example 1: Create a simple classmethod:

In this example, we are going to see a how to create classmethod, for this we created a class
 with geeks name with member variable course and created a function purchase which prints the object.

Now we passed the method geeks.purchase into classmethod which converts the methods to 
a class method and then we call the class function purchase without creating a function object.

"""

"""
class geeks:
    course = 'DSA'
  
    def purchase(obj):
        print("Puchase course : ", obj.course)
  
  
geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()
"""

"""
Example 2: Create class method using classmethod():

# Python program to understand the classmethod
  
class Student:
  
    # create a variable
    name = "Geeksforgeeks"
  
    # create a function
    def print_name(obj):
        print("The name is : ", obj.name)
  
  
# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
Student.print_name = classmethod(Student.print_name)
  
# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()
"""
# Example 3: Factory method using Class method:
"""
# Python program to demonstrate
# use of a class method and static method.
from datetime import date
  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
  
    def display(self):
        print("Name : ", self.name, "Age : ", self.age)
  
person = Person('mayank', 21)
person.display()
"""
"""The @classmethod Decorator:

The @classmethod decorator is a built-in function decorator which is an expression that gets
 evaluated after your function is defined. The result of that evaluation shadows your function definition. 
A class method receives the class as the implicit first argument, just like an instance method 
receives the instance.
 
 Syntax:

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       
"""


'''
class Class:
    pass
    # STATE
        # ==> Fields(1,2)  which represents data

        1. Class variables
        2. Instance variables
        3. local variables

    # BEHAVIOR
        # ==> Methods which represents implementation

       1. Class Method
       2. Instance Method
       3. Static method
'''

# Get employee count at a given point of time.


class Employee:
    comp = 'ORACLE'  # sharing
    emp_count = 0   # sharing + Modifying

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.emp_count += 1

    # instance method(can access instance,class variables)
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)

    # class method (can access only class variables)
    @classmethod
    def get_ecount(cls):
        print("Employee count : ", cls.comp, " -- ", cls.emp_count)

Employee.get_ecount()
madhu = Employee(100, 'Madhu N', 10000)
madhu.get_edata()      # instance method ==> Employee.get_edata(madhu)
Employee.get_ecount()  # class method    ==> Employee.get_ecount(Employee)

# To call class method, we can call using object,But don't do it.
# madhu.get_ecount()

jaya = Employee(101, 'Jayadeep  Chowdary A', 20000)
jaya.get_edata()
Employee.get_ecount()

mohan = Employee(102, 'Mohan Kumar', 45000)
mohan.get_edata()
Employee.get_ecount()

'''
btech : stu_id, name, marks ==> instance variables
        college name        ==> class variables(share)
        attendance          ==> class variable (share+Modify)

        
employees : eid,name,sal   Instance vars  UNIQUE(INDIVIDUAL DATA)
            comp_name      class vars     SHARABLE to all employees
            emp_count      class vars     SHARABLE + MODIFY
            attendance     class vars     SHARABLE + MODIFY 
            
   

class variables    : data which is sharable to all objects
                     data which is SHARE + MODIFY actions
class methods      : 1. To act only on class variables


instance variables : data is unique for each object 
instance methods   : 1. To act only on instance variables OR 
                     2. Both instance and class variables
                     
                   

CV   - ClassMethod, InstanceMethod 
IV   - InstanceMethod
 
'''