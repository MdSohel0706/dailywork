'''

def eating(self):
    print("SUPER :: Animal : eating")
    ....
Method:
        I.  Method signature   ==> def eating(self):
        II. Method body(impl.) ==> print("SUPER :: Animal : eating") ...

Code resuability :  1. Signature + Body (Implementation)
                    2. Only signature

'''

'''  REUSE*
I: All sub classes required 
                method signature -  common  
                method body      -  common** implementation
                
                        Animal
                          - eating()
                Tiger   Lion     Cat   Dog
'''
class Animal:

    def __init__(self):
        pass
        # print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal : eating")

class Tiger(Animal):

    def __init__(self):
        pass
        # print("SUB  :: Tiger constructor")

class Lion(Animal):

    def __init__(self):
        pass
        # print("SUB  :: Lion constructor")

class Cat(Animal):

    def __init__(self):
        pass
        # print("SUB  :: Cat constructor")

class Dog(Animal):

    def __init__(self):
        pass
        # print("SUB  :: Dog constructor")

ani = Animal()
ani.eating()

tiger = Tiger()
tiger.eating()

lion = Lion()
lion.eating()

cat = Cat()
cat.eating()

dog = Dog()
dog.eating()

"""
def eating(self):
    print("SUPER :: Animal : eating")
    ....
Method:
        I.  Method signature   ==> def eating(self):
        II. Method body(impl.) ==> print("SUPER :: Animal : eating") ...

Code re-usability :  1. Signature + Body (Implementation)
                    2. Only signature

"""

'''  REUSE*
I: All sub classes required 
                method signature -  common  
                method body      -  common** implementation

                        Animal
                          - eating()
                Tiger   Lion     Cat   Dog
'''


class Animal:

    def _init_(self):
        pass
        # print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal : eating")


class Tiger(Animal):

    def _init_(self):
        pass
        # print("SUB  :: Tiger constructor")


class Lion(Animal):

    def _init_(self):
        pass
        # print("SUB  :: Lion constructor")


class Cat(Animal):

    def _init_(self):
        pass
        # print("SUB  :: Cat constructor")


class Dog(Animal):

    def _init_(self):
        pass
        # print("SUB  :: Dog constructor")


ani = Animal()
ani.eating()

tiger = Tiger()
tiger.eating()

lion = Lion()
lion.eating()

cat = Cat()
cat.eating()

dog = Dog()
dog.eating()

print(".........................................................")


class EarthHuman:
    """
    def _init_(self):
        print('Human Pass')
    """

    def talk(self):
        print("Human talk ........")


class IndiaHuman(EarthHuman):
    def _init_(self):
        print("India Human Pass")


ih = IndiaHuman()
ih.talk()


class AmericaHuman(EarthHuman):
    def _init_(self):
        print("American Human ")


ah = AmericaHuman()
ah.talk()


class ChinaHuman(EarthHuman):
    def _init_(self):
        print("China Human ")


ch = ChinaHuman()
ch.talk()

'''  REUSE*
I: All sub classes required
                method signature -  common
                method body      -  common** implementation
'''

"""
Electronic gadget
   Fan                    AC                   laptop               laptop                    
(electricity)        (electricity)           (electricity)        (electricity)             


                                                        (Charge)
  """


class E_Gadget:
    def _init_(self):
        print("Super class")

    def electricity(self):
        print("Need electricity")


class Fan(E_Gadget):
    print("Fan is working")


class AC(E_Gadget):
    print("AC is working")


class Laptop(E_Gadget):
    print("laptop working")

    def charge(self):
        print("put in charge")


class Mobile(Laptop):
    print("mobile is working")

    def charge(self):
        pass


obj = E_Gadget()
obj.electricity()

obj1 = Laptop()
obj1.charge()
obj1.electricity()

obj2 = Mobile()
obj2.electricity()


# Single Inheritance


class Fruits:
    def _init_(self):
        print("Super class")

    def health(self):
        print("Fruits are good for health")


class Apple(Fruits):
    print("Inherit super class properties into sub class")

    def _init_(self):
        pass


obj = Fruits()
obj.health()


class Person():

    # Constructor
    def _init_(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Rinky")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Manu")  # An Object of Employee
print(emp.getName(), emp.isEmployee())


class Person():

    # _init_ is known as the constructor
    def _init_(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# child class
class Employee(Person):
    def _init_(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        print("Details of emp :  ", self.salary, self.post)

        # invoking the _init_ of the parent class
        Person._init_(self, name, idnumber)

    # creation of an object variable or an instance


a = Employee('Shyama', 886012478, 200000, "Trainee")

# calling a function of the class Person using its instance
a.display()


# Multiple Inheritance

class Parent1:
    pass


class Parent2:
    pass


class Child(Parent1, Parent2):
    pass


if issubclass(Child, (Parent1, Parent2)):
    print("Child is a subclass of Parent1 and Parent2")


class Parent1:

    def display1(self):
        print("In class Parent1")


class Parent2:

    def display2(self):
        print("In class Parent2")


class Child(Parent1, Parent2):
    print("Inherit properties from two diff class")


obj = Child()
obj.display1()
obj.display2()


class A:

    def display(self):
        print("Class A")


class X(A):

    def display(self):
        print("Class X")


class Y(A):

    def display(self):
        print("Class Y")


class Z(X, Y):
    pass


obj = Z()
obj.display()


class A:

    def display(self):
        print("Class A")


class X(A):
    print("working")


class Y(A):

    def display(self):
        print("Class Y")


class Z(X, Y):
    pass


obj = Z()
obj.display()