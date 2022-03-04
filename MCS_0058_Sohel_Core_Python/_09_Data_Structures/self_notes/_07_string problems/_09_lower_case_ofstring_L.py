# converting the lower case to upper case and upper case to lower case of given string

'''
CRUD : Update
state : string, list
behaviour : for, if

Taking a string as input from the user and initializing a empty list and empty string
using for loop iterate the string and using if else condition converting the lower to upper case
and upper to lower case of the given string and appending into new list and later joining to empty string
'''

s = str(input('enter a string:'))
li = []
ns = ' '

for i in s:
    if i.islower():
        li.append(i.upper())
    else:
        li.append(i.lower())

ns = ''.join(li)
print('the new string:', ns)

# ----- function ------

s = str(input('enter a string:'))
ns = ' '


# ----- function --------

def lower_upper(s1):
    ls = []
    for k in s:
        if k.islower():
            ls.append(k.upper())
        else:
            ls.append(k.lower())
    return ls


ns = ''.join(li)
print('the new string is :', ns)
