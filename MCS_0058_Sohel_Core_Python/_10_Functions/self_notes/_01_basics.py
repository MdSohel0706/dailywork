#Python Functions:

"""Python Functions is a block of related statements designed to perform a computational, logical,
or evaluative task. The idea is to put some commonly or repeatedly done tasks together and make a
function so that instead of writing the same code again and again for different inputs,
 we can do the function calls to reuse code contained in it over and over again.

Functions can be both built-in or user-defined. It helps the
 program to be concise, non-repetitive, and organized."""


"""def function_name(parameters):
    docstring
    statement(s)
    return expression"""


"""# A simple Python function

def fun():
    print("Welcome to GFG")"""
'''
# sum of 2 numbers
-------------------
STATE    ==> 1
BEHAVIOR ==> 2,3

       # 1. Customer input
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

       # 2. Business Logic
result = num1 + num2
       # 3. Give response to user
print("Addition is : ",result)

# FUNCTIONS

Advantages: - Avoids code duplication ==> Code reusability
            - When enhancements are required,
                        we need to change code only one place

# Functions:
----------------
f(x) = 2x2+3x+1. Find the value of f(x) when x is 10
f(10) = 2(10*10)+3(10)+1
      = 2(100)+30+1
	  = 200+30+1
f(10) = 231

Find the behavior  of f(x) when x value ranges from -2 to 2
f(-2) = 2(-2*-2)+3(-2)+1  = 3
f(-1) = 2(-1*-1)+3(-1)+1  = 0
f(0)  = 2(0*0)+3(0)+1  	  =	1
f(1)  = 2(1*1)+3(1)+1     = 6
f(2)  = 2(2*2)+3(2)+1     =15

f(x)   = 2x2+3x+1  # Function definition
f(2)               # Function calling by passing value
2(2*2)+3(2)+1      # Function execution
15                 # Function end result
'''

# REQ: Find sum of 2 numbers
    # I. STATE
"""num1 = int(input("Enter number 1 :"))   # 1. Customer input
num2 = int(input("Enter number 2 :"))

    # II. BEHAVIOR
result = num1 + num2             # 2. Business Logic
print("Addition is : ", result)  # 3. Give response to user
"""
# Problem with above code
'''
Code duplication == we should achieve ==> Code reusability
'''


x = 15 #state
x = 2+x #expression
print(x)

x = 34 #state
action = (x*34+677-8778/545%34)#expression
result = (x/546)
print("function caculation :", x ,type(x) )

a = "satish" #state
b = "123456" #behaviour
print("Adding the elements :",(a + b)) #Business Logic

a = "123+334" #state
b = "233+333"#behaviour
print("Adding the elements :",(a+b)*3)#Business Logic

# variables = parameters
# values = Arguments

