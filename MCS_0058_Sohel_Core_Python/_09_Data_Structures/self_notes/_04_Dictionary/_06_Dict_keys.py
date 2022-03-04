""" keys()
												------

-->keys() method is used to get the keys() from a dictionary. keys() returns the dictionary keys object. To get the keys from the keys() object, we can loop over it.
example:
--------
dict1 = {'a': 'apple', 'b': 20, 'c' : [1,2,3]}
print(dict1.keys())
for i in dict1.keys():
    print(i)
output:
-------
dict_keys(['a', 'b', 'c'])
a
b
c


-->when we loop over the dictionary, it returns the keys. no need to use the dict1.keys()
example:
--------
dict1 = {'a': 'apple', 'b': 20, 'c' : [1,2,3]}
print(dict1.keys())
for i in dict1:
    print(i)
output:
-------
dict_keys(['a', 'b', 'c'])
a
b
c


example: if you loop over the empty dictionary, it returns nothing, but don't give any error.
--------
dict1 = dict()
for i in dict1:
    print(i)
"""