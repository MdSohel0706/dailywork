#Python Sequence Types

'''1 Some basic sequence type classes in python are, list, tuple, range.
2 There are some additional sequence type objects, these are binary data
and text string.
3.Some common operations for the sequence type
object can work on both mutable and immutable sequences.
'''

'''list_value = [12, 22, 13, 54, 35, 76, 14]
print("List1 : ", list_value )

# 1. Sequence operations

print("----------1. Indexing-------------")
                                                                    
    [12, 22, 13, 54, 35, 76, 14]   1 2 3 4 5 6 7 8 9 10 
      0  1   2   3   4   5   6   '''
'''print("List1 1    : ", list_value [1])
print("List1 5,-1 : ", list_value [5], list_value [6], list_value [-1])

print("----------2. Slicing-------------")
print("Slicing operation : ", list_value [2:])
print("Slicing operation : ", list_value [2:5])
print("Slicing operation : ", list_value [:5])
print("Slicing operation : ", list_value [::1])
print("Slicing operation : ", list_value [::2])

print("----------3. Adding-------------")
print("Adding 2 lists    :", [1, 2, 3] + [4, 5, 6])  # print(10+20)
list_value  = [10, 20, 30]
list_value  = [11, 12, 13]
print("Adding 2 lists    :", list_value +list_value )   # x=10 y= 20   print(x+y)


print("----------4. Multiplying-------------")
print("Multiply 2 lists :", [1, 2, 3] * 5)

print("----------5. Membership-------------")
print("Check value : ", 1 in [1, 2, 3])

print("----------6. length-------------")
print("Length of list1 : ", len(list_value ))

print("----------7. max-------------")
print("Length of list1 : ", max(list_value ))

print("----------8. min-------------")
print("Length of list1 : ", min(list_value ))'''

'''myList1 = [10, 20, 30, 40, 50]
myList2 = [56, 42, 79, 42, 85, 96, 23]

if 30 in myList1:
   print('30 is present')
    
if 120 not in myList1:
   print('120 is not present')
    
print(myList1 + myList2) #Concatinate lists
print(myList1 * 3) #Add myList1 three times with itself
print(max(myList2))
print(myList2.count(42)) #42 has two times in the list

print(myList2[2:7])
print(myList2[2:7:2])

myList1.append(60)
print(myList1)

myList2.insert(5, 17)
print(myList2)

myList2.pop(3)
print(myList2)
myList1.reverse()
print(myList1)

myList1.clear()
print(myList1)'''
