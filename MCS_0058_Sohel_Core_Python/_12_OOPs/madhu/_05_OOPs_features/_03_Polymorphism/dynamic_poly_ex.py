# Dynamic polymorphism   ==> Method overriding


# Dynamic polymorphism   ==> Method overriding
# From child class constructor we can call parent class constructor by using super() method.

class Animal:

    def _init_(self):
        pass

    def sleeping(self):
        print("Animal sleeping")


class Tiger(Animal):

    def _init_(self):
        super()._init_()

    def sleeping(self):  # Method overriding
        print("Tiger sleeping")


tiger = Tiger()
tiger.sleeping()

print('..........................................')


class P:
    def property(self):
        print('Gold+Land+Cash+Power')

    def marry(self):
        print('Appalachia')


class C(P):
    def marry(self):
        print('Katrina')


c = C()
c.property()
c.marry()

print("....................Constructor overriding..............")


class P:
    def _init_(self):
        print('Parent Constructor')


class C(P):
    def _init_(self):
        super()._init_()
        print('Child Constructor')


c = C()

print("...................................................................")


class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def _init_(self, name, age, eno, esal):
        super()._init_(name, age)
        self.eno = eno
        self.esal = esal

    def display(self):
        print('Employee Name:', self.name)
        print('Employee Age:', self.age)
        print('Employee Number:', self.eno)
        print('Employee Salary:', self.esal)


e1 = Employee('Ali', 24, 872425, 26000)
e1.display()
e2 = Employee('Ila', 42, 872426, 36000)
e2.display()
class Animal:

    def __init__(self):
        pass

    def sleeping(self):
        print("Animal sleeping")

class Tiger(Animal):

    def __init__(self):
        pass

    def sleeping(self): # Method overriding
        print("Tiger sleeping")


tiger = Tiger()
tiger.sleeping()