"""items()
												-------
-->It returns all the items(key-value pair) of a dictionary. the items() returns the dictionary items object. we can loop over it to get the keys and values.
example:
--------
dict1 = {'a': 'apple', 'b': 20, 'c' : [1,2,3]}
print(type(dict1.items()))
for key, value in dict1.items():
    print(key , " : ", value)

output:
-------
<class 'dict_items'>
a  :  apple
b  :  20
c  :  [1, 2, 3]


-->actually the items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair. the dictionary view object returns the copy of values and shows the underlying dictionary data.
example:
--------
dict1 = {'a': 'apple', 'b': 20, 'c' : [1,2,3]}
print(dict1.items())
output:
-------
dict_items([('a', 'apple'), ('b', 20), ('c', [1, 2, 3])])"""

