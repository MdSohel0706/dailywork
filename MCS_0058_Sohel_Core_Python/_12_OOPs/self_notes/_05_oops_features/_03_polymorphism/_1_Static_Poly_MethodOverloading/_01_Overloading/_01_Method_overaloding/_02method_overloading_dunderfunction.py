"""
Dunder or magic methods in Python are the methods having two prefix and
suffix underscores in the method name. Dunder here means “Double Under (Underscores)”.
These are commonly used for operator overloading.

Few examples for magic methods are: _init, __add, __len, __repr_ etc.

The _init_ method for initialization is invoked without any call,
when an instance of a class is created, like constructors in certain other programming
languages such as C++, Java, C#, PHP etc. These methods are the reason we can
add two strings with ‘+’ operator without any explicit typecasting.

"""

# declare our own string class
class String:

    # magic method to initiate object
    def _init_(self, string):
        self.string = string


# Driver Code
if _name_ == '_main_':
    # object creation
    string1 = String('Hello')

    # print object location
    print(string1)


# declare our own string class
class String:

    # magic method to initiate object
    def _init_(self, string):
        self.string = string

    # print our string object
    def _repr_(self):
        return 'Object: {}'.format(self.string)


# Driver Code
if _name_ == '_main_':
    # object creation
    string1 = String('Hello')

    # print object location
    print(string1)


# declare our own string class
class String:

    # magic method to initiate object
    def _init_(self, string):
        self.string = string

    # print our string object
    def _repr_(self):
        return 'Object: {}'.format(self.string)


# Driver Code
if _name_ == '_main_':
    # object creation
    string1 = String('Hello')

    # concatenate String object and a string
    print(string1 + ' world')

#Now add _add_ method to String:#class:
# declare our own string class
class String:

    # magic method to initiate object
    def _init_(self, string):
        self.string = string

        # print our string object

    def _repr_(self):
        return 'Object: {}'.format(self.string)

    def _add_(self, other):
        return self.string + other


# Driver Code
if _name_ == '_main_':
    # object creation
    string1 = String('Hello')

    # concatenate String object and a string
    print(string1 + ' Geeks')

def _init_(self,names):
    if names:
        self.names = names.copy()
        for name in names:
            self.versions[name] = 1
    else:
        raise Exception("Please Enter the names")
p = softwares (['S1','S2','S3'])
p1 =softwares([])

#str
def _str_(self):
    s ="The current softwares and their versions are listed below: \n"
    for key,value in self.versions.items():
        s+= f"{key} : v{value} \n"
    return s
print(p)

#setitem
def _setitem_(self,name,version):
    if name in self.versions:
        self.versions[name] = version
    else:
        raise Exception("Software Name doesn't exist")
p['S1'] = 2
p['2'] = 2

#getitem
def _getitem_(self,name):
    if name in self.versions:
        return self.versions[name]
    else:
        raise Exception("Software Name doesn't exist")
print(p['S1'])
print(p['1'])

#delitem
def _delitem_(self,name):
    if name in self.versions:
        del self.versions[name]
        self.names.remove(name)
    else:
        raise Exception("Software Name doesn't exist")
del p['S1']


#len
def _len_(self):
    return len(self.names)
print(len(p))

#contains
def _contains_(self,name):
    if name in self.versions:
        return True
    else:
        return False
if 'S2' in p:
    print("Software Exists")
else:
    print("Software DOESN'T exist")
#complete code
class softwares:
    names = []
    versions = {}

    def _init_(self, names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception("Please Enter the names")

    def _str_(self):
        s = "The current softwares and their versions are listed below: \n"
        for key, value in self.versions.items():
            s += f"{key} : v{value} \n"
        return s

    def _setitem_(self, name, version):
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception("Software Name doesn't exist")

    def _getitem_(self, name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("Software Name doesn't exist")

    def _delitem_(self, name):
        if name in self.versions:
            del self.versions[name]
            self.names.remove(name)
        else:
            raise Exception("Software Name doesn't exist")

    def _len_(self):
        return len(self.names)

    def _contains_(self, name):
        if name in self.versions:
            return True
        else:
            return False
#some more dunder functions
class point:
    x = None
    y = None

    def _init_(self, x, y):
        self.x = x
        self.y = y

    def _str_(self):
        s = f'({self.x},{self.y})'
        return s


p1 = point(5, 4)
p2 = point(2, 3)

#add
def _add_(self,p2):
    x = self.x + p2.x
    y = self.y + p2.y
    return point(x,y)
p3 = p1 + p2
#iadd
def _iadd_(self,p2):
    self.x += p2.x
    self.y += p2.y
    return self
p1 += p2
print(p1)

#complete code
class point:
    x = None
    y = None

    def _init_(self, x, y):
        self.x = x
        self.y = y

    def _str_(self):
        s = f'({self.x},{self.y})'
        return s

    def _add_(self, p2):
        print("In add")
        x = self.x + p2.x
        y = self.y + p2.y
        return point(x, y)

    def _iadd_(self, p2):
        self.x += p2.x
        self.y += p2.y
        return self

    def _isub_(self, p2):
        self.x -= p2.x
        self.y -= p2.y
        return self

    def _imul_(self, p2):
        self.x *= p2.x
        self.y *= p2.y
        return self

    def _itruediv_(self, p2):
        self.x /= p2.x
        self.y /= p2.y
        return self

    def _ifloordiv_(self, p2):
        self.x //= p2.x
        self.y //= p2.y
        return self

    def _call_(self):
        print(f"Called Point {self.x},{self.y}")