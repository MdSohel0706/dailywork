x = 344  #this for read operation
print(x)  #this for write operation
print(12+34) #Addition operation


list_tuple = (1,2,3,4,5)
print("Enter the tuple values :",list_tuple ,type(list_tuple))

list_tuple = ()
print("Empty tuple list :",list_tuple ,type(list_tuple))

list_tuple = (1,)
print("Enter the values :",list_tuple,type(list_tuple))
"""
#TUPLE:
1.Python tuples are a data structure that store an ordered sequence of values.
2.Tuples are immutable. This means you cannot change the values in a tuple.
3.They let you store an ordered sequence of items.
For example, you may use a tuple to store a list of employee names.
4.Python Tuple is used to store the sequence of immutable Python objects.
5.The tuple is similar to lists since the value of the items stored in the list can be changed,
6.whereas the tuple is immutable, and the value of the items stored in the tuple cannot be changed.

#Creating a tuple:

1.A tuple can be written as the collection of comma-separated (,) values enclosed with the small () brackets.
2.The parentheses are optional but it is good practice to use.
3.Creating a tuple with single element is slightly different.
4.We will need to put comma after the element to declare the tuple.
5.A tuple is indexed in the same way as the lists.
6.The items in the tuple can be accessed by using their specific index value.

#Tuple indexing and slicing:

1.The indexing and slicing in the tuple are similar to lists.
2.The indexing in the tuple starts from 0 and goes to length(tuple) - 1.
3.The items in the tuple can be accessed by using the index [] operator.
4.Python also allows us to use the colon operator to access multiple items in the tuple.

#Negative Indexing:

1.The tuple element can also access by using negative indexing.
2.The index of -1 denotes the rightmost element and -2 to the second last item and so on.
3.The elements from left to right are traversed using the negative indexing.

#Deleting Tuple:

1.Unlike lists, the tuple items cannot be deleted by using the del keyword as tuples are immutable.
2.To delete an entire tuple, we can use the del keyword with the tuple name.

#Accessing Values in Tuples:

1.To access values in tuple, use the square brackets for slicing along with the index
2.or indices to obtain value available at that index.

#Updating Tuples:

1.Tuples are immutable which means you cannot update or change the values of tuple elements

#Unpacking a Tuple:

1.When we create a tuple, we normally assign values to it. This is called "packing" a tuple
2.But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"

Packing a tuple:

fruits = ("apple", "banana", "cherry")

Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*:

1.If the number of variables is less than the number of values, you can add an * to the variable name
2.and the values will be assigned to the variable as a list

Example:

Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Loop Tuples:
##Loop Through a Tuple

1.You can loop through the tuple items by using a for loop.

Example
Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Loop Through the Index Numbers:

1.You can also loop through the tuple items by referring to their index number.
2.Use the range() and len() functions to create a suitable iterable.

Example
Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Using a While Loop:

1.You can loop through the list items by using a while loop.
2.Use the len() function to determine the length of the tuple.
3.then start at 0 and loop your way through the tuple items by refering to their indexes.
4.Remember to increase the index by 1 after each iteration.

Example
Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#Join Tuples:
##Join Two Tuples

1.To join two or more tuples you can use the + operator.


#Multiply Tuples:

1.If you want to multiply the content of a tuple a given number of times
you can use the * operator:

EXAMPLE:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#Where use tuple?

1.Using tuple instead of list gives us a clear idea that tuple data is constant
and must not be changed.

2. Tuple can simulate a dictionary without keys.
Consider the following nested structure, which can be used as a dictionary.

"""
"""
##Basic Tuple operations:

  The operators like concatenation (+), repetition (*), Membership (in) works
  in the same way as they work with the list.

1.Repetition
    The repetition operator enables the tuple elements to be repeated multiple times.

ex:T1*2 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

2.Concatenation
    It concatenates the tuple mentioned on either side of the operator.

ex:T1+T2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

3.Membership
    It returns true if a particular item exists in the tuple otherwise false

ex:print (2 in T1) prints True.

4.Iteration:
	The for loop is used to iterate over the tuple elements.

ex:for i in T1:
    print(i)

5.Length:
	It is used to get the length of the tuple.

ex:len(T1) = 5
"""