'''
1.Find grade of a student based on below requirement.
marks >= 80  => A+  , 60-79 => A,  50-60=> B, 35-50 => C,  Below 35 FAIL
if  elif elif elif   else
'''
print("----Student Grade----")
# 1. Customer provided input   ==> static,dynamic way
marks = int(input("Enter your marks ::")) # Dynamic way
#marks = 100  # Static way
'''
<= 79 
< 80 BETTER
'''

# Server side validations 0 to 100
# Validate the input data  <0   >100

# 2. Validation logic  ==> i.e, Server side validations
if marks < 0 or marks > 100:
    print("***Please enter correct marks***")
    if marks < 0:
        print("Enter marks 0 or greater than 0")
    elif marks > 100:
        print("Enter marks 100 or less than 100")
else:
    # Business logic
    if marks >= 80:
        print("A+ Grade")
        if marks == 100:
            print("**** Congratulations ***")
    elif marks >= 60 and marks < 80:
        print("A Grade")
    elif marks >= 50 and marks < 60:
        print("B Grade")
    elif marks >= 35 and marks < 50:
        print("C Grade")
    else:
        print("FAIL")
        if marks == 0:
            print("****  SUPER   ****")


'''
Test Scenarios : 
======================
Negative tests:
---------------
S1. Lessthan 0     <0
S2. Greterthan 100 >100

Positive tests:
---------------
S1 : A+ Grade ==>  I. 80   II. >80    III. 100
S2 : A grade  ==>  I. 60   II. 65     III. 79 
S3 : B grade  ==>  I. 50   II. 54     III. 59 
S4 : C grade  ==>  I. 35   II. 41     III. 49 
S5 : Fail     ==>  I. 34   II. 14     III. 0 



'''

'''
if marks >= 0 and  marks <= 100:
    # Business logic
    if marks >= 80:
        print("A+ Grade")
    elif marks >= 60 and marks < 80:
        print("A Grade")
    elif marks >= 50 and marks < 60:
        print("B Grade")
    elif marks >= 35 and marks < 50:
        print("C Grade")
    else:
        print("FAIL")
else:
    print("***Please enter correct marks***")
'''

'''
# Steps to implement code for given requirement
    1. Receive the customer provided input   # STATE* : Here we defined the state
    2. Perform validations                   # server side validations
    3. Implement business logic              # BEHAVIOR* : Implemented code(bus logic) for requirement
'''

'''
# REQ : Find given number is even or odd
in_no = 120 # int(input("Enter number : "))      # 1
if in_no == 0:                             # 2
    print("Please enter no. other than 0")
else:
    if in_no % 2 == 0:                      # 3
        print("Even number")
    else:
        print("Odd number")
'''