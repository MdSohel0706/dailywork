# finding the length of longest string in user input string
"""
CRUD : Retrieval
state : string, list
behavior : for, >

"""
'''
code is taking the input string'
spilt the string to list
appending the len of string in list to another list
using max function getting the higgest number in list
'''
# ----- built in ----

string = str(input('enter a string:'))
string = string.split(' ')
ls1 = []
for i in string:
    ls1.append(len(i))
print('longest length of string: ', max(ls1))

# ----- function -----
"""
code is taking the string as user input
then spliting the string to list
by swaping the len of each string value in list to sort the list
by slicing taking last string length for longest length
"""
string = str(input('enter a string:'))


def long_length(s):
    li = s.split(' ')
    for k in range(len(li)-1):
        if len(li[k]) > len(li[k + 1]):
            li[k], li[k + 1] = li[k + 1], li[k]
    return len(li[-1])


print('longest length of the string', long_length(string))
