
"""
print("Hello World")
x = 10  # int(10) --> Int(10)
print(x)
print(x, type(x))
list1 = [1,2,3]
print("List data : ", list1)

def get():
    print("Function get()")
    #....

print("Function name :", get)  # Function name    x = 10   get = <func addr>
get()  # Function call

# print("Employee address : ",Employee)
"""

'''
Here python will load the class Employee and provides memory for class body'''
"""
class Employee:
    def __init__(self, eid, name, sal, adddr):
        print("Self address  ", self)
        self.eid = eid
        self.name = name
        self.sal = sal
        self.adddr = adddr

    def get_e_info(self):
        print("Employee details are : ", self.eid, self.name, self.sal,self.adddr)

print("Employee address : ", Employee)

madhu = Employee(100, 'Madhu Nettem', 15000, {'hno':12,'area':'BLR'})  # object creation
madhu.get_e_info()"""
'''
Step1 : 2 parts : 
             I. Employee  
            II. (100, 'Madhu Nettem', 15000)
Step2 : Python will check and find the address of Employee
Step3 : First python creates empty object of Employee class
        Employee class __init__ method will be called, passes 
                1. Address of empty object to self parameter         ==> self
                2. the tuple of arguments will be passed to remaining parameters  ==> (eid, name, sal) 
Step4 : Data passes to local variables (eid, name, sal)               
Step5 : self.eid = eid 
        LHS eid = instance variable
        RHS eid = local variable 
        ==> Local variable eid data,we are setting to instance variable 
        
        self.name = 'Madhu Nettem'
        self.sal = '15000'

        - Empty object will be created by python and gives to self
        - __init__ method helps to initialize the STATE of object(instance)


'''
"""
print("Madhu object : ", madhu)
madhu.get_e_info()

# string list tuple dictionary set
msg = 'Hello world'  # STATE
msg.capitalize()     # BEHAVIOR
list1 = [1,2,3,4,5]  # STATE
list1.append(10)     # BEHAVIOR


# STATE
item_id = 1001
name = 'Chocolate'
price = 15


def get_final_price(i_id, c_name, c_price):
    if c_price <= 5:
        disc = 5*10/100
        final_price = c_price - disc
        print("Final price : ", final_price)
    elif c_price >=5 and c_price <= 10:
        10

get_final_price(item_id, name, price)"""

"""
class Student:

    #STATE
    def _init_(self, name, id, percentage):
        self.name = name
        self.id = id
        self.percentage = percentage

    def get_details(self):
        print(self.name, ' id is : ', self.id)
        print('student name is : ', self.name)
        print(self.name, ' percentage is : ', self.percentage)


student1 = Student('mike', '101', '85%')
student1.get_details()

student2 = Student('john', '102', '70%')
student2.get_details()
"""

"""
class Employee(object):

    # STATE
    def _init_(self, name, eid, salary):
        self.name = name
        self.eid = eid
        self.salary = salary

    # BEHAVIOR
    def get_details(self):
        print('employee name is : ', self.name)
        print(self.name, ' id is : ', self.eid)
        print(self.name, ' salary is : ', self.salary)


e1 = Employee('venkat', '123', 10000)
e1.get_details()
e2 = Employee('satish', '456', 20000)
e2.get_details()
"""
"""
class Square:

    #STATE
    def _init_(self, length):
        self.length = length

    #BEHAVIOR
    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


s = Square(20)
print('area of square is : ', s.area())
print('perimeter of square is : ', s.perimeter())
"""
"""
class Rectangle:

    #STATE
    def _init_(self, length, width):
        self.length = length
        self.width = width

    #BEHAVIOR
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.width + self.length)


r1 = Rectangle(20, 30)
print('area of rectangle is : ', r1.area())
print('perimeter of rectangle is : ', r1.perimeter())
"""

