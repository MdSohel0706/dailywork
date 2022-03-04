# program to check whether a string starts with specified characters

'''
CRUD : Retrieval
state : string
Behaviour : if, ==

Taking the one string and one character as the user input and using the condition print true or false

'''

# ---- algorithm -----
# ---- state ----
string = str(input('enter a string: '))
char = str(input('enter a character to check string started with this character: '))
# ----- Behaviour -----
if string[0] == char:
    print('patter matches', True)
else:
    print('pattern matches', False)

# ---- function ----
# ----- state ----
string = str(input('enter a string: '))
char = str(input('enter a character to check string started with this character: '))


# ---- behaviour ----
def start_spec(s, c):
    if s[0] == c:
        return True
    else:
        return False


print(start_spec(string, char))
