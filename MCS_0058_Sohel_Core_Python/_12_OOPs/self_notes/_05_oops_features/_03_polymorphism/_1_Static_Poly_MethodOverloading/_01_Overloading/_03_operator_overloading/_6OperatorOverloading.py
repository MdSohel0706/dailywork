
class Employee:
    def __init__(xyz, eid):
        pass

    def getdata(xyz):
        pass

madhu = Employee(10)

"EVERYTHING IS AN OBJECT IN PYTHON"
x = int(10)
'''
class int:
    def __init__(self,var):
        self.var = var
    
'''

x = 10 + 20  # ==> obj.__add__(20)

print(x)

list1 = [1,2,3]
list2 = [3,4,5]
print(list1 + list2)  # list1.__add__(list2)
#1 : Observe RHS, LHS parts
#2 : Find what is the expression
#3 : Analyse whether expression is valid or not
#4 : Find the type of operands i.e., int
#5 : Based on operator,call the respective method in that class
     # p1.__add__(p2)
       
 


x = 10 
y = 20
print(x + y) # x.__add__(y)        def __add__(self, obj):

'''
 __add__
 __sub__
 __mul__
 __div__
 
 '''
list1 = [1,2,3]
list2 = [1,2,3]
list3 = [7,8,9]
print(list1 == list2)
print(list1 is list2)
print(list2)
print("Two lists : ",list1+list2+list3)

class Employee(object):
    
    def __init__(self,id):
        self.id= id
        
    def __add__(self,obj):
        result = self.id + obj.id # 10 + 20
        return result
        
madhu = Employee(10)
print("Madhu obj ",madhu)
mani = Employee(20)

print("Mani obj ", madhu)

print("Adding both objects ",madhu + mani)  # madhu.__add__(mani)

'''

https://www.programiz.com/python-programming/operator-overloading
Python operators work for built-in classes. 
But same operator behaves differently with different types. For example, the + operator will, 
perform arithmetic addition on two numbers, merge two lists and concatenate two strings.
Addition
p1 + p2
p1.__add__(p2)
Subtraction
p1 - p2
p1.__sub__(p2)
Multiplication
p1 * p2
p1.__mul__(p2)
Power
p1 ** p2
p1.__pow__(p2)


Less than  p1 < p2   p1.__lt__(p2)

http://www.python-course.eu/python3_magic_methods.php
'''

a = 10
b = 20
print("Sum of a,b is :",a+b)
print("--------------------------------")


name1 = "Madhu"

name2 = "Sudhan"
print("Concat names ",name1+name2)
print("--------------------------------")

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)

p1 = Point(2,3)   
print(p1)      
print("Print object :", p1)

p2 = Point(4,5)                
print("Print object :", p2)

print("--------------------------------")
print("Add 2 objects :", p1 + p2)
print("--------------------------------")
print("Add 2 objects :", p1 - p2)

'''
Operator Overloading Special Functions in Python
Operator              Expression    Internally
============================================================
Addition              p1 + p2        p1.__add__(p2)
Subtraction           p1 - p2        p1.__sub__(p2)
Multiplication        p1 * p2        p1.__mul__(p2)
Power                 p1 ** p2       p1.__pow__(p2)
Division              p1 / p2        p1.__truediv__(p2)
Floor Division        p1 // p2       p1.__floordiv__(p2)
Remainder (modulo)    p1 % p2        p1.__mod__(p2)
Bitwise Left Shift    p1 << p2       p1.__lshift__(p2)
Bitwise Right Shift   p1 >> p2       p1.__rshift__(p2)
Bitwise AND           p1 & p2        p1.__and__(p2)
Bitwise OR            p1 | p2        p1.__or__(p2)
Bitwise XOR           p1 ^ p2        p1.__xor__(p2)
Bitwise NOT           ~p1            p1.__invert__()
'''