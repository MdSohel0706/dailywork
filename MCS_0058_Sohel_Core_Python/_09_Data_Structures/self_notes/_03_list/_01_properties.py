'''
# REQ: so and so......
           1. CRUD :  CREATE RETRIEVE UPDATE DELETE
           2. Datatype/structure
           3. State(variable)
           4. Behavior(Operators, DM, Loops)

'''
x = 10
x = 10.5
is_bool = True
msg = 'Hello World' # '@!#!@#3213213{}<>?<VCXVEWREWRSDFSDF'

'''List properties'''

'''
List properties:
==================
# 1. List will allow both homogeneous and heterogenous
# 2. List allows duplicate elements
# 3. Insertion order maintains
# 4. List is mutable
# 5. Follows indexing mechanism while storing elements 
'''

# 1.List will allow both homogeneous and heterogenous
    # Homo
'''print("----------Homegeneous---------")
list_value = [1,2,3,4,5,6]
print("In this integer list: ", list_value,type(list_value),id (list_value))

list_value = [1.2,3.4,4.5,6.7,8.7,8.9,]
print("In this float list :",list_value,type(list_value),id(list_value))

list_value = ['satish','venkat', 'kumar','shiva',]
print("In this string list :",list_value,type(list_value),id(list_value))

list_value = [(1.2),(2.0),(7.8)]
print("Enter the list: ",list_value, type(list_value))

list_value = [(1,2),("satish"),(1.2,4.6),]
print("Enter the list :",list_value ,type(list_value))

list_value= [{1,2},{"venkat"},{3.3,3.4}]
print("Enter the dic :",list_value,type(list_value))

list_value = [{1.2},{"satish"},{200,300}]
print("Enter the set : ",list_value,type(list_value))

# heterogenous:
list_value = [1,2.3,"satish",(1),("satish"),(4.3),{230},{1.2},{"satish"}]
print("Enter the heterogenous: ",list_value,type(list_value))

# 2. List allows duplicate elements
list_value = [12,12,30]
print("Enter the Duplicate values :",list_value,type(list_value))

# 3. Insertion order maintains
list_value = [1,2,3,4,5,6,7,8,9,10]
print("Enter the order of the list :",list_value,type(list_value))

# 4. List is mutable
list_value = [1,2,3,4,5,6]
print("Before the list:",list_value)
list_value[2] = 300
print("After the list :",list_value)

# 5. Follow indexing mechanism
list_value = [1,2,3,4,5]
        #0 1 2 3 4'''

'''
- Handle group of elements
- Homogeneous/heterogenous, 
- Mutable structures
- With Duplicate values 
'''

'''list_value = [1,2.3,"satish",True,265454]
print(list)
print("Indexing of the list :",list_value[2])
print("Indexing of the list :", list_value[2][-3])
print("Indexing of the list :",list_value[4])'''

'''# Slicing
list_value = [1,2.3,"satish",True,265454]
print("Print the Slicing :",list_value[2:5])

list_value = [1,2.3,"satish",True,265454]
print(list_value[-1: -5: -1])

# Adding
list_value = [(123,344)+(233,677),['satish']+['babu']]
print("Adding of the elements :", list_value )
'''
'''# multiplying
list_value = [1,2,3]*3
print("Multiply the elements:",list_value)

# Membership
list_value = [1,2,3,"satish",2.3]
print("Check the element present in the list:","satish" in list_value )'''

# len
'''list_value = [1,2,3,4,5,6]
print("Find the length of the element: ",len(list_value))'''

# max
'''list_value = [1,2,3,4,5,6,7]
print("Find the length of the element: ",max(list_value))

#min
list_value = [1,2,3,4,5,6,7]
print("Find the min length of element :",min(list_value))'''


'''list_value = []
print("Find the min length of element :",min(list_value))'''
#ValueError: min() arg is an empty sequence


list_value1 = [1,2,3,4,5]
list_value2 = [True,False,False]
list_value3 = ['Hello','World','python']
list_value4 = [[1,2,3],[4,5,6],[7,8,9]]
list_value5 = [(1,2),(3,4,5)]
list_value6 = [{1:1,2:2},{1:'satish',2:'katta'},{}]
list_value7 = [{1,2,3},{4,5,6}]

print("-----------List_value4 operations---------")
list_value4 = [[1,2,3], [4,5,6], [7,8,9]]
print("List_value4 : ",list_value4[0])
print("List_value4 : ",list_value4[0][1])
print("List_value4 : ",list_value4[0:1])


list_value3 = ['Hello','World','python']
print("List_value3 : ",list_value3[0])
print("List_value3 : ",list_value3[0][1])
print("List_value3 : ",list_value3[0:1])

list_value5 = [(1,2),(3,4,5)]
print("List_value5 : ",list_value5[0])
print("List_value5 : ",list_value5[0][1])
print("List_value5 : ",list_value5[0:1])

"""**BUILT IN FUNCTIONS ON LIST:==>

1	cmp(list1, list2)
    It compares the elements of both the lists.
    This method is not used in the Python 3 and the above versions.

2	len(list)
    It is used to calculate the length of the list.
EXAMPLE:=>

L1 = [1,2,3,4,5,6,7,8]
print(len(L1))

OUTPUT:    8

3	max(list)
    It returns the maximum element of the list.

EXAMPLE:>

L1 = [12,34,26,48,72]
print(max(L1))

OUTPUT:>72

4	min(list):
	It returns the minimum element of the list.

EXAMPLE:=> L1 = [12,34,26,48,72]
print(min(L1))

OUTPUT:
12

5	list(seq):
	It converts any sequence to the list.

EXAMPLE:>

str = "Johnson"
s = list(str)
print(type(s))

OUTPUT:><class list>

6. list.append(obj)

    Appends object obj to list

7.list.count(obj)

    Returns count of how many times obj occurs in list

8.list.extend(seq)

    Appends the contents of seq to list

9.list.index(obj)

    Returns the lowest index in list that obj appears

10. list.insert(index, obj)

    Inserts object obj into list at offset index

11. list.pop(obj=list[-1])

    Removes and returns last object or obj from list

12. list.remove(obj)

    Removes object obj from list

13.list.reverse()

    Reverses objects of list in place

14.list.sort([func])

    Sorts objects of list, use compare func if given

15.append()
	Adds an element at the end of the list
16.clear()
	Removes all the elements from the list
17.copy()
	Returns a copy of the list
18.count()
	Returns the number of elements with the specified value
19.extend()
	Add the elements of a list (or any iterable), to the end of the current list
20.index()
    Returns the index of the first element with the specified value
21.insert()
	Adds an element at the specified position
22.pop()
    Removes the element at the specified position
23.remove()
	Removes the item with the specified value
24.reverse()
    Reverses the order of the list
25.sort()
    Sorts the lis"""
