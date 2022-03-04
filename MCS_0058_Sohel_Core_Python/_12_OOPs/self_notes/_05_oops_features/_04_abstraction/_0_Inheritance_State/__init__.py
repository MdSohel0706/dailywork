# https://www.journaldev.com/15911/python-super

class Employee:

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def get_emp_details(self):
        print("Employee details ",self.id,self.name)

class SoftwareEmployee(Employee):

    def __init__(self,id,name,sal,pf):
        Employee.__init__(self,id,name)  # First initialize the state of super class
        self.sal = sal
        self.pf = pf

    def get_emp_details(self):  # Method overriding
        print("SoftwareEmployee details : ",self.sal,self.pf)

se = SoftwareEmployee(100,'Madhu',10000,55)
se.get_emp_details()


'''
Class,Object  -- class logical strucure,object physical
Encapsulation -- Binding the data members and member methods into single entity
Inheritance   -- Super - Sub class method - method reusability  SI MLI  HI HyI  MI
Polymorphism  -- Static - MOL Dynamic - MOR
Abstraction   -- Hiding implementation details,exposing only signature to other modules
'''




'''
Combinations :
------------------
- 1.1 We can reuse super class method 
  1.2 Override the super class method,implement your own body in sub class.
      But don't create your own methods
- 2.  Write your own specific methods in sub class

1. Inheritance without Specification:      
               Inheritance: - 1.1  
                              1.2
                              1.1 + 2 
                              1.2 + 2         
   
2. Inheritance with Specification: 
               Combinations - 1.1  
                              1.2
   
mobile phones: charger Specification X
ctype charger 
CD Drive, Pen drive     
-------------------
laptop car bike 


Specification -- CD Drive   10CM  15CM
Pendrive : USB cable 
MRF CIAT -- 
XYZ -- 

Spefication : Latpop USB Ports
                     A-Z a-z
                     0 to 9 
                     all special chars 


class LaptopSpec:
    # Specification
      #STATE
      #BEHAVIOR

class Dell     class Lenovo             
                            
               
'''

