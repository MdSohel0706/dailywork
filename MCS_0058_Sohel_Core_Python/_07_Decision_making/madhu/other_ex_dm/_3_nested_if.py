
# STATE    datatypes int  float bool       string     list tuple dictionary set
                    # eid sal   is_female  name
# BEHAVIOR

result = "PASS"  # input("Enter your result")
print(id(result),type(result))
#if result > 10:
#    pass

result = 'XYZ'

if result == 'PASS':
    print("Passed")
elif result == 'FAIL':
    print("Failed")
elif result == 'WITHHOLD':
    print("Result is on hold")
else:
    print("Invalid input")




x = 10
sal = 10.5
is_active = False
name = 'Madhu'

print(id(x),type(x))
print(id(sal),type(sal))
print(id(is_active),type(is_active))
print(id(name),type(name))






'''
REQUIREMENT : Display student result(Pass/Fail) based on his marks for a specific subject
              If marks are greater than or equal to 35 display result as  "PASS"
              else if marks less than 35 and gt 0 display as "FAIL" else if marks are 0
              then display as ABSENT.
              # Conditions : marks >= 0 and <= 100. 
              

Input data (STATE)    : marks
Bus logic  (BEHAVIOR) : If marks are greater than or equal to 35 display result as  "PASS"
                        else if marks less than 35 and gt 0 display as "FAIL" else if marks are 0
                        then display as ABSENT
End Req              :  Display student result(Pass/Fail/Absent) based on his marks for a specific 
                        subject
'''
# STATE
print("-----Student result2 ------")

# Approach 1 :
marks = int(input("Enter your marks :")) # providing data dynamically
'''
# Validation  Madhu MadhuNettem123!@#  Madhu@123!#Nettem
if marks > 100 or marks < 0:  #mutually exclusive
    print("***Please enter valid marks***")
else:
'''
# Server side validations
if marks < 0 or marks > 100:
    print("Please enter valid marks between 0 and 100")

# Business Logic
if marks >= 35 and marks <= 100:   # Behavior  # Business logic
    print("PASS")
elif marks < 35 and marks > 0:
    print("FAIL")
elif marks == 0:
    print("ABSENT")

# Approach 2 :
marks = int(input("Enter your marks :")) # providing data dynamically
'''
# Validation  Madhu MadhuNettem123!@#  Madhu@123!#Nettem
if marks > 100 or marks < 0:  #mutually exclusive
    print("***Please enter valid marks***")
else:
'''
# Server side validations
if marks < 0 or marks > 100:
    print("Please enter valid marks between 0 and 100")
else:
    # Business Logic
    if marks >= 35 and marks <= 100:   # Behavior  # Business logic
        print("PASS")
        if marks >= 90 and marks <= 100:
            print("*** DISTINCTION  ***")
            if marks == 100:
                print("---Showstopper----")
        elif True:
            pass
        elif True:
            pass
        elif True:
            pass

    elif marks < 35 and marks > 0:
        print("FAIL")
    else:
        print("ABSENT")
