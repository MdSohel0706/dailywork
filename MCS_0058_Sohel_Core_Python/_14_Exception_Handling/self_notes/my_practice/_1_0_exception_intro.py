'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/Batch_13/B13_PythonTraining/_13_Exception_handling/_1_Introduction.py", line 20, in <module>
    x = int(input("Enter numerator value :"))
ValueError: invalid literal for int() with base 10: 'dfgads'
'''
'''
Requirement: As an end user i will give 2 values,
             display division result for the same.
             
#Exceptions in Python
"""
Python has many built-in exceptions that are raised when your program encounters an error 
(something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes
it to the calling process until it is handled. If not handled, the program will crash."""
 """


'''
# Before Exception handling
print("----Before Exception handling----")

x = int(input("Enter numerator value :"))
y = int(input("Enter denominator value :"))
print("Division :", x / y)  # 0/any value = 0   any value/0 = infinity
print("Remaining Code")
print("---------------------------------")

'''
blocks :if else elif for while  function class

blocks to handle the exception    
try*      : Code which causes the exception
except*   : to handle exception occured in try block
else
finally
'''

#Catching Exceptions in Python
"""
In Python, exceptions can be handled using a try statement.
The critical operation which can raise an exception is placed inside the try clause. 
The code that handles the exceptions is written in the except clause.
We can thus choose what operations to perform once we have caught the exception.
"""

# After Exception handling
print("----After Exception handling----")
try:
    x = int(input("Enter numerator value :"))
    y = int(input("Enter denominator value :"))
    print("Division :", x / y)  #  any value/0 = infinity
    print("---Division result usage---")
    print("---In try block3 ---")
except:
    print("Please enter denominator other than 0")
print("---Remaining code---")
print("---------------------------------")

"""
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
"""

"""
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
"""

"""# Before Exception handling
print("----Before Exception handling----")

a = int(input("Enter numerator value :"))
b = int(input("Enter denominator value :"))
print("Division :", a / b)  # 0/any value = 0   any value/0 = infinity
print("Remaining Code")
print("---------------------------------")
"""
