# Program to remove a newline in python

'''
CRUD : Update
State : string
Behaviour : for, == , +=

initialising a new empty string and using for loop iterating the string
using condition removing the new lines from string and printing the normal string

'''

# ---- algorithms -----

# ----- state ------

string = 'hi \n shiva \n how are you'
ns = ' '
# ------ behaviour ------

for j in string:
    if j == '\n':
        continue
    else:
        ns += j
print(ns)

# ----- functions -------

string = 'hi \n shiva \n how are you'


def rem_newline():
    ns = ' '
    for j in string:
        if j == '\n':
            continue
        else:
            ns += j
    return ns


print('the new string is :', rem_newline())
