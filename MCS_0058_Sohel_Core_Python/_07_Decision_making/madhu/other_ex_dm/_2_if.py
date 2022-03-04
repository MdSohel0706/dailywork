'''
True  ==> True NonZero non None
False ==> False Zero None
'''
a = 15
print(a)
print("Is equal ?",a == 10)
print("Is equal ?",a != 10)
# Final output value : number boolean string list tuple dict set None
# Operation : anything ==> Final output value
x = 10
'''
x = 10+20+30+40
  = 30+30+40
  = 60+40
  = 100
'''
print("----True conditions----")
if True:
    print("Yes it is True")
if -10:
    print("Value is -10")
if not None:
    print("Yes it is not None")
if 'Madhu':
    print("Value is Madhu")
print("----False conditions----")
if False:
    print("Cant print False")
if 0:
    print("Cant print 0")
if None:
    print("Cant print None")
'''
if None{
    print("Cant print None");
    }
'''
print("----False conditions----")
a = 30
if a > 20:
    print("Value of A is :",a)
    print("Line no 43")
print("End of program")

a = 10
b = 20
if a+b >= 30:
    print("Res is : ",a+b)
    print("Addition completed")
print("End of program")

print("----")







a = 15
print("Hello")
if a > 10 or a < 5:   # True, 10, -5, 'Madhu', [1,2,3], (1,2,3), {1:1,2:2}, {1,2,3}  False, 0, None
    print("Condition is satisfied")
    print("Welcome to Python World")
print("Thank you")

# if 50 examples
a = 10
b = 20
print("Arithmetic operators")
if a+b == 30:
    print("Result is 30")










