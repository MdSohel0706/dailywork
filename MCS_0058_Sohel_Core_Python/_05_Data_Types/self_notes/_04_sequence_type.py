#sequence_type:
"""In Python, sequence is the ordered collection of similar or different data types.
Sequences allows to store multiple values in an organized and efficient fashion. There
are several sequence types in Python"""

### STRING_DATATYPE

"""
-->The string formatting is used to print the string exactly the way we want. In the string formatting we use the {} as the place holders and use the format() method to fill the placeholders. We pass the values to the format() method.
exmaple:
--------
a = {'name': 'venkat', 'age' : 26}
sentence = 'my name is {}, age is {}'.format(a['name'], a['age'])
print(sentence)

-->we can also grab the specific things. Directly write the values in placeholders.
example:
--------
a = {'name': 'venkat', 'age' : 26}
sentence = 'my name is {0[name]}, age is {1[age]}'.format(a,a)
print(sentence)

-->In the above program we just write the dictionary a 2 times in the format(). Instead of the we can write the 'a' one time and write the 0 in the all the place holders. which means the values in the dictionary will be passed to the placeholders. 
example:
---------
a = {'name': 'venkat', 'age' : 26}
sentence = 'my name is {0[name]}, age is {0[age]}'.format(a)
print(sentence)

-->This is the same way that we access the list values also.
exmaple:
----------
a = {'name': 'venkat', 'age' : 26}
l = ['venkat', 26]
sentence = 'my name is {0[0]}, age is {0[1]}'.format(l)
print(sentence)

-->we can put the numbers in the placeholders, like which value should by stored in which placeholder. the number in the placeholder denotes the order of the values we passed in the fomat() method.
exmpale:
---------
a = {'name': 'venkat', 'age' : 26}
sentence = 'my name is {0}, age is {1}'.format(a['name'], a['age'])
print(sentence)

->we can also use the tags.
example:
--------
tag = h1
text  = 'this is the heading tag'
sentence = '<{0}> {1} </{0}>'.format(tag, text)
print(sentence)

----------------------------------------------------------------------------------------------------------

-->Shorthand if else statement
example:
--------
a = input(int("enter the fist number"))
b = input(int("entere the second number"))
print(" b is greater than a") if a < b else print("a is greater than b")

-----------------------------------------------------------------------------------------------------------------------"""
###TUPLE_DATATYPE:

