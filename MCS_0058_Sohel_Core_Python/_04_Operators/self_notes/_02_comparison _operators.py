#Comparison Operators:
"""Comparison of Relational operators compares the values. It either returns True or
False according to the condition."""
"""> Greater than: True if the left operand is greater than the right x > y
< Less than: True if the left operand is less than the right x < y
== Equal to: True if both operands are equal x == y
!= Not equal to – True if operands are not equal x != y
>= Greater than or equal to True if the left operand is greater than
or equal to the right
x >= y
<= Less than or equal to True if the left operand is less than or
equal to the right
x <= y"""

"""a = 13
b = 33
# a > b is False
print(a > b)
# a < b is True
print(a < b)
# a == b is False
print(a == b)
# a != b is True
print(a != b)
# a >= b is False
print(a >= b)
# a <= b is True
print(a <= b)"""\

#print even numbers using comparison operator
"""numbers = [1,2,3,4,5,6,7,8]

for i in numbers:
    if i % 2 ==  0:
        print(i)

list1 = [i for i in numbers if i % 2 == 0]
print(list1)

n = 0
while n < len(numbers):
    if numbers[n] % 2 == 0:
        print(numbers[n])
    n = n + 1"""

list1 = ["satish","venkat","madhukar","kiran"]
list2 = ["satish","venkat","madhukar","kiran","sam"]
if(list1 < list2 ):
    print("Result :","True")
else :
    print("Result :","False")
