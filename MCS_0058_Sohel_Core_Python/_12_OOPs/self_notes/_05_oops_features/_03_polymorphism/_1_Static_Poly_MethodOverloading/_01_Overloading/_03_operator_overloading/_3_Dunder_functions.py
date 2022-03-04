
class Employee(object):
    def __init__(self,eid):
        self.eid = eid

madhu = Employee(100)
print("Madhu object :", madhu)  # madhu.__str__()


x = 10
print("Integer : ", x)  # x.__str__()


class Employee(object):
    def __init__(self,eid):
        self.eid = eid

    def __str__(self):  # method overriding
        return '%s' % (self.eid)

madhu = Employee(100)
print("Madhu object :", madhu)  # madhu.__str__()



# https://www.geeksforgeeks.org/str-vs-repr-in-python/


"""
- str() is used for creating output for end user while repr() is mainly used for debugging and development.
- repr’s goal is to be unambiguous and str’s is to be readable.
  For example, if we suspect a float has a small rounding error, repr will show us while str may not.
- repr() compute the “official” string representation of an object
  (a representation that has all information about the object) and str() is used to compute the “informal” string
  representation of an object (a representation that is useful for printing the object).
- The print statement and str() built-in function uses __str__ to display the string representation of the object
  while the repr() built-in function uses __repr__ to display the object.
"""
# __str__
print("-------------str-----------")
s = 'Hello, Geeks.'
print(str(s)) 
print(str(2.0/11.0))

# __repr__
print("-------------repr-----------")
s = 'Hello, Geeks.'
print(repr(s))
print(repr(2.0/11.0))
print("--------------------------------")
import datetime
today = datetime.datetime.now()
# Prints readable format for date-time object
print("str format ",str(today))

# prints the official format of date-time object
print("repr format ",repr(today))



print("-----------Customized classes--------------------")
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x ,self.y)

p1 = Point(10,20)
print("Point object :", p1)  # p1.__str__()


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return 'Rational(%s, %s)' % (self.real, self.imag)

    def __str__(self):
        return '%s + i%s' % (self.real, self.imag)


# Driver program to test above
t = Complex(1, 2)
print(str(t))  # Same as "print(t)"
print(repr(t))


class Employee(object):
    pass
madhu = Employee
print("madhu str : ",madhu)  # madhu.__str__()


class Employee(object):
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def __repr__(self):
        return 'Employee object(%s, %s, %s)' % (self.eid, self.name, self.sal)

    def __str__(self):
        return '%s * %s * %s' % (self.eid, self.name, self.sal)

madhu = Employee(100,'Madhu Nettem',1000)
print("madhu str :",madhu)
print("madhu str :",str(madhu))
print("madhu repr:",repr(madhu))
