#Constructors in Python

"""Constructors are generally used for instantiating an object. The task of constructors is
to initialize(assign values) to the data members of the class when an object of the
class is created. In Python the __init__() method is called the constructor and is always
called when an object is created.
Syntax of constructor declaration :
def __init__(self):
# body of the constructor
Types of constructors :

Attention geek! Strengthen your foundations with the Python Programming
Foundation Course and learn the basics.
To begin with, your interview preparations Enhance your Data Structures concepts
with the Python DS Course. And to begin with your Machine Learning Journey, join
the Machine Learning - Basic Level Course

default constructor: The default constructor is a simple constructor which doesn’t
accept any arguments. Its definition has only one argument which is a reference to
the instance being constructed.

parameterized constructor: constructor with parameters is known as
parameterized constructor. The parameterized constructor takes its first argument
as a reference to the instance being constructed known as self and the rest of theparameterized constructor
"""
"""
Features of Python Constructors: 

In Python, a Constructor begins with double underscore (_) and is always named as __init__().
In python Constructors, arguments can also be passed.
In Python, every class must necessarily have a Constructor.
If there is a Python class without a Constructor, a default Constructor is automatically created without any arguments and parameters."""
"""
Counting the number of objects of a class
The constructor is called automatically when we create the object of the class. Consider the following example."""
"""
class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)    
"""
"""Python Default Constructor
When we do not include the constructor in the class or forget to declare it,
then that becomes the default constructor.
It does not perform any task but initializes the objects. """

"""
class Student:  
    roll_num = 101  
    name = "Joseph"  
  
    def display(self):  
        print(self.roll_num,self.name)  
  
st = Student()  
st.display()  
"""
class Employees():

   def __init__(self, Name, Salary):
       self.Name = Name
       self.Salary = Salary

   def details(self):
       print ("Employee Name : ", self.Name)
       print ("Employee Salary: ", self.Salary)
       print ("\n")

first = Employees("Khush", 10000)
second = Employees("Raam", 20000)
third = Employees("Lav", 10000)
fourth = Employees("Sita", 30000)
fifth = Employees("Lucky", 50000)

first.details()
second.details()
third.details()
fourth.details()
fifth.details()
"""
"""
class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information

emp1.display()

# accessing display() method to print employee 2 information
emp2.display()
"""
class GeekforGeeks:

# default constructor
      def __init__(self):
        self.geek = "GeekforGeeks"
# a method for printing data members
         def print_Geek(self):
print(self.geek)
# creating object of the class
obj = GeekforGeeks()
# calling the instance method using the object obj
obj.print_Geek()"""

class Employee:
    pass

'''
converts as below
                        class Employee:
                            def __init__(self):
                                pass
'''
print("Employee class @ ", Employee)
obj = Employee()

# Default constructor
class Employee:

    def __init__(self):  # Default constructor
        pass  # to perform any generic action


    def getedata(self, eid, sal):
        print("Employee Data", eid, sal)

venkat = Employee()
venkat.getedata(101, 10000)  # Employee.getedata(madhu,101,10000)

# while defining class, default constructor is not mandatory. Python give automatically

# Employee CRUD Operations

'''
REQUIREMENT :
1. Create an employee with eid,name,sal  #
2. Retrieve emp details 
3. Give hike for employee based on experience
    Acceptance Criteria : 0 to 2 exp  => 5% hike
                          2 to 3 exp  => 10% hike
                          3 to 5 exp  => 20% hike
                          5+          => 30% hike
                          
4. Delete emp once he exits from company

GUI  -->  Backend             ---> Database

UI  --->  Python/Java/.Net    --->  Oracle/Postgresql/Mysql/Mongodb
'''

print("-----------Employee hike---------------")

class Employee:
    # create employee
    def __init__(self, eid, name, sal):  #emailid,mobiileno,perm_address,pre_add,joining_date,bloodgr,gendder
        self.eid = eid
        self.name = name
        self.sal = sal

    # 2. Retrieve emp details
    def get_emp_info(self):
        print("Employee details : ", self.eid, self.name, self.sal)

    # 3. Update emp sal based on exp
    '''
        3. Give hike for employee based on experience
        Acceptance Criteria : 0 to 2 exp  => 5% hike
                              2 to 3 exp  => 10% hike
                              3 to 5 exp  => 20% hike
                              5+          => 30% hike
    '''
    def update_emp_sal(self, exp):
        # Server validations
        if exp < 0:
            print("Please enter valid experience.")
            return None
        if exp >= 0 and exp < 2:
            hike = (self.sal * 5) // 100
            self.sal = self.sal + hike
        elif exp >= 2 and exp < 3:
            hike = (self.sal * 10) // 100
            self.sal = self.sal + hike
        elif exp >= 3 and exp < 5:
            hike = (self.sal * 20) // 100
            self.sal = self.sal + hike
        elif exp >= 5:
            hike = (self.sal * 30) // 100
            self.sal = self.sal + hike
        print("Employee  after hike : ", self.eid, self.name, self.sal)

    def delete_emp(self):
        pass


# Data hard coding
satish = Employee(100, 'satish', 1500000)
satish.get_emp_info()
satish.update_emp_sal(4)


'''
UI PAGE:
---------
EmmpID: 101
name  : satish
exp   : -10 
Mobileno : 34232443243

# client validations 
# server validations
'''