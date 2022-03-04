 #Python List index():

'''index() is an inbuilt function in Python, which searches for a given element from the
start of the list and returns the lowest index where the element appears.
Syntax:
list_name.index(element, start, end)

Parameters:
1 element – The element whose lowest index will be returned.
2 start (Optional) – The position from where the search begins.
3 end (Optional) – The position from where the search ends.'''

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# Will print the index of '4' in list1
print(list1.index(4))

list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
# Will print the index of 'cat' in list2
print(list2.index('cat'))

'''list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# Will print index of '4' in sublist
# having index from 4 to 8.
print(list1.index(4, 4, 8))
# Will print index of '1' in sublist
# having index from 1 to 7.
print(list1.index(1, 1, 7))'''

'''# Random list having sublist and tuple also
list1 = [1, 2, 3, [9, 8, 7], ('cat', 'bat')]
# Will print the index of sublist [9, 8, 7]
print(list1.index([9, 8, 7]))
# Will print the index of tuple
# ('cat', 'bat') inside list
print(list1.index(('cat', 'bat')))'''
""""""
"""'''
 ***LIST DATATYPE:

1. The list is one of the most widely used data types in Python.
2.A Python List can be easily identified by square brackets [ ]
3.Lists are used to store the data items where each data item is separated by a comma (,).
4.A Python List can have data items of any data type, be it an integer type or a boolean type.
5.A list in Python is used to store the sequence of various types of data.
6.Python lists are mutable type its mean we can modify its element after it created.
7.However, Python consists of six data-types that are capable to store the sequences, but the most common and reliable type is the list.
8.A list can be defined as a collection of values or items of different types.

1.List Items***:

    1.List items are ordered, changeable, and allow duplicate values.

    2.List items are indexed, the first item has index [0], the second item has index [1] etc.


2.Ordered-*:

    When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

    If you add new items to a list, the new items will be placed at the end of the list.

3.Changeable**:

    The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

4.Allow Duplicates-**:

    Since lists are indexed, lists can have items with the same value

4.1.List Length**:

    To determine how many items a list has, use the len() function

5.List Items - Data Types**

    List items can be of any data type

6.type()**:

    From Python's perspective, lists are defined as objects with the data type 'list'

7.The list() Constructor**
    It is also possible to use the list() constructor when creating a new list.

**Example:
Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

8.Accessing Values in Lists**:

    To access values in lists, use the square brackets for slicing along with the index or indices to obtain value available at that index.

==>example:-

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

9.Updating Lists**:

    You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator
    and you can add to elements in a list with the append() method.

10.Delete List Elements:-

    To remove a list element, you can use either the del statement
    if you know exactly which element(s) you are deleting or the remove() method if you do not know.

11.List Operations:==>

Python Expression	                            Results	                                             Description

1.len([1, 2, 3])                                    3                                                    Length

2.[1, 2, 3] + [4, 5, 6]	                      [1, 2, 3, 4, 5, 6]	                                    Concatenation

3.['Hi!'] * 4                           ['Hi!', 'Hi!', 'Hi!', 'Hi!']	                                Repetition

4.3 in [1, 2, 3]	                            True                                                	Membership

5.for x in [1, 2, 3]: print x,	                 1 2 3	                                                Iteration

12.  Characteristics of Lists:

The list has the following characteristics:

    1.The lists are ordered.
    2.The element of the list can access by index.
    3.The lists are the mutable type.
    4.The lists are mutable types.
    5.A list can store the number of various elements.

13.List indexing and splitting:=>

    1.The indexing is processed in the same way as it happens with the strings.
    2.The elements of the list can be accessed by using the slice operator [].
    3.The index starts from 0 and goes to length - 1.
    4.The first element of the list is stored at the 0th index, the second element of the list is stored at the 1st index, and so on.
13.1 Indexing in a List are of two types:

    1. Positive Indexing – Here the indexing starts from 0, moving from left to right.

    2. Negative Indexing – In this, the indexing starts from right to left and the rightmost element has an index value of -1.

14.Updating List values:=>

    Lists are the most versatile data structures in Python since they are mutable, and their values can be updated by using the slice and assignment operator.

    Python also provides append() and insert() methods, which can be used to add values to the list.

15.Adding elements to the list=>

    Python provides append() function which is used to add an element to the list.
    However, the append() function can only add value to the end of the list.

16.Removing elements from the list=>

    Python provides the remove() function which is used to remove the element from the list

17.Join Lists:

    1.There are several ways to join, or concatenate, two or more lists in Python.
    One of the easiest ways are by using the + operator.
    2. Another way to join two lists is by appending all the items from list2 into list1, one by one
EXAMPLE:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

    3.you can use the extend() method, which purpose is to add elements from one list to another list

18.Copy Lists:

    1.You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1
     and changes made in list1 will automatically also be made in list2.
    2.There are ways to make a copy, one way is to use the built-in List method copy()

EXAMPLE:==>

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

    3.Another way to make a copy is to use the built-in method list()

EXAMPLE:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

19. Sort Lists:

    List objects have a sort() method that will sort the list alphanumerically, ascending, by default

19.1 Customize Sort Function:

    You can also customize your own function by using the keyword argument key = function.
    The function will return a number that will be used to sort the list (the lowest number first)

EXAMPLE:

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

19.2 Case Insensitive Sort

    By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

20.Reverse Order:

    What if you want to reverse the order of a list, regardless of the alphabet?
    The reverse() method reverses the current sorting order of the elements.

21.Loop Through the Index Numbers:

    You can also loop through the list items by referring to their index number.
    Use the range() and len() functions to create a suitable iterable

EXAMPLE:==>

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

22.List Comprehension: Elegant way to create Lists

    List comprehension is an elegant and concise way to create a new list from an existing list in Python.

    A list comprehension consists of an expression followed by for statement inside square brackets.

    Here is an example to make a list with each item being increasing power of 2.

pow2 = [2 ** x for x in range(10)]
print(pow2)"""