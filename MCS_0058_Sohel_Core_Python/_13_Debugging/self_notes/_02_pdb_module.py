print("Start of program")
num = 1
while num <= 10:   # Each iteration
    print(num)
    num = num + 1
print("End of program")


list1 = [1, 12, 10, 22, 44, 3, 34, 10, 5, 66, 6, 10, 7, 88, 18, 9, 100]
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Before list  :", list1)
for val in list1:
    if val % 2 == 0:
        list1.remove(val)  # [1,10,22,44....]
print("After list   :", list1)

print("Before list  :", list1)
li2 = []
for val in list1:
    if val % 2 == 0:
        li2.append(val)
print("To be removed :",li2)
print("After list   :", list1)




'''
Production issue occurance : Live environment / Production environment
Issue will be reported by customer 
Ticket to developer 
 - I. Replicate(reproduce) the issue 
        - Issues Exists
            - 1.2 Root cause analysis (Find what is the reason for issue) # DEBUGGING
            - 1.3 Fix the issue
            - 1.4 Testing  (Local, DEV, Test, UAT ) instances
            - 1.5 Deploy to production instance 
        - Issue doesnt exist
            - Return mail to customer
'''

#debugging:

"""'debugging' term is popularly used to process of locating and rectifying errors in a program.
Python's standard library contains pdb module ' 'which is a set of utilities for debugging '
of Python programs.

The debugging functionality is defined in a Pdb class. The module internally makes
used of bdb and cmd modules.

The pdb module has a very convenient command line interface.
It is imported at the time of execution of Python script by using –m switch"""



import pdb
x=8
def power_of_itself(a):
      return a**a
pdb.set_trace()
seven=power_of_itself(7)
print(seven)
three=power_of_itself(3)
print(three)

# Program to print Multiplication
# table of a Number
n=5
for x in range(1,11) :
    print( n , '*' , x , '=' , n*x )


# Python Program to print Multiplication Table
# We want to debug the for loop so we use
# set_trace() call to pdb module

import pdb


# It means , the Start of Debugging Mode
pdb.set_trace()

n=5
for x in range(1,11) :
    print( n , '*' , x , '=' , n*x )

import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())