x1 = "123"
x2 = "456"
x3 = "789"
print("")
"""Functions
												---------

-->Functions are basically some instructions that are packaged together to perform a specific task. To create a fucntion we use the "def" keyword. 

example:
----------
def func() :
	pass
print(func()) #this calls the function, but it returns none becuase there nothing in the function.
print(func) #this prints the function with particular location.
print(id(func)) #this return the id of the func.

Note: the id and the memory location are different. id is an integer value and the memory location is the alpha numeric value.

-->Usually we have pre-defined functions and the user defined function. we have already seen the user defined functions such as type(), print(), id(), input() etc. we need the user defined functions to write the functions with customized behaviour. with functions we can achieve the code reusability also. which means once the function is created, we can call that function from anywhere in the program, any number of times, with different input values. let's create a sample function. we use the keyword 'def'.

syntax:
-------
def func_name(parameters):
   <statement>

example:
--------
def func(a, b):
    result = a + b
    print('sum is : ', result)

func(10,20)
output:
-------
sum is : 30

-->the statement def func(a,b): is called as the function definition or we can call it as the function signature. a, b are called as the parameters. 10, 20 are arguments. 

state : 
-------
-->here 10, 20 are the state. simply the state is the input or the values with particular data type, on which we are going to develop some business logic.

bahaviour : 
-----------
-->here the behaviour is the business logic, which is the adding of the 2 numbers. 

Responsibility : 
----------------
-->This means here we are printing the result. some times we have to returns the result back to it's caller. these are kind of responsibility statements.


--------------------------------------------------------------------------------------------------------------

                                        passing different values:
                                        -------------------------

passing the expression:
-----------------------
-->we can also pass the expressions to the function directly. but first the expression is evaluated first and then is passed.
example:
--------
def func(a, b):
    result =  a + b
    print('sum is :', result)

func(20 + 20, 30 + 30)
output:
--------
sum is : 100


passing the positional arguments:
---------------------------------
-->we can pass the values using the positional arguments. 
example:
--------
def func(a, b):
    result =  a + b
    print('sum is :', result)

func(10, 20)
output:
-------
sum is : 30


--------------------------------------------------------------------------------------------------------------

                                            default parameters:
                                            ------------------

-->Python has a different way of representing syntax and default values for function arguments. Default values indicate that the function argument will take that value if no argument value is passed during function call.

example:
--------
def func(msg1, msg2 = ' how are you'):
    result = msg1 + msg2
    print('message is :', result)

func('hello')
output:
-------
message is : hello how are you

-->here even we don't pass the value for the parameter msg2, it takes it's defualt value. if we pass the value to the default parameter, the defualt value will be changed to new value.

example:
--------
def func(msg1, msg2 = ' how are you'):
    result = msg1 + msg2
    print('message is :', result)

func('hello', ' message changed')
output:
-------
message is : hello message changed


-->if all the parameters are the default, then we dont' have to call the function with arguments.
example:
--------
def func(msg1 = 'hello ', msg2 = ' how are you'):
    result = msg1 + msg2
    print('message is :', result)

func()
output:
-------
message is : hello  how are you


--------------------------------------------------------------------------------------------------------------

                                        keyword arguments:
                                        ------------------

-->When we call a function with some values, these values get assigned to the arguments according to their position. Python allows functions to be called using keyword arguments. When we call functions in this way, the order (position) of the arguments can be changed.

example:
--------
def func(a, b, c):
    result = a + b + c
    print('sum is : ',result)

func(a = 10, b = 20, c = 30)
output:
-------
sum is :  60

-->here the order of keyword arguments is not mandatory. the values will go into their respective position.
example:
--------
def func(a, b, c):
    result = a + b + c
    print('sum is : ',result)

func(c = 30, b = 20, a = 10)
output:
-------
sum is :  60


-->here the name of the keyword arguments and the parameter names should be same.
example:
--------
def func(a, b, c):
    result = a + b + c
    print('sum is : ',result)

func(x = 10, b = 20, c = 30)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 5, in <module>
    func(x = 10, b = 20, c = 30)
TypeError: func() got an unexpected keyword argument 'x'


--------------------------------------------------------------------------------------------------------------


                                                return statement
                                                ----------------

-->You can use the return statement to make your functions send Python objects back to the caller code. These objects are known as the function’s return value. You can use them to perform further computation in your programs. A return statement consists of the return keyword followed by an optional return value.

-->In python there are 2 types in returning values
1)Implicit return
2)Explicit return


                                            Implicit return :
                                            -----------------

-->A Python function will always have a return value. There is no notion of procedure or routine in Python. So, if you don’t explicitly use a return value in a return statement, or if you totally omit the return statement, then Python will implicitly return a default value for you. "That default return value will always be None".
example:
--------
def func(a,b):
    #performs the sum
    result = a + b
    
print(func(10, 20))
output:
-------
None

-->here function is not returning any value. so by default it returns the None.

-->If you don’t supply an explicit return statement with an explicit return value, then Python will supply an implicit return statement using None as a return value.
example:
--------
def func(a,b):
    result = a + b
    print('sum is :', result)

print(func(10, 20))
output:
-------
sum is : 30
None
-->here the function is printing the result, but it is not returning anything back to it's caller, so the return value of this function is also None.


example:
--------
def func():
    #performs nothing
    pass
    
print(func())
output:
-------
None
-->a function with no impelementation also returns None.



                                        Explicit return:
                                        ----------------

-->An explicit return statement immediately terminates a function execution and sends the return value back to the caller code. To add an explicit return statement to a Python function, you need to use return followed by an optional return value. 
Note: 
-----
You can use explicit return statements with or without a return value. If you build a return statement without specifying a return value, then you’ll be implicitly returning None. see below :
example:
--------
def func(a, b):
    result = a + b
    return

print(func(10, 20))
output:
-------
None


example:
--------
def func(a, b):
    result = a + b
    return result

print('sum is : ', func(10, 20))

output:
-------
sum is :  30


example: returning a list comprehension
--------
def func(n):
    return [i for i in range(n)]

print('values are : ', func(10))
output: 
-------
values are :  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


example:
--------
def func(n):
    return sum(n)

print('sum of elements in list : ', func([1,2,3,4,5,6]))
output:
-------
sum of elements in list :  21


                                    returning multiple values:
                                    --------------------------

-->You can use a return statement to return multiple values from a function. To do that, you just need to supply several return values separated by commas.

example:
--------
def func(n):
    #performs sum, min, max of the list
    return sum(n), min(n), max(n)

print('sum of elements in list : ', func([1,2,3,4,5,6]))
output:
-------
sum of elements in list :  (21, 1, 6)

-->if you observe, the function returns the result in the tuple format. so if a returns statement is returning a value or multiple values, it returns them in the form of tuples. 'NOT ONLY return, MANY FUNCTIONS IF THEY ARE RETURNING MULTIPLE VALUE, THEY RETURNS IN THE FORM OF TUPLES , LISTS ETC.' Here the result is not in a understandable format. so let's unpack the result which is in the tuple format. 

example:
--------
def func(n):
    #performs sum, min, max of the list
    return sum(n), min(n), max(n)

#tuple unpacking
total, minimum, maximum = func([1,2,3,4,5,6,7])
print('total : ', total)
print('minimum : ', minimum)
print('maximum : ', maximum)
output:
-------
total :  28
minimum :  1
maximum :  7


                                Using return With Conditionals:
                                -------------------------------

-->Python functions are not restricted to having a single return statement. If a given function has more than one return statement, then the first one encountered will determine the end of the function’s execution and also its return value.

-->A common way of writing functions with multiple return statements is to use conditional statements that allow you to provide different return statements depending on the result of evaluating some conditions.

example:
--------
def func(n):
    #check given number is positive or negative
    if n > 0:
        return "positive number"
    else:
        return "negative number"

print(func(-19))
output:
-------
negative number


-->If you’re using if statements to provide several return statements, then you don’t need an else clause to cover the last condition. Just add a return statement at the end of the function’s code block and at the first level of indentation. 

example:
--------
def func(n):
    if n < 0:
        return "negative number"
    return "positive number"

print(func(-19))
output:
-------
negative number



                                        Returning True or False:
                                        ------------------------

-->Another common use case for the combination of if and return statements is when you’re coding a predicate(A predicate is a function that returns the truth value of some condition) or Boolean-valued function. This kind of function returns either True or False according to a given condition.

example:
--------
def func(n):
    #check if the number is divisable by 2 or not.
    if n % 2 == 0:
        return True
    else:
        return False

print(func(10))
output:
-------
True


-->you can directly use a Boolean expression in your return statement. This is possible because these operators such as membership, identity, comparison, boolean return either True or False.
-->let's write the above same program again with different way

example:
--------
def func(n):
    return not n % 2

print(func(11))
output:
-------
False


-->On the other hand, if you try to use conditions that involve Boolean operators like or and and in the way you saw before, then your predicate functions won’t work correctly. That’s because these operators behave differently. They return one of the operands in the condition rather than True or False: 
example:
--------
def func(a, b):
    return a and b

print(func(1, 2))
output:
-------
2

-->Since "and" returns operands instead of True or False, your function doesn’t work correctly. There are at least three possibilities for fixing this problem:
1)An explicit if statement
2)A conditional expression (ternary operator)
3)The built-in Python function bool()

1)If you use the first approach, then you can write func() as follows:

example:
--------
def func(a, b):
    if a and b:
        return True
    return False

print(func(10, 0))
output:
-------
False

-->Here if statement checks if a and b are both truthy. If so, then both_true() returns True. Otherwise, it returns False.

2)If, on the other hand, you use a Python conditional expression or ternary operator, then you can write your predicate function as follows:
example:
--------
def func(a, b):
    return True if a and b else False

print(func(10, 0))
output:
-------
False

3)Finally, if you use bool(), then you can code both_true() as follows:
example:
--------
def func(a, b):
    return bool(a and b)

print(func(10, 2))
output:
-------
True
"""
