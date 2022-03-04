"""
#SET PROGRAMS:

1: Write a program to remove the given number from the set.

my_set = {1,2,3,4,5,6,12,24}
n = int(input("Enter the number you want to remove"))
my_set.discard(n)
print("After Removing:",my_set)

2: Write a program to add multiple elements to the set.

set1 = set([1,2,4,"John","CS"])
set1.update(["Apple","Mango","Grapes"])
print(set1)

3: Write a program to find the union between two set.

set1 = set(["Peter","Joseph", 65,59,96])
set2  = set(["Peter",1,2,"Joseph"])
set3 = set1.union(set2)
print(set3)

4: Write a program to find the intersection between two sets.

set1 = {23,44,56,67,90,45,"Javatpoint"}
set2 = {13,23,56,76,"Sachin"}
set3 = set1.intersection(set2)
print(set3)

5: Write the program to add element to the frozenset.

set1 = {23,44,56,67,90,45,"Javatpoint"}
set2 = {13,23,56,76,"Sachin"}
set3 = set1.intersection(set2)
print(set3)

6: Write the program to find the issuperset, issubset and superset.

set1 = set(["Peter","James","Camroon","Ricky","Donald"])
set2 = set(["Camroon","Washington","Peter"])
set3 = set(["Peter"])

issubset = set1 >= set2
print(issubset)
issuperset = set1 <= set2
print(issuperset)
issubset = set3 <= set2
print(issubset)
issuperset = set2 >= set3
print(issuperset)

7.Python Program to Count the Number of Vowels Present in a String using Sets?

s=raw_input("Enter string:")
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:")
print(count)

8.Python Program to Check Common Letters in Two Input Strings?

s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)

9.Python Program that Displays which Letters are in the First String but not in the Second?

s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
a=list(set(s1)-set(s2))
print("The letters are:")
for i in a:
    print(i)

10.Python Program that Displays which Letters are Present in Both the Strings?

s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
a=list(set(s1)|set(s2))
print("The letters are:")
for i in a:
    print(i)

11.Python Program that Displays which Letters are in the Two Strings but not in Both?


s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
a=list(set(s1)^set(s2))
print("The letters are:")
for i in a:
    print(i)

12.Write a Python program to iteration over sets.?

num_set = set([0, 1, 2, 3, 4, 5])
for n in num_set:
  print(n, end=' ')
char_set = set("w3resource")
# Iterating using for loop
for val in char_set:
    print(val, end=' ')

13.Write a Python program to add member(s) in a set?
#A new empty set
color_set = set()
print(color_set)
print("\nAdd single element:")
color_set.add("Red")
print(color_set)
print("\nAdd multiple items:")
color_set.update(["Blue", "Green"])
print(color_set)

14.Write a Python program to remove item(s) from a given set?

num_set = set([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
num_set.pop()
print("\nAfter removing the first element from the said set:")
print(num_set)

15.Write a Python program to remove an item from a set if it is present in the set.?

#Create a new set
num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("\nRemove 0 from the said set:")
num_set.discard(4)
print(num_set)
print("\nRemove 5 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 2 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 7 from the said set:")
num_set.discard(15)
print(num_set)

16.Write a Python program to check if a set is a subset of another set.?

print("Check if a set is a subset of another set, using comparison operators and issubset():\n")
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
print("x: ",setx)
print("y: ",sety)
print("z: ",setz,"\n")
print("If x is subset of y")
print(setx <= sety)
print(setx.issubset(sety))
print("If y is subset of x")
print(sety <= setx)
print(sety.issubset(setx))
print("\nIf y is subset of z")
print(sety <= setz)
print(sety.issubset(setz))
print("If z is subset of y")
print(setz <= sety)
print(setz.issubset(sety))

17.Write a Python program to create a shallow copy of sets?

setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
#A shallow copy
setr = setp.copy()
print(setr)

18. Write a Python program to remove all elements from a given set.?

setc = {"Red", "Green", "Black", "White"}
print("Original set elements:")
print(setc)
print("\nAfter removing all elements of the said set.")
setc.clear()
print(setc)

19.Write a Python program to use of frozensets?

x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
#use isdisjoint(). Return True if the set has no elements in common with other.
print(x.isdisjoint(y))
#use difference(). Return a new set with elements in the set that are not in the others.
print(x.difference(y))
#new set with elements from both x and y
print(x | y)

20.Write a Python program to find maximum and the minimum value in a set?

#Create a set
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nMaximum value of the said set:")
print(max(setn))
print("\nMinimum value of the said set:")
print(min(setn))

21.Write a Python program to find the length of a set?

#Create a set
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nLength of the said set:")
print(len(setn))

setn = {5, 5, 5, 5, 5, 5}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nLength of the said set:")
print(len(setn))

setn = {5, 5, 5, 5, 5, 5, 7}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nLength of the said set:")
print(len(setn))

22.Write a Python program to check if a given value is present in a set or not?

nums = {1, 3, 5, 7, 9, 11}
print("Original sets(nums): ",nums,"\n")
print("Test if 6 exists in nums:")
print(6 in nums)
print("Test if 7 exists in nums:")
print(7 in nums)
print("Test if 11 exists in nums:")
print(11 in nums)
print("Test if 0 exists in nums:")
print(0 in nums)
print("\nTest if 6 is not in nums")
print(6 not in nums)
print("Test if 7 is not in nums")
print(7 not in nums)
print("Test if 11 is not in nums")
print(11 not in nums)
print("Test if 0 is not in nums")
print(0 not in nums)

23.Write a Python program to check if two given sets have no elements in common?
x = {1,2,3,4}
y = {4,5,6,7}
z = {8}
print("Original set elements:")
print(x)
print(y)
print(z)
print("\nConfirm two given sets have no element(s) in common:")
print("\nCompare x and y:")
print(x.isdisjoint(y))
print("\nCompare x and z:")
print(z.isdisjoint(x))
print("\nCompare y and z:")
print(y.isdisjoint(z))

24.Write a Python program to check if a given set is superset of itself and superset of another given set?

nums = {10,20,30,40,50}
print("Original set: ",nums)
print("If nums is superset of itself?")
print(nums.issuperset(nums))
num1 = {1, 2, 3, 4, 5, 7}
num2 = {2, 4}
num3 = {2, 4}
print("\nnum1 = ", num1)
print("num2 = ", num2)
print("num3 = ", num3)
print("If mum1 is superset of num2:")
print(num1>num2)
print("Compare mum2 and num3:")
print("If mum2 is superset of num3:")
print(num2>num3)
print("If mum3 is superset of num2:")
print(num3>num2)


25.Write a Python program to find the elements in a given set that are not in another set?

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Difference of sn1 and sn2 using difference():")
print(sn1.difference(sn2))
print("Difference of sn2 and sn1 using difference():")
print(sn2.difference(sn1))
print("Difference of sn1 and sn2 using - operator:")
print(sn1-sn2)
print("Difference of sn2 and sn1 using - operator:")
print(sn2-sn1)

26.Write a Python program to remove the intersection of a 2nd set from the 1st set?

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("\nRemove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print("sn1: ",sn1)
print("sn2: ",sn2)
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("\nRemove the intersection of a 2nd set from the 1st set using -= operator:")
sn1-=sn2
print("sn1: ",sn1)
print("sn2: ",sn2)

"""