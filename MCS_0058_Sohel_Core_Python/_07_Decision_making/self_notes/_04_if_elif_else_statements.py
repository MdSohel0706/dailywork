#Nested if Statement
'''if statement can also be checked inside other if statement. This conditional statement
is called a nested if statement. This means that inner if condition will be checked only
if outer if condition is true and by this, we can see multiple conditions to be satisfied.

Syntax:
if (condition1):
# Executes when condition1 is true
if (condition2):
# Executes when condition2 is true
# if Block is end here
# if Block is end here'''
#--------------------------------------------------------------------------------------------------------------
'''marks =  int(input ("Enter the marks"))
if marks >= 90 and marks <= 100:
    print("A Grade")
elif marks >= 80 and marks <= 90:
    print("b Grade")
elif marks >= 70 and marks <= 80:
    print('c grade')
elif marks >= 60 and marks <= 70:
    print("D grade")
else:
    print("The student fail")'''
#-------------------------------------------------------------------------------------------------------------
'''age = int(input ("Enter the age "))
if age >= 70 and age <= 100:
    print("Old person")
elif age >= 60 and age <= 30:
    print("young people")
elif age >= 18 and age <= 30:
    print("bachelors")
else:
    print("small childern")'''
#-------------------------------------------------------------------------------------------------------------
'''year = int(input ("Enter the year : "))
if(year%400 == 0):
    print("The year is leap year")
elif(year%100 == 0):
    print("This year is not a leap year")
elif(year%4 == 0):
    print ("This year is leap year")
else:
    print("This is not leap year")'''
#----------------------------------------------------------------------------------------------------------------

'''numbers = [i for i in range(0,7)]
print(numbers)
min_value = min(numbers)
max_value = max(numbers)
mid_value = numbers[len(numbers)//2]

value = int(input("enter the value"))

if value == min_value:
    print("the given number is minimum value")
elif value == max_value:
    print("the given number is maximum value")
elif value == mid_value:
    print("the given value is middle value")
else:
    print("normal number")'''
#------------------------------------------------------------------------------------------------------
'''id = int(input('enter the id'))
if id == 101:
    print('satish')
elif id == 102:
    print('venkat')
elif id == 103:
    print('sai')
else:
    print("id not is not matched")
'''
#---------------------------------------------------------------------------------------------------------------
