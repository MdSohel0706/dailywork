'''
# In JAVA

def product(a, b):
    res = a * b
    print(res)
def product(a, b, c):
    res = a * b * c
    print(res)
product(10,20)  # 7th line
product(10,20,30) # 10th line
'''

# First product method.
# Takes two argument and print their
# product
def product(a):
    pass

def product(a, b):
    res = a * b
    print(res)

product(10)  # ERROR

# We can call only in one way,by passing both arguments
product(3, 4) # Positional args
product(a = 3, b = 4) # Keyword args
product(b = 4, a = 3) # Keyword args

print("Function product : ",product)
# Second product method
# Takes three argument and print their
# product

def product(a, b, c = 1):
    p = a * b * c
    print(p)

print("Function product : ",product)
# Uncommenting the below line shows an error    
product(4, 5)
# This line will call the second product method
product(3, 4)
product(4, 5, 5)


def sum(a, b, c = 0):
    return a + b + c

print("Sum :",sum(10, 20))

# In JAVA

def product(a, b):
    res = a * b
    print(res)
def product(a, b, c):
    res = a * b * c
    print(res)
product(10,20)  # 7th line
product(10,20,30) # 10th line
"""

# First product method.
# Takes two argument and print their
# product
def product(a):
    pass

def product(a, b):
    res = a * b
    print(res)

product(10)  # ERROR

# We can call only in one way,by passing both arguments
product(3, 4) # Positional args
product(a = 3, b = 4) # Keyword args
product(b = 4, a = 3) # Keyword args

print("Function product : ",product)
# Second product method
# Takes three argument and print their
# product

def product(a, b, c = 1):
    p = a * b * c
    print(p)

print("Function product : ",product)
# Uncommenting the below line shows an error
product(4, 5)
# This line will call the second product method
product(3, 4)
product(4, 5, 5)


def sum(a, b, c = 0):
    return a + b + c

print("Sum :",sum(10, 20))


#examples:
class product():
    def product(self,x,y,z):
          a=x*y*z
          print(a)
product(3,5,6)

from itertools import product

if _name_ == "_main_":
    arr1 = [1, 2, 3]
    arr2 = [5, 6, 7]
print( list(product(arr1, arr2)) )
"""