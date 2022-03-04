"""values():
												---------

-->values() returns the values of the dictionary. values() return the dict.values() object. to get the values from that object, we use the for loop.
example:
--------
dict1 = {'a': 'apple', 'b': 20, 'c' : [1,2,3]}
print(dict1.values())
for value in dict1.values():
    print(value)
output:
-------
dict_values(['apple', 20, [1, 2, 3]])
apple
20
[1, 2, 3]


example: we can apply values() on the empty dict, it dont' return anything, not even error.
--------
dict1 = {'a': 'apple', 'b': 20, 'c' : [1,2,3]}
print(dict1.values())
for value in dict():
    print(value)"""