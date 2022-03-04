

'''
S1 : REQUIREMENT : Print numbers which are divisible by 4 between 0 to 100

S2,S3 :Analysis,Design:
-----------------------
Step1: Take the user input,iterate till upper limit
Step2: Check whether the value divisible by 4 or not
Step3: If True, print the value
'''

# 0 1 2 3 4 5 6 7 8 9 10... 100
print("--------Numbers between 0 to 100---------")
x = 0
while x <= 100:
    if x % 4 == 0:
        print(x)
    x += 1


'''
# S1: REQUIREMENT : Print numbers which are divisible by 
                    either 3 or 8 between 1 to 1000
'''
print("-------------either 3 or 8 between 1 to 1000-------------")
x = 1
while x <= 1000:
    if x % 3 == 0 or x % 8 == 0:
        print(x)
    x += 1



'''
# S1: REQUIREMENT : Print numbers which are 
                    divisible by 5 and 10 between 1 to 100
'''
print("---------either 5 and 7 between 1 to 100-------------")
x = 1
while x <= 100:
    if x % 5 == 0 and x % 10 == 0:
        print(x)
    x += 1

x = 10
y = 20
print(x > y and y < 100)



# Arithmetic, Comparasion, Logical




'''
Print numbers f
1 - 5
2 - 10
3 - 15
4 - 20
5 - 25
6 - 30
'''

