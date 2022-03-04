# OOPs concepts
'''
Class Object
Encapsulation
Abstraction
Inheritance
Polymorphism
'''
'''
# STATE    - data structures  - fields
# BEHAVIOR - functions        - methods

variables value                 #   x = 10
parameters arguments functions  #  def func(params)  func(args)
fields, methods                 #  Inside class 

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