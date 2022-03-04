"""pop()
											-----

-->the pop() method removes and returns an elements from a dictionary having the given key.
Syntax : dictionary.pop(key[, default])

key - key which is to be searched for removal
default - value which is to be returned when the key is not in the dictionary

If key is found - removed/popped element from the dictionary
If key is not found - value specified as the second argument (default)
If key is not found and default argument is not specified - KeyError exception is raised

example:
--------
dict1 = {'eid' : 123, 'ename' : 'Guido', 'salary' : 10000, 'Nationality' : 'USA'}

#this returns the value of the deleted key if key is found.
print(dict1.pop('eid'))
print(dict1)
output:
-------
123
{'ename': 'Guido', 'salary': 10000, 'Nationality': 'USA'}


example: pop the element which is not in the dictionary
--------
dict1 = {'eid' : 123, 'ename' : 'Guido', 'salary' : 10000, 'Nationality' : 'USA'}
print(dict1.pop('address'))
print(dict1)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 3, in <module>
    print(dict1.pop('address'))
KeyError: 'address'


example : if key not found while doing pop(), instead of error, we can give the default value to return
---------
dict1 = {'eid' : 123, 'ename' : 'Guido', 'salary' : 10000, 'Nationality' : 'USA'}
#here I provided the default value New york if key address is not found
print(dict1.pop('address', 'New York'))
print(dict1)
output:
-------
New York
{'eid': 123, 'ename': 'Guido', 'salary': 10000, 'Nationality': 'USA'}"""