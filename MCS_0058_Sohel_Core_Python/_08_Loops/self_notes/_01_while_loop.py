#loops in python:

'''Python programming language provides following types of loops to handle looping
requirements. Python provides three ways for executing the loops. While all the ways
provide similar basic functionality, they differ in their syntax and condition checking
time.'''


# While Loop:

'''1. In python, while loop is used to execute a block of statements repeatedly until a
given a condition is satisfied.
2.And when the condition becomes false, the line
immediately after the loop in program is executed.'''

#while loop examples

'''count = 0 #state
while (count < 3): #condition
    count = count+1 #increment
    print (count)''' #business logic

#----------------------------------------------------------------------------------------------------------------------
'''count = 10;
while (count > 5):
    count = count-1
    print(count)'''

#--------------------------------------------------------------------------------------------------------------------------

# Print numbers from 1 to 10

'''num = 1             # state
while num <= 9:     # condition check each iteration(business logic)
    num = num + 1   #  increment
    print(num)      # part behaviour'''
#----------------------------------------------------------------------------------------------------------------
# print 1,2,3,4,5,......10
"""num = 0
while num <= 9:
    num = num + 1
    print(num,end=' ')
print() """
#----------------------------------------------------------------------------------------------------------------
# even number and odd numbers

"""num = 0
while num <= 10:
    num = num + 1
    if num %2 == 0:
        print("even number",num)
    else:
        print("odd number",num) """
#--------------------------------------------------------------------------------------------------------------------
# even number and odd numbers
"""
num = 0
while num <= 10:
    num = num + 1
    if num %2 == 0:
        print("even number",num)
    else:
        print("odd number",num) """
#----------------------------------------------------------------------------------------------------------------
"""
num = 0
while (num <=11):
    num = num + 1
    if num%3==0 :
        print(num,"divisible by 3")
"""
#------------------------------------------------------------------------------------------------------------------
# print numbers divisible by 3 and 5
"""num = 0
while num <= 100:
    num = num + 1
    if num % 3 == 0 and num % 5 == 0:
        print(" 3 and 5 divisibles are",num) """
#------------------------------------------------------------------------------------------------------------------------

# print numbers 20 to 40
'''a=20                     # state
while a <=40:            # defining conditional
    print(a)             # behaviour
    a+=1                 # increment'''

"""
a = int(input("enter a number"))
b = int(input("enter b number "))
if a < b:
    while a <= b:
        if a % 2 == 0:
            print(a)   """
#---------------------------------------------------------------------------------------------------------------------
# numbers between the even numbers
'''num1 = int(input("enter num1"))    # state, user input
num2 = int(input("enter num2 "))   # state   , user input
while num1 < num2:                 # defining condition (comparision num1 and num2)
    if num1 % 2 == 0:              # business logic
        print(num1)                # behaviour
    num1 = num1 +1                 # increment
print("-------------")
print("----end -----------")'''
#-------------------------------------------------------------------------------------------------
# odd numbers
'''num1 = int(input("enter number1"))
num2 = int(input("enter number2"))
while num1 <= num2:
    if num1%2 == 1:
        print("odd number is",num1)
    num1 +=1
print('------end--------')'''

#--------------------------------------------------------------------------------------------------------
# print 1 to 10
'''print("---------------------print 1 to 10----------------")
num = 1
while num <= 10:
    print(num, end=' ')
    num+=1
print('\n'"-----end ---------")'''
#--------------------------------------------------------------------------------------------------------------------------

# print 10 to 1
'''print("---------------------print 10 to 1----------------")
num = 10
while num >= 1:
    print(num, end=' ')
    num-=1
print('\n'"-----end ---------")'''

#--------------------------------------------------------------------------------------------------------------------------------------
# 8 multiples
'''print('---------------8 multiples------------------')
num = 1
while num <=100:
    if num % 8 == 0:
        print(num)
    num+=1
print("---------end--------------")'''
#--------------------------------------------------------------------------------------------------------------------------

#prime numbers
'''print("---------------prime numbers  between 1 to 100--------------")
num = 2
while num <= 100:
    if num%2 != 0 and num%3 != 0 and num%5 != 0:
        print(num)
    num+=1'''

#----------------------------------------------------------------------------------------------------------------------------------
