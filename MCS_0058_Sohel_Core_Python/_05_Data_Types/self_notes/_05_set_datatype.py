###Sets:
"""------
Sets are the unordered list of the value with no duplicates.
For example if we have 2 sets with common values. To find those common values we use the method intersection(). We can also perform the union operation using the method union().
Python’s set is an unordered collection in Python. It can be used to compute standard math operations, such as intersection, union, difference, and symmetric difference. Other collections — like list, tuple, and dictionary — don’t support set operations. Dict view objects are set-like, which allows set operations.

exmaple:
-------------
set1 = {'apple','mango','cherry','banana'}
set2 = {'apple','mango', 'papaya','gauva'}

new_set1 = set1.intersection(set2)
new_set2 = set1.difference(set2) #returns items in set1 not in set2
new_set3 = set.union(set2)
print(new_set1)
print(new_set2)
print(new_set3)"""

"""# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)

"""