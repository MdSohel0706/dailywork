'''
First Class Objects
In Python, functions are first class objects that mean that
functions in Python can be used or passed as arguments.

Properties of first class functions:

A function is an instance of the Objecttype.
You can store the function in a variable.
You can pass the function as a parameter to another function..
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
'''
# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))

'''
In the above example, we have assigned the function shout to a variable.
This will not call the function instead it takes the function object referenced by a shout
and creates a second name pointing to it, yell.
'''