# True ==> non-zero non None
# False ==> zero    None
is_active = True
is_perm = False
'''
Water and Coffee
---------------
True and True*   = True
True and False*  = False
False* and True   = False
False* and False  = False

Coffee or Tea:
----------------
True* or True = True
True* or False = True
False or True* = True
False or False* = False

True --> nonZero              nonNone 
         10 -10 10.4 -3.4     'Hello' [1,2,3] (1,2,3) {1:1,2:2} {1,2,3}
False --> 0 None              '' [] ()  {} {}


Telugu and Hindi and English
True       True      False    - False
False*  

BTech final semester  2 subjects 

MM or M1 
True*  True      -- True
True*  False     -- True
False True*       -- True
False False*      -- False 


'''

print("Arithmetic :", 10 + 20)
print("Relational :", 10 >= 20)
print("10 and 20 :", 10 and 20)  # 20 True and True --> True
print("10 and 0  :", 10 and 0)   #  0 True and False --> False
print("0 and 20 :", 0 and 20)    #  0 False and True --> False
print("0 and 0 :", 0 and 0)      #  0 False and False --> False
print("10 or 20 :", 10 or 20)
print("10 or 0 :", 10 or 0)
print("0 or 20 :", 0 or 20)
print("0 or 0 :", 0 or 0)
print("Membership :", 10 in [10, 20, 30])
print("Identity    :", 10 is 10)



'''
Arithmetic ops: +-*/ // %       ==> 0 / nonzero 
Relational ops: > >= < <= == != ==> True/False
Assignment ops:                     x = 10  x = -10.4
                                    x = 0   x = None
Logical  ops   :                ==> True/False
Bitwise       :                 ==> 0 or 1   False/True
Membership    : in not in       ==> True/False
Identity      : is is not       ==> True/False

'''

'''
1. Single condition     : 1 ==> if 


2. Multiple conditions  : 2 ==> if else
                          3 ==> if elif else            # if   else if    else 
                          4 ==> if elif elif else
                          5 ==> if elif elif elif else

3. nested conditions    : nested if 

                10th exam   
                -----------
L1:            1. PASS                            2. FAIL 
L2:         1.continue     2. disc.           1. retry    2. stop 
L3:    1.Inter   2.Diploma        
L4:  1.MPC  2. BiPC
L5:        1.Govt  2.Pvt

'''
'''
S1 : REQUIREMENT : If user entered value is 20, 
                   then print  "Welcome to Python World" message

S2:  Functional Analysis
     Technical Analysis

S3: Design

Step1 : Take the user input
Step2 : Compare the customer input with given value
Step3 : If True, print the message "Welcome to Python World"

S4: Development

if <condition>:
    block of statements
'''
print("----------if---------------")
# S4: DEVELOPMENT
# Business logic implementation
in_no = 20 # 20 30 40 50 60 100 0
if in_no == 20:
    print("Welcome to Python World")
# S5 : Testing
# code execution

# True Cases
'''
Condition : Success ==> True  nonZero nonNone
            Failure ==> False Zero    None
 True    / False 
 Non 0   / 0  
 nonNone / None
1. Single condition : if 
'''
# arithmetic
if 10+20:  # 30
    print("Successfully executed 10+20")  # Indentation

if True:
    print("True condition")

if False:
    print("False condition")

if not False:
    print("Print False condition")


if True or False:
    print("OR - condition ")

if True and True:
    print("AND - condition")

if 0:
    print("Value 0")
if None:
    print("Value None")
if not 0:
    print("Value 1")
if not None:
    print("Value not None")

if 10-20:
    print("Addition is success")

if 10 < 20:
    print("End of the program")