"""Tuples:
-------
tuples are immutable object which follows the order like list. Once the values are assigned, they can't be modified. The below program gives the error " the tuple object doesn't support the item assignment". If it was a List, the item in the index position 1 will changed in both sample and sample1. We can't perform the operations like append(), remove() etc. Duplicates are allowed in tuples.

example:
--------
sample = ('apple','mango','chery')
sample1  = sample
sample[0] = 'banana'
print(sample)
print(sample1)

-->we can also create the tuple without the paranthesis.
example:
--------
a = 1,2,3
print(a)
output : (1,2,3)

-->If we want to create the tuple with only one item, we have to put the comma after the value.
a = (1,)
b = ('hello',)
c = 'mike',
-->if you don't put the comma, the value is not treated as the tuple. if you write like a = (1), then the type of a is int, for b = ('hello'), the type of b is string.

-->tuples has only 2 methods which are index() and count().
index():
--------
index() return the first index at which the value occures. if we give the value which is not in the tuple, it gives the 'valueError'
animals = ('lama', 'sheep', 'cat','lama')
print(animals.index('lama')) #this prints 0.

count():
--------
the count() method returns the no of times the value appeared in the tuple. If item is not in the tuple, then it returns 0.
animals = ('lama', 'sheep', 'cat', 'lama')
print(animals.count('lama')) #this returns 2

tuple unpacking:
----------------
-->tuples are useful for sequence unpacking
x,y = (10,11)
print(x,y)
output : 10 11
--------------------------------------------------------------------------------------------------------------"""
###LIST_DATATYPE
"""lists:
------
Lists are mutable and duplicates are allowed.
When you tried to print the sum of the element in a list when the list is empty, the sum operation returns zero.
example:
--------
a = []
print(sum(a)) # this returns 0

the difference between the append() and insert() method is insert() takes the position number as the argument. The common thing between the insert() and append() while adding the another list to the existing list, it is added as the sublist for the both the method, but append() don't take the position as the argument, but the insert () is. While adding the single element to another list using the append() and insert() like a.append(10) or a.insert(1,10) it is added as the single element, not as the sublist.

example:
--------
sample = ['maths','physics', 'history','economics']
new_sample = ['python', 'c']
sample.append('chemistry')
sampel.insert(1,'chemistry') #here 1 is the position where we want to insert the new data in the list.
sample.append(new_sample) #this adds the new_sample as the sub list

-->Here the insert() method must take the 2 arguments or it will give the error. Another way of adding the values to the list is using the extend() method. This method is useful when we want to add the multiple list of values to another list. If we add the single element or another list to the existing list using the extend() method, they will added as the individual elements, not as the sublist. we can aslo use the insert method to add the list of items to the existing list. but it will be added as the sub list. While adding the single element to the list using the insert() method the item will be added as the single element not as the sublist, if we try to add the another list to the existing list using the insert() the item will be added as the sublist.
example :
---------
sample = ['history','maths', 'physics','chemisty']
new_sample = ['arts', 'science']

sample.insert(1,new_sample) #this adds as the sub list
sample.extend(new_sample) # this adds as the individual items

-->To remove the items in the list we use the methods remove() or pop(). remove() takes the list item to be removed as the argument and the pop() method by default removes the last item in the list. pop() returns the value it removes. when the function is returning the value means, the result of that function must be stored in a variable. if the value that we want to remove is not found in the list, then it gives the value error, the element not in the list.
example:
--------
sample = ['maths','arts','science']
sample.remove('maths')
popped_value = sample.pop()
print(popped_value)

-->the sort() method is used to sort the items in the list. if the items in the list are text then the they will be sorted in the alphabetical order, if the items are the numbers they will be sorted in ascending order. To reverse the list we use the method reverse(). We can aslo pass the reverse = True as the argument to the sort() method.
example:
---------
sample = ['maths','economics','physics','arts']
sample.sort()
sample.sort(reverse = True)
sample.reverse()

-->the above mentioned methods, they change the original order of the list. If we don't want our original list order must not be changed. We can use the method sorted(). this only returns the modified version of the list. The sort() and reverse() methods returns None. 

sorted(sample) or sorted(sample, reverse = True)

-->To find the min and the max values in the list we use the methods min() and max() for list with the numbers.
example:
----------
number = [1,2,4,5,6,6]
min(number) #this returns 1
max(number) #this returns 6

-->To find the index of the item in the list we use the method index().if the element whose index we want to find out is not in the list, then it returns the valueError saying element not in the list.
syntax : list.index(element, start, end)
sample  =['apple','mango','cherry','banana']
sample.index('apple')
sample.index("guave") #this returns the valueError

-->To check if particular list item is in the list we can use the keyword "in". This returns true or false.
sample = ['apple','mango','cheyy']
print('mango' in sample)

-->To print the list of values with the customized index we use the method enumerate(). This method returns 2 value. one is the index and the item. Here we used start = 1 means we can start the index position starting from one. we can also use any number to start.
example:
--------
sample = ['apple','cherry','mango']
for index, item in enumerate(sample, start = 1):
	print(index,item)
	print(index, " : " , item)

-->If we want make the string version of comma seperated values from our list. we use the method join().
join() method returns the value of str data type, split() method returns the value in the list format. The join() method takes only one argument either the single strig value or the list of string.
example:
--------
sample = ['apple','mango','cherry']
sample1 = ' , '.join(sample)#this means all the elements will be joined by putting comma in between them
print(sample1)
new_sample = sample1.split(' , ') #this method removes the comma seperation and forms the new list.
print(new_sample)
output:
-------
apple , mango , cherry
['apple', 'mango', 'cherry']
-----------------------------------------------------------------------------------------------------------------------"""

