''''''
'''
# Types 
1. Predefined Functions   : print() id() type()   int float str list tuple dict set
2. User defined Functions : Programmer defined functions 
'''
x = 10
'''
x  <==> variable 
10 <==> value
=  <==> Assignment operator 
'''
print("Value of x : ", x)
'''
Function definition syntax :    def <func_name> () :    # f(var)
                                  # def sum(n1, n2):    # f(x)   

n1,n2 are parameters not variables
'''

# Requirement : Sum of 2 given numbers

# A. With out functions
        # I. STATE
num1 = 10
num2 = 20
        # II. BEHAVIOR
result = num1 + num2
print("Addition is : ", result)


print("-----------Using functions--------")
# B. With Functions
        # I. STATE
num1 = 10
num2 = 20
        # II. BEHAVIOR

# Function definition
def sum(n1, n2):       # function signature
    result = n1 + n2   # function body
    print("Addition is : ", result)

# Function calling
sum(num1, num2)
sum(10, 20)




'''
1. Function definition:
                                def sum(n1, n2):
                                    result = n1 + n2 
                                    print("Addition is : ", result)

    -   Function signature:
                                def sum(n1, n2):

    -  Function body/implementation
                                result = n1 + n2 
                                print("Addition is : ", result)

'''
