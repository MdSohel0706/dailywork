'''
4 Copies of last 2 chars
Insert a string in the middle of a string
'''
"""CRUD : Retrieval
state : string
Behaviour : if,elif, ==,for

Taking the one string and one character as the user input and using the condition print true or false
"""
str1 = 'Kobe Bryant'


def two_chars(string):
    return string[0:2] * 4


print('Input String :', str1)
print('4 copies of first 2 chars :', two_chars(str1))

