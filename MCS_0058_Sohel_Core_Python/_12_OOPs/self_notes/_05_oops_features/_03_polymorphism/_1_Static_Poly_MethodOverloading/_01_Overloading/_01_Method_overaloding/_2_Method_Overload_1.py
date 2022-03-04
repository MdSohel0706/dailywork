class FeedbackForm:

    def __init__(self):
        pass

    def feedback(self, rating=10, comments=None):   # method overloading (function overloading)
        print("Feedback is :", rating, ", ", comments)

# Method overloading
feed = FeedbackForm()

feed.feedback()   # Default args
feed.feedback(4)  # Default args
feed.feedback(9, 'Good')  # Positional args
feed.feedback(comments='Very Bad')  # keyword args
feed.feedback(comments='Very Bad', rating=1)  # keyword args

'''
In java/.net
def feedback(self):
    pass

def feedback(self, rating):
    pass
    
def feedback(self, rating, comments):
    pass

def feedback(self,comments):
    pass
'''

#Function overloading
def sum(a=10, b=20, c=30):
    print("Sum is ", a+b+c)

# Overloading - Depends on how many arguments we are passing
sum()
sum(15)
sum(15, 25)
sum(15, 25, 35)
sum(b=200, a=100)
sum(b=200, c=300)
sum(a=100, c=300)
sum(b=200, a=100, c=300)



def add(x, y):
    pass


def sum(a, b):
    res = add(a, b)


"""
2.Method Overloading:

If 2 methods having same name but different type of arguments then those methods are said to
be overloaded methods.

Eg: m1(int a)
m1(double d)
But in Python Method overloading is not possible.
If we are trying to declare multiple methods with same name and different number of arguments
then Python will always consider only last method.

"""

#example:

class Test:
    def m1(self):
       print('no-arg method')
    def m1(self,a):
        print('one-arg method')
    def m1(self,a,b):
        print('two-arg method')
t=Test()
#t.m1()
#t.m1(10)
t.m1(10,20)


class Person:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
# Create instance
obj = Person()
# Call the method
obj.Hello()
# Call the method with a parameter
obj.Hello('Edureka')


# Program to illustrate method overloading
class edpresso:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')


# Create an instance
obj = edpresso()

# Call the method
obj.Hello()

# Call the method with a parameter
obj.Hello('Kadambini')


class FeedbackForm:

    def _init_(self):
        pass

    def feedback(self, rating=10,
                 comments=None):  # method overloading (function overloading)
        print("Feedback is :", rating, ", ", comments)


# Method overloading
feed = FeedbackForm()

feed.feedback()  # Default args
feed.feedback(4)  # Default args
feed.feedback(9, 'Good')  # Positional args
feed.feedback(comments='Very Bad')  # keyword args
feed.feedback(comments='Very Bad', rating=1)  # keyword args

"""
In java/.net
def feedback(self):
    pass

def feedback(self, rating):
    pass

def feedback(self, rating, comments):
    pass

def feedback(self,comments):
    pass

"""
# Function overloading
def sum(a=10, b=20, c=30):
    print("Sum is ", a + b + c)


# Overloading - Depends on how many arguments we are passing
sum()
sum(15)
sum(15, 25)
sum(15, 25, 35)
sum(b=200, a=100)
sum(b=200, c=300)
sum(a=100, c=300)
sum(b=200, a=100, c=300)


def add(x, y):
    pass


def sum(a, b):
    res = add(a, b)
