"""Arguments of a Function:

Arguments are the values passed inside the parenthesis of the function.
 A function can have any number of arguments separated by a comma."""
"""Types of Arguments:

Python supports various types of arguments that can be passed at the time of the function call.
 Let’s discuss each type in deta"""

"""Default arguments:
A default argument is a parameter that assumes a default value if a value is not provided
 in the function call for that argument.
 The following example illustrates Default arguments. """

"""# Python program to demonstrate
# default arguments
 
 
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
 
 
# Driver code (We call myFun() with only
# argument)
myFun(10)"""


"""Keyword arguments:
The idea is to allow the caller to specify the argument name with
 values so that caller does not need to remember the order of parameters."""

"""
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
 
 
# Keyword arguments
student(firstname='satish', lastname='Practice')
student(lastname='Practice', firstname='satish')"""

"""Variable-length arguments: 

In Python, we can pass a variable number of arguments to a function
 using special symbols. There are two special symbols:

*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)"""

"""
# Python program to illustrate
# *args for variable number of arguments
 
 
def myFun(*argv):
    for arg in argv:
        print(arg)
 
 
myFun('Hello', 'Welcome', 'to', 'satish')"""


# Python program to illustrate
# *kargs for variable number of keyword arguments


"""def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='satish', mid='for', last='babu')"""

"""Docstring:
The first string after the function is called the Document string or Docstring in short. 
This is used to describe the functionality of the function. The use of docstring in functions 
is optional but it is considered a good practice.

The below syntax can be used to print out the docstring of a function:

Syntax: print(function_name.__doc__)"""

"""# A simple Python function to check
# whether x is even or odd
 
 
def evenOdd(x):
    Function to check if the number is even or odd
     
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code to call the function
print(evenOdd.__doc__)"""



"""
# A simple Python function to check
# whether x is even or odd
 
 
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code to call the function
evenOdd(2)
evenOdd(3)"""


#Return Type

#Requirement: Add two nos
#Without return type
#State
x=30
y=40

def add(a,b): #Function Definition
  #Business Logic
  print("Addition of two no  : ", a+b)     #Responsibility

add(x,y)   # Function Calling

'''
Here  x= 30     
      y=40      #   x,y<==> variable;  30,40 <==> Value
     add(a,b) <===>  Parameter
     add(x,y)<===> Arguments
'''
#With return type
#State
x=30
y=40

def add(a,b): #Function Definition
  #Business Logic
   sum = a+b
   return sum

sum=add(x,y)   # Function Calling
print("Addition of two no using return type  : ", sum)


#Requirement: check given no is even or not


#With return type
#State
num=int(input("Enter a no"))

def check(n): #Function Definition
  #Business Logic
   if n%2==0:
    return n
   else:
     print("Enter no is not a even")

n1=check(num)   # Function Calling
print("Addition of two no using return type  : ", n1)   # Addition of two no using return type  :  44


'''
scenario 1
Enter a no 45
Enter no is not a even
Addition of two no using return type  :  None


scenario 2

Enter a no88
Addition of two no using return type  :  88

'''


#With return type
#State
num=int(input("Enter a no"))

def check(n): #Function Definition
  #Business Logic
   if n%2==0:
    return 1
   else:
     return 0

n1=check(num)   # Function Calling
print("Addition of two no using return type  : ", n1)

'''
Enter a no45
Addition of two no using return type  :  0


Enter a no44
Addition of two no using return type  :  1
'''

# Requirement : check the no is even or not,if even multiply with 4 otherwise multiply with 9

#With return type
#State
num=int(input("Enter a no   "))

def check(n): #Function Definition
  #Business Logic
   if n%2==0:
    return 1
   else:
     return 0

n1=check(num)   # Function Calling
if n1==1:
  multi=num*4
  print ("multiplication of even no =  ", multi)
else:
    multi1=num*9
    print("multiplication of odd no =  ", multi1)

'''
Enter a no 5 
Addition of two no using return type  :  0
multiplication of odd no =   45


Enter a no   4
multiplication of even no =   16

'''

# Requirement : Find the factorial and multiply with 10
#With return type
#State

def fact(i):
      f = 1
      while i > 1:
          f = f * i
          i -= 1
      print("Factorial of a no:", f)
      return f
f1=fact(num)
multi = f1*10
print("After multiplying with factorial  " , multi)

