# Everything is an object in Python

# string list tuple dictionary set
"""age = 10
'''
age = int(10) object creation   
      Employee(100,'satish',15000)
'''
age = int(10)  # int() float() long() str() list() tuple() dict() set()
print(age)
print(id(age), type(age))

li = [1, 2, 3]  # list([1,2,3])
li = list([1, 2, 3])
li.append(100)
# li.xyz()


msg = 'Hello World'  # str('Hello World')
msg = str('Hello World')


'''
madhu = Employee(100, 'MadhuN')
li = list( [1,2,3] )
list    -  classname -> builtins.py module 
[1,2,3] -  argument 
li      -  object**/ instance*/ ref. variable 
'''


# satish = Employee(100,'satish',1000) ==> object creation

print(li, id(li), type(li))

print(type(10.5), type(True), type('Hello'), type((1, 2, 3)))

print(li)  # list1.__repr__()   str() vs repr()

dict1 = {1: 1, 2: 2}
dict1.keys()"""

"""list_2  = [1, 2, 3,4,5,6,7,8,9]  # list([1,2,3]) #state
list_2 = list([1, 2, 3,4,5,6,7,8,9])# li.xyz()
list_2.append(100) #behaviour
#TypeError: 'list' object is not callable

list_1 = [1, 2, 3,4,5,6,7,8,9]  # list([1,2,3]) #state
list_1 = list([1, 2, 3,4,5,6,7,8,9])# li.xyz()
list_1.append(400,444,44445) #behaviour #TypeError: list.append() takes exactly one argument (3 given)

print(list_1)
print(list_2)"""


"""
msg = input("Enter the Name :")   #state
msg = str(msg) #behaviour
msg = msg +"babu"  #behaviour
print(msg)
"""

"""
msg = input("Enter the Name :")   #state
msg = str(msg) #behaviour
msg = msg.upper()+"babu"  #behaviour
print(msg)
"""

"""msg = input("Enter the Name :")   #state
msg = str(msg) #behaviour
msg = msg.title()+"babu"  #behaviour
print(msg)"""

"""age = int(input("Enter the number :")) # object creation
Employee = (100,'satish',1500)
print(age,Employee)"""
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



