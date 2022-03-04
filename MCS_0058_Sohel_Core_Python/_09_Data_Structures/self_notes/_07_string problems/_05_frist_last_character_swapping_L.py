# first and last characters swapping
"""
CRUD : update
state : string
behaviour : +

Taking a string  as input from user
storing last and first characters into variables
replacing the first and the last letter with opposite variable to achieve swapping
"""

string = str(input('enter the string:'))

s1 = string[0]
s2 = string[-1]
string = string[:0] + s2 + string[1:]
string = string[:-1] + s1
print(string)

# ------ or --------

string = str(input('enter the string:'))
li = []
ns = ' '
for i in string:
    li.append(i)
li[0], li[-1] = li[-1], li[0]
for j in li:
    ns += j
print('the new string is: ', ns)
