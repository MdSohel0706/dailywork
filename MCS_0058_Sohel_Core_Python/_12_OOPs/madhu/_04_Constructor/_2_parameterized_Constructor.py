"""Python Parameterized Constructor:

The parameterized constructor has multiple parameters along with the self.
"""
"""class Student: 
 
    # Constructor - parameterized  
    def __init__(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
student = Student("John")  
student.show()
 """
# Positional arguments

"""
class Employee:
    # Parameterized Constructor
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        pass

satish = Employee(200, 'satish', 10000)
"""

'''
# Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional arguments
            - Default arguments
            - keyword arguments

'''
# Default arguments example
"""
class Employee:
    # parameterized constructors
    def __init__(self, eid=None, name=None, sal=None):  # Constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        print("Employee info : ", self.eid, self.name, self.sal)


satish = Employee()
satish.getedata()

sam = Employee(201)
sam.getedata()

venkat = Employee(201, 'venkat')
venkat.getedata()

ravi = Employee(200, 'ravi', 10000)
ravi.getedata()

raju= Employee(name='raju', sal=20000)
raju.getedata()


class Student:
    def __init__(self):
        print("The First Constructor")

    def __init__(self):
        print("The second contructor")


st = Student()  
"""
"""
lass Student:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  
  
    # creates the object of the class Student  
s = Student("John", 101, 22)  
  
# prints the attribute name of the object s  
print(getattr(s, 'name'))  
  
# reset the value of attribute age to 23  
setattr(s, "age", 23)  
  
# prints the modified value of age  
print(getattr(s, 'age'))  
  
# prints true if the student contains the attribute with name id  
  
print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  
  
# this will give an error since the attribute age has been deleted  
print(s.age)  
"""

"""
class Student:    
   
    def __init__(self,name,id,age):    
        self.name = name;    
        self.id = id;    
        self.age = age    
   
    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))
            
s = Student("John",101,22)    
print(s.__doc__)    
print(s.__dict__)    
print(s.__module__) 
"""
