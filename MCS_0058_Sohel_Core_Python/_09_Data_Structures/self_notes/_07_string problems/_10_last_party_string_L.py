# Removing last party of the string by taking a character as the input from user

'''
CRUD : update
state : string
behaviour :
'''

# ----- builtin --------

string = 'Success is not final, failure is not fatal'
print(string)
char = str(input('enter a character from where you want to skip:'))
ns = string.rsplit(char, 1)
print('the new string is :', ns[0])

# ---- algorithm ----


string = 'satish'
char = str(input('enter a character:'))
li = []
for i in range(len(string) - 1, -1, -1):
    if string[i] == char:
        li.append(string[:i])
        break
for i in li:
    print(i, end=' ')
    print('')

# ------ function -------

string = 'satish'
char = str(input('enter a character:'))


def last_part():
    for i in range(len(string) - 1, -1, -1):
        if string[i] == char:
            li.append(string[:i])
            break
    return li


for i in li:
    print(i, end=' ')
