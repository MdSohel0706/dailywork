from copy import copy, deepcopy

a = [[1,2,3],[4,5,6],[7,8,9],11,12,13]
b=deepcopy(a)
b[2][1]=200
print(b)
print(id(b[2]))
print(a)
print(id(a[2]))


print("*"*40)


a = [[1,2,3],[4,5,6],[7,8,9],11,12,13]
b=copy(a)
b[2][1]=200
print(b)
print(id(b[2]))
print(a)
print(id(a[2]))