'''
Factorial of a no: 120
After multiplying with factorial   1200

'''
# with factorial() <===> without using return type & function
import math
n=int(input("enter a no"))
print("Factorial of no", math.factorial(n))


# with factorial() <===> with using return type function
#state
n=int(input("enter a no  "))
def fact(n):   #Function definition
    # function body
     f=math.factorial(n)
     return f
f=fact(n)   # function calling
print("factorial of a no  ", f)

# using for loop

n=int(input("enter a no  "))
def fact(n):   #Function definition
    # function body
    f=1
    for i in range(1,n+1):
     f= f*i
     i+=1
    print(f)
    return f
f=fact(n)   # function calling
print("factorial of a no  ", f)



#requirement : Add two no
#Behavior

def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
add(10,75)     # Argument



#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
add(10+60,75)     # Argument




#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
add(10+60,75-85)     # Argument




#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
n=int(input("Enter a no"))
add(n,75-85)     # Argument


#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
n=int(input("Enter a no"))
add(n,0)     # Argument


#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
#n=int(input("Enter a no"))
print("zero")
add(0,0)     # Argument



#Behavior
def add(n1,n2):   # Parameter
# Function body
 result= n1+n2
 print("Sum of a no = " ,result)    # Responsibility

 #State
n=int(input("Enter a no"))
print("zero")
add(0,0)     # Argument




#requirment : Increase 30% from current salary
#Behavior
def hike(sal=30000):     # Function defination
 fsal=sal+sal*30/100
 print("After hike sal =  ", fsal)        # Responsibility
 #State
hike()    # function calling without argument



#requirment : Deduct 10% from current salary
#Behavior
def deduct(sal):   #Function Calling
 fsal=sal-sal*10/100
 print("After deduction sal is =  " , fsal)    # Responsibility
#State
esal=int(input("Enter sal of employee"))
deduct(esal)     # function calling with argument

#requirment : Add new data in exist list
#Behavior

def list(lst):    #Function definition
  print(lst)
  lst1 = []
  lst.append("rasnami")
  print(lst)
  # State
fruits = ['Apple', 'Mango', 'Banana', 'Cherry']
list(fruits)       #Function Calling


#requirment : Add set in exist list
#Behavior

def list(lst,sn):     ##Function definition
  print(lst)
  lst1 = []
  lst.append("rasnami")
  lst.append(sn)
  print(lst)      #['Apple', 'Mango', 'Banana', 'Cherry', 'rasnami', {1, 2, 3, 4}]
fruits = ['Apple', 'Mango', 'Banana', 'Cherry']
sl={1,2,3,4}
list(fruits,sl) # Function calling


#requirment : Add set in exist list
#Behavior

def list(lst,sn):     ##Function definition
  print(lst)
  lst1 = []
  lst.append("rasnami")
  lst.append(sn)
  print(lst)      #['Apple', 'Mango', 'Banana', 'Cherry', 'rasnami', {1, 2, 3, 4}]
fruits = ['Apple', 'Mango', 'Banana', 'Cherry']
sl={1,2,3,4}
list(fruits,sl) # Function calling




# REQ : Find sum of 2 given numbers

# 1. STATE
'''
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
'''
num1 = 10
num2 = 20


# 2. BEHAVIOR
"""def sum(n1, n2):
    result = n1 + n2
    print("Addition : ", result)


sum(10, 20)
sum(num1, num2)
sum(5 + 5, 10 + 10)

'''
9,10 : num1,num2  ==> Variables 
     : 10,20      ==> values
13   : n1,n2      ==> Parameters
17,18,19 :        ==> arguments     

'''
print(100)
print(40+60)


n1 = 123
n2 = 234
print("Enter the number :",n1+n2,type(n1,n2))
"""
"""x1 = 123 #state
x2 = 23 #state
print("Adding the elements:",x3 = x1+x2)"""#behaviour

'''name = "satish"#state
name1 = "venkat"#state
name2 = "kumar"#state
print("Enter the best friends names :",(name+ ", "+name1+" ,"+name2))#behaviour

x1 = "21323"#state
x2 = "43545"#state
print("enter the values :",(x1+x2))#behaviour'''

"""digit1 = int(input("Enter the digit1 values :"))# state
digit2 = int(input("Enter the digit2 values :"))# state
if(digit1>digit2): #business logic
    print("True")

else:
    print("false")"""

x1 = 12
y1 = 13

def add (a,b):
    add
    print("Enter the values :",(x1+y1))



