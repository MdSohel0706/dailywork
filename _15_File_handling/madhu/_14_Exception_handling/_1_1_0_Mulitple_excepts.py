'''
# Without EH
print("Start of program")
x = int(input("Enter numerator value :"))   # ValueError
y = int(input("Enter denominator value:"))  # ValueError
li = [1,2,3,4]
print(li[3])   # IndexError
print("Division :", x / y)  # ZeroDivisionError
print("Hello world")
print("---------------------------------")
'''

# Handling multiple exceptions
'''
HANDLING MULITPLE EXCETIONS

To handle multiple exceptions,write mulitple except blocks
Below code is not proper 
'''
print("Start of program")
try:
    # print("----While Exception handling----")
    x = int(input("Enter numerator value :"))  # ValueError
    y = int(input("Enter denominator value:"))
    li = [1, 2, 3, 4]
    print("List val:", li[2])  # IndexError
    print("Division :", x / y)  # ZeroDivisionError
    print("Hello world")
    print("---------------------------------")
except Exception as e:
    print("** Error occured :  **", e)
'''
except:
    print("** Error occured :  **")
    
    5L Water <-- 1L 2L 2.5L 3L 3.5L 4L 5L
    
    Animal  a = Tiger()   5L CAN <---- 2L Water
    Animal  a = Lion()
    Animal  a = Cat()
    Animal  a = Dog()
'''