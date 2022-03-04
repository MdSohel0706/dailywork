

# Function categories
''''''
'''
1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type

T T 
T F
F T
F F
'''

# Sum functionality

print("------------CAT 1 -------------------")
# 1st -> T T :: Function with parameters, with return type
num1 = 10
num2 = 20

def sum(n1, n2):
    res = n1 + n2
    return res

output = sum(num1, num2)
print("Addition is : ", output)


print("------------CAT 2 -------------------")

# 2nd -> T F :: Function with parameters, without return type

num1 = 10
num2 = 20

def sum(n1, n2):
    res = n1 + n2
    print("Addition is : ", res)

sum(num1, num2)
print("Second cat : ", sum(num1, num2))

print("------------CAT 3 -------------------")


# 3rd --> F T :: Function without parameters, with return type

def sum():
    n1 = 10
    n2 = 20
    res = n1 + n2
    return res

output = sum()
print("Addition is : ", output)

print("------------CAT 4 -------------------")

# 4th  --> F F  :: Function without parameters, without return type

def sum():
    n1 = 10
    n2 = 20
    res = n1 + n2
    print("Addition is : ", res)

sum()
print("Cat 4 : ", sum())


x = 10.5
print(int(x))