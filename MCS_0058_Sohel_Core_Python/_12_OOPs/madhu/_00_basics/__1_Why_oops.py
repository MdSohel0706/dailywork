
'''
Object Oriented Programming System
'''

'''
Class/Object

Encapsulation
Abstraction
Inheritance
Polymorphism
'''

# REQUIREMENT : Sum of 2 given numbers

# STATE :   -  Data Initialization  ==> Data types/data structures
n1 = 10  # int(input("Enter number1"))
n2 = 20  # int(input("Enter number2"))

# BEHAVIOR   - Implementation       ==>  Functions
def get_sum(num1, num2):
    result = num1 + num2
    return result

print("Sum of 2 numbers is : ", get_sum(n1, n2))

'''if elif else 
   for while 
   functions 
   class 
   try except finally 
   with
'''



"""class structure

class <class-name>:
        # 1. STATE
    n1 = 10
    n2 = 20
    
        # 2. BEHAVIOR
    def get_sum(num1, num2):
        result = num1 + num2
        return result"""


# REQ : Display each employee information   CRUD -> RETRIEVAL
'''
CRUD 
Data type/structures
STATE
BEHAVIOR
'''
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
    name = 'Madhu Nettem' # input("Enter name : ")
    sal = 15000 # int(input("Enter sal :"))

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
madhu = Employee(100, 'Madhu Nettem', 15000)    # x = 10
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

madhu = Student(23, 'Madhu Nettem', 65)
madhu.get_sinfo()