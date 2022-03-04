'''
Length of first 3 chars
Write a Python function to get a string made of its first three characters of a specified string.
If the length of the string is less than 3 then return the original string.
'''
"""CRUD : Retrieval
state : string
Behaviour : if,elif, ==,for

Taking the one string and one character as the user input and using the condition print true or false
"""
str1 = 'Indigo red' #state


def three_chars(string): #responsiability
    return string[0:3]


print('Input String :', str1)
print('First 3 chars : ', three_chars(str1))


def addition(a,b):
    a = 10
    b = 20
    return a +b
print(addition(10,20))