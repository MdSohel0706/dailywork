'''
Replace first occurrence of string
functionality : replace the first occurrence with the mentioned character
replace() : replaces part of string with given string
input : string
'''
"""CRUD : Retrieval
state : string
Behaviour : if,elif, ==,for

Taking the one string and one character as the user input and using the condition print true or false
"""
str1 = str(input('Enter a string :')) #state
print('Replace char using replace()') #responsibility
print(str1.replace('h','#',1))  #responsibility
print('\n')  #responsibility
print('Replace char using without replace()')  #responsibility
char = 'h'  #state
new_string = ''  #state
for i in str1: #Behaviour
    if i != char:
        new_string += i
    elif i == char:
        new_string += '#'
print(new_string)


