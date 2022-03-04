

list1 = [1,2,3,4]
print("Before : ",list1, type(list1))
tup1 = tuple(list1)
print("After : ",tup1, type(tup1))


t1 = (10,43,2,532,53,64,24,25,53)
print("Iterate the tuple")
for each in t1:
    print(each)

le = len(t1)
for  ind in range(le):  # range(9)
    print(ind," : ",t1[ind])


# Find index of 64
t1 = (10, 43, 2, 532, 53, 64, 24, 25, 24, 10,  53, 10)

for ind in range(len(t1)):
    if t1[ind] == 64:
        print("Index is : ",ind)

print("Count : ", t1.count(10))

print("Index : ", t1.index(64))