"""
class Student:
    def __init__(self, student_id,student_name,student_age,student_phone_number):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_phone_number = student_phone_number

        # BEHAVIOR

    def get_details(self):
        print("Enter the student id :",self.student_id)
        print("Enter the student name :",self.student_name)
        print("Enter the student age :",self.student_age)
        print("Enter the student phone_number :",self.student_phone_number)

print("Enter the First Student Details :")
student1 = Student(101,"satish",23,"9656736465")
student1.get_details()

print("Enter the Second Student Details :")
student2 = Student(102,"venkat",27,"8956736465")
student2.get_details()
"""
"""
class Mobile:

    # 1. STATE
    def _init_(self, brand_name, m_name, m_price):
        self.brand_name = brand_name
        self.m_name = m_name
        self.m_price = m_price

    # 2. BEHAVIOR
    def get_info(self):
        print("Mobile details are ", self.brand_name, self.m_name, self.m_price)

m_details = Mobile("Realme", 'Realme GT', 25000)
m_details.get_info()
"""
"""
class Company:
   #State
    def _init_(self , c_name,c_hq,c_size,c_tbranch):
     self.c_name=c_name
     self.c_hq = c_hq
     self.c_size=c_size
     self.c_tbranch=c_tbranch
 #Behavior
    def get_info(self):
     print("Company information    ", self.c_name, self.c_hq, self.c_size,self.c_tbranch)

c_info=Company("Grab","USA",1001,5)     #obj creation
c_info.get_info()    #calling the method
"""
"""
class AC:

    #State
    def _init_(self,ac_brand,ac_mno,ac_price):
        self.ac_brand=ac_brand
        self.ac_mno=ac_mno
        self.ac_price=ac_price
 #Behavior
    def get_info(self):
     print("info of AC  " ,self.ac_brand,self.ac_mno, self.ac_price)
ac_info=AC("Voltas","1.5 Ton" , 34000)
ac_info.get_info()

"""
"""
class Car:

    #State
    def _init_(self,c_name,c_mno,c_price):
        self.c_name=c_name
        self.c_mno=c_mno
        self.c_price=c_price
 #Behavior
    def get_info(self):
     price=self.c_price + self.c_price*10/100
     print("info of Car  " ,self.c_name,self.c_mno, price)
c_info=Car("FORTUNER","1.5MT" , 3400000)
c_info.get_info()
"""
"""
class Fan:

    #State
    def _init_(self,f_bname,f_mno,f_price,f_clr):
        self.f_bname=f_bname
        self.f_mno=f_mno
        self.f_price=f_price
        self.f_clr=f_clr
 #Behavior
    def get_info(self):
     price=self.f_price - self.f_price*10/100
     print("info of Fan  " ,self.f_bname,self.f_mno, price,self.f_clr)
f_info=Fan("USHA","1ght" , 2400,"blue")
f_info.get_info()
"""
"""
  class Lappi:

    #State
    def _init_(self,l_bname,l_mno,l_price,l_clr):
        self.l_bname=l_bname
        self.l_mno=l_mno
        self.l_price=l_price
        self.l_clr=l_clr
 #Behavior
    def get_info(self):
     print("info of about Laptop  " ,self.l_bname,self.l_mno, self.l_price,self.l_clr)
l_info=Lappi("HP","HP4511BH00" , 65000,"Black")
l_info.get_info()
"""

"""
class Tiles:

    #State
    def _init_(self,t_bname,t_price,t_clr):
        self.t_bname=t_bname
        self.t_price=t_price
        self.t_clr=t_clr
 #Behavior
    def get_info(self):
     print("info of about Laptop  " ,self.t_bname, self.t_price,self.t_clr)
t_info=Tiles("somany" , 650,"Fossil Natural")
t_info.get_info()
"""

"""
class Lipstick:

    #State
    def _init_(self,bname,price,clr):
        self.bname=bname
        self.price=price
        self.clr=clr
 #Behavior
    def get_info(self):
     print("info of about Laptop  " ,self.bname, self.price,self.clr)
lp_info=Lipstick("Estee Lauder" , 3650,"sting")
lp_info.get_info()
"""

