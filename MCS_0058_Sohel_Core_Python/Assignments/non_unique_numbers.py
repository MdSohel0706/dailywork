'''l1 = [1,2,3,4,5,6]
l2 = [9,8,1,2,3]
l3 = [i for i in l1 if str(i) not in "".join([str(i) for i in l2])]
l4 = [i for i in l2 if str(i) not in "".join([str(i) for i in l1])]
print(l3 + l4)'''

'''l1 = [1,2,3,4,5,6]
l2 = [9,8,1,2,3]
result = []
for i in l1:
    if(i not in l2):
        result.append(i)

for i in l2:
    if(i not in l1):
        result.append(i)

print(result)'''

'''l1 = [1,2,3,4,5,6]
l2 = [9,8,1,2,3]
print([i for i in l1 if i not in l2]+[i for i in l2 if i not in l1])'''

'''l1 = set([1,2,3,4,5,6])
l2 = set([9,8,1,2,3])
print(l1.symmetric_difference(l2))'''

