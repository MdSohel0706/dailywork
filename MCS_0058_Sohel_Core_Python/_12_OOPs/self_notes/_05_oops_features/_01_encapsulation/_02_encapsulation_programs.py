"""
1. Encapsulation :
-----------------
Definition: Binding the data members & member methods into single entity

entity         : class/object
data members   : Fields/Variables/Attributes  (class,instance variables)
member methods : Methods (Instance Methods,Class Methods,Static Methods)

satish = Employee(100,'satish, 15000)

Class  ===> Logical  -- DATA    Physical -- METHODS
Object ===> Physical -- DATA    Logical  -- METHODS (Through method access)

Ex : class is an example for encapsulation
     object is also an example


satish = Employee1(100,"satish",15000)
"""
"""
Encapsulation is the packing of data and functions that work on that data within a 
single object. By doing so, you can hide the internal
state of the object from the outside. This is known as information hiding.

A class is an example of encapsulation. A class bundles data and methods into a single unit.
 And a class provides the access to its attributes via methods.

The idea of information hiding is that if you have an attribute that isn’t visible to the outside, 
you can control the access to its value to make sure your object is always has a valid state.
"""
"""
class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0
        """
"""
The Counter class has one attribute called current which defaults to zero. And it has three methods:
increment() increases the value of the current attribute by one.
value() returns the current value of the current attribute
reset() sets the value of the current attribute to zero.
The following creates a new instance of the Counter class and calls the increment() method three
 times before showing the current value of the counter to the s
 """
"""
counter = Counter()


counter.increment()
counter.increment()
counter.increment()

print(counter.value())
"""
"""
class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0
        """

"""
class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0
        """
"""# Creating a base class
class Base:
    def __init__(self):
         
        # Protected member
        self._a = 2
 
# Creating a derived class   
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)
 
obj1 = Derived()
         
obj2 = Base()
 
# Calling protected member
# Outside class will  result in
# AttributeError
print(obj2.a)
 
Calling protected member of base class: 

Private members
Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class. However, to define a private member prefix the member name with double underscore “__”.
 

Note: Python’s private and protected member can be accessed outside the class through python name mangling.
 
# Python program to
# demonstrate private members
 
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
# Driver code
obj1 = Base()
print(obj1.a)
 
# Uncommenting print(obj1.c) will
# raise an AttributeError
 
# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
"""
"""
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
"""
"""
class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blue", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
"""

"""
class Teacher:

   #state
    def __init__(self,name,id,subject,phno):
        self.name = name
        self.id = id
        self.subject = subject
        self.phno = phno

        #behaviour
    def satish_get(self):
        print("Enter the teacher Details:",self.name, self.id,self.subject,self.phno)

employee = Teacher("satish",101,"java","9556566563")
employee.satish_get()
"""
"""
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
"""

"""
class Bankemployee:

#state

  def __init__(self,bankemployeename,bankemployeeid,bankemployeeemail):
      self.bankemployeename = bankemployeename
      self.bankemployeeid = bankemployeeid
      self.bankemployeeemail = bankemployeeemail

              #behaviour

  def satish_get(self):
      print("Enter the bank employee Details:",self.bankemployeename,self.bankemployeeid,self.bankemployeeemail)


venkat = Bankemployee("venkat",101,"venkat143@gmail.com")
venkat.satish_get()
"""








