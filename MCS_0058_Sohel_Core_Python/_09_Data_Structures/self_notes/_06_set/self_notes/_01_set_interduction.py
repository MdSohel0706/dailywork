"""
#SET:

1.A Python set is the collection of the unordered items.
Each element in the set must be unique, immutable, and the sets remove the duplicate elements.
Sets are mutable which means we can modify it after its creation.

2.Unlike other collections in Python, there is no index attached to the elements of the set.
i.e., we cannot directly access any element of the set by the index.
However, we can print them all together, or we can get the list of elements by looping through the set.

#Creating a set:

1.The set can be created by enclosing the comma-separated immutable items with the curly braces {}.
2.Python also provides the set() method, which can be used to create the set by the passed sequence.

#Adding items to the set:

1.Python provides the add() method and update() method which can be used to add some particular item to the set.

2.The add() method is used to add a single element whereas the update() method is used to add multiple elements to the set.

3.To add more than one item in the set, Python provides the update() method. It accepts iterable as an argument.

#Removing items from the set:

1.Python provides the discard() method and remove() method which can be used to remove the items from the set.
2.The difference between these function, using discard() function if the item does not exist in the set
3.then the set remain unchanged whereas remove() method will through an error.
4.Python provides also the remove() method to remove the item from the set.
5.We can also use the pop() method to remove the item.
Generally, the pop() method will always remove the last item but the set is unordered
we can't determine which element will be popped from set.

#Difference between discard() and remove():

1.Despite the fact that discard() and remove() method both perform the same task
There is one main difference between discard() and remove().

2.If the key to be deleted from the set using discard() doesn't exist in the set
the Python will not give the error. The program maintains its control flow.

3.On the other hand, if the item to be deleted from the set using remove() doesn't exist in the set
the Python will raise an error.

#Python Set Operations:

    1.Set can be performed mathematical operation such as union, intersection, difference, and symmetric difference.
    2.Python provides the facility to carry out these operations with operators or methods.

1.Union of two Sets
    The union of two sets is calculated by using the pipe (|) operator.
    The union of the two sets contains all the items that are present in both the sets.

2.Intersection of two sets
    The intersection of two sets can be performed by the and & operator or the intersection() function.
    The intersection of the two sets is given as the set of the elements that common in both sets.

3.The intersection_update() method:

    The intersection_update() method removes the items from the original set
    that are not present in both the sets (all the sets if more than one are specified).

    The intersection_update() method is different from the intersection() method
    since it modifies the original set by removing the unwanted items,
    on the other hand, the intersection() method returns a new set.

4.Difference between the two sets:

    The difference of two sets can be calculated by using the subtraction (-) operator or intersection() method.
    Suppose there are two sets A and B, and the difference is A-B that denotes
    the resulting set will be obtained that element of A, which is not present in the set B.

5.Symmetric Difference of two sets:

    The symmetric difference of two sets is calculated by ^ operator or symmetric_difference() method.
    Symmetric difference of sets, it removes that element which is present in both sets.

6.Set comparisons:

    Python allows us to use the comparison operators i.e., <, >, <=, >= , ==
    with the sets by using which we can check whether a set is a subset,
    superset, or equivalent to other set.
    The boolean true or false is returned depending upon the items present inside the sets.

#FrozenSets:

1.The frozen sets are the immutable form of the normal sets, i.e.,
the items of the frozen set cannot be changed and therefore it can be used as a key in the dictionary.

2.The elements of the frozen set cannot be changed after the creation.
We cannot change or append the content of the frozen sets by using the methods like add() or remove().

3.The frozenset() method is used to create the frozenset object.
The iterable sequence is passed into this method which is converted into the frozen set as
a return type of the method

#DIFFERENCES BETWEEN SUBSET AND SUPERSET?
1.A set A is said to be a subset of a set B; if and only if,
2.every element of set A is also an element of set B. Such a relation between sets is denoted by A ⊆ B. ...
For an example, A = {1, 3} is a subset of B = {1, 2, 3},
3.since all the elements in A contained in B. B is a superset of A, because B contains A

#WHAT IS SUBSET:?

1.The issubset() method returns True if all elements of a set are present
2.in another set (passed as an argument). ...
3.Set A is said to be the subset of set B if all elements of A are in B .
4.Subset of a Set. Here, set A is a subset of B .


# WHAT IS SUPERSET:?

1.The issuperset() method returns True if a set has every elements of another set
(passed as an argument). ...
2.Set X is said to be the superset of set Y if all elements of Y are in X.
 """
"""

# SET BUILT IN METHODS:

1	add(item):	It adds an item to the set. It has no effect if the item is already present in the set.

2	clear():	It deletes all the items from the set.

3	copy()	:It returns a shallow copy of the set.

4	difference_update(....)	:It modifies this set by removing all the items
that are also present in the specified sets.

5	discard(item)	:It removes the specified item from the set.

6	intersection()	:It returns a new set that contains only the common elements of both the sets.
(all the sets if more than two are specified).

7	intersection_update(....)	:It removes the items from the original set that are not present
in both the sets (all the sets if more than one are specified).

8	Isdisjoint(....):	Return True if two sets have a null intersection.

9	Issubset(....):	Report whether another set contains this set.

10	Issuperset(....):	Report whether this set contains another set.

11	pop()	:Remove and return an arbitrary set element
that is the last element of the set. Raises KeyError if the set is empty.

12	remove(item):	Remove an element from a set; it must be a member.
If the element is not a member, raise a KeyError.

13	symmetric_difference(....):	Remove an element from a set; it must be a member.
If the element is not a member, raise a KeyError.

14	symmetric_difference_update(....):	Update a set with the symmetric difference of itself and another.

15	union(....):	Return the union of sets as a new set.
(i.e. all elements that are in either set.)

16	update():	Update a set with the union of itself and others
"""