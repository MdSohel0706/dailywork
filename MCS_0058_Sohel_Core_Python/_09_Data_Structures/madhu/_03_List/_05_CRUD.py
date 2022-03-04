# CRUD Operations


# 1. CREATE
list1 = [1, 2, 3, 4, 5, 6]

# 2. RETRIEVE
list1 = [1, 2, [30,40,50], (11,22,33), {1,2,3}, {1:100,2:200}]
print('List values1 : ', list1)
print('List values2 : ', list1[2])
print('List values21 : ', list1[2][1])
# 3. UPDATE
list1[1] = 200
print('List values2 : ', list1)

# 4. DELETE
del list1[2]
print('List values3 : ', list1)
del list1
#print('List values4 : ', list1)

