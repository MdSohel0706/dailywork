'''
@classmethod
@staticmethod

Decorator : Provides additional functionality for class or method/function
'''
# 1 :print(10)   # one time usage
# 2
''' 
#1 one time usage
print(10)

# 2 or more places
x = 10  
print(x)         XXX ---> print(10)
print(x+100)     XXX ---> print(10+100)
'''


def sum1(num1, num2):
    res = num1 + num2
    return res

sum1(10,20) # No use

#1 one time usage
print("Sum is : ", sum1(10, 20))

#2 two or more places
output = sum1(10, 20)
print("First usage: ", output)
print("Second usage: ", output+24)

def sum2(num1, num2):
    res = num1 + num2
    print("Addition is : ", res)

sum2(10,20)   # Direct function call
n1 = 10
n2 = 20
sum2(n1, n2)
'''
#1 one time usage
print("Sum is : ", sum2(10, 20))

#2 two or more places 
output = sum2(10, 20)
print("First usage: ", output)
print("Second usage: ", output+24)
'''

# IF function has return type
    #1  Single time
print("Type 1 :", sum1(10, 20))  # print(10)
print("Type 1 :", sum1(10, 20) + 100)
    #2 Mulitple times
output = sum1(10, 20)
print(output)   # x = 10 print(x)
print(output + 100)
print(output + 200)

# IF function has no return type
sum1(10, 20)                # We are not expecting function return type

print("------------------Function details------------------  ")

def getdata():
    print("I am in getdata")
    return 100

print("Function call  : ", getdata())
print("Function name  : ", getdata)
print("Function type  : ", type(getdata))
print("Function name  : ", id(getdata))




class Employee:
    pass
print("Class details  ")

print("----Name :", Employee)
print("----Type :", type(Employee))
print("----Type :", id(Employee))

# Concept : We can pass "function name" as an argument to any other function

print("---------Variable concept------")
x = 10
print(x, type(x))   # x.__str__()

x = 10
y = 20
print("Sum function call ", sum1(x, y))
print("Sum function def  ", sum1)

# https://realpython.com/primer-on-python-decorators/

'''
Functions:
============
1. First Class functions
2. Nested Functions
3. Returning Functions
'''
print("----------Function calls------------------")

def foo(bar):
    #print("Output is :", bar + 1)
    return bar + 1
# 1
foo(10) # if print statement is there inside function
# 2
print(foo(10)) # if return stmt exists
# 3
x = foo(10)   # if return stmnt exits and output is being used in 2 or more places
print(x)

print("Comparison :", foo(20) > 3+10)  # functions return a value based on the given arguments.

print("----------Function calls------------------")

'''
                Steps execution:
                1. foo(20) - function call   will get response         ==> 21   
                2. 3+10    - perform arithmetic ops. and give result   ==> 13
                3. compare function response with arithm ops result   ==> 21 > 13  => True
                4. Give result to print function
                
                
                print("Comparision ", 10)      # 0
                print("Comparision ", 10+20)   # 1
                print("Comparision ", 10+20 == 30)   # 2
                print("Comparision ", 10+20 == 10+30)   # 3
                print("Comparision ", foo(10+20) == 10+30)   # 4
'''


def foo2(bar):
    return bar + 1


foo2(2)
print(foo2(3))
print(type(foo2))
print(foo2)

print("---Function calling Chain-----")

def x():
    print("x function")

def y():
    print("y function")
    x()

y()

# 1. FIRST CLASS FUNCTIONS:
print("============1. FIRST CLASS FUNCTIONS=============")

'''
Here foo_func requires function name why because we have used 
the same parameter during function call

X               Y                       Z        
Abdul   <--   Dileep             <--  Kamal                 
            10K
        
foo(bar)           medium(f_name, var)  <==    get_data()
   return bar+1      out = f_name(var)                  functionname -   foo  
                     return out                         args         -   10 
                                                 resp = medium(foo, 10)
                                                 # business logic    
       
'''


print(" *** Without first class function  ***")
# foo - Abdul
# get_data - Kamal

def foo(bar):   # Abul
    return bar + 1

def get_data():  # Kamal
    res = foo(100)  #  We are calling other function from our function
    print("Val from foo is : ", res)

get_data()

print(" *** With first class function  ***")

def foo(bar):    # Abdul
    return bar + 1

def mediator(foo_func, val):  # Dileep
    output = foo_func(val)  # foo(100)
    return output

def get_daata():  # Kamal
    res = mediator(foo, 100)
    print("Val from foo is : ", res)

get_daata()

print("------------------------------------")