"""
class Bottle:

    #State
    def _init_(self,bname,price,clr):
        self.bname=bname
        self.price=price
        self.clr=clr
 #Behavior
    def get_info(self):
     print("info of about Bottle  " ,self.bname, self.price,self.clr)
b_info=Bottle("bkr" , 2600,"white")
b_info.get_info()
"""

"""
class Vegetable:

    #State
    def _init_(self,vname,vprice,Calories ):
        self.vname=vname
        self.vprice=vprice
        self.Calories=Calories
 #Behavior
    def get_info(self):
     print("info of about vegetable  " ,self.vname, self.vprice,self.Calories)
v_info=Vegetable("Ladies Finger" , 30, 20.5)
v_info.get_info()
"""

"""
class Bag:

    #State
    def _init_(self,bname,price,clr):
        self.bname=bname
        self.price=price
        self.clr=clr
 #Behavior
    def get_info(self):
     print("info of about Bag  " ,self.bname, self.price,self.clr)
b_info=Bag("Safari" , 2600,"Blue+yellow")
b_info.get_info()
"""

"""
class Bag:

    #State
    def _init_(self,bname,price,clr):
        self.bname=bname
        self.price=price
        self.clr=clr
 #Behavior
    def get_info(self):
     print("info of about Bag  " ,self.bname, self.price,self.clr)
b_info=Bag("Safari" , 2600,"Blue+yellow")
b_info.get_info()
"""

"""
class Table:

    #State
    def _init_(self,bname,price,clr):
        self.bname=bname
        self.price=price
        self.clr=clr
 #Behavior
    def get_info(self):
     print("info of about Table  " ,self.bname, self.price,self.clr)


t_info=Table("Furniture" , 25000,"brown")
t_info.get_info()
"""

"""
class Vehicle:

    # State
    def _init_(self, bname,v_type, price, clr):
        self.bname = bname
        self.price = price
        self.clr = clr
        self.v_type=v_type
    # Behavior
    def get_info(self):
        print("info of about vehicles ", self.bname, self.price, self.clr,self.v_type)


c_info = Vehicle("Hundai", "4 wheeler", "Grey", 3500000)
c_info.get_info()
"""

"""
class Employee:

    # State
    def _init_(self, eid,ename,edept, esal):
        self.eid = eid
        self.ename = ename
        self.edept = edept
        self.esal=esal
    # Behavior
    def get_info(self):
        sal=self.esal+self.esal*25/100
        print("info of about employee ", self.eid, self.ename, self.edept,sal)


e_info = Employee("GB101", "Ramanuja", "HR", 30000)
e_info.get_info()
"""

"""
class Person:

    # State
    def _init_(self, pname,pheight, pweight):
        self.pname= pname
        self.pheight = pheight
        self.pweight = pweight
    # Behavior
    def get_info(self):

        print("info of about person ", self.pname, self.pheight, self.pweight)


p_info = Person("Rama", "6'8",75)
p_info.get_info()
"""

"""
class Product:

    # State
    def _init_(self, pid,pname,p_type, p_price):
        self.pid = pid
        self.pname = pname
        self.p_price = p_price
        self.p_type=p_type
    # Behavior
    def get_info(self):

        print("info of about product ", self.pid, self.pname, self.p_price,self.p_type)


p_info = Product("p002", "Furniture",30000,"Bed")
p_info.get_info()
"""

"""
class Watch:

    # State
    def _init_(self, bname,w_type, w_price):
        self.bname = bname
        self.w_type=w_type
        self.w_price = w_price
    # Behavior
    def get_info(self):

        print("info of about Watch ",  self.bname, self.w_price,self.w_type)
        w_info = Watch("Fastrack", 3500 ,"Hand Watch")
w_info.get_info()
"""

"""
class Refrigerators:

    # State
    def _init_(self, bname,f_clr, f_price):
        self.bname = bname
        self.f_clr=f_clr
        self.f_price = f_price
    # Behavior
    def get_info(self):

        print("info of about Refrigerators: ",  self.bname, self.f_price,self.f_clr)


f_info = Refrigerators("Samsung", 48999 ,"Goldyred")
f_info.get_info()
"""

