# Remove odd index value in string
'''
CRUD : update
state : string
behaviour : for, != , +=

taking the string from user
initializing the new string
using for loop iterating the user given string and using the if condition filtered the odd index positions and
added to new string
'''

# ------- algorithm ---------

s = str(input('enter a string: '))
ns = ' '
for i in range(len(s)):
    if i % 2 != 0:
        ns += s[i]
print('the new string with odd index number of original string:', ns)

# --------function -----------
s = str(input('enter a string: '))


def rem_odd_index(st):
    k = 0
    ns = ' '
    while i < len(st):
        if i % 2 != 0:
            ns += s[i]
            k += 1
    return ns


print('the new string with odd index number of original string:', ns)
