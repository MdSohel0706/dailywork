# finding length of the given string
"""
CRUD : Retrieval
state : string
behaviour : for , = , += , < , while,
"""

name = 'satish'

# -------- Built in ----------
print('the length of string is', len(name))

# ------- algorithm -------

count = 0
for i in range(len(name)):
    count += 1
print('the length of string is:', count)

# ---- 0r -----

count = 0
i = 0
while i < len(name):
    count += 1
    i += 1
print('the length of string is:', count)


# -----  functions -----

def len_of_str(x):
    C = 0
    k = 0
    while k < len(x):
        C += 1
        k += 1
    print('the length of string is:', C)


len_of_str('satish')
