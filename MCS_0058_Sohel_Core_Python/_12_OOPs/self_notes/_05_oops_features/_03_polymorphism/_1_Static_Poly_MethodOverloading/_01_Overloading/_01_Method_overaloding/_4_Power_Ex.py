'''
Created on 13-Jun-2021
@author: madhu
'''
'''Below fucntion can be called in 2 ways
 1. By passing one argument only
 1. By passing two argument only
'''
def get_power(voltage, state='MY_STATE'):
    print("Voltage, State : ",voltage,state)

get_power(10)        # Default
get_power(10, "AP")  # Positional
get_power(state='Karnataka', voltage=10)  # keyword
get_power(voltage=10, state='Telangana')  # keyword

print("----------------------------")

def get_power(voltage, state='state', action='action', type='type'):
    print("VOLTAGE = ", voltage)
    print("STATE   = ", state)
    print("ACTION  = ", action)
    print("TYPE    = ", type)
    print("---------------End of method--------------")

'''
Error function calls:
----------------------
get_power(10,action='HELLO',100)    # Positional argument after keyword argument
get_power()                         # required argument missing
get_power(voltage=5.0, 'dead')      # non-keyword argument after a keyword argument
get_power(110, voltage=220)         # duplicate value for the same argument
get_power(110, actor='NTR')         # unknown keyword argument
'''

print("--------# 1 positional argument----------")
get_power(1000)
get_power(1000, 'X')
get_power(1000, 'X', 'Y')
get_power(1000, 'X', 'Y', 'Z')
get_power('a million', 'brief of life', 'jump')
print("------------------# 2 keyword argument------------------------")
get_power(action="myaction", type="mytype", voltage=1000)  # 2 keyword argument
print("------------------------------------------")
get_power(voltage=1000000, action='VOOOOOM')               # 2 keyword arguments
print("------------------------------------------")
get_power(action='VOOOOOM', voltage=1000000)               # 2 keyword arguments
print("------------------------------------------")
print("------------------------------------------")
get_power(1000, action='Hello World')           # 1 positional, 1 keyword
print("------------------------------------------")

#default arguments
def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")

def pow(x, y, mod=None):
    r = x ** y
    if mod is not None:
        r %= mod
    return r

pow(2, 10)  # valid
pow(2, 10, 17)  # valid
pow(2, 10, mod=17)  # valid
pow(x=2, y=10)  # invalid, will raise a TypeError
pow(2, y=10)  # invalid, will raise a TypeError

#Calculate power of a number using a while loop
base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))

# Python code to demonstrate pow()
# version 1

print("The value of 3**4 is : ", end="")

# Returns 81
print(pow(3, 4))


# Python code to demonstrate pow()
# version 2

print("The value of (3**4) % 10 is : ", end="")

# Returns 81%10
# Returns 1
print(pow(3, 4, 10))


# Python code to discuss negative
# and non-negative cases

# positive x, positive y (x**y)
print("Positive x and positive y : ", end="")
print(pow(4, 3))

print("Negative x and positive y : ", end="")
# negative x, positive y (-x**y)
print(pow(-4, 3))

print("Positive x and negative y : ", end="")
# positive x, negative y (x**-y)
print(pow(4, -3))

print("Negative x and negative y : ", end="")
# negative x, negative y (-x**-y)
print(pow(-4, -3))


base = int(input("Enter base:"))
power = int(input("Enter power:"))
n = 1
for i in range(1,power+1):
    n=base*n
print ("The value of",base,"**",power," is",n)


x = 7
y = 2
z = 5

print(pow(x, y, z))

# positive x, positive y (x**y)
print(pow(2, 2))

# negative x, positive y
print(pow(-2, 2))

# positive x, negative y (x**-y)
print(pow(2, -2))

# negative x, negative y
print(pow(-2, -2))

# Python code to demonstrate naive method
# to compute power
n = 1
for i in range(1, 5):
    n = 3 * n

print("The value of 3**4 is : ", end="")
print(n)

# Python code to demonstrate pow()
# version 1

print("The value of 3**4 is : ", end="")

# Returns 81
print(pow(3, 4))

# Python code to demonstrate pow()
# version 2

print("The value of (3**4) % 10 is : ", end="")

# Returns 81%10
# Returns 1
print(pow(3, 4, 10))
'''
Created on 13-Jun-2021
@author: madhu
'''
'''Below fucntion can be called in 2 ways
 1. By passing one argument only
 1. By passing two argument only
'''
def get_power(voltage, state='MY_STATE'):
    print("Voltage, State : ",voltage,state)

get_power(10)        # Default
get_power(10, "AP")  # Positional
get_power(state='Karnataka', voltage=10)  # keyword
get_power(voltage=10, state='Telangana')  # keyword

print("----------------------------")

def get_power(voltage, state='state', action='action', type='type'):
    print("VOLTAGE = ", voltage)
    print("STATE   = ", state)
    print("ACTION  = ", action)
    print("TYPE    = ", type)
    print("---------------End of method--------------")

'''
Error function calls:
----------------------
get_power(10,action='HELLO',100)    # Positional argument after keyword argument
get_power()                         # required argument missing
get_power(voltage=5.0, 'dead')      # non-keyword argument after a keyword argument
get_power(110, voltage=220)         # duplicate value for the same argument
get_power(110, actor='NTR')         # unknown keyword argument
'''

print("--------# 1 positional argument----------")
get_power(1000)
get_power(1000, 'X')
get_power(1000, 'X', 'Y')
get_power(1000, 'X', 'Y', 'Z')
get_power('a million', 'brief of life', 'jump')
print("------------------# 2 keyword argument------------------------")
get_power(action="myaction", type="mytype", voltage=1000)  # 2 keyword argument
print("------------------------------------------")
get_power(voltage=1000000, action='VOOOOOM')               # 2 keyword arguments
print("------------------------------------------")
get_power(action='VOOOOOM', voltage=1000000)               # 2 keyword arguments
print("------------------------------------------")
print("------------------------------------------")
get_power(1000, action='Hello World')           # 1 positional, 1 keyword
print("------------------------------------------")


