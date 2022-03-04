"""
#KEYWORDS:

The True & False Keywords
==========================
The True and False are the truth value in Python. Comparison operators returns
True or False. Boolean variables also can hold them.
e.g.

print(5 < 10)            #it is true
print(15 < 10)       #it is false

O/P
True
False
***********

The class, def, return Keywords
================================
The class keyword is used to define new user-define class in Python.
The def is used to define user-defined function.
And the return keyword is used to go back from a function and send a value to the invoker function.
************

The if, elif, else Keywords
============================
These three keywords are used for conditional branching or decision making.
When the condition is true for the if statement, it enters the if block.
When it is false, it searches for another condition, so if there are some elif block,
it checks the condition with them. And finally, when all conditions are false, it enters into the
else part.

e.g.

def check(x):
    if x < 0:
        print(" x is -ve no")
    elif x == 0:
       print(" x is zero")
    else:
       print("x is +ve no")
check(20)
check(-20)
check(0)
***********

The try, except, raise, finally Keywords
=============================================
These keywords are used to handle different exceptions in Python. In the try block, we can write
some code, which may raise some exceptions, and using the except block, we can handle them.
The finally block is executed even if there is an unhandled exception.

e.g.
def check(x):
   if x == 0:
      raise ZeroDivisionError('Cannot divide by zero') #raise an exception
   else:
      return 1/x
def try_block_example(x):
   result = 'Unable to determine' #initialize
   try: #try to do next tasks
      result = check(x)
   except ZeroDivisionError: #except the ZeroDivisionError
      print('Invalid number')
   finally: # Always execute the finally block
      print(result)
try_block_example(15)
try_block_example(0)
************

The for, in, is, not Keywords
===============================
The for keyword is basically the for loop in Python. and the in keyword is used to check
participation of some element in some container objects.
The is keyword is used to test the identity of an object.
The not keyword is used to invert any conditional statements.
e.g.

f_list = [ 'Rose' , 'Sunflower', 'Lili' , 'Rajnigandha' , 'Chamelli']
for flw in f_list: #iterate through all flowers in f_list
   if flw is 'Lili': #equality checking using 'is' keyword
      print(flw + " " + "You can buy ")
   elif flw is not 'Chamelli': #negation checking using 'not' keyword
      print(flw + " " + 'check another flower')

O/P
Rose check another flower
Sun flowercheck another flower
Lili You can buy
Rajnigandha check another flower
************

The from, import Keywords
============================
The import keyword is used to import some modules into the current namespace.
The from…import is used to import some special attribute from a module.

e.g.

from math import factorial
print(factorial (5))
************

The global Keyword
===================
The global keyword is used to denote that a variable, which is used inside a block is global variable.
When the global keyword is not present, the variable will act like read only. To modify the value,
we should use the global keyword.

e.g.

a = 50
def read_global():
   print(a)
def write_global1(x):
   global a
   a = x
def write_global2(x):
   a = x
read_global()
write_global1(100)
read_global()
write_global2(150)
read_global()

O/P
50
100
100
***********
The nonlocal Keyword
====================
The nonlocal keyword is used do declare a variable in a nested function is not local to it. So it is
local for the outer function, but not the inner function. This keyword is used to modify some nonlocal
 variable value, otherwise it is in read only mode.
e.g.
def outer():
   x = 50
   print('x from outer: ' + str(x))
   def inner():
      nonlocal x
      x = 100
      print('x from inner: ' + str(x))
   inner()
   print('x from outer: ' + str(x))
outer()

O/P
x from outer: 50
x from inner: 100
x from outer: 100
***********
The lambda Keyword
===================
The lambda keyword is used to make some anonymous function. For anonymous functions, there is no name.
 It is like an inline function. There is no return statement in the anonymous functions.

e.g.

square = lambda x: x**2
for item in range(5, 10):
   print(square(item))
************
The pass Keyword
==================
The pass keyword is basically the null statement in Python. When the pass is executed,
nothing happens.This keyword is used as a placeholder.

e.g.
def sample_function():
pass #Not implemented now
sample_function()

O/P
NO OUTPUT
************
The while, break, continue, and Keywords
=========================================
The while is the while loop in Python. The break statement is used to come out from the current loop,
and the control moves to the section, which is immediately below the loop. The continue is used to
ignore the current iteration. It moves to the next iteration in different loops.

The and keyword is used for logical and operation in Python, when both of the operands are true,
it returns a True value.

e.g.
 i = 2
while True:
   i += 1
   if i>= 5 and i<= 10:
      continue #skip the next part
   elif i == 15:
      break #Stop the loop
   print(i)

   O/P
   3
   4
   11
   12
   13
   14
***********
The with, as Keywords
=========================

The with statement is used to wrap the execution of a set of codes, within a method, which is defined
by the context manager. The as keyword is used to create an alias.

e.g.
with open('sampleTextFile.txt', 'r') as my_file:
print(my_file.read())

***********
The del, or Keywords
======================
The del keyword is used to delete the reference of an object. And the or keyword performs the logical
or operation. When at least one of the operands is true, the answer will be true.

e.g.
my_list = [10, 20, 60, 40, 50, 30, 70, 80, 90, 100, 110]
index = []
for i in range(len(my_list)):
   if my_list[i] == 30 or my_list[i] == 60:
      index.append(i)
      print(index)
for item in index:
   print(item)
   del my_list[item]
print(my_list)
************

The assert Keyword
===================
The assert statement is used for debugging. When we want to check the internal states,
we can use assert statement. When the condition is true, it returns nothing, but when it is false,
the assert statement will raise AssertionError.

e.g.
x = 10
assert x>100

O/P
Traceback (most recent call last):
  File "C:\Users\PINKY KUMARI\PycharmProjects\mypythonProject\main.py", line 2, in <module>
    assert x >100
AssertionError

x = 10
assert x <100

O/P
print nothing
*******
The None Keyword
===================
The None is a special constant in Python. It means null value or absence of value. We cannot create
multiple none objects, but we can assign it to different variables.
e.g
deftest_function(): #This function will return None
   print('Hello')
   return 'hello'
x = test_function()
print(x)

O/P
Hello
None


"""