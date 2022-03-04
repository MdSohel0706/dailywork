
"""

to using pdb is causing the interpreter to enter the debugger when you want it to.
There are a few different ways to do that,
depending on your starting conditions and what you need to debug.


"""

"""class MyObj(object):

    def _init_(self, num_loops):
        self.count = num_loops

    def go(self):
        for i in range(self.count):
            print (i)
        return

if _name_ == '_main_':
    MyObj(5).go()



import pdb

def f(n):
    for i in range(n):
        j = i * n
        print (i, j)
    return

if _name_ == '_main_':
    pdb.set_trace()
    f(5)

import pdb

def calc(i, n):
    j = i * n
    return j

def f(n):
    for i in range(n):
        j = calc(i, n)
        print (i, j)
    return

if _name_ == '_main_':
    pdb.set_trace()
    f(5)


import pdb


def addition(a, b):
	answer = a + b
	return answer


pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)


def multiply(a, b):
	answer = a * b
	return answer


x = input("Enter first number : ")
y = input("Enter second number : ")
result = multiply(x, y)
print(result)


def addition(a, b):
	answer = a + b
	return answer


x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)


# importing pdb
import pdb

# make a simple function to debugg
def fxn(n):
	for i in range(n):
		print("Hello! ", i+1)


# starting point to debugg
pdb.set_trace()
fxn(5)


# a simple function
def fxn(n):
	for i in range(n):
		print("Hello! ", i+1)


# using breakpoint
breakpoint()
fxn(5)

 # Printing Variables or expressions

# importing pdb
import pdb

# define recursive function
def rec_fxn(r):
	if r > 0:

		# set trace
		pdb.set_trace()
		rec_fxn(r//2)
	else:
		print("recursion stops")
	return

# set trace at start
pdb.set_trace()
rec_fxn(5)"""
"""
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
"""

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
"""
for i in range(0, 10, 1):
    if i % 2 == 0:
        print(i)"""

"""number = 20 #state
while(number < 30): # each iteration 
    print("Enter the number :",number)
    number = number+1 # business logic
    print("End the program")"""

"""
list1 = [18, 42, 24, 22, 44, 36, 34, 10, 8, 44, 6, 10, 76, 88, 18, 9, 888]
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
"""
