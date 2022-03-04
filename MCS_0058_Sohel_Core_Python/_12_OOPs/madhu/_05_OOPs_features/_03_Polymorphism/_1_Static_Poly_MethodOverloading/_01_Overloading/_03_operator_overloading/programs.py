# https://www.programiz.com/python-programming/operator-overloading
# https://www.geeksforgeeks.org/operator-overloading-in-python/

# Python program to show use of  + operator for different purposes.

print(1 + 2)   # 1.__add__(2)  obj.method(arg)

print("Geeks" + "For")  # "Geeks".__add__("For")

print(3 * 4)   # 3.__mul__(4)

print("Geeks" * 4)   # "Geeks".__mul__(4)

x = int(10)
x = 10
#x.__add__()
y = 20
print(x+y)  # x.__add__(y)
print(10 == 20) # 10.__eq__(20)

'''
class Employee(object):
    def __init__(self,sal):
        self.sal = sal

madhu = Employee(1000)
kiran = Employee(2000)
print(madhu+kiran) # madhu.__add__(kiran)
'''
# With Operator overloading with +
class Employee:
    def __init__(self,sal):
        self.sal = sal

    # adding two objects
    def __add__(self, obj):
        return self.sal + obj.sal  # ==> 1000 + 2000  ==> 1000.__add__(2000)

madhu = Employee(1000)
kiran = Employee(2000)
print("Adding 2 emp objects ",madhu + kiran)   # madhu.__add__(kiran)

# With Operator overloading with gt >=

class Student(object):

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, obj):
        if(self.marks >= obj.marks):  # 25 > 32 ==>25.__gt__(32)
            return True
        else:
            return False

madhu = Student(25)
prakash = Student(32)
if(madhu > prakash):  # madhu.__gt__(prakash)
    print("Madhu got marks greater than Prakash")
else:
    print("Prakash got marks greater than Madhu")

list1= list([1,23])


x = 10
print(x)  # x.__str__()

class Employee: # class Employee(object)

    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

madhu = Employee(10,'MadhuN',10000)
print(madhu)  # ==> madhu.__str__() # It will give only address of variable

class Employee(object):

    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

    def get_emp_details(self):
            print("Employee Details are : ",self.id,self.name,self.sal)

    def __str__(self):  # Method overriding
        obj = str(self.id)+" || "+self.name+" || "+str(self.sal)
        return obj

madhu = Employee(100,'MadhuN',4000)
print("Madhu object address :", madhu)  # madhu.__str__()

li = [1,2,3,4]
print(li) # li.__str__()

# madhu.get_emp_details()

print("----------------------------------")
# madhu.__getattribute__()
print("Madhu hash val ",madhu.__hash__())
print("Madhu obj :",madhu)  # madhu.__str__()


'''
str vs repr
init vs new
object class in detail


'''

list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2)   # list1.__add__(list2)
print(list1 * 3)       # list1.__mul__(3)

x = 10

#list1.append()



class Employee(object):

    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

    def __add__(self, other):
        return self.sal + other.sal

madhu = Employee(100,'MadhuN',15000)
ashok = Employee(102,"Ashok B",20000)
print(madhu + ashok)  # madhu.__add__(ashok)

