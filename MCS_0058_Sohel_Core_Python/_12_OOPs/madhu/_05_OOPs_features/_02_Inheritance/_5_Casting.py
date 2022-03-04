

'''
'''


'''
    Water              Watercan
    =====================================================
    1. 2L of water      2L Can   -  OK
    2. 5L of water      5L Can   -  OK
    3. 2L of water      5L Can   -  OK      Memory wastage
    4. 5L of water      2L Can   - NOT OK   Data Loss
    
    class Employee:    # 5L can
    
    class SoftEmp(Employee):   # 2L can
     
        
        can    water
        --------------
     1. int x = 10       # 2L can <--- 2L water
     2. float x = 10.5   # 5L can <--- 5L water
     3. float x = 10     # 5L can <--- 2L water    # Implicit casting  ==> 10.0
 XX  4. int x = 10.5     # 2L can <--- 5L water    # Explicit casting  ==> 10    int x = (int)10.5
    
    
    Employee
      |  m1()
      |
    Software Employee
         m2()
    
    Capacity          Content
    --------------------------------------------
    1. SoftEmp emp  = SoftEmp(100, 'MadhuN', 15000)     2L Can  <--- 2L Water
    2. Employee emp = Employee(100, 'MadhuN', 15000)    5L Can  <--- 5L Water
    3. Employee emp = SoftEmp(100, 'MadhuN', 15000)     5L Can  <--- 2L Water   Memory loss # Upcasting
    4. SoftEmp emp  = Employee(100, 'MadhuN', 15000)    2L Can  <--- 5L Water   Data loss   # Downcasting

'''

'''
Specification

IEEE standards 

SoftEmp semp  = SoftEmp(100, 'MadhuN', 15000)
semp.m1()
semp.m2()

Employee emp  = Employee(100, 'MadhuN', 15000)
emp.m1()

SUPER CLASS:
============
As a sub class, use my super class methods AS IS   (or) 
                                           Override my super class method
                        but don't write your own methods
                         
Employee emp = SoftEmp(100, 'MadhuN', 15000) 
emp.m1()
emp.m2()  # ERROR


'''
     
     

'''