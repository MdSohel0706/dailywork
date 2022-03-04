# list is mutable
# tuple is immutable

list1 = [1, 2, 3, 4, 5, 6]
'''
# Builtin functions:
---------------------
append insert extend   : UPDATE
pop  remove            : DELETE 
count                  : RETRIEVE
index                  : RETRIEVE
reverse                : UPDATE 
sort                   : UPDATE
copy                   : CREATE

'''
# 1. append(): It appends element(any value) at end of the list
             # list1.append(obj) Appends any object obj to list
"""list1 = [1, 2, 3, 4, 5, 6]
print("Before append : ",list1)
list1.append(10)
print("After append  : ", list1)
list1.append(10.4)
list1.append(True)
list1.append('Hello')
list1.append([1, 2, 3])
list1.append((10, 20, 30))
list1.append({1: 1})
list1.append({100, 200, 300})

for ind, val in enumerate(list1):
    print(ind, "----", val)

print("After append  :", list1)


# extend  : only sequence str,list,tuple
         #: list1.extend(seq)         Appends the contents of seq to list

list1 = [1, 2, 3, 4, 5, 6]
print("DEBUG : Before extend : ", list1)
# append([10,20,30]) :       ==> [1,2,3,4,5,6,[10,20,30]]
list1.extend([10, 20, 30])   #  ==> [1,2,3,4,5,6,10,20,30]
print("DEBUG : After extend  : ", list1)
list1.extend('Hello World')
list1.extend((1, 2, 3))
print("DEBUG : After extend  : ", list1)


# append vs extend

list1 = [1, 2, 3]
list1.append([10, 20])
list1.extend([100, 200])
print("List after append,extend : ",list1)

# 3. pop
            # list.pop(obj=list[-1]) Removes and returns last object or obj from list
list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before pop   : ", list1)
list1.pop(3)  # index
print("After  pop   : ",list1) # [23, 12, 46, 14, 7, 2, 19, 25]
list1.pop()
print("After  pop   : ",list1) # [23, 12, 46, 14, 7, 2, 19]

rem_ele = list1.pop(0)
print("Popped element : ",rem_ele)
print("After  pop   : ",list1)

# 4. remove
            # list.remove(obj)    Removes object obj from list
list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before removal : ", list1)
list1.remove(34)
print("After removal  : ", list1)

list1 = [23, 14, 12, 46, 34, 14, 7, 2, 14, 19, 25]
print("Before removal : ",list1)
#list1.remove(14)
list1.pop(5)
print("After removal  : ",list1)

# 5.list.insert(index, obj)  Inserts object obj into list at offset index
list1 = [1, 2, 3, 4, 5]
print("Before index : ",list1)
list1[0] = 150  # [150, 2, 3, 4, 5]  Replace the value in index
print("After index   : ",list1)
list1.insert(0, 100) # [100, 150, 2, 3, 4, 5] Insert the value in index
print("After insert  : ",list1)
list1.insert(5, 100)
print("After insert   : ",list1)

# 6. count ==> list.count(obj)Returns count of how many times obj occurs in list
list1 = [1,1,3,2,3,2,4,5,3,2,1]
print("List count 2: ",list1.count(2))
# 7. index  ==> list.index(obj) Returns the lowest index in list that obj appears
list1 = [23,76,23,32,53,34,25,21,53,43,16,25,7,53,13,59]
print("List index : ",list1.index(53))

# 8. reverse ==> list.reverse()  Reverses objects of list in place
list1 = [1,2,3,4,5]
list1.reverse()
print("List after reverse : ",list1)

# 9. sort ==> list.sort(obj)Sorts the elements
list1 = [23,76,23,32,53,34,25,21,53,43,16,25,7,53,13,59]
list1.sort()  # ascending order
print("List sort ascending : ",list1)

list1.sort(reverse=True) # descending order
print("List sort descending: ",list1)

# 10. copy()

list1 = [1,2,3,4,5]
print("Before copy list1 : ", list1)
list2 = list1.copy()
print("After copy list2  : ", list2)
print("Normal copy function : ",id(list1),id(list2))
list1.append(100)

print("After append : list1 :", list1)
print("After append : list2 :", list2)

# 2nd way of copy

list1 = [1,2,3,4,5]
list2  = list1
print("Variable  copy : ", id(list1),id(list2))
list1.append(100)
print("After var copy :", list1,list2)
list2.extend(([11,22]))
print("After var copy :", list1,list2)

"""
'''
                                                                <<==LIST PROGRAMS==>>

1- Write the program to remove the duplicate element of the list.

list1 = [1,2,2,3,55,98,65,65,13,29]
# Declare an empty list that will store unique values
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

2- Write a program to find the sum of the element in the list.

list1 = [3,4,5,9,10,12,24]
sum = 0
for i in list1:
    sum = sum+i
print("The sum is:",sum)

3- Write the program to find the lists consist of at least one common element.

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,2,10]
for x in list1:
    for y in list2:
        if x == y:
            print("The common element is:",x)

4- Program to check if the Given List is in Ascending Order or Not

list1 = [1, 2, 3, 5, 4, 8, 7, 9]
temp_list = list1[:]
list1.sort()
if temp_list == list1:
    print("Given List is in Ascending Order")
else:
    print("Given List is not in Ascending Order")

5-Program to Find Even Numbers From a List

list2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
for i in list2:
    if i % 2 == 0:
        print(i)

6-Program to Merge Two Lists

list3 = [1, 2, 4, 6]
list4 = [9, 3, 19, 7]
list3.extend(list4)
print(list3)

7-Interchange First and Last Element of a List

list5 = [1, 29, 51, 9, 17, 6, 7, 23]
list5[0], list5[-1] = list5[-1], list5[0]
print(list5)

8-Program to Subtract a List from Another List

a = [1, 2, 3, 5]
b = [1, 2]
l1 = []
for i in a:
    if i not in b:
        l1.append(i)
print(l1)

9-Program to Get Data Items From a List Appearing Odd Number of Times

x = [1,2,3,4,5,1,3,3,4]
l1 = []
for i in x:
    if x.count(i) % 2 != 0:
        if i not in l1:
            l1.append(i)
print(l1)

10- Python Program to Find the Largest Number in a List?

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])


11-Python Program to Find the Second Largest Number in a List

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Second largest element is:",a[n-2])

12-Python Program to Put Even and Odd elements in a List into Two Different Lists

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)


13-Python Program to Merge Two Lists and Sort it

a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)


14-Python Program to Sort a List According to the Length of the Elements

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=input("Enter element:")
    a.append(b)
a.sort(key=len)
print(a)

15-Python Program to Find the Union of two Lists


l1 = []
num1 = int(input('Enter size of list 1: '))
for n in range(num1):
    numbers1 = int(input('Enter any number:'))
    l1.append(numbers1)

l2 = []
num2 = int(input('Enter size of list 2:'))
for n in range(num2):
    numbers2 = int(input('Enter any number:'))
    l2.append(numbers2)

union = list(set().union(l1,l2))

print('The Union of two lists is:',union)

16-Python Program to Find the Intersection of Two Lists

def intersection(a, b):
    return list(set(a) & set(b))

def main():
    alist=[]
    blist=[]
    n1=int(input("Enter number of elements for list1:"))
    n2=int(input("Enter number of elements for list2:"))
    print("For list1:")
    for x in range(0,n1):
        element=int(input("Enter element" + str(x+1) + ":"))
        alist.append(element)
    print("For list2:")
    for x in range(0,n2):
        element=int(input("Enter element" + str(x+1) + ":"))
        blist.append(element)
    print("The intersection is :")
    print(intersection(alist, blist))
main()


17-Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))
a=[(x,x**2) for x in range(l_range,u_range+1)]
print(a)


18-Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10

l=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
a=[]
a=[x for x in range(l,u+1) if (int(x*0.5))*2==x and sum(list(map(int,str(x))))<10]
print(a)

19-Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List

import random
a=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)

20-Python Program to Swap the First and Last Value of a List


a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("New list is:")
print(a)

21-Python Program to Remove the Duplicate Items from a List

a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non-duplicate items:")
print(unique)

22-Python Program to Read a List of Words and Return the Length of the Longest One


a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The word with the longest length is:")
print(temp)


23-Python Program to Remove the ith Occurrence of the Given Word in a List where Words can Repeat

a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
print(a)
c=[]
count=0
b=input("Enter word to remove: ")
n=int(input("Enter the occurrence to remove: "))
for i in a:
    if(i==b):
        count=count+1
        if(count!=n):
            c.append(i)
    else:
        c.append(i)
if(count==0):
    print("Item not found ")
else:
    print("The number of repetitions is: ",count)
    print("Updated list is: ",c)
    print("The distinct elements are: ",set(a))


24-Program for Adding, removing elements in the list

# Declaring a list with integer and string elements
list = [10, 20, 30, "New Delhi", "Mumbai"]

# printing list
print "List elements are: ", list

# adding elements
list.append (40)
list.append (50)
list.append ("Chennai")

# printing list after adding elements
print "List elements: ", list

# removing elements
list.pop () ;
# printing list
print "List elements: ", list
# removing elements
list.pop () ;
# printing list
print "List elements: ", list

25-Program to add an element at specified index in a list?

# Declaring a list
list = [10, 20, 30]

# printing elements
print (list)
# O/P will be: [10, 20, 30]

# inserting "ABC" at 1st index
list.insert (1, "ABC")
# printing
print (list)
# O/P will be: [10, 'ABC', 20, 30]

# inserting "PQR" at 3rd index
list.insert (3, "PQR")
# printing
print (list)
# O/P will be: [10, 'ABC', 20, 'PQR', 30]

# inserting 'XYZ' at 5th index
list.insert (5, "XYZ")
print (list)
# O/P will be: [10, 'ABC', 20, 'PQR', 30, 'XYZ']

# inserting 99 at second last index
list.insert (len (list) -1, 99)
# printing
print (list)
# O/P will be: [10, 'ABC', 20, 'PQR', 30, 99, 'XYZ']


26-Program to remove first occurrence of a given element in the list


# Declaring a list
list = [10, 20, 30, 40, 30]

# print list
print "List element:"
for l in range(len(list)):
	print (list[l])

# removing 30 from the list
list.remove(30);

# print list after removing 30
print "List element after removing 30:"
for l in range(len(list)):
	print (list[l])


27-Remove all occurrences a given element from the list?

# list with integer elements
list = [10, 20, 10, 30, 10, 40, 10, 50]
# number (n) to be removed
n = 10

# print original list
print ("Original list:")
print (list)

# loop to traverse each element in list
# and, remove elements
# which are equals to n
i=0 #loop counter
length = len(list)  #list length
while(i<length):
	if(list[i]==n):
		list.remove (list[i])
		# as an element is removed
		# so decrease the length by 1
		length = length -1
		# run loop again to check element
		# at same index, when item removed
		# next item will shift to the left
		continue
	i = i+1

# print list after removing given element
print ("list after removing elements:")
print (list)


28-Program to remove all elements in a range from the List

# Declaring a list
list = [10, 20, 30, 40, 50]

# print list
print "List element:"
for l in range(len(list)):
	print (list[l])

# delete element from index 1 to 30del list[1.3]
del list[1:3]

# print list after deleting
# element from index 1 to 3
print "List element after del[1:3]:"
for l in range(len(list)):
	print (list[l])

29-Program to sort the elements of given list in Ascending and Descending Order

# List of integers
num = [10, 30, 40, 20, 50]

# sorting and printing
num.sort()
print (num)

# List of float numbers
fnum = [10.23, 10.12, 20.45, 11.00, 0.1]

# sorting and printing
fnum.sort()
print (fnum)

# List of strings
str = ["Banana", "Cat", "Apple", "Dog", "Fish"]

# sorting and  printing
str.sort()
print (str)


30-Program to find the differences of two lists

# list1 - first list of the integers
# lists2 - second list of the integers
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 60, 70]

# printing lists
print "list1:", list1
print "list2:", list2

# finding and printing differences of the lists
print "Difference elements:"
print (list (set(list1) - set (list2)))
'''


