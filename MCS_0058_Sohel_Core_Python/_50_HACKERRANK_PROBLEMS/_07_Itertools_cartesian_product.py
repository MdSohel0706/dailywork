import itertools as it
'''
a = [1,2,3]
b = [4,5,6]
x = it.product(a,b, repeat = 1)
y = list(it.product(a,b, repeat = 1))
print(*y, sep = "_")
print(list(x))
'''
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = list(it.product(a,b))

print(*c, sep = " ")