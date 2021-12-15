'''
# The process in which conversion of
# class object --> bytes - pickle or serialization. Here,using dump()
# syntax: pickle.dump(object, file)

# bytes --> class object - unpickle or deseriliazation. Here, using load()
# syntax: object=pickle.load(file)

# we need to create class for structured data of different data types string,int,float
# create a class with instance variables id, name, sal
'''''
import pickle

class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
    def display(self):
        print("{:5d} {:20s} {:10.2f}".format(self.id, self.name, self.sal))
'''
# we need to create a object to the class, to store actual data into that object.Later this
# object should be stored into a binary file in the form of bytes.
# pickle.dump(object, file) stores object into binary file
# for unpickling , using load()
# object = pickle.load(file)

# To pickle Emp class objects , we have to import Emp.py file as module is available.

import Emp, pickle

# opening emp.dat file as binary file for writing
f =open('emp.dat', 'wb')
n = int(input('How many emloyees to add : '))

for i in range(n):
    id = int(input('Enter id:'))
    name = input('Enter name: ')
    sal = float(input('Enter salary: '))

# create an Emp class object
    e = Emp.Emp(id, name, sal)

# store the object e into file f

    pickle.dump(e, f)

# close the file
f.close()


# for unpickling, as we stored Emp class ocjects in emp.dat file, to retrieve those
# objects we have to unpickle
# obj = pickle.load(f)

# Reads an object from file f, and returns into obj
# since obj belongs to Emp class  we can use display method use obj.display()
use loop when we reach end of file and could not find any objects to read then 
raise an EOFError
'''
import Emp, pickle
f = open('emp.dat', 'rb')
print('Employee details: ')
while True:
    try:
        # read object from file f
        obj = pickle.load(f)
        # display the contents of employee obj
        obj.display()
    except EOFError:
         print('End of file reached...')
         break
