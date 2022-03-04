# Guest is expecting water and coffee.End result is Satisfied or Not Satisfied
print("------Guest program-----")
water = False
coffee = True
if water and coffee:
    print("Satisfied !")
else:
    print("Not Satisfied !")

if 'Hello World':
    print("Welcome to Python")
else:
    print("Welcome to other language")




'''
REQUIREMENT : Display student result(Pass/Fail) based on his aggregate marks
              If marks are greater than or equal to 35 display result as  "PASS"
              else display as "FAIL"
'''
print("-----Student result------")

# STATE     : Customer(End user) provided input
# BEHAVIOR  : Implementation of cust. req.  (Business logic)

# State    : student provided marks
# Behavior : Display student result(Pass/Fail)
             # To implement behavior - bus logic impl
#                                       ==> marks >= 35 PASS else FAIL

marks = 23  # State   #customer input data (student is end user)
# Behavior    # Implementing Business logic
if marks >= 35:
    print("PASS")
else:
    print("FAIL")


'''
As per SSC exam board,below are the grades
marks >= 90 and marks < 100 ==> 'DISTINCTION'
marks >= 60 and marks < 90  ==> 'First class'
marks >= 50 and marks < 60  ==> 'Second class'
marks >= 35 and marks < 50  ==> 'Third class'
marks < 35                  ==> 'Fail'
'''
# STATE
marks = 45  # customer/user provided input (student)
# BEHAVIOR
if marks >= 90 and marks < 100:
    print("DISTINCTION")
elif marks >= 60 and marks < 90:
    print("First class")
elif marks >= 50 and marks < 60:
    print("Second class")
elif marks >= 35 and marks < 50:
    print("Third class")
else:
    print("Fail")

