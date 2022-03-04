# counting the words present in the string

'''
CRUD : retrieve
state : string
behaviour : for, if, ==, +=

'''

# ----- built in --------

s = str(input('enter a string: '))

s = s.split()
print('the number of words in the string are:', len(s))

'''
taking a string as user input
initializing count value with 1 
using for loop iterating the string and with the help of if condition increasing the count 

'''

# ----- algorithm -------

s = str(input('enter a string:'))
cnt = 1
for i in s:
    if i == ' ':
        cnt += 1
print('the count of words in string', cnt)

# ------ function ------

s = str(input('enter a string:'))


def ctn_word(s1):
    cnt = 1
    for i in s:
        if i == ' ':
            cnt += 1
    return cnt


print('the count of words in string', ctn_word(s))
