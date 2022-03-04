''''''
'''
# sum of 2 numbers
-------------------
STATE    ==> 1 
BEHAVIOR ==> 2,3

       # 1. Customer input
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

       # 2. Business Logic
result = num1 + num2
       # 3. Give response to user
print("Addition is : ",result)

# FUNCTIONS

Advantages: - Avoids code duplication ==> Code reusability
            - When enhancements are required, 
                        we need to change code only one place 

# Functions:
----------------
f(x) = 2x2+3x+1. Find the value of f(x) when x is 10
f(10) = 2(10*10)+3(10)+1
      = 2(100)+30+1
	  = 200+30+1
f(10) = 231

Find the behavior  of f(x) when x value ranges from -2 to 2
f(-2) = 2(-2*-2)+3(-2)+1  = 3
f(-1) = 2(-1*-1)+3(-1)+1  = 0
f(0)  = 2(0*0)+3(0)+1  	  =	1
f(1)  = 2(1*1)+3(1)+1     = 6
f(2)  = 2(2*2)+3(2)+1     =15

f(x)   = 2x2+3x+1  # Function definition
f(2)               # Function calling by passing value
2(2*2)+3(2)+1      # Function execution
15                 # Function end result 
'''

# REQ: Find sum of 2 numbers
    # I. STATE
"""num1 = int(input("Enter number 1 :"))   # 1. Customer input
num2 = int(input("Enter number 2 :"))

    # II. BEHAVIOR
result = num1 + num2             # 2. Business Logic
print("Addition is : ", result)  # 3. Give response to user
"""               
# Problem with above code
'''
Code duplication == we should achieve ==> Code reusability
'''




