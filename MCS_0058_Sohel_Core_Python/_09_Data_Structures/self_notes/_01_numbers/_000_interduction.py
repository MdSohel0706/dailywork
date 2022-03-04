""""

#BUILTIN FUNCTIONS:

1	cmp(tuple1, tuple2)
Compares elements of both tuples.

2	len(tuple)
Gives the total length of the tuple.

3	max(tuple)
Returns item from the tuple with max value.

4	min(tuple)
Returns item from the tuple with min value.

5	tuple(seq)
Converts a list into tuple

"""
"""
##List vs. Tuple:

1	The literal syntax of list is shown by the [].
    The literal syntax of the tuple is shown by the ().

2	The List is mutable.
    The tuple is immutable.

3	The List has the a variable length.
    The tuple has the fixed length.

4	The list provides more functionality than a tuple.
    The tuple provides less functionality than the list.

5	The list is used in the scenario in which we need to store the simple collections
    with no constraints where the value of the items can be changed.
    The tuple is used in the cases where we need to store the read-only collections
    i.e., the value of the items cannot be changed. It can be used as the key inside the dictionary.

6	The lists are less memory efficient than a tuple.
    The tuples are more memory efficient because of its immutability.

"""

"""
#BUILTIN METHODS:

1.keys()
	Returns a new object of the dictionary's keys.

2.pop(key[,d])
	Removes the item with the key and returns its value or d if key is not found.
	If d is not provided and the key is not found, it raises KeyError.

3.popitem()
    Removes and returns an arbitrary item (key, value).
    Raises KeyError if the dictionary is empty.

4.setdefault(key[,d])
    Returns the corresponding value if the key is in the dictionary.
    If not, inserts the key with a value of d and returns d (defaults to None).

5.update([other])
    Updates the dictionary with the key/value pairs from other, overwriting existing keys.

6.values()
	Returns a new object of the dictionary's values

7.clear()
    Removes all items from the dictionary.

8.copy()
    Returns a shallow copy of the dictionary.

9.fromkeys(seq[, v])
	Returns a new dictionary with keys from seq and value equal to v (defaults to None).

10.get(key[,d])
	Returns the value of the key. If the key does not exist, returns d (defaults to None).

11.items()
	Return a new object of the dictionary's items in (key, value) format.

12.dic.clear()
    It is used to delete all the items of the dictionary.

13.dict.copy()
    It returns a shallow copy of the dictionary.

14.dict.fromkeys(iterable, value = None, /)
    Create a new dictionary from the iterable with the values equal to value.

15.dict.get(key, default = "None")
    It is used to get the value specified for the passed key.

16.dict.has_key(key)
    It returns true if the dictionary contains the specified key.

17.	dict.items()
    It returns all the key-value pairs as a tuple.

18.dict.keys()
    It returns all the keys of the dictionary.

19.dict.setdefault(key,default= "None")
    It is used to set the key to the default value if the key is not specified in the dictionary

20.dict.update(dict2)
    It updates the dictionary by adding the key-value pair of dict2 to this dictionary.

21.dict.values()
    It returns all the values of the dictionary

"""