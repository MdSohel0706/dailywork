#if-statement:

'''If the simple code of block is to be performed if the condition holds true then if
statement is used. Here the condition mentioned holds true then the code of block
runs otherwise not.

if condition:
# Statements to execute if
# condition is true
'''
#--------------------------------------------------------------------------------------------------------------
# if statement example
'''if 10 > 5:
    print("10 greater than 5")
    print("Program ended")'''
#--------------------------------------------------------------------------------------------------------------
'''if -10:
    print('-ten value is true')'''
#--------------------------------------------------------------------------------------------------------------------
''''if 5==5:
    print('condition is true')'''
#----------------------------------------------------------------------------------------------------------
'''a = 12
b = 10
if a > b and a > b:
    print("hello satish")
    print("The statement is not correct")'''
#------------------------------------------------------------------------------------------------------------
#In the if statement both conditions are true it returns true
# if one condition is true another condition is false it returns false
#In the if statement checks n number of statements these conditions validate
#-------------------------------------------------------------------------------------------------------------
'''x = "satish"
y = "venkat"
if x < y:
    print ("validate statement")'''
#------------------------------------------------------------------------------------------------------------------
'''a = 3.78
b = 45.76
if a != b:
    print("venkat is CSE")'''
#-------------------------------------------------------------------------------------------------------
'''a  = 12+65-45*67/56
b  = 13+64-45*67/56
if a==b:
    print("condition is true")'''
#-------------------------------------------------------------------------------------------------------------
'''if set((10,32,43)):
    print("true")
    if set():
        print("false")'''

#---------------------------------------------------------------------------------------------------------------
'''id = int(input("Enter the id :"))
if id==201:
    print("satish")
if id==202:
        print("venkat")'''
#-----------------------------------------------------------------------------------------------------------------
"""a = [1,2,3,3,5]
b = [6,7,8,9,10]
if(a < b):
    print("True")

list1 = ["apple","mango","cherry","graphs"]
list1 = ["rose","roses","flowers","redroses"]
if(b > a):
    print("True")

x = {12,32,45}
y = {23,34,44}
print(x + y) #TypeError: unsupported operand type(s) for +: 'set' and 'set'
if(x < y):
    print("True")"""

"""x = (23,34,45)
y = (23,34,45)
z = (23,34,45)
print(x + y)
if(x == y == z):
    print("true")
"""

a = "12323,32424,43434,5453456"
b = "545353,5435345,34434544"
print("Adding the values:",(a+b))
if (a < b):
    print("True")