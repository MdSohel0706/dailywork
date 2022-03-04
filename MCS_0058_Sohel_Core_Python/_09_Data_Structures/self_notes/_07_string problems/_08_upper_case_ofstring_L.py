# converting the string to upper case if one character in the string is upper case
'''
CRUD : update
state : string
behaviour : for, if, =

taking user input as string and iterating the string with for loop
using if condition checking whether string have at least one upper case letter
if true then the string will be converted to upper case

'''
# ---  state behaviour -----

string = str(input('enter a string: '))

# ----- behaviour --------

for i in string:
    if i.isupper():
        string = string.upper()
        break

print(string)

# converting the string to upper case if two character in the string is upper case

# ---- state ------

string = str(input('enter a string: '))


# ----- behaviour -----

def upper_case(s):
    cnt = 0
    for i in string:
        if i.isupper():
            cnt += 1
    if cnt == 2:
        s = s.upper()
    return s


print(upper_case(string))

# ----- oops -------


class Upper_case:
    # ------- state -------

    def __init__(self, s, cnt):
        self.s = s
        self.cnt = cnt

    # ------ behaviour ------

    def upper(self):
        for i in string:
            if i.isupper():
                self.cnt += 1
        if self.cnt == 2:
            self.s = self.s.upper()
        return self.s


U = Upper_case(str(input('enter a string: ')),0)
print(U.upper())
