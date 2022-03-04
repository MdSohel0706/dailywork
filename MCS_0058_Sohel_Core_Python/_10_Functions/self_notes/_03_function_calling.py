#Calling a Function
"""Calling a  Function
After creating a function we can call
it by using the name of the function followed by parenthesis containing parameters of that particular function."""

"""
# A simple Python function
 
def fun():
  print("Welcome to GFG")
         
# Driver code to call a function
fun()"""


'''
To call a function, use the function name followed by parenthesis:
Requirement: Add two no
#function defination

def add(n1,n2):    # function signature
  "#function body"
  n3= n1+n2
  print("sum of a no", n3)
add(87,52)   # Function calling
------------------------------------------------

#Requirement :  check Enter no is +ve or -ve
#State
num=int(input("Enter a no"))
# Behavior

def check(num): #Function Definition
# Function body
 if num>0:
  print(num,"is +ve no")
 else:
  print(num,"is -ve no")

check(num)     # calling function
------------------------------------------
#Requirement :  print table
# Behavior
def multi(n): #Function Definition
 print(n)
 i=1
 while i<11:
  result=i*n
  i += 1
  print("Table of",n, "is =",result)
#State
num = int(input("Enter a no"))
multi(num)     # calling function

-------------------------------------------------

#Requirement :  print table
# Behavior
def multi(n): #Function Definition
 print("Table of ", n ,"is")
 i=1
 while i<11:
  result=i*n
  i += 1
  print(result)
#State
num = int(input("Enter a no"))
multi(num)     # calling function
-------------------------------------------------
#Requirement :  Concatinate name enter name
# Behavior
def multi(fn,ln): #Function Definition
 full_name = fn +" "+ ln
 print("Full Name of student",full_name)
#State
fname= input("Enter first name of Student")
lname= input("Enter last name of Student")
multi(fname,lname)     # calling function

-------------------------------------------------
#Requirement :  Concatinate enter name and marks
# Behavior
def multi(fn,ln,m): #Function Definition
 details = fn +" "+ ln + "    Marks =", m
 print("Full Name of student",details)

#State
fname= input("Enter first name of Student")
lname= input("Enter last name of Student")
marks = int(input("Enter marks of student"))
multi(fname,lname,marks)     # calling function
'''

# REQ : Find sum of 2 given numbers

# 1. STATE
'''
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
'''
num1 = 10
num2 = 20


# 2. BEHAVIOR
def sum(n1, n2):  # Function definition
    result = n1 + n2
    print("Addition : ", result)


sum(num1, num2)  # Function calling
sum(10, 20)
sum(5 + 5, 10 + 10)

'''

9,10 lines : num1,num2  ==> Variables 
           : 10,20      ==> values
13         : n1,n2      ==> Parameters
17,18,19 :              ==> arguments     

'''



